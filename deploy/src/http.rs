// START_MODULE_CONTRACT
//   PURPOSE: Verify the served site by fetching its manifest over plain HTTP.
//   SCOPE: HTTP/1.1 GET with the standard library. No redirects, no TLS. Read-only.
//   DEPENDS: M-AICC-DEPLOY manifest module
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   get - fetch a URL and return the body text
//   verify - poll the served manifest until it equals the published one or time runs out
//   manifest_url - manifest location under a served base URL
// END_MODULE_MAP

use crate::manifest::MANIFEST_NAME;
use std::io::{Read, Write};
use std::net::TcpStream;
use std::time::{Duration, Instant};

struct Url {
    host: String,
    port: u16,
    path: String,
}

fn parse_url(url: &str) -> Result<Url, String> {
    let rest = url.strip_prefix("http://").ok_or_else(|| format!("only http:// URLs are supported for verification: {url}"))?;
    let (authority, path) = match rest.find('/') {
        Some(i) => (&rest[..i], &rest[i..]),
        None => (rest, "/"),
    };
    let (host, port) = match authority.rsplit_once(':') {
        Some((h, p)) => (h.to_string(), p.parse::<u16>().map_err(|_| format!("bad port in {url}"))?),
        None => (authority.to_string(), 80),
    };
    if host.is_empty() {
        return Err(format!("no host in {url}"));
    }
    Ok(Url { host, port, path: path.to_string() })
}

pub fn manifest_url(base: &str) -> String {
    format!("{}{}{}", base, if base.ends_with('/') { "" } else { "/" }, MANIFEST_NAME)
}

fn decode_chunked(mut body: &[u8]) -> Result<Vec<u8>, String> {
    let mut out = Vec::new();
    loop {
        let eol = body.windows(2).position(|w| w == b"\r\n").ok_or("bad chunk framing")?;
        let size_str = String::from_utf8_lossy(&body[..eol]);
        let size = usize::from_str_radix(size_str.split(';').next().unwrap_or("").trim(), 16).map_err(|_| "bad chunk size")?;
        body = &body[eol + 2..];
        if size == 0 {
            return Ok(out);
        }
        if body.len() < size + 2 {
            return Err("truncated chunk".into());
        }
        out.extend_from_slice(&body[..size]);
        body = &body[size + 2..];
    }
}

pub fn get(url: &str) -> Result<String, String> {
    let u = parse_url(url)?;
    let mut stream = TcpStream::connect((u.host.as_str(), u.port)).map_err(|e| format!("cannot connect to {}:{}: {e}", u.host, u.port))?;
    stream.set_read_timeout(Some(Duration::from_secs(10))).ok();
    stream.set_write_timeout(Some(Duration::from_secs(10))).ok();
    let req = format!("GET {} HTTP/1.1\r\nHost: {}\r\nUser-Agent: aicc-deploy\r\nAccept: */*\r\nConnection: close\r\n\r\n", u.path, u.host);
    stream.write_all(req.as_bytes()).map_err(|e| format!("request failed: {e}"))?;
    let mut raw = Vec::new();
    stream.read_to_end(&mut raw).map_err(|e| format!("response failed: {e}"))?;
    let split = raw.windows(4).position(|w| w == b"\r\n\r\n").ok_or("malformed response")?;
    let head = String::from_utf8_lossy(&raw[..split]).to_string();
    let mut lines = head.lines();
    let status_line = lines.next().unwrap_or("");
    let code: u16 = status_line.split_whitespace().nth(1).and_then(|c| c.parse().ok()).ok_or("malformed status line")?;
    if code != 200 {
        return Err(format!("{url} answered {code}"));
    }
    let chunked = lines.any(|l| l.to_ascii_lowercase().starts_with("transfer-encoding:") && l.to_ascii_lowercase().contains("chunked"));
    let body = &raw[split + 4..];
    let bytes = if chunked { decode_chunked(body)? } else { body.to_vec() };
    String::from_utf8(bytes).map_err(|_| "response is not UTF-8".to_string())
}

pub fn verify(base_url: &str, expected: &str, timeout: Duration, interval: Duration) -> Result<(), String> {
    let url = manifest_url(base_url);
    let start = Instant::now();
    let mut last;
    loop {
        match get(&url) {
            Ok(body) if body.trim_end() == expected.trim_end() => return Ok(()),
            Ok(_) => last = "served manifest differs from the published manifest".to_string(),
            Err(e) => last = e,
        }
        if start.elapsed() >= timeout {
            return Err(format!("served site does not match after {}s: {last} ({url})", timeout.as_secs()));
        }
        std::thread::sleep(interval);
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::net::TcpListener;
    use std::thread;

    fn serve(responses: Vec<Vec<u8>>) -> u16 {
        let listener = TcpListener::bind("127.0.0.1:0").unwrap();
        let port = listener.local_addr().unwrap().port();
        thread::spawn(move || {
            for resp in responses {
                if let Ok((mut s, _)) = listener.accept() {
                    let mut buf = [0u8; 2048];
                    let _ = s.read(&mut buf);
                    let _ = s.write_all(&resp);
                }
            }
        });
        port
    }

    fn ok(body: &str) -> Vec<u8> {
        format!("HTTP/1.1 200 OK\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{body}", body.len()).into_bytes()
    }

    #[test]
    fn url_parsing() {
        let u = parse_url("http://host.example:8080/aicc/").unwrap();
        assert_eq!((u.host.as_str(), u.port, u.path.as_str()), ("host.example", 8080, "/aicc/"));
        assert_eq!(parse_url("http://h").unwrap().port, 80);
        assert!(parse_url("https://h/").is_err());
    }

    #[test]
    fn manifest_url_adds_slash_once() {
        assert_eq!(manifest_url("http://h/aicc/"), "http://h/aicc/package-manifest.json");
        assert_eq!(manifest_url("http://h/aicc"), "http://h/aicc/package-manifest.json");
    }

    #[test]
    fn get_with_content_length() {
        let port = serve(vec![ok("hello")]);
        assert_eq!(get(&format!("http://127.0.0.1:{port}/x")).unwrap(), "hello");
    }

    #[test]
    fn get_with_chunked_body() {
        let resp = b"HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\nConnection: close\r\n\r\n5\r\nhello\r\n6\r\n world\r\n0\r\n\r\n".to_vec();
        let port = serve(vec![resp]);
        assert_eq!(get(&format!("http://127.0.0.1:{port}/")).unwrap(), "hello world");
    }

    #[test]
    fn non_200_is_an_error_and_redirects_are_not_followed() {
        let port = serve(vec![b"HTTP/1.1 302 Found\r\nLocation: http://elsewhere/\r\nConnection: close\r\n\r\n".to_vec()]);
        assert!(get(&format!("http://127.0.0.1:{port}/")).unwrap_err().contains("302"));
    }

    #[test]
    fn verify_retries_until_the_manifest_matches() {
        let port = serve(vec![ok("old"), ok("old"), ok("new\n")]);
        let r = verify(&format!("http://127.0.0.1:{port}/aicc/"), "new", Duration::from_secs(5), Duration::from_millis(20));
        assert!(r.is_ok(), "{r:?}");
    }

    #[test]
    fn verify_fails_after_the_timeout() {
        let port = serve(vec![ok("old"), ok("old"), ok("old"), ok("old"), ok("old"), ok("old")]);
        let r = verify(&format!("http://127.0.0.1:{port}/"), "new", Duration::from_millis(60), Duration::from_millis(20));
        assert!(r.unwrap_err().contains("does not match"));
    }
}
