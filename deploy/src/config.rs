// START_MODULE_CONTRACT
//   PURPOSE: Defaults and command-line parsing for aicc-deploy.
//   SCOPE: Every path, remote name and URL default lives here, in one place.
//   DEPENDS: none
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   DEFAULT_SOURCE - generated site, relative to the working directory
//   DEFAULT_DEPLOY_REPO - clean deploy repository on this host
//   DEST_SUBDIR - folder inside the deploy repository that is served
//   DEFAULT_URL - internal served URL used for verification
//   DEFAULT_BRANCH - expected branch in the deploy repository
//   DEFAULT_REMOTES - push order: storage remote, then the deploy trigger
//   DEFAULT_CHECK_CMD - command that proves html/aicc equals a fresh build
//   Config - resolved settings
//   parse - parse command-line arguments
//   USAGE - help text
// END_MODULE_MAP

use std::path::PathBuf;

pub const DEFAULT_SOURCE: &str = "html/aicc";
pub const DEFAULT_DEPLOY_REPO: &str = "/devops/websvc/websvc-ob-aicc";
pub const DEST_SUBDIR: &str = "html/aicc";
pub const DEFAULT_URL: &str = "http://hetzner-cx43.alpines-krait.ts.net/aicc/";
pub const DEFAULT_BRANCH: &str = "main";
pub const DEFAULT_REMOTES: [&str; 2] = ["origin", "websvc"];
pub const DEFAULT_CHECK_CMD: &str = "python3 portal/tools/check.py --idempotent";

pub const USAGE: &str = "aicc-deploy - publish the generated AICC portal to the deploy repository

Usage: aicc-deploy [options]

Default is a dry run: it checks everything and prints what would change, and writes nothing.

Options:
  --publish              mirror the site, commit, push origin then websvc, verify the served site
  --dry-run              show what would change (default)
  --source DIR           generated site to publish (default: html/aicc)
  --deploy-repo DIR      clean deploy repository (default: /devops/websvc/websvc-ob-aicc)
  --url URL              served URL used for verification (default: internal Tailscale URL)
  --branch NAME          expected deploy branch (default: main)
  --no-origin            do not push origin (still pushes websvc)
  --check-cmd CMD        command run in the source repository first (default: python3 portal/tools/check.py --idempotent)
  --skip-verify          do not fetch the served manifest afterwards
  --verify-timeout SECS  how long to wait for the served site to match (default: 30)
  --help                 show this text

Exit codes: 0 success or nothing to do, 1 refused or failed, 2 usage error.
";

#[derive(Debug, Clone)]
pub struct Config {
    pub source: PathBuf,
    pub deploy_repo: PathBuf,
    pub url: String,
    pub branch: String,
    pub remotes: Vec<String>,
    pub check_cmd: String,
    pub publish: bool,
    pub skip_verify: bool,
    pub verify_timeout_secs: u64,
}

impl Default for Config {
    fn default() -> Self {
        Config {
            source: PathBuf::from(DEFAULT_SOURCE),
            deploy_repo: PathBuf::from(DEFAULT_DEPLOY_REPO),
            url: DEFAULT_URL.to_string(),
            branch: DEFAULT_BRANCH.to_string(),
            remotes: DEFAULT_REMOTES.iter().map(|s| s.to_string()).collect(),
            check_cmd: DEFAULT_CHECK_CMD.to_string(),
            publish: false,
            skip_verify: false,
            verify_timeout_secs: 30,
        }
    }
}

pub enum Parsed {
    Run(Config),
    Help,
}

pub fn parse(args: &[String]) -> Result<Parsed, String> {
    let mut cfg = Config::default();
    let mut i = 0;
    let value = |i: &mut usize, flag: &str| -> Result<String, String> {
        *i += 1;
        args.get(*i).cloned().ok_or_else(|| format!("{flag} needs a value"))
    };
    while i < args.len() {
        match args[i].as_str() {
            "--help" | "-h" => return Ok(Parsed::Help),
            "--publish" => cfg.publish = true,
            "--dry-run" => cfg.publish = false,
            "--no-origin" => cfg.remotes.retain(|r| r != "origin"),
            "--skip-verify" => cfg.skip_verify = true,
            "--source" => cfg.source = PathBuf::from(value(&mut i, "--source")?),
            "--deploy-repo" => cfg.deploy_repo = PathBuf::from(value(&mut i, "--deploy-repo")?),
            "--url" => cfg.url = value(&mut i, "--url")?,
            "--branch" => cfg.branch = value(&mut i, "--branch")?,
            "--check-cmd" => cfg.check_cmd = value(&mut i, "--check-cmd")?,
            "--verify-timeout" => {
                cfg.verify_timeout_secs = value(&mut i, "--verify-timeout")?
                    .parse()
                    .map_err(|_| "--verify-timeout needs a whole number of seconds".to_string())?
            }
            other => return Err(format!("unknown option {other}")),
        }
        i += 1;
    }
    Ok(Parsed::Run(cfg))
}

#[cfg(test)]
mod tests {
    use super::*;

    fn args(v: &[&str]) -> Vec<String> {
        v.iter().map(|s| s.to_string()).collect()
    }

    fn cfg(v: &[&str]) -> Config {
        match parse(&args(v)).unwrap() {
            Parsed::Run(c) => c,
            Parsed::Help => panic!("help"),
        }
    }

    #[test]
    fn default_is_dry_run_with_both_remotes() {
        let c = cfg(&[]);
        assert!(!c.publish);
        assert_eq!(c.remotes, vec!["origin", "websvc"]);
    }

    #[test]
    fn publish_and_no_origin() {
        let c = cfg(&["--publish", "--no-origin", "--skip-verify"]);
        assert!(c.publish && c.skip_verify);
        assert_eq!(c.remotes, vec!["websvc"]);
    }

    #[test]
    fn dry_run_after_publish_wins_last() {
        assert!(!cfg(&["--publish", "--dry-run"]).publish);
    }

    #[test]
    fn values_are_taken() {
        let c = cfg(&["--source", "s", "--deploy-repo", "d", "--url", "u", "--branch", "b", "--verify-timeout", "5"]);
        assert_eq!(c.source, PathBuf::from("s"));
        assert_eq!(c.deploy_repo, PathBuf::from("d"));
        assert_eq!((c.url.as_str(), c.branch.as_str(), c.verify_timeout_secs), ("u", "b", 5));
    }

    #[test]
    fn errors() {
        assert!(parse(&args(&["--nope"])).is_err());
        assert!(parse(&args(&["--source"])).is_err());
        assert!(parse(&args(&["--verify-timeout", "x"])).is_err());
    }
}
