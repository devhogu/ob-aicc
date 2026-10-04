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

The standalone [Cloud LAB page](html/cloudlab/index.html) is a static package derived from the shared O! flow-first design trial in the EA repository. Its prior page is retained under [html-alt/cloudlab/](html-alt/cloudlab/index.html). The `aicc-deploy` tool publishes `html/aicc/`; Cloud LAB is outside that publisher's scope.

The [STS O! workspace](html/sts/en/index.html) is a generated eight-page design trial built by [sts-portal/](sts-portal/README.md) from the retained [STS source](html-alt/sts/en/index.html). It also sits outside the `aicc-deploy` publication scope.

The [CSR · Customer Service Resolution trial](html/csr/ru/index.html) is a generated bilingual proposal explorer built by [csr-portal/](csr-portal/README.md) from the retained [Customer Intelligence source](html-alt/intelligent-customer-service-resolution/ru/index.html). It is a standalone static trial outside `aicc-deploy`.

The [Financial Services O! trial](html/financial-services/ru/index.html) applies the shared brand shell and typography to all 152 retained bilingual framework pages. [Build and verification](finance-portal/README.md) preserve the source layouts and interactions; this conceptual framework is outside `aicc-deploy`.
