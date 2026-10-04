# CSR · Customer Service Resolution

This standalone O! workspace trial builds `html/csr/` from the retained bilingual project proposal under `html-alt/intelligent-customer-service-resolution/`. Russian is the entry page; English is available from the same navigation. The original 34 diagrams per language, proposal text, document anchors and diagram viewer remain the content source.

```sh
python3 csr-portal/build.py
python3 -m http.server 8905 --bind 0.0.0.0 --directory html/csr
```

The new front-door map takes its eight case-work stages and improvement loop directly from the proposal's process-integration table. It distinguishes existing service work from **proposed** intelligence support; it is not evidence of a live Bank process. CSS and interaction code live in `csr-portal/assets/`; the shared font, token and workspace files come from `obank-uiux/site/`. `html/csr/` is generated output.

[Verification](verification.md) covers responsive layouts, bilingual navigation, themes, map selection and the original diagram viewer.
