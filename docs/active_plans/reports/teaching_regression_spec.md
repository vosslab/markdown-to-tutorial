# Regression lesson specification review

Date: 2026-10-22. This is an independent product/specification review of the rebuilt caffeine
and PETase bundles, not a classroom-quality approval. Required corrections remain below.

## Reviewed artifacts and method

Read the four complete current lesson sources, the original caffeine outline prose (excluding
embedded base64 image definitions), the original PETase scenario/assay sections and contaminated
continuation, [TUTORIAL_SPEC.md](../../TUTORIAL_SPEC.md), and
[teaching_regression_fixes.md](teaching_regression_fixes.md). The latter identifies intended
changes but does not establish their success. Original caffeine is a draft foundation, not a
quality benchmark. The original PETase Bradford task supplies teaching intent; its subsequent
microbial mean-test material does not.

Used the repo-rules-reader and pdf-guide skills. Read `AGENTS.md`, the relevant style guides,
and the latest changelog entry. Python inspection uses `source source_me.sh && python3`.
No LibreOffice process was launched in this review and no source/product files were edited.

Inspected these actual bundles under `tutorial_output/<stem>/`:

| Stem | PDF pages | PDF creation, local time |
| --- | --- | --- |
| caffeine_1_descriptive_statistics | 3 | 2026-10-22 16:46:20 |
| caffeine_2_linear_regression | 8 | 2026-10-22 16:46:23 |
| caffeine_3_quadratic_regression | 7 | 2026-10-22 16:46:25 |
| petase_1_linear_regression | 6 | 2026-10-22 16:46:40 |

All 24 PDF pages were newly rendered with `pdftoppm -scale-to 1100 -png` and individually
viewed. No old contact sheet was used. Fresh page images and extracted page text are in
`tutorial_output/verification/teaching_review/regression_spec/`; filenames are
`<stem>-<page>.png` and `<stem>.txt`. The actual DOCX files were reopened with python-docx;
the actual initial XLSX files were reopened with openpyxl. `bundle_inspection.json` records
artifact SHA256 hashes, headings, seeds, blank targets, widths, wrapping, and heights.

The workbook walkthrough follows the visible instruction order against actual initial cells.
It checks availability and assignments, not interaction with a live Google session. No live
Google import, formula calculation, chart creation, or rendered spreadsheet screenshot is claimed.

## Required corrections

### R1: Align chart-bearing illustrations

These are visible instructional contradictions, not decoration preferences. Correct the specific
illustrations while retaining neutral character art and the academy story.

| Actual page and step | Observed problem | Required result |
| --- | --- | --- |
| Caffeine 2 p4, Step 3 / 3.1 | `caffeine_06.png` is positioned immediately above sleep-versus-score chart instructions, but its large chart explicitly says caffeine concentration versus final score and shows a negative slope. | The worked/example visual must use the requested sleep x-axis and score y-axis, or be unmistakably separated from the actual-data chart task. The actual data have a positive fitted linear slope. |
| Caffeine 3 p1, introduction / Step 1 | `caffeine_09.png` describes original data with maximum 9 hours and newly complaining students reporting up to 14 hours. | Remove this invented missing-data scenario from the actual dataset introduction. All 25 observations are already supplied and the observed range is 3 to 11.5 hours. |
| Caffeine 3 p6, Step 6 | `caffeine_13.png` shows an upward-opening U and quadratic R-squared 0.88 as the better fit. The adjacent prose corrects only the number to 0.847. | The comparison visual must show the fitted downward curvature and agree with the supplied data. The current numeric disclaimer does not correct the opposite curve direction. |
| Caffeine 2 p2, Step 1 | `caffeine_04.png` includes a bottom-right DATA COLLECTED placard with a garbled/invented student count and caffeine-intake text. The visible prompt otherwise asks the correct sleep research question. | Remove/correct that conflicting placard, or replace this illustration with a neutral research-question visual. Do not infer a precise sample count from its unclear lettering. |

Evidence: the four named fresh page PNGs; native `caffeine_04.png` was additionally viewed to
avoid reporting its unclear sample-count lettering as an exact number.

Other illustrations are not the same defect: caffeine 2 p5's small alternative-pattern sketches
are conceptual contrasts, caffeine 3 p4 illustrates a general polynomial equation rather than
an asserted fit, and caffeine 3 p7's final sleep question is story humor followed by explicit
causal/extrapolation limits. These do not require blanket removal.

### R2: Activate the chart

The repeated chart-editing tasks need a short instruction to reopen the chart editor after
working in worksheet cells:

- Caffeine 2 p6, Step 4: after computing `E2`, `E6`, and `E10`, the next visible action selects
  `A1:B26`, then chooses Chart editor > Customize > Series. A sheet-range selection does not
  itself activate the existing chart.
- Caffeine 3 p6, Step 6: after the model and test calculations, the text immediately chooses
  Chart editor > Customize > Series > Trendline.
- PETase p3-4, Part 1 Step 5: after entering `G2:G4`, the text immediately chooses Chart editor
  > Customize > Series > Trendline.

Add a direct action such as "Double-click your scatterplot" at these three reentry points.
Google's official [trendline instructions](https://support.google.com/docs/answer/6075154?hl=en)
start chart customization by double-clicking the chart. This is an instruction-completeness
finding; actual live Sheets execution was not available.

### R3: Keep label and entry together

Three otherwise readable page boundaries split a label from its immediately following formula
in the same worksheet row:

- Caffeine 2 p6 ends with `Label G2: Slope`; p7 begins with `Enter H2: =INDEX(...)`.
- Caffeine 3 p4 ends with `Label H5: Quadratic R-squared`; p5 begins with `Enter I5: =INDEX(...)`.
- PETase p3 ends with `Label F3: Intercept (A595)`; p4 begins with `Enter G3: =INTERCEPT(...)`.

Keep each adjacent label/formula pair on one page through semantic paragraph flow. Hardcoded
page breaks are unnecessary. This is repeated navigation friction during simultaneous document
and spreadsheet use; the formulas themselves remain readable and complete.

## Direct lesson checks

### Caffeine 1

- P1, introduction: names Tania and Roohana, introduces the academy, states the six-statistic
  assignment, and explicitly requires no previous tutorial. The introductory image renders.
- P1-2, Step 1: gives personal-copy instructions, sheet name, exact data extent, first/last
  observation checks, formula entry including equals sign/Enter, formula-bar inspection, and
  a place for written responses.
- P2, Steps 2-3: mean/median explanations precede calculations; sleep uses `A2:A26`, score
  uses `B2:B26`, and the paired-row sorting warning is present. The actual workbook has all
  25 numeric pairs, starting (3,55) and ending (8.5,100).
- P3, Steps 4-5: sample SD is distinguished from center and retains original units. Submission
  collects six statistics plus interpretation; the same-mean/different-spread question tests
  transfer. This is a complete endpoint rather than a future-work placeholder.
- Actual XLSX: all 12 label/formula destinations are blank and wrapped; column D width is 27,
  E/F widths 16. The long future label "Sample standard deviation" is accounted for without
  pre-entering it. All authored seeds match actual cells.

### Caffeine 2

- P1-3, introduction / Steps 1-2: the full 25 pairs and all required concepts are introduced;
  a completed earlier workbook is explicitly unnecessary. The predictor is sleep, response is
  score, and causal limits are stated. R1 identifies the conflicting image content.
- P4, Step 3: visible generated labels `3.1` and `3.2` match their parent Step 3. Instructions
  specify a scatter chart, sleep horizontal axis, score vertical axis, chart title, and a
  prediction before fitting. The specific p4 figure contradiction remains R1.
- P5-6, Steps 4-5: the line equation and terms are explained. Actual calculation targets are
  initially empty; formulas consistently use score first and sleep second. The equation
  45 + 5*x is explicitly hypothetical, not supplied-data output. The seven-hour prediction
  uses the student's fitted coefficients. R2 affects reopening the actual chart.
- P6-8, Step 6 / 6.1-6.4 / Step 7: LINEST/INDEX coefficient extraction and standard error,
  t statistic, residual df=23, two-tailed p-value, alpha, and interpretation are all present.
  Tail/direction appears at both the hypotheses and answer record. Numeric recovery checks
  give slope about 3.18 and R-squared about 0.347. The final deliverable includes chart,
  calculation, prediction, decision, and model-shape/causal reasoning.
- Actual XLSX: 23 destinations are blank; labels receive D=28, G=29, J=46 character widths;
  result columns H/K are 12 and wrapped. No authored seed or worksheet-name mismatch occurs.

### Caffeine 3

- P1-2, introduction / Step 1: requires linear-regression concepts or the named prior lesson,
  supplies all 25 pairs, and reconstructs its own linear comparison in `L:M`. It requires no
  previous answer file. R1 identifies the invented missing-data illustration.
- P3, Step 2: exactly two compact visible fills appear: `C2:C26` and `E2:F26`. There are three
  seed Enter instructions, not dozens of printed descendant Enter actions. The instructions
  teach selection including the first row, shortcuts/handle, relative references, rectangular
  copying, and endpoint formula/value checks (`C26=72.25`, `E26=8.5`, `F26=72.25`).
- P4-5, Steps 3-5: the polynomial equation, coefficient order, scalar extraction, b2 sign,
  varying marginal change, df=22, seven-hour prediction, and two-tailed curvature test are
  present. The post-selection exploratory-p-value limitation is explicit. R3 identifies a
  label/formula page split.
- P6-7, Steps 6-7: model comparison distinguishes training R-squared from validation and asks
  about new data; submission collects both equations, both fit measures, prediction, test,
  and verdict. The 16-hour question is an extrapolation transfer task, not an instruction to
  add fictional records. R1/R2 remain at the comparison chart.
- Actual XLSX: all 105 targets, including every generated Fill destination, are blank. Future
  label H11 receives width 48 and explicit row-11 height 33 with wrapping; formula column I
  is 12. Predictor columns C/E/F are 21/23/25. All seeded cells match the source.

### PETase

- P1-2, introduction: synthetic status, new-hire task, three expression strategies, partial
  purification, Bradford color/wavelength mechanism, BSA-equivalent total protein limitation,
  regression equation, and inverse prediction are included. No prior lab data/file is required.
  The unrelated original microbial t-test continuation is absent.
- P2-4, Part 1: blank correction precedes the calibration plot and line. `C2:C8` keeps `$B$2`
  fixed; the endpoint check gives `C8=0.599`. Chart instructions specify numeric concentration
  on x and corrected absorbance on y, remove the raw series, and give correct axis titles.
  Residuals use the fitted coefficient anchors and `I2:J8` fill with final-row checks.
- P4-5, Part 2 Steps 1-4: interpolation limits precede inverse calibration, then dilution,
  then recovered mass. Cells `E13:E15`, `F13:F15`, `G13:G15` are filled once per column;
  the final-row check and clear volume/dilution definitions preserve units and scope.
- P5-6, Part 2 Step 5: numerical recovery checks and a report/submission endpoint are present.
  Recovered total protein is explicitly separated from PETase abundance and activity.
- Actual XLSX: seeded standard/sample concentrations, absorbances, dilution factors, and
  volumes match the source. All 38 calculation/label targets are blank and wrapped; F=26,
  G=24, I=13, J=15 widths preserve space for future labels/results. R2/R3 affect chart
  reentry and one page boundary, respectively.

## Numbering and evidence limits

Every generated Part/Step/Substep heading appears as native text in the actual DOCX and is
visible in the corresponding PDF. Caffeine 1 has Part 1 / Steps 1-5; caffeine 2 has Part 1 /
Steps 1-7 with 3.1-3.2 and 6.1-6.4; caffeine 3 has Part 1 / Steps 1-7; PETase has Part 1 /
Steps 1-6 and Part 2 / Steps 1-5. No manual old ordinal is required to follow the sequence.

All four actual workbooks freeze at A2, preserve source seeds, and leave every student target
empty. Structural lint reports no errors. Caffeine 2/3 retain six/twelve INDEX/LINEST static
coverage warnings, respectively. Every worksheet has an unmapped-Google note. Static workbook
width/wrapping evidence does not establish live Google row sizing or import behavior.

Verified Google Fill down shortcuts against the official
[Google Sheets shortcut reference](https://support.google.com/docs/answer/181110?hl=en):
Ctrl+D on PC and Command+D on Mac. The current instructions match those shortcuts. Their
selection and relative/anchored-reference explanations are consistent with the intended fills.

This review records the 16:46 bundle snapshot. Later fixes/rebuilds require new visual evidence
for affected pages. R1-R3 are actionable findings for the coordinator; this report does not
provide the separate classroom-quality acceptance requested after corrections.
