# Portal scaffolding

The scaffolding of the AICC charter site. It fixes the structure before the build: which pages exist, under which section, from which source, in what order, and what each page contains. It holds no charter text and defines no rule. The charter folder stays the only source of the content, and this folder is the plan for where each piece appears.

Status: scaffold, for review. The site is a static knowledge base and the department site of AICC, and its live matters are kept in the Registry, Jira, Confluence, and Service Management. The change that builds the site is `C-PORTAL-CHARTER` in `.grace/changes/active/`, and it is a draft. Nothing here is portal source until that change is approved, and the folder moves under `portal/` with it.

## Contents

| Item | Holds |
| --- | --- |
| [site-structure.md](site-structure.md) | The narrative: the kind of site, the sitemap, the navigation model, the page types, the wireframes, the authored items, and the open points |
| [content-fit.md](content-fit.md) | The evaluation of the first scaffold against the size and shape of the charter, and the reasons for the placement that this scaffold adopts |
| [inventory.md](inventory.md) | The table of all pages: section, address, type, source, sections of the source, words, and production |
| [sitemap.json](sitemap.json) | The sitemap in machine-readable form: the sections and the 73 pages |
| [pages/](pages/) | One outline file for each page, in a folder for each section |
| [reading-routes.md](reading-routes.md) | The five reading routes, as sequences of page identifiers |
| [voice.md](voice.md) | The voice and the labelling rules of the site, provisional until the style guidelines are issued |
| [make_pages.py](make_pages.py) | The page definitions, and the tool that writes the sitemap, the inventory, and the outline files from them |
| [check.py](check.py) | The check of the scaffolding against the charter |

## The sections

| Order | Section | Address | Holds |
| --- | --- | --- | --- |
| 1 | About AICC | /about/ | Statement of Intent (four pages), AICC Charter, the charter in outline, where AICC is stated |
| 2 | What AICC does | /what-aicc-does/ | Business Model, Engagement workflow and guide |
| 3 | How AICC works | /how-aicc-works/ | Portfolio Management Model (five pages), Solution Lifecycle Model (seven pages), Service delivery and Cadence workflows and guides, Collaboration tooling workflow |
| 4 | Organization | /organization/ | Operating Model foundations, Roles, Decisions, the Organization guide, and the seven Role pages |
| 5 | Responsible AI | /responsible-ai/ | AI Policy, AI risk and control workflow |
| 6 | Governance and oversight | /governance/ | The control loops, records and evidence, controls and the control catalogue, the records, controls, and measures of delivery, Unit governance workflow and guide |
| 7 | Library | /library/ | The 13 templates |
| 8 | Reference | /reference/ | Vocabulary, Document Catalog, change history, Records and systems |

## The outline file of a page

Each file in `pages/` begins with this front matter.

| Field | Meaning |
| --- | --- |
| id | The identifier of the page: section and name. It is stable and is used by the reading routes |
| title | The title that the page shows |
| section | The section that holds the page |
| order | The place of the page in its section, which also gives the previous and next links |
| type | The page type: home, section, document, workflow, guide, template, catalogue, reference, records, index, role, or outline |
| slug | The address of the page, the same in every language |
| source | The charter or Registry files that supply the content |
| source_sections | For a page of a split document, the numbers of the sections of the source that the page holds |
| document, part | For a page of a split document, the document and the place of the page among its parts |
| words | The size of the page, when the page holds a document or a part of one |
| companion | The workflow or the guide that explains the same subject |
| production | Authored (written for the site), generated (produced from the source), or a combination |
| status | Scaffold, until the page is built |

The body of the file holds the source, the sections of the source with their sizes, and the outline of the page.

## Rules of the scaffolding

1. Every file under `charter/` supplies the content of at least one page. Every section of a split document, and every workflow, guide, and template, has exactly one canonical page. `check.py` verifies it.
2. A document of more than 3,000 words is presented as pages of 600 to 1,800 words, cut at its top-level sections. Short sections are grouped, no section is divided, and the clause numbers and the permanent links do not change. A document of 3,000 words or fewer stays on one page.
3. The sitemap assigns each page to a section of the site, so that one document can serve more than one section without a second copy. A page that shows a document for another section is a view of the canonical page and holds no second text.
4. A guide sits beside its subject and names its workflow as its companion. The templates are cross-cutting forms and sit in the Library.
5. The site states no rule. An authored page introduces, orders, and links, and it restates nothing that a document says.
6. The addresses and the identifiers are the same in every language, so that a reference stays valid.
7. The page definitions are changed in `make_pages.py`. The tool writes the sitemap, the inventory, and the outline files, and `check.py` verifies the result.

## Use

```sh
python3 portal-scaffolding/make_pages.py
python3 portal-scaffolding/check.py
```
