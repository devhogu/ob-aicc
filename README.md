# AICC

The AI Competence Center of O!Bank Kyrgyzstan. This repository is the source of truth for its governance, its records, and its portal. Its content holds no figures of the Bank, no data, no documents of the functions, and no code. It is private, and its content is promoted to the portal and to the corporate folder when it is ready.

| Folder | Holds | Promoted to |
| --- | --- | --- |
| [charter/](charter/README.md) | The static body of knowledge: documents, workflows, templates, and guides | The charter portal, the clean portal repository, and the corporate folder |
| [registry/](registry/README.md) | The process records: decisions, proposals, deliverables, and the state of the work | The corporate folder, and the registry view of the portal |
| [portfolio/](portfolio/README.md) | The catalog of the solutions and services that AICC defines and tries | The corporate folder, and the portfolio view of the portal |
| [wiki/](wiki/README.md) | Lineage, research, and open items behind the charter, and the archive of earlier versions | Stays here |
| `portal/`, `html/`, `deploy/` | The portal generator, its generated output, and the tool that publishes it | The output goes to the clean portal repository |
| [obank-uiux/](obank-uiux/README.md) | Shared O! brand, layout, assets, working examples and the Cloud LAB flow-first recipe | New internal page design and material restyling |

The `.grace/` folder and `CLAUDE.md` govern the portal as a software product.

For new UI or material restyling, start with the [O! UI/UX adoption guide](obank-uiux/ADOPT.md).

The portal is published from `html/aicc/` by the `aicc-deploy` tool. Each language has a router at `html/aicc/{en,ru}/index.html` that leads to five branches: `center/` (the charter, operating models, knowledge base and templates), `discovery/` (the Discovery Catalog), `portfolio/` (the Initiatives on the Portfolio Kanban), `program/` (the Program Kanban and the project documents) and `lab/` (the AI Lab).

The [STS O! workspace](html/sts/en/index.html) is a generated eight-page design trial built by [sts-portal/](sts-portal/README.md) from the retained [STS source](html-alt/sts/en/index.html). It sits outside the `aicc-deploy` publication scope.

The Discovery Catalog section of the portal is built from the Markdown records of the catalog in [portfolio/en/discovery/](portfolio/en/discovery/README.md) and `portfolio/ru/discovery/`, one record for each page in each language; the README there describes the record format.
