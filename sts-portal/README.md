# STS O! workspace trial

This builds a branded, static STS portal from the retained `html-alt/sts/en/` pages. The old pages are the content source; the transformation adds the shared O! shell, local fonts/assets, a lifecycle front door and visual rules that distinguish structure from sequence. It preserves the reference explorer and three interactive prototypes.

From the AICC repository root:

```sh
python3 sts-portal/build.py
python3 -m http.server 8904 --bind 0.0.0.0 --directory html/sts
```

Open `html/sts/` or `html/sts/en/`. Edit `sts-portal/assets/` for this trial's presentation and `html-alt/sts/en/` for the retained source content. `html/sts/` is generated; do not maintain its copied pages by hand. The source contains conceptual STS and industry-reference material; this trial does not establish O!Bank's actual operating model.

The shared style comes from `obank-uiux/site/` version 0.1.1. The application-specific layout follows `obank-uiux/design-system/content/cloud-lab.md`: sticky O! header, left navigation, central map, local horizontal scrolling, selectable activity detail and explicit flow meaning. STS's outer/inner model domains and ITIL practices remain classifications, while the managed-service states are the lifecycle example.

[Verification](verification.md) covers all eight pages, responsive layouts, the retained interactions and accessibility. The source and this trial are English-only; a Russian-first product requires actual translated content from shared identities and facts.
