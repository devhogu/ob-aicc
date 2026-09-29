// START_MODULE_CONTRACT
//   PURPOSE: Scan a directory into a sorted list of files with hashes, and diff two scans.
//   SCOPE: Regular files only. Symlinks and other file types are rejected, not followed.
//   DEPENDS: M-AICC-DEPLOY sha256 module
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   Entry - relative path, SHA-256 and size of one file
//   Diff - added, changed and removed paths between two scans
//   scan - sorted scan of a directory, skipping listed names at the top level
//   diff - compare a source scan with a destination scan
// END_MODULE_MAP

use crate::sha256::sha256_hex;
use std::fs;
use std::io;
use std::path::Path;

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Entry {
    pub path: String,
    pub sha256: String,
    pub size: u64,
}

#[derive(Debug, Default, PartialEq, Eq)]
pub struct Diff {
    pub added: Vec<String>,
    pub changed: Vec<String>,
    pub removed: Vec<String>,
}

impl Diff {
    pub fn is_empty(&self) -> bool {
        self.added.is_empty() && self.changed.is_empty() && self.removed.is_empty()
    }
}

/// Scan `root` recursively. Files whose top-level name is in `skip` are ignored.
/// A missing root scans as empty so a first publish works.
pub fn scan(root: &Path, skip: &[&str]) -> io::Result<Vec<Entry>> {
    let mut out = Vec::new();
    if !root.exists() {
        return Ok(out);
    }
    walk(root, root, skip, &mut out)?;
    out.sort_by(|a, b| a.path.cmp(&b.path));
    Ok(out)
}

fn walk(root: &Path, dir: &Path, skip: &[&str], out: &mut Vec<Entry>) -> io::Result<()> {
    for item in fs::read_dir(dir)? {
        let item = item?;
        let path = item.path();
        let meta = fs::symlink_metadata(&path)?;
        let rel = path.strip_prefix(root).expect("path under root");
        let rel_str = rel.to_string_lossy().replace('\\', "/");
        if dir == root && skip.contains(&rel_str.as_str()) {
            continue;
        }
        if meta.file_type().is_symlink() {
            return Err(io::Error::new(io::ErrorKind::InvalidData, format!("symlink not allowed: {rel_str}")));
        }
        if meta.is_dir() {
            walk(root, &path, skip, out)?;
        } else if meta.is_file() {
            let bytes = fs::read(&path)?;
            out.push(Entry { path: rel_str, sha256: sha256_hex(&bytes), size: meta.len() });
        } else {
            return Err(io::Error::new(io::ErrorKind::InvalidData, format!("unsupported file type: {rel_str}")));
        }
    }
    Ok(())
}

pub fn diff(source: &[Entry], dest: &[Entry]) -> Diff {
    let mut d = Diff::default();
    for s in source {
        match dest.iter().find(|x| x.path == s.path) {
            None => d.added.push(s.path.clone()),
            Some(x) if x.sha256 != s.sha256 => d.changed.push(s.path.clone()),
            Some(_) => {}
        }
    }
    for x in dest {
        if !source.iter().any(|s| s.path == x.path) {
            d.removed.push(x.path.clone());
        }
    }
    d
}

#[cfg(test)]
mod tests {
    use super::*;

    fn e(path: &str, sha: &str) -> Entry {
        Entry { path: path.into(), sha256: sha.into(), size: 0 }
    }

    #[test]
    fn diff_reports_added_changed_removed() {
        let src = vec![e("a", "1"), e("b", "2"), e("c", "3")];
        let dst = vec![e("b", "2"), e("c", "x"), e("d", "4")];
        let d = diff(&src, &dst);
        assert_eq!(d.added, vec!["a"]);
        assert_eq!(d.changed, vec!["c"]);
        assert_eq!(d.removed, vec!["d"]);
        assert!(!d.is_empty());
    }

    #[test]
    fn identical_trees_have_empty_diff() {
        let t = vec![e("a", "1")];
        assert!(diff(&t, &t).is_empty());
    }

    #[test]
    fn scan_is_sorted_hashes_files_and_skips_top_level_names() {
        let dir = std::env::temp_dir().join(format!("aicc-deploy-scan-{}", std::process::id()));
        let _ = fs::remove_dir_all(&dir);
        fs::create_dir_all(dir.join("z/deep")).unwrap();
        fs::write(dir.join("b.txt"), b"abc").unwrap();
        fs::write(dir.join("z/deep/a.txt"), b"").unwrap();
        fs::write(dir.join("skip.json"), b"x").unwrap();
        let got = scan(&dir, &["skip.json"]).unwrap();
        let paths: Vec<_> = got.iter().map(|x| x.path.as_str()).collect();
        assert_eq!(paths, vec!["b.txt", "z/deep/a.txt"]);
        assert_eq!(got[0].sha256, "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");
        assert_eq!(got[0].size, 3);
        fs::remove_dir_all(&dir).unwrap();
    }

    #[test]
    fn missing_root_scans_empty() {
        assert!(scan(Path::new("/nonexistent/aicc-deploy-test"), &[]).unwrap().is_empty());
    }

    #[cfg(unix)]
    #[test]
    fn symlinks_are_rejected() {
        let dir = std::env::temp_dir().join(format!("aicc-deploy-link-{}", std::process::id()));
        let _ = fs::remove_dir_all(&dir);
        fs::create_dir_all(&dir).unwrap();
        std::os::unix::fs::symlink("/etc/hostname", dir.join("l")).unwrap();
        assert!(scan(&dir, &[]).is_err());
        fs::remove_dir_all(&dir).unwrap();
    }
}
