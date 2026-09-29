// START_MODULE_CONTRACT
//   PURPOSE: Integration tests for aicc-deploy against temporary repositories and local bare remotes.
//   SCOPE: Never touches the real deploy repository or its remotes.
//   DEPENDS: M-AICC-DEPLOY binary
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   Fixture - temporary source repository, deploy repository and two bare remotes
// END_MODULE_MAP

use std::fs;
use std::io::{Read, Write};
use std::net::TcpListener;
use std::path::{Path, PathBuf};
use std::process::{Command, Output};
use std::sync::atomic::{AtomicUsize, Ordering};
use std::thread;

static COUNTER: AtomicUsize = AtomicUsize::new(0);

fn git(dir: &Path, args: &[&str]) -> String {
    let out = Command::new("git")
        .arg("-C")
        .arg(dir)
        .args(args)
        .env("GIT_AUTHOR_NAME", "Test")
        .env("GIT_AUTHOR_EMAIL", "test@example.invalid")
        .env("GIT_COMMITTER_NAME", "Test")
        .env("GIT_COMMITTER_EMAIL", "test@example.invalid")
        .output()
        .expect("git runs");
    assert!(out.status.success(), "git {:?} failed: {}", args, String::from_utf8_lossy(&out.stderr));
    String::from_utf8_lossy(&out.stdout).trim().to_string()
}

struct Fixture {
    root: PathBuf,
    src: PathBuf,
    deploy: PathBuf,
    origin: PathBuf,
    websvc: PathBuf,
}

impl Fixture {
    fn new() -> Fixture {
        let n = COUNTER.fetch_add(1, Ordering::SeqCst);
        let root = std::env::temp_dir().join(format!("aicc-deploy-it-{}-{n}", std::process::id()));
        let _ = fs::remove_dir_all(&root);
        let (src, deploy, origin, websvc) = (root.join("src"), root.join("deploy"), root.join("origin.git"), root.join("websvc.git"));
        for d in [&src, &deploy] {
            fs::create_dir_all(d).unwrap();
        }
        for b in [&origin, &websvc] {
            fs::create_dir_all(b).unwrap();
            git(b, &["init", "-q", "--bare", "-b", "main"]);
        }
        // source repository with a committed generated site
        git(&src, &["init", "-q", "-b", "main"]);
        write(&src.join("html/aicc/index.html"), "root v1");
        write(&src.join("html/aicc/ru/index.html"), "ru v1");
        write(&src.join("html/aicc/en/index.html"), "en v1");
        write(&src.join("html/aicc/assets/site.css"), "css v1");
        git(&src, &["add", "-A"]);
        git(&src, &["commit", "-q", "-m", "site v1"]);
        // deploy repository with a README and a stale published file
        git(&deploy, &["init", "-q", "-b", "main"]);
        write(&deploy.join("README.md"), "deploy readme");
        write(&deploy.join(".gitignore"), ".DS_Store\n");
        write(&deploy.join("html/aicc/stale.html"), "old placeholder");
        git(&deploy, &["add", "-A"]);
        git(&deploy, &["commit", "-q", "-m", "initial"]);
        git(&deploy, &["remote", "add", "origin", origin.to_str().unwrap()]);
        git(&deploy, &["remote", "add", "websvc", websvc.to_str().unwrap()]);
        git(&deploy, &["push", "-q", "origin", "main"]);
        git(&deploy, &["push", "-q", "websvc", "main"]);
        Fixture { root, src, deploy, origin, websvc }
    }

    fn run(&self, extra: &[&str]) -> Output {
        Command::new(env!("CARGO_BIN_EXE_aicc-deploy"))
            .current_dir(&self.src)
            .args(["--source", self.src.join("html/aicc").to_str().unwrap()])
            .args(["--deploy-repo", self.deploy.to_str().unwrap()])
            .args(["--check-cmd", "true"])
            .args(extra)
            .env("GIT_AUTHOR_NAME", "Test")
            .env("GIT_AUTHOR_EMAIL", "test@example.invalid")
            .env("GIT_COMMITTER_NAME", "Test")
            .env("GIT_COMMITTER_EMAIL", "test@example.invalid")
            .output()
            .expect("binary runs")
    }

    fn heads(&self) -> (String, String) {
        (git(&self.origin, &["rev-parse", "main"]), git(&self.websvc, &["rev-parse", "main"]))
    }

    /// Hash of every file in the deploy repository, including html/aicc, excluding .git.
    fn snapshot(&self) -> Vec<(String, Vec<u8>)> {
        let mut out = Vec::new();
        fn walk(root: &Path, dir: &Path, out: &mut Vec<(String, Vec<u8>)>) {
            let mut items: Vec<_> = fs::read_dir(dir).unwrap().map(|e| e.unwrap().path()).collect();
            items.sort();
            for p in items {
                if p.file_name().unwrap() == ".git" {
                    continue;
                }
                if p.is_dir() {
                    walk(root, &p, out);
                } else {
                    out.push((p.strip_prefix(root).unwrap().to_string_lossy().into_owned(), fs::read(&p).unwrap()));
                }
            }
        }
        walk(&self.deploy, &self.deploy, &mut out);
        out
    }

    fn outside_snapshot(&self) -> Vec<(String, Vec<u8>)> {
        self.snapshot().into_iter().filter(|(p, _)| !p.starts_with("html/aicc/")).collect()
    }
}

impl Drop for Fixture {
    fn drop(&mut self) {
        let _ = fs::remove_dir_all(&self.root);
    }
}

fn write(path: &Path, text: &str) {
    fs::create_dir_all(path.parent().unwrap()).unwrap();
    fs::write(path, text).unwrap();
}

fn text(o: &Output) -> String {
    format!("{}{}", String::from_utf8_lossy(&o.stdout), String::from_utf8_lossy(&o.stderr))
}

#[test]
fn dry_run_writes_and_pushes_nothing() {
    let f = Fixture::new();
    let before = (f.snapshot(), f.heads(), git(&f.deploy, &["rev-parse", "HEAD"]), git(&f.deploy, &["status", "--porcelain"]));
    let o = f.run(&[]);
    assert!(o.status.success(), "{}", text(&o));
    let out = text(&o);
    assert!(out.contains("Added (4)") && out.contains("Removed (1)") && out.contains("stale.html"), "{out}");
    assert!(out.contains("Dry run"));
    let after = (f.snapshot(), f.heads(), git(&f.deploy, &["rev-parse", "HEAD"]), git(&f.deploy, &["status", "--porcelain"]));
    assert_eq!(before, after);
}

#[test]
fn publish_mirrors_removes_stale_commits_and_pushes_both_remotes_in_order() {
    let f = Fixture::new();
    let outside = f.outside_snapshot();
    let src_head = git(&f.src, &["rev-parse", "HEAD"]);
    let heads_before = f.heads();

    let o = f.run(&["--publish", "--skip-verify"]);
    assert!(o.status.success(), "{}", text(&o));

    let served = f.deploy.join("html/aicc");
    assert_eq!(fs::read_to_string(served.join("ru/index.html")).unwrap(), "ru v1");
    assert_eq!(fs::read_to_string(served.join("assets/site.css")).unwrap(), "css v1");
    assert!(!served.join("stale.html").exists(), "stale file removed");
    let manifest = fs::read_to_string(served.join("package-manifest.json")).unwrap();
    assert!(manifest.contains(&src_head) && manifest.contains("\"file_count\": 4") && manifest.contains("ru/index.html"));

    let msg = git(&f.deploy, &["log", "-1", "--format=%B"]);
    assert!(msg.contains(&src_head[..12]) && msg.contains("Added 4, changed 0, removed 1"), "{msg}");
    let head = git(&f.deploy, &["rev-parse", "HEAD"]);
    assert_eq!(f.heads(), (head.clone(), head));
    assert_ne!(heads_before.0, f.heads().0);
    assert_eq!(f.outside_snapshot(), outside, "nothing outside html/aicc changed");
    assert_eq!(git(&f.deploy, &["status", "--porcelain"]), "");
}

#[test]
fn second_publish_without_changes_commits_and_pushes_nothing() {
    let f = Fixture::new();
    assert!(f.run(&["--publish", "--skip-verify"]).status.success());
    let heads = f.heads();
    let count = git(&f.deploy, &["rev-list", "--count", "HEAD"]);
    let o = f.run(&["--publish", "--skip-verify"]);
    assert!(o.status.success(), "{}", text(&o));
    assert!(text(&o).contains("Nothing to publish"));
    assert_eq!(f.heads(), heads);
    assert_eq!(git(&f.deploy, &["rev-list", "--count", "HEAD"]), count);
}

#[test]
fn a_changed_source_is_published_as_a_change_and_no_origin_skips_origin() {
    let f = Fixture::new();
    assert!(f.run(&["--publish", "--skip-verify"]).status.success());
    write(&f.src.join("html/aicc/ru/index.html"), "ru v2");
    git(&f.src, &["add", "-A"]);
    git(&f.src, &["commit", "-q", "-m", "site v2"]);
    let origin_before = f.heads().0;
    let o = f.run(&["--publish", "--skip-verify", "--no-origin"]);
    assert!(o.status.success(), "{}", text(&o));
    assert!(text(&o).contains("Changed (1)"));
    assert_eq!(f.heads().0, origin_before, "origin untouched with --no-origin");
    assert_eq!(f.heads().1, git(&f.deploy, &["rev-parse", "HEAD"]));
}

fn refuses(f: &Fixture, extra: &[&str], needle: &str) {
    let heads = f.heads();
    let snap = f.snapshot();
    let o = f.run(extra);
    assert_eq!(o.status.code(), Some(1), "{}", text(&o));
    assert!(text(&o).contains(needle), "expected '{needle}' in: {}", text(&o));
    assert_eq!(f.heads(), heads);
    assert_eq!(f.snapshot(), snap, "refusal must not write");
}

#[test]
fn refuses_deploy_changes_outside_the_served_folder() {
    let f = Fixture::new();
    write(&f.deploy.join("README.md"), "edited");
    refuses(&f, &["--publish", "--skip-verify"], "outside html/aicc/");
    let g = Fixture::new();
    write(&g.deploy.join("notes.txt"), "untracked");
    refuses(&g, &["--publish", "--skip-verify"], "outside html/aicc/");
}

#[test]
fn refuses_the_wrong_branch() {
    let f = Fixture::new();
    git(&f.deploy, &["checkout", "-q", "-b", "feature"]);
    refuses(&f, &["--publish", "--skip-verify"], "expected 'main'");
}

#[test]
fn refuses_a_missing_remote() {
    let f = Fixture::new();
    git(&f.deploy, &["remote", "remove", "websvc"]);
    refuses(&f, &["--publish", "--skip-verify"], "no remote named 'websvc'");
}

#[test]
fn refuses_when_the_source_check_fails() {
    let f = Fixture::new();
    refuses(&f, &["--publish", "--skip-verify", "--check-cmd", "echo not-fresh; false"], "source check failed");
}

#[test]
fn refuses_a_dirty_source_checkout_and_untracked_site_files() {
    let f = Fixture::new();
    write(&f.src.join("html/aicc/ru/index.html"), "edited but not committed");
    refuses(&f, &["--publish", "--skip-verify"], "uncommitted changes");
    let g = Fixture::new();
    write(&g.src.join("html/aicc/new.html"), "untracked");
    refuses(&g, &["--publish", "--skip-verify"], "untracked files");
}

#[test]
fn refuses_an_incomplete_source_site() {
    let f = Fixture::new();
    fs::remove_file(f.src.join("html/aicc/en/index.html")).unwrap();
    git(&f.src, &["add", "-A"]);
    git(&f.src, &["commit", "-q", "-m", "drop en"]);
    refuses(&f, &["--publish", "--skip-verify"], "incomplete");
}

#[test]
fn a_failed_first_push_is_reported_and_leaves_the_local_commit() {
    let f = Fixture::new();
    git(&f.deploy, &["remote", "set-url", "origin", f.root.join("missing.git").to_str().unwrap()]);
    let o = f.run(&["--publish", "--skip-verify"]);
    assert_eq!(o.status.code(), Some(1));
    let out = text(&o);
    assert!(out.contains("nothing was pushed") && out.contains("exists locally"), "{out}");
    assert_eq!(f.heads().1, git(&f.deploy, &["rev-parse", "HEAD~1"]), "websvc must not be pushed when origin failed");
}

#[test]
fn verification_succeeds_when_the_served_manifest_matches_and_fails_otherwise() {
    // Serve the manifest file from the deploy repository once, then a wrong body.
    let f = Fixture::new();
    let listener = TcpListener::bind("127.0.0.1:0").unwrap();
    let port = listener.local_addr().unwrap().port();
    let manifest_path = f.deploy.join("html/aicc/package-manifest.json");
    thread::spawn(move || {
        for _ in 0..20 {
            let Ok((mut s, _)) = listener.accept() else { return };
            let mut buf = [0u8; 2048];
            let _ = s.read(&mut buf);
            let body = fs::read_to_string(&manifest_path).unwrap_or_default();
            let _ = s.write_all(format!("HTTP/1.1 200 OK\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{body}", body.len()).as_bytes());
        }
    });
    let url = format!("http://127.0.0.1:{port}/aicc/");
    let o = f.run(&["--publish", "--url", &url, "--verify-timeout", "5"]);
    // The server reads the manifest after it has been written, so it matches.
    assert!(o.status.success(), "{}", text(&o));
    assert!(text(&o).contains("Verified"));

    // A different served body must fail with a clear message and a non-zero exit.
    let g = Fixture::new();
    let l2 = TcpListener::bind("127.0.0.1:0").unwrap();
    let p2 = l2.local_addr().unwrap().port();
    thread::spawn(move || {
        for _ in 0..20 {
            let Ok((mut s, _)) = l2.accept() else { return };
            let mut buf = [0u8; 2048];
            let _ = s.read(&mut buf);
            let _ = s.write_all(b"HTTP/1.1 200 OK\r\nContent-Length: 3\r\nConnection: close\r\n\r\nold");
        }
    });
    let o = g.run(&["--publish", "--url", &format!("http://127.0.0.1:{p2}/aicc/"), "--verify-timeout", "1"]);
    assert_eq!(o.status.code(), Some(1));
    assert!(text(&o).contains("does not match"), "{}", text(&o));
}
