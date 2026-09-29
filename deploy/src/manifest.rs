// START_MODULE_CONTRACT
//   PURPOSE: Render the deterministic package manifest for a published tree.
//   SCOPE: JSON text only. No timestamps, so identical trees give identical bytes.
//   DEPENDS: M-AICC-DEPLOY tree module
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   MANIFEST_NAME - file name of the manifest inside the published folder
//   render - manifest JSON for a scan and a source commit
// END_MODULE_MAP

use crate::tree::Entry;

pub const MANIFEST_NAME: &str = "package-manifest.json";

fn escape(s: &str) -> String {
    let mut out = String::with_capacity(s.len() + 2);
    for c in s.chars() {
        match c {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if (c as u32) < 0x20 => out.push_str(&format!("\\u{:04x}", c as u32)),
            c => out.push(c),
        }
    }
    out
}

pub fn render(entries: &[Entry], source_commit: &str) -> String {
    let mut s = String::new();
    s.push_str("{\n");
    s.push_str("  \"generator\": \"aicc-deploy\",\n");
    s.push_str(&format!("  \"source_commit\": \"{}\",\n", escape(source_commit)));
    s.push_str(&format!("  \"file_count\": {},\n", entries.len()));
    s.push_str("  \"files\": [\n");
    for (i, e) in entries.iter().enumerate() {
        s.push_str(&format!(
            "    {{\"path\": \"{}\", \"sha256\": \"{}\", \"size\": {}}}{}\n",
            escape(&e.path),
            e.sha256,
            e.size,
            if i + 1 < entries.len() { "," } else { "" }
        ));
    }
    s.push_str("  ]\n}\n");
    s
}

#[cfg(test)]
mod tests {
    use super::*;

    fn e(path: &str, sha: &str, size: u64) -> Entry {
        Entry { path: path.into(), sha256: sha.into(), size }
    }

    #[test]
    fn lists_every_file_with_hash_and_source_commit() {
        let m = render(&[e("a.html", "aa", 1), e("ru/index.html", "bb", 22)], "abc123");
        assert!(m.contains("\"source_commit\": \"abc123\""));
        assert!(m.contains("\"file_count\": 2"));
        assert!(m.contains("{\"path\": \"a.html\", \"sha256\": \"aa\", \"size\": 1},"));
        assert!(m.contains("{\"path\": \"ru/index.html\", \"sha256\": \"bb\", \"size\": 22}\n"));
    }

    #[test]
    fn identical_input_gives_identical_bytes() {
        let t = [e("a", "1", 1)];
        assert_eq!(render(&t, "c"), render(&t, "c"));
    }

    #[test]
    fn paths_are_escaped() {
        let m = render(&[e("we\"ird\\name", "1", 1)], "c");
        assert!(m.contains("we\\\"ird\\\\name"));
    }

    #[test]
    fn empty_tree_is_valid_shape() {
        let m = render(&[], "c");
        assert!(m.contains("\"files\": [\n  ]"));
    }
}
