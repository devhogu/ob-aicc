// START_MODULE_CONTRACT
//   PURPOSE: Refuse unsafe states before anything is written.
//   SCOPE: Source site and checkout, source build check, deploy repository state.
//   DEPENDS: M-AICC-DEPLOY git and config modules
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   Context - resolved paths and the source commit
//   run - run every check and return the context, or one clear refusal message
//   outside_dest - status lines that fall outside the served folder
// END_MODULE_MAP

use crate::config::{Config, DEST_SUBDIR};
use crate::git;
use std::path::PathBuf;
use std::process::Command;

pub struct Context {
    pub source_dir: PathBuf,
    pub source_commit: String,
    pub deploy_repo: PathBuf,
    pub dest_dir: PathBuf,
}

/// Porcelain status lines whose path is not inside `dest_prefix` (for example `html/aicc/`).
pub fn outside_dest(lines: &[String], dest_prefix: &str) -> Vec<String> {
    lines
        .iter()
        .filter(|l| {
            let path = l.get(3..).unwrap_or("");
            path.split(" -> ").any(|p| !p.trim_matches('"').starts_with(dest_prefix))
        })
        .cloned()
        .collect()
}

pub fn run(cfg: &Config) -> Result<Context, String> {
    // Source site
    let source_dir = cfg.source.canonicalize().map_err(|e| format!("source {} not found: {e}", cfg.source.display()))?;
    for required in ["index.html", "ru/index.html", "en/index.html"] {
        if !source_dir.join(required).is_file() {
            return Err(format!("source site is incomplete: {} is missing", source_dir.join(required).display()));
        }
    }

    // Source checkout
    let source_repo = git::toplevel(&source_dir).map_err(|e| format!("source is not inside a git repository: {e}"))?;
    let tracked = git::status_lines(&source_repo, None, false)?;
    if !tracked.is_empty() {
        return Err(format!(
            "source checkout has uncommitted changes to tracked files ({}). Commit them first so the published copy names a real commit.",
            tracked.first().unwrap().trim()
        ));
    }
    let site = git::status_lines(&source_repo, Some(&source_dir), true)?;
    if !site.is_empty() {
        return Err(format!(
            "generated site has uncommitted or untracked files ({}). Commit the rebuilt site first.",
            site.first().unwrap().trim()
        ));
    }
    let source_commit = git::head(&source_repo).map_err(|e| format!("source has no commit: {e}"))?;

    // Source build check
    let check = Command::new("sh").arg("-c").arg(&cfg.check_cmd).current_dir(&source_repo).output()
        .map_err(|e| format!("cannot run the source check: {e}"))?;
    if !check.status.success() {
        return Err(format!(
            "source check failed ({}), so html/aicc is not a verified fresh build:\n{}{}",
            cfg.check_cmd,
            String::from_utf8_lossy(&check.stdout),
            String::from_utf8_lossy(&check.stderr)
        ));
    }

    // Deploy repository
    let deploy_repo = cfg.deploy_repo.canonicalize().map_err(|e| format!("deploy repository {} not found: {e}", cfg.deploy_repo.display()))?;
    let top = git::toplevel(&deploy_repo).map_err(|e| format!("deploy path is not a git repository: {e}"))?;
    if top.canonicalize().map_err(|e| e.to_string())? != deploy_repo {
        return Err(format!("deploy path {} is not the root of its git repository ({})", deploy_repo.display(), top.display()));
    }
    let branch = git::branch(&deploy_repo).map_err(|e| format!("deploy repository has no current branch: {e}"))?;
    if branch != cfg.branch {
        return Err(format!("deploy repository is on branch '{branch}', expected '{}'", cfg.branch));
    }
    for remote in &cfg.remotes {
        if !git::has_remote(&deploy_repo, remote) {
            return Err(format!("deploy repository has no remote named '{remote}'"));
        }
    }
    let status = git::status_lines(&deploy_repo, None, true)?;
    let prefix = format!("{DEST_SUBDIR}/");
    let stray = outside_dest(&status, &prefix);
    if !stray.is_empty() {
        return Err(format!(
            "deploy repository has changes outside {DEST_SUBDIR}/ ({}). Commit or discard them first.",
            stray.first().unwrap().trim()
        ));
    }

    Ok(Context { dest_dir: deploy_repo.join(DEST_SUBDIR), source_dir, source_commit, deploy_repo })
}

#[cfg(test)]
mod tests {
    use super::*;

    fn l(s: &str) -> String {
        s.to_string()
    }

    #[test]
    fn changes_inside_dest_are_allowed() {
        let lines = vec![l(" M html/aicc/index.html"), l("?? html/aicc/new/x.html"), l("D  html/aicc/old.html")];
        assert!(outside_dest(&lines, "html/aicc/").is_empty());
    }

    #[test]
    fn changes_outside_dest_are_reported() {
        let lines = vec![l(" M README.md"), l(" M html/aicc/index.html"), l("?? html/other/x")];
        assert_eq!(outside_dest(&lines, "html/aicc/"), vec![l(" M README.md"), l("?? html/other/x")]);
    }

    #[test]
    fn renames_are_checked_on_both_sides() {
        let lines = vec![l("R  html/aicc/a.html -> README.md")];
        assert_eq!(outside_dest(&lines, "html/aicc/").len(), 1);
    }

    #[test]
    fn similar_prefix_is_not_inside() {
        let lines = vec![l(" M html/aicc-extra/x")];
        assert_eq!(outside_dest(&lines, "html/aicc/").len(), 1);
    }
}
