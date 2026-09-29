// START_MODULE_CONTRACT
//   PURPOSE: Mirror the source site into the served folder of the deploy repository, then commit and push.
//   SCOPE: Writes only inside the destination folder, plus git add, commit and push of that folder.
//   DEPENDS: M-AICC-DEPLOY tree, manifest, git and config modules
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   apply - copy added and changed files, delete removed files, write the manifest
//   Outcome - result of commit_and_push
//   commit_and_push - stage only the served folder, commit, push each remote in order
//   short - abbreviate a commit id
// END_MODULE_MAP

use crate::config::{Config, DEST_SUBDIR};
use crate::git;
use crate::manifest::MANIFEST_NAME;
use crate::tree::Diff;
use std::fs;
use std::io;
use std::path::Path;

pub fn short(commit: &str) -> &str {
    &commit[..commit.len().min(12)]
}

pub fn apply(source: &Path, dest: &Path, diff: &Diff, manifest_text: &str) -> io::Result<()> {
    fs::create_dir_all(dest)?;
    for rel in diff.added.iter().chain(diff.changed.iter()) {
        let target = dest.join(rel);
        if let Some(parent) = target.parent() {
            fs::create_dir_all(parent)?;
        }
        fs::write(&target, fs::read(source.join(rel))?)?;
    }
    for rel in &diff.removed {
        let target = dest.join(rel);
        fs::remove_file(&target)?;
        let mut dir = target.parent().map(|p| p.to_path_buf());
        while let Some(d) = dir {
            if d == dest || fs::remove_dir(&d).is_err() {
                break;
            }
            dir = d.parent().map(|p| p.to_path_buf());
        }
    }
    fs::write(dest.join(MANIFEST_NAME), manifest_text)
}

#[derive(Debug, PartialEq, Eq)]
pub enum Outcome {
    NothingStaged,
    Pushed(Vec<String>),
}

pub fn commit_and_push(deploy_repo: &Path, cfg: &Config, source_commit: &str, diff: &Diff) -> Result<Outcome, String> {
    git::run(deploy_repo, &["add", "-A", "--", DEST_SUBDIR])?;
    if git::succeeds(deploy_repo, &["diff", "--cached", "--quiet"]) {
        return Ok(Outcome::NothingStaged);
    }
    let title = format!("Publish AICC portal from {}", short(source_commit));
    let body = format!(
        "Source commit: {source_commit}\nAdded {}, changed {}, removed {} file(s) under {DEST_SUBDIR}/.\nPublished by aicc-deploy.",
        diff.added.len(),
        diff.changed.len(),
        diff.removed.len()
    );
    git::run(deploy_repo, &["commit", "-q", "-m", &title, "-m", &body])?;
    let mut pushed = Vec::new();
    for remote in &cfg.remotes {
        git::run(deploy_repo, &["push", remote, &cfg.branch]).map_err(|e| {
            let done = if pushed.is_empty() { "nothing was pushed".to_string() } else { format!("already pushed: {}", pushed.join(", ")) };
            format!("{e} ({done}; the commit exists locally in {})", deploy_repo.display())
        })?;
        pushed.push(remote.clone());
    }
    Ok(Outcome::Pushed(pushed))
}

#[cfg(test)]
mod tests {
    use super::*;

    fn tmp(name: &str) -> std::path::PathBuf {
        let d = std::env::temp_dir().join(format!("aicc-deploy-sync-{name}-{}", std::process::id()));
        let _ = fs::remove_dir_all(&d);
        fs::create_dir_all(&d).unwrap();
        d
    }

    #[test]
    fn short_abbreviates() {
        assert_eq!(short("0123456789abcdef"), "0123456789ab");
        assert_eq!(short("abc"), "abc");
    }

    #[test]
    fn apply_copies_deletes_prunes_and_writes_manifest() {
        let root = tmp("apply");
        let (src, dst) = (root.join("src"), root.join("dst"));
        fs::create_dir_all(src.join("ru")).unwrap();
        fs::write(src.join("ru/index.html"), b"new").unwrap();
        fs::write(src.join("a.txt"), b"changed").unwrap();
        fs::create_dir_all(dst.join("old/deep")).unwrap();
        fs::write(dst.join("old/deep/gone.txt"), b"x").unwrap();
        fs::write(dst.join("a.txt"), b"before").unwrap();
        let diff = Diff { added: vec!["ru/index.html".into()], changed: vec!["a.txt".into()], removed: vec!["old/deep/gone.txt".into()] };
        apply(&src, &dst, &diff, "{}\n").unwrap();
        assert_eq!(fs::read(dst.join("ru/index.html")).unwrap(), b"new");
        assert_eq!(fs::read(dst.join("a.txt")).unwrap(), b"changed");
        assert!(!dst.join("old").exists(), "empty directories are pruned");
        assert!(dst.exists());
        assert_eq!(fs::read(dst.join(MANIFEST_NAME)).unwrap(), b"{}\n");
        fs::remove_dir_all(&root).unwrap();
    }
}
