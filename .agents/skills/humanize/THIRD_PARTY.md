# Third-party content

`humanize/data/vendor/` holds rule sets copied from these MIT-licensed Claude skills. Each folder keeps its original `LICENSE`; each entry file was renamed from `SKILL.md` to `instructions.md` so hosts do not load it as a separate skill.

| Folder | Source | License |
|---|---|---|
| `humanize/data/vendor/unslop/` | https://github.com/MohamedAbdallah-14/unslop (`skills/unslop`) | MIT, Copyright (c) 2026 Mohamed Abdallah |
| `humanize/data/vendor/humanize-pro/` | https://github.com/msdanyg/humanize-pro (`skills/humanize-pro`) | MIT, Copyright (c) 2026 Daniel Glickman |
| `humanize/data/vendor/humanize-writing/` | https://github.com/lguz/humanize-writing-skill (`skills/humanize-writing`) | MIT, Copyright (c) 2026 Luis Guzman |

`humanize/data/tells.json` derives its word and phrase lists from these sources; each entry records its source. `humanize/data/vale.ini` configures [Vale](https://vale.sh). Its styles are downloaded by `vale sync` at the pinned releases in `humanize/data/versions.json` and are not shipped:

| Style | Source | License |
|---|---|---|
| Microsoft | https://github.com/vale-cli/Microsoft | MIT |
| write-good | https://github.com/vale-cli/write-good | MIT |
