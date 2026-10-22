# Regression specification recheck

Date: 2026-10-22. This is a fresh, product-facing recheck of the rebuilt caffeine and PETase
DOCX/PDF bundles after the figure and label-pagination corrections. It addresses the earlier
[regression specification findings](teaching_regression_spec.md), not the separate classroom-quality
review.

## Artifacts and method

Inspected the current files under `tutorial_output/<stem>/`, not the earlier regression-review PNGs
or staged DOCX files. Their modification times are 2026-10-22 16:51:14-16:51:36 local time. Reopened
the actual DOCX files with python-docx (paragraph content and embedded-image counts), extracted text
from each actual PDF with `pdftotext -layout`, and rendered all 24 current PDF pages with Poppler
`pdftoppm -scale-to 1100 -png`. Reviewed the rendered pages in four contact sheets and opened the
affected pagination pages individually. Page PNGs, inspected WebP copies (quality 90), contact
sheets, and extracted text are in
`tutorial_output/verification/teaching_review/regression_spec_recheck/`.

| Bundle | DOCX embedded images | PDF pages |
| --- | ---: | ---: |
| Caffeine descriptive statistics | 1 | 3 |
| Caffeine linear regression | 6 | 8 |
| Caffeine quadratic regression | 5 | 7 |
| PETase linear regression | 2 | 6 |

All four PDFs show sequential printed page numbers. The rendered text and figures fit within their
page margins; no clipped content, missing glyphs, or page breaks through text were visible. The
actual DOCX documents contain the expected current text and their embedded illustrations. No
LibreOffice process was launched. This inspection does not claim live Google Sheets behavior.

## R1: Chart-bearing illustrations - resolved

- Caffeine 2 p2 now shows the neutral researcher illustration in the research-question section;
  the conflicting `caffeine_04.png` placard is absent. On p4, the actual 25-observation scatterplot
  has Hours of sleep on x and Final exam score (%) on y; its visible point pattern rises overall.
- Caffeine 3 p1 no longer presents the `caffeine_09.png` invented missing-data scenario. On p6,
  the model comparison uses the same 25 observations and shared axes, shows the quadratic curve
  bending downward, and reports linear R-squared 0.347 and quadratic R-squared 0.847.
- `caffeine_04.png`, `caffeine_09.png`, and `caffeine_13.png` remain in the asset directory, but
  the current caffeine source files no longer reference them. Neutral story illustrations remain
  in the current DOCX/PDF bundles.

## R2: Chart reentry instructions - resolved

The current rendered pages include the explicit action before returning to chart customization:

- Caffeine 2 p6, Step 4: "Double-click your scatterplot."
- Caffeine 3 p6, Step 6: "Double-click your scatterplot."
- PETase p4, Part 1 Step 5: "Double-click your scatterplot."

These actions appear after the relevant worksheet work and before the Chart editor instructions.

## R3: Label and formula page splits - resolved

The actual rendered PDF now keeps all three label/formula pairs on one page:

- Caffeine 2 p7: `Label G2: Slope` followed by `Enter H2`.
- Caffeine 3 p5: `Label H5: Quadratic R-squared` followed by `Enter I5`.
- PETase p4: `Label F3: Intercept (A595)` followed by `Enter G3`.

The adjacent entries remain readable, and their labels do not end the preceding page. No forced page
break is needed for these pairs.

## Sequence and verdict

The current PDFs show coherent generated sequences: Caffeine 1 Part 1 Steps 1-5; Caffeine 2 Part 1
Steps 1-7, with 3.1-3.2 and 6.1-6.4; Caffeine 3 Part 1 Steps 1-7; PETase Part 1 Steps 1-6 and
Part 2 Steps 1-5. Each sequence follows the printed page order.

R1-R3 are resolved in the rebuilt products. This recheck found no new specification blocker in the
four regression bundles. It does not replace the requested fresh classroom-quality/HCI review or
establish interactive chart editing in Google Sheets.
