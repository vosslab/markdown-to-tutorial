# Dr. Caffeine migration evidence

Date: 2026-10-22. Authoring migration completed; full build and Google calculation evidence are
recorded separately when performed. Student answer cells remain blank in initial workbooks.

## Source identity and dataset

Original source, read without modification:
`/Users/vosslab/nsh/SLIDES/djot-slide-builder/Tutorial_Outline.md`.
Title: Dr. Caffeine's All-Nighter Academy / Does Sleep Affect Exam Scores? The warm-up section
credits Tania and Roohana. Source SHA256:
`b1d00c8712671fcc19bf5e6b1f665942e8943498f811209d1a6d16329c38f84d`.
Its 467 physical lines include 14 base64 PNGs; all 14 were extracted byte-for-byte into
`tutorials/assets/caffeine_01.png` through `caffeine_14.png`, without image regeneration.
A contact-sheet review confirmed these are narrative comic illustrations, not workbook screenshots.
Their drawn charts/text are illustrative; each migrated introduction explicitly says to use the
actual data and student-created charts as evidence.

The explicit source link at original line 119 identifies the
[original Google workbook](https://docs.google.com/spreadsheets/d/1mhOQhC_1hqnbvYItPT3y-V-_9l9q3pN7MtZDcOevaA0/edit?gid=0#gid=0).
Read-only XLSX export succeeded on 2026-10-22. The fetched file's SHA256 was
`7e004e0b5cda7a9b98b5f674864165815087b254cee2afb625b9aa9f4c4fe74f`.
All six worksheets were inspected: Data, Sample Mean, Linear Regression,
Linear Regression Reflection, Quadratic Regression, and Quadratic Regression Reflection.
Data!A2:B26 contains exactly 25 numeric sleep/score pairs. No additional observations occur
elsewhere. Each migrated source includes these 25 pairs, in the original order, without synthetic
substitutes or sampling. First pair: (3,55); last pair: (8.5,100); sleep range: 3 to 11.5 hours.
No data are missing.

The exported workbook is acquisition evidence, not a new permanent content source. All required
numbers now live in the authored tutorial Markdown. The generated worksheet is consolidated as
Sleep and scores. Original gid=0 refers to the source Data tab, so it is retained as provenance
only, not falsely mapped to a newly uploaded worksheet's cell hyperlinks.

## Three boundaries and complete coverage

| Original lines | Original content | Migrated home |
| --- | --- | --- |
| 3-9 | Academy title and introduction; image 1 | Tutorial 1 introduction; regression definition in tutorial 2 |
| 11-30 | Exported table of contents and separator | Replaced by native structural headings; no unique teaching content |
| 32-80 | Part 0 orientation, copying, mean/median/SD | caffeine_1_descriptive_statistics.md, all five steps |
| 82-112 | Part 1 scenario, research question, hypotheses; images 2-4 | caffeine_2_linear_regression.md introduction and prepare/evaluate steps |
| 114-142 | Setup and predictor/response distinction; image 5 | Tutorial 2 prepare/identify steps |
| 146-173 | Scatterplot, relationship patterns, prediction; images 6-7 | Tutorial 2 scatterplot substeps |
| 175-213 | Linear equation, functions, chart; image 8 | Tutorial 2 calculate regression step |
| 217-243 | Hypothetical 45+5x, slope/intercept, 7-hour prediction | Tutorial 2 interpret and predict step |
| 247-305 | R-squared, hypotheses, LINEST, t, two-tail p, decision | Tutorial 2 evaluate step and four substeps |
| 307-311 | Whole-pattern interpretation | Tutorial 2 final reflection step |
| 313-338 | Plot twist, linear comparison, quadratic hypotheses; images 9-11 | caffeine_3_quadratic_regression.md introduction and revisit step |
| 340-347 | Squared sleep column and fill | Tutorial 3 square predictor step |
| 349-391 | Quadratic equation, predictors, LINEST ordering; image 12 | Tutorial 3 equation and fit steps |
| 393-402 | R-squared comparison and complexity caveat; image 13 | Tutorial 3 comparison step |
| 404-410 | Congratulations, causation caveat, wrap-up; image 14 | Tutorial 3 verdict step |
| 412-439 | Repeated planning outline, scenario through interpretation | All covered by tutorial 2 steps and tutorial 3 comparison; omitted duplicated outline |
| 441-467 | Embedded image definitions | All 14 extracted assets referenced exactly once across the three files |

Tutorial 1 has orientation, mean, median, and sample standard deviation for **both** variables.
Tutorial 2 covers scatterplot, equation, interpretation, prediction, fit, uncertainty, slope testing,
and whole-pattern reflection. Tutorial 3 rebuilds the linear comparison, constructs squared
predictors, extracts quadratic statistics, tests curvature, compares models, and draws a qualified
conclusion. Each has the full starting data; neither tutorial 2 nor 3 depends on answers saved in a
previous workbook. Their prerequisites and progression links are explicit.

## Recorded adaptations and scientific corrections

- Placeholder template links and requests to insert an example screenshot were unfinished export
  scaffolding. Replace them with concrete generated-workbook upload/copy instructions. Preserve the
  original explicit template link as provenance; do not claim the illustrations are screenshots.
- Consolidate separate analysis/reflection tabs into one worksheet per tutorial. Students record
  narrative reflections in notes; every original reflection question remains represented.
- Original warm-up A-column formulas were inconsistently described as exam-score calculations.
  Teach A-column sleep and B-column scores separately; sample STDEV.S makes the estimator explicit.
- Original intercept reflection pointed to D6 (a label); use the computed E6 value.
- Original quadratic `B2:26` and `{A2:A26,,E2:E26}` are malformed. Use the valid response range
  B2:B26 and explicit adjacent sleep/squared-sleep predictors E2:F26.
- Original spill LINEST would produce a matrix. Use INDEX(LINEST(...),row,column) to obtain scalar
  outputs at explicitly labeled destinations. The fitted model and statistical quantities are the
  same; coefficient order is reversed relative to predictor-column order.
- Fill instructions list the resulting Enter formulas so static assignment/reference checks can
  recognize every student-created predictor cell. These instructions do not seed formulas.
- Correct the assertion that the data show no meaningful linear trend: independently, the slope is
  positive and its two-tailed p-value is about 0.00196. That does not make a straight line adequate:
  the scatterplot has curvature and the quadratic model accounts for more variation.
- Original narrative's 2-hour/14-hour examples are outside the recovered 3-11.5-hour data range.
  Remove those unsupported descriptions; retain the moderate-sleep peak as an observed pattern.
- Original quadratic hypotheses had no executable coefficient test. Add standard error, t, residual
  degrees of freedom, and two-tailed p-value instructions so the stated question is answerable.
- Keep two-tailed direction beside both hypothesis statements and p-value answer prompts. Do not
  teach one-tailed inference after selecting a direction from the observed slope.
- Keep association/causation and R-squared complexity caveats; add concise model-assumption caveats
  and residual/new-data follow-up so significant p-values are not mistaken for model validation.
- Render equations as editable plain text plus supported sub/sup/entities rather than unsupported
  TeX. Use ASCII source with HTML entities where needed.

Authoritative technical/scientific references checked during migration:

- [Google LINEST](https://support.google.com/docs/answer/3094249?hl=en): multiple predictor ranges,
  reverse coefficient order, and verbose statistics.
- [Google INDEX](https://support.google.com/docs/answer/3098242?hl=en): row/column scalar extraction.
- [Microsoft LINEST](https://support.microsoft.com/en-us/excel/functions/linest-function): full
  verbose-array layout, including standard errors, R-squared, and residual degrees of freedom.
- [Google T.DIST.2T](https://support.google.com/docs/answer/9368252?hl=en): two-tailed distribution;
  ABS supplies the required nonnegative argument.
- [NIST model validation](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm): R-squared
  alone is insufficient, and residual analysis supports assessment of fit.
- [NIST assumptions](https://itl.nist.gov/div898/handbook/pri/section2/pri245.htm): independence,
  normal errors, and constant error variance for classical regression inference.

## Independent numerical checks

Using the repository Python bootstrap, NumPy least-squares and covariance calculations, and SciPy
Student-t survival probabilities were run on the recovered 25 observations. This is an independent
numerical oracle, not a claim that Google Sheets executed the authored formulas.

| Quantity | Value |
| --- | --- |
| Sleep mean / median / sample SD | 7.16 / 7 / 2.36607973942835 |
| Score mean / median / sample SD | 80.84 / 83 / 12.7758887492547 |
| Linear intercept | 58.077850550602 |
| Linear slope | 3.17907115215056 |
| Linear slope standard error | 0.910069460307 |
| Linear R-squared | 0.346638667858 |
| Linear residual df | 23 |
| Linear slope t | 3.493218145943 |
| Linear two-tailed p | 0.001960190300455 |
| Linear prediction at 7 hours | 80.3313486156594 |
| Linear overall F (1,23) | 12.2025730151432 |
| Quadratic intercept | -12.00460399 |
| Quadratic linear coefficient | 24.99323790 |
| Quadratic squared coefficient | -1.52025034 |
| Quadratic squared-coefficient standard error | 0.17910279 |
| Quadratic R-squared | 0.847164660392 |
| Quadratic residual df | 22 |
| Quadratic-term t | -8.488144514209 |
| Quadratic-term two-tailed p | 0.000000021780044115745 |
| Quadratic prediction at 7 hours | 88.4557945471496 |
| Quadratic overall F (2,22) | 60.9728828960158 |

LINEST coordinates checked: one predictor slope (1,1), slope SE (2,1), df (4,2);
two predictors squared coefficient (1,1), linear coefficient (1,2), intercept (1,3),
R-squared (3,1), squared-coefficient SE (2,1), df (4,2).
A JSON oracle supplied to the Sheets-validation workstream checks 103 numeric cells: 6 descriptive,
10 linear, and 87 quadratic (including all 75 squared/copied predictor entries).
Absolute tolerance 1e-10 and relative tolerance 1e-7 are recorded in that oracle.

Exact data comparison passed for all three authored tables; all 14 image binaries exactly match
the original embedded bytes. All three authored sources use ASCII. Each source has exactly one
H1, Workbook section, Tutorial section, worksheet, and populated Part with substantive Steps.
Compiler and output checks are appended below when available.

## Compiler and artifact checks

With the new compiler available, all three sources compiled with zero errors. Tutorial 1 has
zero warnings; tutorial 2 has six function-coverage warnings; tutorial 3 has twelve. These warnings
are solely the compiler's conservative INDEX/LINEST compatibility status. No conflicting writes,
invalid references, unavailable inputs, unsupported markup, or missing images were reported.
Each source has the expected note that new generated worksheets have no Google cell-link mapping.
The official documentation and independent numerical checks above support the functions, but an
offline compiler does not claim live Sheets evaluation.

Direct compiler/renderer checks wrote XLSX and DOCX for all three sources under the ignored
`output_caffeine_migration/` directory. XLSX round-trip verification and DOCX ZIP/XML reopening
passed for all three. Every Label/Enter destination was checked in the generated initial XLSX and
remains blank: 12 descriptive, 23 linear, and 105 quadratic destinations. All 25 original pairs
remain in A2:B26. DOCX embedded-image counts are 1, 7, and 6 respectively, totaling all 14 originals.
These direct checks do not claim a PDF render, Google import, cell navigation, or live calculation;
those belong to the final bundle/Google acceptance workflows.
