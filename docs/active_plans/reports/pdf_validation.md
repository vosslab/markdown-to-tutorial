# PDF validation

Snapshot note (2026-10-22): the 88-page report below records an earlier build and is superseded
for current artifacts by [readiness_visual.md](readiness_visual.md), which reviewed the current
12 PDFs (65 pages). Do not use the older page count as the current output inventory.

Path note (2026-10-22): paths and command examples below use the current repository layout.
Recorded observations belong to their stated snapshots; renamed output manifests retain their
original contents until the final rebuild and verification refresh.

Final visual review: 2026-10-22. The final output PDFs were rendered after the last rebuild and visually reviewed across all pages.

All 12 tutorial bundles rebuilt successfully with the default `all` formats. The final PDFs contain 88 pages total. Every page was rendered at 110 dpi with PyMuPDF and visually inspected through contact sheets; pagination and table transitions were also inspected at full raster size. This is local LibreOffice PDF evidence; Google import, live link navigation, and spreadsheet recalculation are separate checks.

## Commands and artifacts

- Build environment: `source source_me.sh && python3`.
- Sequential command for each source: `python3 make_tutorial.py build tutorial_data/<name>.md`.
- The build process invoked LibreOffice outside the macOS sandbox using an approved escalated execution.
- Every final bundle build returned exit code 0.
- Final PDF SHA256 fingerprints and page counts: `tutorial_output/verification/pdf/render_inventory.json`.
- Current contact sheets: `tutorial_output/verification/pdf/contact_sheets/`, one per tutorial.
- Full-size pagination and image samples: `tutorial_output/verification/pdf/pages/`.
- Rendering: `fitz.open(pdf)` then `page.get_pixmap(dpi=110).save(path)`.
- Retained review images are under `tutorial_output/verification/pdf/`; the redundant `tests/_temp/pdf_review/` copies were removed after review.

## Page inventory

| Tutorial | Pages | Build status |
| --- | ---: | --- |
| babies_1_z_test | 8 | Exit 0 |
| babies_2_t_test | 6 | Exit 0 |
| babies_3_two_sample_t_test | 4 | Exit 0 |
| caffeine_1_descriptive_statistics | 3 | Exit 0 |
| caffeine_2_linear_regression | 8 | Exit 0 |
| caffeine_3_quadratic_regression | 9 | Exit 0 |
| microbes_1_z_test | 8 | Exit 0 |
| microbes_2_t_test | 7 | Exit 0 |
| microbes_3_two_sample_t_test | 12 | Exit 0 |
| microbes_4_f_test | 9 | Exit 0 |
| microbes_5_anova | 8 | Exit 0 |
| petase_1_linear_regression | 6 | Exit 0 |

Total: 88 pages.

## Visual findings

- No clipped page-margin text, overlapping content, unexpected blank pages, broken glyph boxes, or distorted image proportions were visible in the 88-page contact-sheet pass.
- Heading hierarchy, nested lists, blue cell references, formula text, and left-aligned tables remain legible. Long formulas fit the page, including the Welch degrees-of-freedom expression.
- Accepted pagination imperfection: `babies_1_z_test` page 8 contains only the short statistical-reference paragraph after the story on page 7. It is readable; no visual defect or content loss is present.
- `babies_2_t_test` no longer leaves the `One-Tailed Test` parent bullet alone at the bottom of page 4. Page 4 contains the section 8.2 introduction and test choices; page 5 continues with the p-value instructions. That continuation is understandable, though the page begins with a nested bullet rather than a repeated section label.
- `microbes_3_two_sample_t_test` splits the Welch example table across pages 4-5 at a row boundary. Page 5 repeats the column header; no row text is split or clipped.
- `microbes_5_anova` keeps the complete ANOVA setup table on page 2. Page 3 begins the group-statistics calculations; the previous split-table issue is resolved.
- PDFs have no visible footer page numbers. This was observed consistently; no page-number requirement was inferred.
- Retained screenshots and illustrations preserve their proportions. The historical spreadsheet screenshots in `babies_1_z_test` page 3 and protest illustration on page 7 have soft small labels; the normal-distribution illustration on page 5 and the chemical-structure image in `petase_1_linear_regression` remain legible at page size.

## Individual page inspections

Full-size PNG views supplement the all-page contact sheets:

- `babies_1_z_test`: pages 7-8 (illustration and isolated reference paragraph).
- `babies_2_t_test`: pages 4-5 (section continuation and tail-specific p-value formulas).
- `caffeine_2_linear_regression`: page 7 (LINEST, INDEX, and test formulas).
- `caffeine_3_quadratic_regression`: page 6 (quadratic formulas and explanation).
- `microbes_3_two_sample_t_test`: pages 4-5 (long Welch formula and repeated table header).
- `microbes_5_anova`: pages 2-3 (complete setup table and next-step transition).
- `petase_1_linear_regression`: page 1 (image and chemical structure).

## Diagnostic limits

The recorded source/compiler warnings include intentional range overshoots, unavailable-input analysis warnings, unsupported manual function coverage, and unmapped Google worksheets. PDF page counts and fingerprints identify the final rendered files; visual inspection does not resolve those warnings or verify external application behavior. Generated `validation.json` keeps external behavior marked `unchecked`; this report holds the manual PDF evidence.
