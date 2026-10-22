# Regression teaching review

Review date: 2026-10-22. Independent read-only audit of all three caffeine lessons and PETase 1.
The caffeine original is a work in progress: the acceptance target is three complete, polished,
standalone lessons developed from that foundation. Fidelity to unfinished instructions is not an
acceptance requirement. PETase is a separate, explicitly synthetic salvage exercise.

## Evidence and boundaries

- Read the actual original caffeine Markdown and its 21-page PDF at
  `/Users/vosslab/nsh/SLIDES/djot-slide-builder/Tutorial_Outline.md` and `.pdf`.
  Physical PDF pages below refer to that PDF, not its stale table of contents.
- Read `2025_Artifacts/PETase_1_Linear_Regression_Tutorial_Fall_2025.md` directly, including its
  scenario, mechanism, regression motivation, and unrelated microbial-diversity instructions.
- The old caffeine migration report supplied only the original source location. None of its
  completion claims served as approval evidence.
- Reopened the four actual generated DOCX and XLSX bundles under `tutorial_output/`, extracted
  every PDF page, and rendered/viewed every generated PDF page in contact sheets. DOCX image
  hashes independently match all 14 original caffeine images and both original PETase images.
- Entered every authored Label/Enter instruction into temporary copies of the actual starting
  workbooks, checking the initial destinations for collisions. All destinations were initially
  blank and no instruction overwrote seeded data: 12, 23, 105, and 38 actions respectively.
  These copies retain formulas; this is an address/workflow inspection, not live Sheets execution.
- Independently fitted the actual caffeine XLSX observations with NumPy and SciPy. Linear slope
  = 3.17907115, R-squared = 0.346638668, two-tailed slope p = 0.00196019; quadratic coefficients
  = -12.004604, 24.993238, -1.52025034, R-squared = 0.847164660, quadratic-term p = 2.178e-8.
  This supports corrections to the draft's claims about absence of a linear trend.
- Temporary evidence is in
  `tutorial_output/verification/teaching_review/regression/`: original text extracts, four PDF
  and DOCX extracts, workbook inventories, temporary student-entered workbooks,
  `walkthrough.json`, individual PNG pages, and three PDF contact sheets.

## Consequential findings

1. **Caffeine 3: replace enumeration with an efficient fill workflow.** Original Step 9 (physical
   PDF p.16; Markdown lines 340-347) teaches the fill handle in four short actions. Generated
   Step 2 occupies PDF pp.3-5; pp.4-5 are almost entirely repeated Enter instructions. Students
   are told to fill but then see each individual cell as another apparent task. There are 75
   predictor formulas, including seed cells; this does not teach 75 different operations.
   Smallest correction: enter `=A2^2` in C2, explicitly fill C2:C26; enter `=A2` and `=C2` in
   E2:F2, explicitly fill E2:F26; explain the fill handle or Fill down once, and retain endpoint
   checks. A compact authored range-fill contract should infer translated formulas for validation
   without expanding them into the student document. All labels/answers remain student-entered.

2. **All caffeine workbooks: size blank destinations for their eventual labels.** The actual
   initial XLSX uses default width 12 for columns containing later Label tasks. Caffeine 1 D4
   will hold "Sample standard deviation" beside E4's value; caffeine 2 G5 and J6 will hold
   "Residual degrees of freedom" beside results; caffeine 3 H11 will hold a 51-character
   two-tailed p-value label beside I11. Once adjacent results are entered, these labels cannot
   overflow into their neighbors and become difficult to read. `walkthrough.json` identifies
   all candidates. Smallest correction: use authored Label text when setting column widths and
   wrapping/row heights, while keeping initial cells blank. This is a repeated workbook design
   issue across all three lessons, not a request to prefill student answers. Width inspection
   demonstrates the risk; a real spreadsheet visual check of the corrected entered copy should
   establish final readability.

3. **All caffeine documents: progression references target unavailable Markdown files.** Actual
   DOCX hyperlink relationship targets are literal `caffeine_1_descriptive_statistics.md`,
   `caffeine_2_linear_regression.md`, or `caffeine_3_quadratic_regression.md`. Those files are not
   present in the standalone output directories. PDF text also displays raw filenames. Replace
   these with readable lesson titles and numbering in the student material, or supply working
   published lesson URLs. Existing complete datasets and recreated baselines already support
   standalone use; preserve that behavior.

4. **PETase: restore the explanatory bridge and startup role.** Original sections "Your Task"
   and "Concept: How the Bradford BSA Assay Works" (Markdown lines 30-43) explain why a new hire
   needs a calibration, how acidic free dye becomes protein-bound blue dye, why absorbance is
   read at 595 nm, and why identical treatment of standards and unknowns matters. Generated
   PDF pp.1-2 compress the mechanism into one sentence and remove the learner's new-hire role.
   The later workflow has valid cautionary detail but loses the positive conceptual motivation.
   Retain the synthetic disclosure and total-protein qualification; restore one short mechanism
   paragraph and a direct assignment to the student. Do not restore the unsupported claim that
   Bradford identifies the best PETase-producing strain. Manufacturer documentation supports
   explaining dye binding and color change without overclaiming PETase specificity:
   [Thermo Fisher Bradford assay](https://www.thermofisher.com/us/en/home/life-science/protein-biology/protein-assays-analysis/protein-assays/bradford-assays.html).

5. **Local comic guidance would improve caffeine 3.** PDF p.8 faithfully retains the original
   comparison comic, which prints quadratic R-squared about .88; the actual workbook gives .847.
   The introduction already correctly calls these drawings illustrative. Add a short local
   caption asking students to use their own values, so a learner comparing the adjacent graphic
   and cells does not mistake .88 for the expected answer. Keep the original image untouched.

6. **Attribution deserves preservation.** Original warm-up credits Tania and Roohana (Markdown
   line 32, PDF p.2); generated caffeine 1 omits that credit. Restore the credit in a brief
   attribution without carrying over unfinished placeholder instructions.

## Lesson comparisons

### Caffeine 1

| Source section | Generated material | Assessment |
| --- | --- | --- |
| Warm-up workspace, PDF p.2 | PDF pp.1-2, Step 1 | Personal copy, rename, paired columns, and orientation survive. Full embedded data remove missing-template dependence. |
| Mean, median, SD, PDF pp.2-3 | PDF pp.2-3, Steps 2-4 | Definitions, interpretation blanks, comparison prompts, and variability survive. Both variables are now correctly analyzed, with explicit units and sample SD. |
| Congratulations and transition, PDF p.3 | PDF p.3 ending | Sequence survives; target is an unavailable Markdown link. |
| Intro image and author credit | PDF p.1 image; no credit | Image binary preserved. Credit lost; restore briefly. |

This is a complete standalone introductory lesson: students need no previous workbook or hidden
data. The warning against sorting one column prevents destruction of pairing, and separating
hours from percentage points corrects the draft's mixed labels. The additional center/spread
reflection prepares regression appropriately. No original substantive practice task is lost.
Actual initial XLSX contains all 25 pairs in A2:B26, no calculated answers, and no charts; students
create the intended six summaries. Main remaining problems are label readability and transition
presentation. The three-page PDF has no visible clipping; p.3 is sparsely occupied but contains a
coherent final reflection.

### Caffeine 2

| Source section | Generated material | Assessment |
| --- | --- | --- |
| Scenario and question, PDF pp.3-5 | PDF pp.1-3, opening/Step 1 | Dr. Caffeine, coffee humor, sleep/scores question, and association framing survive. Full data replace copying between incomplete template tabs. |
| Variables/scatterplot, PDF pp.6-7 | PDF pp.3-4, Steps 2-3 | Predictor/response, axes, pattern descriptions, pause-before-calculation, and chart procedure survive. Curvature is explicitly allowed. |
| Equation and functions, PDF pp.8-9 | PDF pp.5-6, Step 4 | Slope/intercept/R-squared calculations and chart comparison survive; clearer least-squares wording added. |
| Hypothetical 45+5x and prediction, PDF p.10 | PDF p.6, Step 5 | Worked interpretation example, actual coefficient interpretation, zero-hour caveat, and seven-hour prediction survive. |
| Fit, inference, decision, PDF pp.11-13 | PDF pp.6-7, Step 6 | R-squared=.60 example, two-tailed slope test, t statistic, p-value, decisions, and p-value limitation survive. |
| Whole-pattern reflection, PDF p.13 | PDF p.7, Step 7 | Students still challenge a straight line using plot and statistics. |

The statistical repairs are justified: moving the intercept reference from label D6 to value E6,
extracting labeled scalar LINEST statistics, clarifying tail direction, and avoiding a declaration
of "no relationship" after an insignificant slope. The resulting scientific content does not
require restoring the WIP draft's errors. The lesson is standalone with complete data and chart
instructions; earlier descriptive-statistics familiarity is helpful rather than an undeclared
dependency. The initial XLSX has all pairs, blank answer destinations, and no seeded charts or
formulas. Student tasks reach a calculated prediction and defensible qualified conclusion.
Preserving reflection responses in separate notes is workable because the lesson says so.
Seven images survive and render legibly. Remaining material issues are widths and broken lesson
references. Moving the hypotheses earlier would be a defensible teaching choice, but is not
necessary to fix the working lesson.

### Caffeine 3

| Source section | Generated material | Assessment |
| --- | --- | --- |
| Plot twist and straight line, PDF pp.13-15 | PDF pp.1-2, Step 1 | Academic roller-coaster narrative and visual comparison survive; fresh data and recreated linear baseline make it standalone. |
| Squared predictor, PDF p.16 | PDF pp.3-5, Step 2 | Intended math survives, but two simple fills are buried under repetitive formulas. |
| Equation and LINEST, PDF pp.16-17 | PDF pp.6-7, Steps 3-4 | Coefficient meanings/order survive; malformed response range and combined range are repaired. |
| Curvature hypotheses, PDF p.15 | PDF pp.2,7, Step 5 | Newly executable two-tailed coefficient test fills a real draft gap. Assumptions and exploratory-model-selection limitation are added. |
| Model comparison, PDF p.18 | PDF p.8, Step 6 | Complexity caveat, visual comparison, and fitted equations survive; residual/new-data question improves validation reasoning. |
| Wrap-up, PDF p.19 | PDF pp.8-9, Step 7 | Snack, water/browser-tabs humor, causal caution, and alternative explanations survive. |

Correcting "absolutely NOTHING linear" is warranted by the actual significant positive slope;
correcting unsupported 2-hour/14-hour examples is warranted by the actual 3-11.5-hour range.
Neither correction requires losing the original story. The derived p-value is explicitly
exploratory, which addresses selecting the curve after seeing the same data. R-squared is
correctly treated as insufficient proof of adequacy; this agrees with
[NIST model validation](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm).
The actual initial XLSX contains the 25 pairs and blank calculation cells through M; there is no
saved answer dependency. Explicitly stated prior regression knowledge is reasonable for the third
lesson. Main gaps are efficient fill teaching and the eventual readability of many labeled cells.
No clipping or broken image is visible in the nine-page PDF; the two pages of nearly pure formula
enumeration are an instructional burden even though technically rendered correctly.

### PETase 1

| Source section | Generated material | Assessment |
| --- | --- | --- |
| PET background, lines 7-14 | PDF p.1 | Material context, organism, PETase role, and both figures survive in compressed form. |
| Yeast strategies/purification, lines 16-28 | PDF pp.1-2 | Three distinct genetic strategies and intracellular/secreted recovery survive. Unsupported established performance claims become fictional proposals. |
| Your task and Bradford mechanism, lines 30-43 | PDF p.2 introduction | Total-protein purpose survives, but learner role and explanatory dye mechanism are substantially reduced. Restore the bridge. |
| Regression motivation, lines 44-46 | PDF p.2; pp.3-4 fit/residual steps | Correct squared-residual criterion, regression equation, inverse prediction, and model checking replace an incomplete calibration objective. |
| Original Step 1, lines 48-57 | PDF pp.2-3 | Complete seeded synthetic standards and samples replace an unavailable relevant dataset. Provenance limitation is explicit. |
| Original Steps 2-9, practice, takeaways, continuation, lines 59-200 | PDF pp.3-6, calibration and samples | Microbial t-test contamination is removed. New calibration, dilution, mass, and interpretation tasks actually fulfill the PETase/Bradford objective. |

The replacement is extensive, but the original becomes a microbial-diversity one-sample t-test
immediately after Bradford setup and never supplies a working Bradford regression analysis.
Removing that content is a justified repair, not lost PETase instruction. Its microbial-data
perturbation practice should not be restored literally. An optional relevant practice task could
change one unknown reading or dilution factor in a copy and predict the effect before recalculation.

The actual XLSX supplies seven standards including the blank, three samples with dilution factors
and recovered volumes, and blank outputs. Following the instructions subtracts the blank once,
fits matching standards, checks interpolation, inverts the fit, corrects dilution once, and
calculates recovered total protein. No required input or output collision was found. Distinguishing
concentration from recovered mass is useful, and the final rejection of PETase-specific or
activity conclusions is scientifically necessary for partially purified samples. Single readings
are openly identified and do not masquerade as biological replicates. The long seeded sample
headings have allocated widths; residual heading J1 is a smaller readability candidate. Two
figures are intact and the six-page PDF shows no clipping, though the final page is sparse.

## Decision

The four artifacts contain substantially usable teaching material and valid, answerable workflows.
They are not yet polished enough to close the classroom-quality review: fix the efficient fill
workflow, eventual worksheet label readability, broken progression references, and PETase's lost
conceptual/learner-role bridge. Preserve the scientific corrections and synthetic disclosure.
Then review freshly rebuilt PDFs and student-entered spreadsheet labels. This audit supplies no
fresh live Google Sheets or browser evidence and makes no claim about that environment.
