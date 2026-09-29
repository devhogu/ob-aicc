// START_MODULE_CONTRACT
//   PURPOSE: aicc-deploy command line. Mirror the generated AICC site into the clean deploy repository,
//            commit it, push origin then websvc, and verify the served site. Dry run by default.
//   SCOPE: Orchestration only. Refuses unsafe states before any write. Writes only under html/aicc in the deploy repository.
//   DEPENDS: M-AICC-DEPLOY config, preflight, tree, manifest, sync and http modules
//   LINKS: M-AICC-DEPLOY, V-M-AICC-DEPLOY
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   main - parse arguments, run, map the result to an exit code
//   run - the whole flow for one configuration
// END_MODULE_MAP

mod config;
mod git;
mod http;
mod manifest;
mod preflight;
mod sha256;
mod sync;
mod tree;

use config::{Config, Parsed};
use std::process::ExitCode;
use std::time::Duration;

const SKIP_IN_DEST: [&str; 1] = [manifest::MANIFEST_NAME];

fn list(label: &str, paths: &[String]) {
    if paths.is_empty() {
        return;
    }
    println!("{label} ({}):", paths.len());
    for p in paths.iter().take(15) {
        println!("  {p}");
    }
    if paths.len() > 15 {
        println!("  ... and {} more", paths.len() - 15);
    }
}

fn run(cfg: &Config) -> Result<(), String> {
    let ctx = preflight::run(cfg)?;
    println!("Source:  {} (commit {})", ctx.source_dir.display(), sync::short(&ctx.source_commit));
    println!("Deploy:  {} -> {}/", ctx.deploy_repo.display(), config::DEST_SUBDIR);

    let source = tree::scan(&ctx.source_dir, &[]).map_err(|e| format!("cannot scan source: {e}"))?;
    let dest = tree::scan(&ctx.dest_dir, &SKIP_IN_DEST).map_err(|e| format!("cannot scan deploy folder: {e}"))?;
    let diff = tree::diff(&source, &dest);

    if diff.is_empty() {
        println!("Nothing to publish: the deploy folder already matches the source ({} files).", source.len());
        return Ok(());
    }
    list("Added", &diff.added);
    list("Changed", &diff.changed);
    list("Removed", &diff.removed);
    println!("Summary: {} added, {} changed, {} removed, {} files in total.", diff.added.len(), diff.changed.len(), diff.removed.len(), source.len());

    if !cfg.publish {
        println!("Dry run: nothing written, nothing pushed. Use --publish to publish.");
        return Ok(());
    }

    let manifest_text = manifest::render(&source, &ctx.source_commit);
    sync::apply(&ctx.source_dir, &ctx.dest_dir, &diff, &manifest_text).map_err(|e| format!("cannot write deploy folder: {e}"))?;
    println!("Mirrored into {}", ctx.dest_dir.display());

    match sync::commit_and_push(&ctx.deploy_repo, cfg, &ctx.source_commit, &diff)? {
        sync::Outcome::NothingStaged => {
            println!("Nothing staged after mirroring; no commit and no push.");
            return Ok(());
        }
        sync::Outcome::Pushed(remotes) => println!("Committed and pushed to: {}", remotes.join(", ")),
    }

    if cfg.skip_verify {
        println!("Verification skipped.");
        return Ok(());
    }
    println!("Verifying {} ...", http::manifest_url(&cfg.url));
    http::verify(&cfg.url, &manifest_text, Duration::from_secs(cfg.verify_timeout_secs), Duration::from_secs(2))?;
    println!("Verified: the served manifest matches what was published.");
    Ok(())
}

fn main() -> ExitCode {
    let args: Vec<String> = std::env::args().skip(1).collect();
    match config::parse(&args) {
        Ok(Parsed::Help) => {
            print!("{}", config::USAGE);
            ExitCode::SUCCESS
        }
        Ok(Parsed::Run(cfg)) => match run(&cfg) {
            Ok(()) => ExitCode::SUCCESS,
            Err(e) => {
                eprintln!("aicc-deploy: {e}");
                ExitCode::from(1)
            }
        },
        Err(e) => {
            eprintln!("aicc-deploy: {e}\n\n{}", config::USAGE);
            ExitCode::from(2)
        }
    }
}
