# Caffeine materials quality review

**Decision: CHANGES NEEDED** for the reviewed 2026-10-22 generated artifacts. The
restored voice and workbook organization are substantially improved, but visible
Markdown backslashes and missing descriptive-statistic destinations require correction
and fresh rendered review. Source SPEC acceptance does not close these findings.

## Method and evidence

This is an expert cognitive walkthrough and visual document inspection using the
`hic-human-interact-expert` and `pdf-guide` skills. Intended learners are students
following the PDF/DOCX while working in the supplied blank XLSX. The review asks whether
each next action is visible, has a findable destination, preserves the explanation and
author voice, and leads to recognizable completion evidence. It is not a student study.

I directly compared the read-only original
`/Users/vosslab/nsh/SLIDES/djot-slide-builder/Tutorial_Outline.md` (excluding base64)
and `/private/tmp/caffeine_source.xlsx`, the restoration plan and human guidance,
current lesson sources, and the three actual student bundles. I inspected all 20 PDF
pages in three contact sheets (3, 10, and 7 pages), then full-size representative pages
for task instructions, equations, tests, charts, and typography. I also checked DOCX
paragraph content, and rendered all three current workbooks and the original workbook's
Data, Linear Regression, reflection, and Quadratic Regression sheets.

Evidence is under `tutorial_output/voice_restoration/quality_caffeine/`:

- `lesson{1,2,3}_contact.webp`: complete PDF page coverage.
- `lessonN_pagePP.webp`: every page rendered at 1.5 scale, WebP quality 90.
- `lesson3_page04.webp`: the four-item squared-column sequence and original joke.
- `lesson2_page04.webp`, `lesson2_page06.webp`, `lesson2_page08.webp`, and
  `lesson2_page09.webp`: full-size chart, equations, test, and reflection examples.
- `lesson1_page02.webp` and `lesson1_page03.webp`: descriptive-statistic task flow.
- `workbook1.webp`, `workbook2.webp`, and `workbook3.webp`: actual blank workbook views.
- `original_sheet2.webp` and `original_sheet4.webp`: original linear/quadratic role areas.
- `rejected_before_squared.webp`: rejected before-output comparison.
- `workbook_structure.json` and `walkthrough_checks.json`: supporting cell evidence.

Workbook render copies change only print/display settings (landscape A3, fit to page,
print bounds/margins, and printed grid/row/column headings). No cell values, formulas,
fills, widths, or labels were added. The canonical workbooks remain unchanged. The
provided screenshot skill LibreOffice script ran outside the sandbox for every export.

## Required corrections

1. **Remove literal hard-break backslashes from student output.** Caffeine 3 page 4
   displays a trailing backslash after numbered items 1, 2, and 3, and after the
   quadratic-regression definition. Caffeine 2 page 4 has an isolated backslash beneath
   the scatterplot and backslashes after nearly every chart action. Pages 6, 8, and 9
   show the same fault in formulas, hypotheses, and interpretation prompts. This is
   pervasive presentation noise that makes source markup look like learner input.
   DOCX content independently contains 7, 51, and 10 paragraphs with literal backslashes
   across lessons 1, 2, and 3. Handle authored hard breaks in the shared conversion path,
   rebuild, and visually verify the affected lists and charts. Do not delete prose or
   flatten the restored grouping to remove the symptom.
2. **State the sleep-formula destinations visibly.** Caffeine 1 page 2 says to use
   `=AVERAGE(A2:A26)` and `=MEDIAN(A2:A26)` but never says E2 or E3; page 3 similarly
   omits E4 for `=STDEV.S(A2:A26)`. Their semantic action destinations are hidden from
   the printed reader. The paired exam formulas explicitly name F2/F3/F4. Because the
   actual XLSX has blank D:F cells, learners must infer the missing sleep destinations.
   Add only the technical references `in E2`, `in E3`, and `in E4` to existing prose and
   verify the rebuilt pages. Preserve the original explanations.

Both findings were sent to the manager during review; no code or lesson-source edits
were made in this review lane.

## Voice and document findings

The four-item squared-column task survives as one compact group on Caffeine 3 page 4
(standalone Step 3, corresponding to original outline Step 9). The introduction, label,
formula, fill action, and full 36-hours joke are visible together. The rejected page 3
instead exposed separate Label/Enter/Fill/Do/Check logs and adjacent-predictor actions.
Current E/F predictor staging appears later on page 5, after the equation explanation;
it does not interrupt or repeat the squared-column task.

The actual pages retain the welcome/orientation and Tania + Roohana heading in lesson 1;
the coffee, dots, hypotheses, hypothetical example, and reflection voice in lesson 2;
and the plot-twist, receipts, roller-coaster, snack, and browser-tabs voice in lesson 3.
Headings are prominent blue and descriptive rather than generic action labels. Formulas
are visibly green, distinct from ordinary prose. The current pages do not expose semantic
URIs or a second visible operation inventory.

Equations and symbols are readable: linear/quadratic equations use explicit `y-hat`
notation with nearby definitions; squared exponents, R-squared, beta hypotheses, alpha,
and inequality symbols display without missing-glyph boxes. The comparison figure has
readable axis labels, the same 25 students, and both fitted R-squared values. Two-tailed
direction is explicit both in the test explanations and beside the p-value answer blanks
(linear page 9; quadratic pages 5-6). Curvature, exploratory inference, association,
and extrapolation limits remain visible.

Page layout is legible, with no observed clipping or overlap. Some pagination is loose:
linear page 5 has substantial whitespace, page 10 carries only the final reflection,
and quadratic page 2 has a sparse lower half. The four-item task stays together and no
heading is stranded without following content. These are polish observations, not new
blockers requiring prose compression or a new layout system.

## Workbook walkthrough

All three actual XLSX files contain the original 25 A/B observation pairs, confirmed
against the original Data sheet, and every cell outside A:B is blank. Blank labels and
answers therefore need to be supplied by the learner; the previews do not fake completed
work. Source data is blue, calculations teal, results orange, and interpretation purple,
with visible borders and spatial separation. These are meaningful task regions, not
merely XML fills verified without rendering.

The original Linear Regression and Quadratic Regression sheets use blue source headers,
orange calculation headers, green statistics headers, a red linear significance-test
header, and grey separator columns. They seed measure labels while leaving regression
data/calculations blank; the original reflection sheet separates written prompts. The
new single-sheet lesson workbooks keep each lesson self-contained, seed the actual paired
data, preserve findable calculation/statistics/test areas, and reserve a distinct written
response region. This is a coherent functional translation, although the original's
preseeded text labels are now learner-entered. Exact cell references in the lesson are
therefore essential; the missing E2/E3/E4 references above are consequential.

| Learner task | Actual blank destination and visible cue | Walkthrough result |
| --- | --- | --- |
| Descriptive summary | D1:F4 teal table; D6:F8 purple written area | Headers and exam-score cells stated; sleep destinations need the correction above. |
| Linear fit and prediction | D1:E14 teal block; E2, E6, E10, E14 blank | Instructions name the label/value cells and match the source A/B ranges. |
| Linear statistics and test | G1:H5 and J2:K10 orange blocks | Scalar LINEST, t, degrees of freedom, and two-tailed p-value have explicit destinations; no spill area is assumed. |
| Linear reflections | M2:O12 purple block or accompanying notes | Opening instruction names the region; source data remains separate. |
| Square sleep once, fill down | C1:C26 teal column beside A/B | Four-item task follows the reserved column; 25 source rows identify the fill extent. |
| Stage adjacent predictors | E1:F26 separate teal block | E2/F2 formulas, fill to row 26, and last-row checks are stated; B is not accidentally included as a predictor. |
| Quadratic fit/test | H1:I11 orange block | Coefficients, reverse LINEST order, residual df, prediction, t, and two-tailed p-value instructions match blank destinations. |
| Compare and explain | L1:M4 orange linear comparison; L7:N16 purple response area | Recreated linear fit makes this workbook independent of prior completed work; final submission criteria are visible. |

This review establishes blank-workbook task mapping and local rendered appearance. It
does not claim live Google Docs/Sheets import, Google calculation behavior, participant
completion rates, or learner outcomes. Those remain unverified here. A fresh review of
rebuilt PDFs/DOCX must close both required corrections before this lane can be accepted.
