// START_MODULE_CONTRACT
//   PURPOSE: Thin wrapper over the git command line.
//   SCOPE: Read-only queries plus add, commit and push. Never force, never edits git configuration.
//   DEPENDS: none
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   run - run git in a directory and return trimmed stdout, or the error text
//   succeeds - true when a git command exits zero
//   toplevel - repository root for a directory
//   branch - current branch name
//   has_remote - whether a remote is configured
//   status_lines - porcelain status lines, optionally limited to a path, including untracked files
//   head - full commit id of HEAD
// END_MODULE_MAP

use std::path::{Path, PathBuf};
use std::process::Command;

pub fn run(dir: &Path, args: &[&str]) -> Result<String, String> {
    let out = Command::new("git")
        .arg("-C")
        .arg(dir)
        .args(args)
        .output()
        .map_err(|e| format!("cannot run git: {e}"))?;
    if out.status.success() {
        Ok(String::from_utf8_lossy(&out.stdout).trim_end().to_string())
    } else {
        let err = String::from_utf8_lossy(&out.stderr);
        let err = err.trim();
        Err(format!("git {} failed: {}", args.join(" "), if err.is_empty() { "no message" } else { err }))
    }
}

pub fn succeeds(dir: &Path, args: &[&str]) -> bool {
    Command::new("git")
        .arg("-C")
        .arg(dir)
        .args(args)
        .output()
        .map(|o| o.status.success())
        .unwrap_or(false)
}

pub fn toplevel(dir: &Path) -> Result<PathBuf, String> {
    run(dir, &["rev-parse", "--show-toplevel"]).map(PathBuf::from)
}

pub fn branch(dir: &Path) -> Result<String, String> {
    run(dir, &["symbolic-ref", "--short", "HEAD"])
}

pub fn has_remote(dir: &Path, name: &str) -> bool {
    run(dir, &["remote"]).map(|s| s.lines().any(|l| l.trim() == name)).unwrap_or(false)
}

pub fn status_lines(dir: &Path, only: Option<&Path>, untracked: bool) -> Result<Vec<String>, String> {
    let mut args: Vec<String> = vec!["status".into(), "--porcelain".into()];
    args.push(if untracked { "--untracked-files=all".into() } else { "--untracked-files=no".into() });
    if let Some(p) = only {
        args.push("--".into());
        args.push(p.to_string_lossy().into_owned());
    }
    let refs: Vec<&str> = args.iter().map(|s| s.as_str()).collect();
    run(dir, &refs).map(|s| s.lines().map(|l| l.to_string()).collect())
}

pub fn head(dir: &Path) -> Result<String, String> {
    run(dir, &["rev-parse", "HEAD"])
}
