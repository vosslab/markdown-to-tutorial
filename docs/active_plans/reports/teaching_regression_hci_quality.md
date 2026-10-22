# Regression lesson quality review

Date: 2026-10-22. Fresh cognitive walkthrough of the current three Caffeine lessons and
PETase lesson after the accepted specification recheck. Verdict: the four bundles are usable
for the stated classroom tasks. No new blocking content, calculation, or pagination defect
was found. One small novice chart-setup clarification is recommended below.

## Scope and evidence

The intended user is a biology student working beside a PDF or editable DOCX in Google Sheets.
The task is to start with the supplied XLSX, calculate and plot the assigned results, interpret
them, and recognize what to submit. This is expert inspection, not a participant study. Success
means the written lesson identifies the next action and target, its dependencies exist, checks
support recognizing/recovering a result, and the concluding interpretation fits the actual data.

Applied the HCI cognitive-walkthrough method and humanizer wording review. Read AGENTS.md and
the Python, Markdown, and repository styles. Reviewed the actual four current DOCX/PDF/XLSX
bundles under `tutorial_output/<stem>/`, rather than treating prior approval as evidence.

- Rendered all 24 actual PDF pages afresh with Poppler and extracted their text. All 24 new page
  raster hashes match the recent specification-recheck rasters; the four contact sheets reviewed
  here therefore represent these exact current pages. Reviewed every page in contact sheets and
  opened critical figures, formula/fill instructions, and page transitions individually at 1100 px.
- Opened every actual DOCX with python-docx, extracted its paragraphs, and checked embedded-image
  counts: 1, 6, 5, and 2 for descriptive, linear, quadratic, and PETase respectively.
- Opened each actual initial XLSX with openpyxl. All Caffeine workbooks contain exactly the same
  25 pairs in A2:B26. There are no seeded result formulas. PETase contains the seven standards,
  three unknowns, dilution factors, recovered volumes, and labeled blank results described below.
- Manually transcribed the formula entries and fill operations from the visible lessons into
  fresh copies of those actual workbooks. No compiler action/execution-case generator was used
  for that transcription. No target collides with a populated input cell. Checked the last-row
  formulas and independently calculated the resulting statistics with NumPy/SciPy.
- Cross-checked the resulting numbers against the existing final-rebuild Calc report at
  `tutorial_output/verification/teaching_review/final_rebuild/calculation/calc/run-wgdwbqqd/report.json`.
  All four current source hashes match that report. Its calculation results support the numerical
  checks; they do not establish interactive Google behavior.

Fresh evidence is in `tutorial_output/verification/teaching_review/regression_quality/`:
the 24 PNGs, four extracted PDF texts, four DOCX texts, four manually entered formula workbooks,
`product_inspection.json`, and `inspection.log`. The JSON records current product hashes, starting
cell contents/widths, independently derived values, transcribed formulas, raster identity checks,
and the relevant existing Calc comparisons. No LibreOffice process was launched by this review.

## Caffeine descriptive statistics

The opening establishes a complete six-statistic task, credits Tania and Roohana, and requires
no previous lesson. Its academy story leads into a two-sentence briefing and an explicit
submission list. All data and workspace instructions are present. The filled result area D:F
is separate from the untouched A:B observations; worksheet widths accommodate the labels.

| Page / step | Student decision and next action | Cell knowledge and recognition | Error / recovery path |
| --- | --- | --- | --- |
| P1-2, Step 1 | Upload the named tutorial workbook, make a personal copy, find Sleep and scores. | Actual A1:B26 headers and 25 pairs agree with the lesson; first 3/55 and last 8.5/100. Formula entry, equals sign, Enter, formula bar, ordinary-text labels, and notes are taught. | A wrong sheet or missing rows can be caught before calculating with the explicit endpoint/count check. |
| P2, Step 2 | Label D1:F1 and D2, enter the two means in E2/F2. | Both destinations are initially blank. AVERAGE uses A2:A26 for sleep and B2:B26 for scores; results are 7.16 hours and 80.84%. | The instruction checks that each mean lies within the observed range and directs the student to check range selection and numbers stored as text. |
| P2, Step 3 | Label D3 and compute E3/F3 with MEDIAN. | Results are 7 hours and 83%. The definition and comparison question explain why this differs from the mean. | Explicitly says not to sort one data column and separate pairs. Formula-bar inspection allows range correction without sorting the source. |
| P3, Step 4 | Label D4 and compute sample SD in E4/F4. | STDEV.S returns 2.36608 hours and 12.77589 percentage points. The lesson explains sample choice, spread, and units. | The prompt explicitly prevents comparing hours against score points as the same unit. Rereading the displayed function/ranges distinguishes sample SD from a wrong-variable calculation. |
| P3, Step 5 | Brief Dr. Caffeine and submit the six labeled statistics plus responses. | The student knows completion requires numbers with units, retained formulas, and the typical-value/variability interpretation. | The checklist allows an omitted second variable or statistic to be identified before submission. |

The retained academy illustration introduces the setting without asserting a fitted relationship.
The ending points to linear regression while remaining a complete descriptive-statistics exercise.

## Caffeine linear regression

The opening calls this lesson 2 of 3 and describes prior descriptive/spreadsheet familiarity as
helpful. It provides its own data, setup, and formula-entry instructions. It therefore works without
a previous completed workbook. The task progresses from variables and visual prediction through
fitting, inference, and a critique of what a significant straight line can establish.

| Page / step | Student decision and next action | Cell knowledge and recognition | Error / recovery path |
| --- | --- | --- | --- |
| P2, Step 1 | Make a copy and work in Sleep and scores; preserve columns A/B. | Actual inputs occupy A1:B26; later targets are blank. Practice explains formula entry and formula-bar inspection; responses go in notes. | Exact input range prevents dependence on another workbook; inspection exposes an accidental overwritten source. |
| P3, Step 2 | Choose sleep as predictor and score as response. | A2:A26 and B2:B26 are stated explicitly, with a reason-to-explain prompt. | The causation paragraph counters treating the choice of predictor as proof of causation. |
| P3-4, Step 3 / 3.1-3.2 | Select A1:B26, insert a scatter chart, name both axes, predict the pattern. | P4 displays the actual 25 observations: overall rise plus a fall among the longest sleepers. Axis directions and names match the workbook. | The axis check catches reversal. The prompt explicitly permits a bend instead of forcing a positive/negative-only judgment. |
| P5-6, Step 4 | Label D/E and compute slope E2, intercept E6, and R-squared E10; then double-click the chart and add its linear trendline. | Values are 3.179071, 58.077851, and 0.346639. Equation, units, and meaning precede interpretation. Scalar formulas leave adjacent cells free. | P6 tells how to reopen the chart and enable its legend if R-squared is hidden; chart/cell agreement checks common data and rounding. |
| P6, Step 5 | Interpret coefficients and predict at 7 hours in E14. | E14 = E6+E2*7 gives 80.33135%. The 45+5x equation is explicitly hypothetical, so it cannot be mistaken for the fitted answer. | Zero-hour extrapolation is identified as outside the actual 3-11.5-hour range; a prediction is distinguished from an individual guarantee. |
| P6-7, Step 6 / 6.1-6.4 | Extract H2/H3/H5, calculate K2/K6, then K10 and compare with 0.05. | LINEST/INDEX positions are explained. H2 matches E2; H3 = 0.910069; H5/K6 = 23; K2 = 3.493218; K10 = 0.00196019. Both hypothesis and answer request say two-tailed/nonzero slope in either direction. | The duplicate slope and explicit df check expose extraction errors. ABS supplies the required nonnegative t magnitude. Conditional reject/fail-to-reject instructions distinguish an unsupported null from proof of no relationship. |
| P7-8, Step 7 | Check fitted values, explain the curve, challenge the causal/individual claim, and submit. | Printed 3.18 and 0.347 checkpoints agree with actual data. Submission names chart, coefficients, 7-hour prediction, test, and response to research question. | The final check explicitly names response-first/predictor-second function order and rows 2-26. The closing explains why significance does not repair wrong shape. |

The retained illustrations are narrative or conceptual examples, not claimed numeric fits.
P5's alternative scatter patterns depict general relationship categories. P4's large actual-data
chart is the recognizable comparison for the student's chart. No contradictory caffeine-intake
axis or invented count is presented as the requested plot. The academy voice remains consistent;
the statistical explanation stays direct enough to perform the task.

## Caffeine quadratic regression

This is independently usable with its expressly stated prerequisite knowledge: the preceding
linear lesson or equivalent knowledge of scatterplots, coefficients, R-squared, and two-tailed
regression tests. It supplies all observations and recreates the linear comparator. It does not
promise to reteach all of that material to a student with no regression background.

| Page / step | Student decision and next action | Cell knowledge and recognition | Error / recovery path |
| --- | --- | --- | --- |
| P1-2, Step 1 | Copy/open the supplied workbook, recreate the labeled scatterplot and linear fit, calculate M2:M4. | All 25 pairs are present; L/M targets are blank. M2 = 3.179071, M3 = 58.077851, M4 = 0.346639. | Exact ranges, axes, and legend reminder permit rebuilding without an earlier workbook. It explicitly warns that a positive slope can miss curvature. |
| P3, Step 2 | Enter C2 = A2^2 and fill C2:C26; create E2 = A2/F2 = C2 and fill E2:F26. | Both the selected range and Ctrl+D/Command+D or fill handle are explained. The first row is included; each column copies its own first formula. C2 = 9; C26/F26 = 72.25; E26 = 8.5. | Last formulas =A26^2, =A26, =C26 expose constant-row or wrong-source filling. The warning keeps scores out of the predictor table and all student rows aligned. |
| P4, Step 3 | Predict the sign that produces an upside-down U and explain zero quadratic coefficient. | The equation defines each term and distinguishes linearity in coefficients from a curve in sleep hours. | This prevents interpreting squared hours as additional sleep or confusing a general polynomial diagram with the fitted sign. |
| P4-5, Step 4 | Extract I2:I7 from LINEST(B2:B26,E2:F26), then predict in I8. | Explicit reverse coefficient order gives b2 = -1.520250, b1 = 24.993238, b0 = -12.004604, R-squared = 0.847165, SE(b2) = 0.179103, df = 22. I8 gives 88.45579% at 7 hours. | The df/sign checks and explicit INDEX positions diagnose wrong extraction. Text explains that b1 alone is not a constant per-hour score gain. Comparison uses the current workbook's M2/M3. |
| P5, Step 5 | Calculate I10 = I2/I6 and I11 = T.DIST.2T(ABS(I10),I7), then decide at 0.05. | t = -8.488145 and two-tailed p = 2.17800e-08; reject a zero quadratic coefficient conditionally. Both statement and answer specify either-direction curvature with the linear term retained. | ABS handles the negative statistic. Assumptions and post-selection warning prevent presenting the exploratory p-value as confirmatory causal evidence. |
| P6, Step 6 | Compare M4/I5, reopen the chart, change its trendline to Polynomial degree 2. | Both actual-data panels share axes and 25 observations; the right curve bends downward and matches the computed model. Printed 0.347/0.847 values agree. | Explicit double-click reentry and distinction between chart settings and cells prevent looking for degree controls in the worksheet. It warns that added predictors alone increase training R-squared. |
| P6-7, Step 7 | Write a verdict, reject 16-hour extrapolation, submit both equations/R-squareds, chart, prediction, and test. | All requested quantities have been created in this workbook. The final paragraph states 3-11.5 hours and limits the causal/optimal-sleep claim. | The checklist exposes a missing linear comparator or test; new-data checking and causal-study reflection constrain conclusions. |

All five retained visuals were inspected. The puzzled researcher, polynomial reading, bathroom
equation, and ending cartoon maintain the story; the equation illustration shows possible forms
rather than asserting the observed fit. The ending character's surprised sleep comment is followed
by explicit interpretation and extrapolation limits. The actual fitted-model comparison carries
the correct downward curve. There is no invented missing-data episode. Numbering is coherent
through Steps 1-7, including continuation pages without repeated or reset steps.

## PETase regression

The scenario now supports a complete Bradford calibration and recovered-total-protein task.
The opening identifies synthetic teaching data and supplies the scientific context needed to
interpret the calculations. No earlier tutorial or lab data are required. It assumes basic
spreadsheet entry/menu familiarity, while teaching relative/absolute filling within this lesson.
The ending requests a report and both charts, and explains what additional measurements are needed
to compare PETase production or activity. The task does not drift into an unrelated mean test.

| Page / step | Student decision and next action | Cell knowledge and recognition | Error / recovery path |
| --- | --- | --- | --- |
| P2-3, Part 1 Steps 1-2 | Copy the workbook, open Bradford illustrative, locate standards and unknowns. | Actual A2:B8 contains 0-0.750 mg/mL standards and raw A595; A13:D15 contains strain, raw A595, dilution, and recovered mL. Result headers E12:G12 are seeded but E13:G15 are blank. | Exact table ranges distinguish the calibration from unknowns. Text identifies synthetic single readings and non-universal calibration bounds. |
| P3, Step 3 | Enter C2 = B2-$B$2 and fill to C8. | $B$2 is 0.052 and remains fixed; C2 = 0, C8 = 0.599, with last formula =B8-$B$2. Shortcut, selection, and handle are explained. | The last-row check catches a drifting blank reference. The explanation says to subtract once, preventing double correction. |
| P3, Step 4 | Insert a scatter chart; use A2:A8 for x and C2:C8 for the only y series; name title/axes. | Concentration must be numeric horizontal axis and corrected A595 vertical axis. The intended ranges and removal of raw readings are clear. | Axis/series check exposes a line chart or accidental raw series. The Series control is not explicitly named; see minor finding Q1. |
| P3-4, Step 5 | Label F2:F4 and compute G2:G4; reopen the chart and show its fitted equation and R-squared. | Slope = 0.798286, intercept = 0.000214286, R-squared = 0.999941. Formula order matches absorbance-on-concentration. | Double-click reentry is explicit. Chart/cell comparison allows rounding and tells students to retain full-precision cell coefficients; intercept is not forcibly zeroed. |
| P4, Step 6 | Enter I2/J2 fitted/residual formulas; fill both columns through row 8; plot residual against concentration. | I8 = $G$2*A8+$G$3 and J8 = C8-I8. Actual residuals range approximately -0.002786 to 0.002429, around zero. | The last-row formulas check anchored coefficients and relative data rows. Text asks students to inspect curvature rather than use R-squared alone. |
| P5, Part 2 Step 1 | Compare unknowns after subtracting the blank with corrected nonzero standards. | Corrected readings 0.240, 0.402, 0.320 lie inside C3:C8 = 0.101-0.599. | Outside-range recovery is to repeat at a suitable dilution and record the new factor, rather than accept extrapolation. |
| P5, Steps 2-4 | Fill E13:E15 diluted concentration, F13:F15 original concentration, G13:G15 recovered mass. | E = 0.300376/0.503311/0.400591 mg/mL; F = 1.501879/5.033107/2.002953 mg/mL; G = 4.505637/10.066213/8.011811 mg. Both concentration and mass rank B > C > A here. | Row-15 references are explicitly checked. Blank/intercept are each subtracted once; dilution is multiplied once. Volume is the original recovered preparation, not the diluted aliquot. |
| P6, Step 5 | Check approximate concentrations and submit both charts, formula cells, and scientific interpretation. | Printed 0.7983 and 1.50/5.03/2.00 checkpoints match calculations. Units and synthetic status are requested; total protein is distinguished from PETase-specific abundance or activity. | The printed troubleshooting instruction names blank subtraction, coefficient anchors, and dilution factors. The final checklist catches omitted residual chart or retained formulas. |

The two introductory figures show PET use and its polymer structure, not unsupported assay results.
The text consistently distinguishes intracellular and secreted preparations, recovered protein,
and BSA-equivalent total protein. No illustration conflicts with the current calibration.

## Minimal clarification and limitations

Q1, minor: PETase p3, Part 1 Step 4 names `Chart editor > Setup > X-axis`, then asks for C2:C8
as the only absorbance series. A novice can identify the intended data but must discover a second
control to set that series. The same knowledge is reused for the residual chart on p4.
The smallest helpful addition is an explicit `Chart editor > Setup > Series > Add series`
instruction for C2:C8, retaining the existing instruction to remove any raw absorbance series.
The corresponding second-chart series is J2:J8. This is a discoverability clarification, not an
observed live failure, and does not invalidate the numerical or scientific task.

The label-pagination code uses native keep-with-next only for adjacent same-row/next-column
Label plus Enter/Replace siblings. Its scope is small and readable; it does not encode lesson
names or page numbers. Current PDFs keep G2/H2 (Caffeine 2 p7), H5/I5 (Caffeine 3 p5), and F3/G3
(PETase p4) together without clipping. The remaining summary headers and step continuations are
readable. No broader layout mechanism or lesson-specific page break is justified by these files.

No live Google Sheets import, chart editor operation, keyboard shortcut execution, screen-reader
session, timed student trial, or user success rate was measured. The manual formula copies are
evidence of instruction interpretation and reference translation, not newly recalculated Calc
workbooks. Numerical claims use independent calculations and the source-matched existing Calc
report. This review establishes a coherent executable teaching path under those limits; it does
not convert offline inspection into a claim of observed novice interaction.
