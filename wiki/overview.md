# Overview

Static HTML portal presenting the AICC's strategy, Statement of Intent, roadmap, knowledge base, and lifecycle-management processes. The formal documents that define AICC are kept in the [charter folder](../charter/README.md), and the Records of the Portfolio in the [portfolio folder](../portfolio/README.md).

## Users

- O!Bank staff across business functions adopting GenAI
- AICC team members who maintain portal content

## Constraints

- Published output is static HTML; no server-side runtime.
- This repo is the only source. The deployment repo gets rendered output only.
- Confirm audience and data classification before publishing content.

## How the portal is built and published

- Python 3 scripts under `portal/tools` build the site (`build.py`) into `html/aicc` and check it (`check.py`).
- The Rust tool `aicc-deploy` (in `deploy/`) mirrors `html/aicc` into the clean deployment repository. It is a dry run unless `--publish` is given.
- The portal copy of a charter document is republished from the charter folder; the charter folder is the source.

## Source of truth

- [requirements](../.grace/context/requirements.xml)
- [technology](../.grace/context/technology.xml)
- [deployment](../.grace/context/deployment.xml)
