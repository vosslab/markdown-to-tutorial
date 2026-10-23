# Microbes 1-3 material quality

## Current verdict

The narrative restoration and workbook task flow are materially complete in the reviewed set. The
current Microbes 1-3 PDFs, DOCX files, and XLSX files show retained scenario and explanatory prose,
visible tail choices, distinct source/calculation/result/interpretation regions, and readable figures
and tables. One PDF pagination finding remains in this snapshot: Microbes 2 page 9 contains only the
standalone next-tutorial link. The final PDF rebuild and a fresh page check are still required after
the active pagination fixes; this is an artifact-quality review, not final acceptance.

No original PDFs were available, so prose fidelity was checked directly against the three Fall 2025
Markdown originals. The old files were read-only. The current files in `tutorial_output/` were treated
as the generated snapshot; SHA-256 values below identify exactly what was reviewed.

## Walkthrough and evidence

The review used a PDF page-contact walkthrough of all 30 pages (Microbes 1: 9, Microbes 2: 9,
Microbes 3: 12), then full-size inspection of Microbes 1 pages 3 and 6 and Microbes 3 pages 4 and 7.
The visual pass checked headings, page transitions, formula legibility, the normal/t reference
figures, the Welch degrees-of-freedom table, and the closing story. Workbook sheets were reviewed
cell-by-cell and rendered from disposable copies with fit-to-page print settings; those settings
and copies were not applied to the canonical workbooks.

| Tutorial | Original-to-output content evidence | Rendered PDF evidence |
| --- | --- | --- |
| Microbes 1 Z-test | Original lines 7-16 introduce Busse Woods, SSU rRNA sampling, the Shannon Index, the benchmark, and hypotheses. The generated PDF retains that sequence on page 1 while qualifying the 4.0 mean and 0.6 SD as stipulated scenario values. Original lines 194-214's supervisor email and transition to the t-test remain on page 9. | Page 5 retains the normal-curve illustration and cumulative-probability explanation. Page 6 visibly prints `In cell D14, enter 0.05.` with the period outside the value, followed by D15-D17 decision formulas. Page 7 retains the lower-tail interpretation and caveat that nonrejection does not establish equality. |
| Microbes 2 one-sample t-test | Original lines 7-21's unknown-population-SD setup and "Why Use a T-Test Now?" material remain on page 1. The generated explanation ties the t-test to estimating the unknown SD; it does not claim that a small sample becomes representative. The original uncertainty/advisor and move-to-2014/2024 narrative remains at the end of page 8. | Pages 1-8 retain the statistic, degrees-of-freedom, tail/function, IF, interpretation, practice, and takeaway sections. **Page 9 contains only** `...Ask the instructor for the next tutorial link.` (51 extracted characters); it is a nearly empty trailing page. |
| Microbes 3 Welch two-sample t-test | Original lines 7-13's advisor suggestion to compare 2014 with 2024 and its "Why Use a Two Sample T-Test Now?" explanation remain on page 1-2. The matched-location/independence limitation appears before the method. Original practice tasks and the advisor's variance/F-test transition remain on pages 11-12. | Page 4's six-row Welch adjustment table is readable without clipped cells. Page 5 retains the t-reference curves. Page 7 keeps the T.TEST input definitions, manual two-tail BETADIST method, and quick T.TEST calculation together; the formula and cell destinations are legible. Page 12 contains the F-test transition rather than an empty page. |

The old spreadsheet-copy instructions were replaced with the supplied workbook workflow. Generated
workbooks have one named worksheet each: `Microbial Z-Test`, `Microbial T-Test`, and `Two Sample
T-Test`. The visible observation rows are 2:25 (24 observations); rows below are open for practice.
Formula ranges through row 101 ignore empty observations. In the generated XLSX files, source cells
are blue (`#DCEAF7`), calculation cells teal (`#DCEFEA`), result cells orange (`#FCE6CF`), and the
interpretation entry lavender (`#EAE2F5`). The LibreOffice screenshots show these colors on the
actual sheet layout.

| Tutorial | Student walkthrough destinations | Workbook regions checked |
| --- | --- | --- |
| Microbes 1 | On `Microbial Z-Test`, enter the benchmark mean in D2 and SD in D3; the lesson then names D5/D6, D8, D10:D12, D14, D15:D17, and the written response D19. The rendered sheet leaves student calculation/result/interpretation cells blank. | Source A1:B101; calculation C1:D9 and C14:D14; results C10:D12 and C15:D17; interpretation C19:D19. |
| Microbes 2 | On `Microbial T-Test`, enter the sample mean, SD, and size in D4:D6, t and df in D8:D9, p-values in D10:D12, alpha in D14, decisions in D15:D17, and interpretation in D19. | Source A1:B101; calculation C1:E9 and C14:D14; results C10:E12 and C15:D17; interpretation C19:D19. |
| Microbes 3 | On `Two Sample T-Test`, enter year-specific statistics in E2:E13, manual and quick p-values in E16:G18, alpha in E21, decisions in E22:E24, and interpretation in E26. | Source A1:C101; calculation D1:G15 and D21:E21; results D16:G18 and D22:E24; interpretation D26:E26. |

## Limits and follow-up

This is an expert document inspection and task walkthrough. No students participated, and no claim is
made about observed student comprehension, task completion, or learning. No calculation behavior or
live Google Sheets behavior was evaluated here. The workbook screenshots establish rendered cell
layout and color, not spreadsheet formula execution.

After the current pagination fixes and final rebuild, rerender the three PDFs and inspect every page
again. Resolve or explicitly accept the Microbes 2 trailing-link page based on that fresh output.

## Snapshot identity

Source SHA-256:

| Source | SHA-256 |
| --- | --- |
| `tutorial_data/microbes_1_z_test.md` | `f11f071cae9b664383f4e83bdaa5838004b9e48ffd61ad758c31c7fc41f150c0` |
| `tutorial_data/microbes_2_t_test.md` | `7e75603806f07ce2762833e1778774ea94fcd5775d02caee7fd504e7160b3d3f` |
| `tutorial_data/microbes_3_two_sample_t_test.md` | `86ca0cce468641ada1dce58f22239b728e46921d96b75a753be46bcbf41e49a8` |

Generated artifact SHA-256:

| Tutorial | PDF | DOCX | XLSX |
| --- | --- | --- | --- |
| Microbes 1 | `65a41965197b5248a98fb3ed2bca7232220b5af3b6b3e1b6924696460b04cb08` | `705fff032e3284ca44a9148257c0634f943638b50a37794ec54d009773cf1c9a` | `2cb426c4c94df8fabd4bb6338ac57e715822f8db8abfc6c20c0bce75a031d096` |
| Microbes 2 | `a08c7d02e4730d646727d425dbc557ac23aadb5c361a43da401e87a20b155c0f` | `7f62fb5fff5743ced3eacc0eaee69e8cef863be384e80db9320ef96bc6830a9f` | `89bce79275e087ff342db229d2ff506ba66245958f7b91203568462bdb9544713` |
| Microbes 3 | `011bc3e53224f2e7bc4cb465dc76b5e2995a00e2324ba6e110616c78e4fb21a9` | `fabb79e49130620cb81268d4db3dc7cb764d73ae2078c67c91fd0be72bc7aeec` | `d12a8c64d3b6f5701486ced08c64974138f34493eccf8ca2378dfccd4821161f` |
