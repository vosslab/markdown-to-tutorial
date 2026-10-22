# Teaching review: Microbes lessons 1-3

Review scope: the three matching 2025 source guides, migrated Markdown, generated DOCX/PDF/XLSX
bundles, and the starting workbook values. Generated PDFs were rendered directly with `pdftoppm`
and visually inspected; DOCX paragraph/table text and PDF page text were also extracted. The source
and output excerpts are preserved in
`tutorial_output/verification/teaching_review/microbes_early/`.
This is a teaching review, not evidence of Google Sheets import or calculation behavior.

## Findings that need action

1. **Lesson 3's independent-samples assumption is not established by the workbook (high).** The
   starting workbook and generated workbook pair the same 24 named locations in 2014 and 2024.
   The new lesson explicitly tells students to assume independence despite the matched row labels
   (original guide lines 15-30; generated Step 1, PDF p. 1, and design caveat, p. 1). That caveat
   exposes the conflict but does not resolve whether these are repeated site measurements. The
   choice changes the inference materially: Welch independent test gives t = -1.91452, df =
   39.49524, two-sided p = 0.06282; treating the rows as matched gives paired t = -3.15281,
   df = 23, two-sided p = 0.00445 (one-sided lower p = 0.00223). Before this lesson is used to
   make claims about the supplied dataset, establish the sampling design. Preserve the intended
   Welch independent-test exercise by explicitly labeling its independence as a hypothetical
   assumption and warning that matching rows would call for a paired method. Clarify what the
   original sampling units were when provenance is available. Do not present the current Welch
   result as an empirical environmental finding.

2. **Current output drops relevant and context-setting original figures (medium).** The source
   assets remain in `tutorial_data/assets/`, but the migrated Markdown does not reference them:
   lesson 1's Busse Woods image (original guide line 3; generated PDF p. 1), lesson 2's Z-test vs
   t-test comparison (original line 3; generated PDF p. 1), and lesson 3's before/after forest
   images and t-vs-normal distribution graphic (original lines 3 and 96; generated PDF pp. 1 and
   3). The current PDF does retain lesson 1's normal-curve image, with useful alt text, but moves
   it to the scenario page before the p-value instruction (p. 1). Restore or deliberately replace
   the graphics that teach the site context or distribution comparison. In lesson 3, retain the
   t-distribution graphic with a clear caption about degrees of freedom; caption the before/after
   image so it is not mistaken for evidence that the supplied Shannon data were caused by that
   visible change.

3. **The migration removes the author's narrative and summary structure (medium).** In lesson 2,
   original lines 7-12 open with "Now, you face a more realistic challenge" and "Feeling the
   pressure but determined to reach a solid conclusion," then tell students what they will do.
   Generated p. 1 replaces this with a generalized model statement and several qualification
   paragraphs. The key learning point (SD is unknown, so estimate it and use t) survives, but the
   student's task and progression in the story disappear. In lesson 3, original lines 7-13 carry
   forward the uncertainty from the preceding t-test, let the advisor propose comparing years, and
   explain why the two-sample test answers a new question. Generated p. 1 compresses this to "Part 2
   did not supply sufficient evidence ... Now compare 2014 and 2024 directly," then adds several
   caveat paragraphs. The inferential qualifications are useful; they could sit inside the advisor's
   continuing task instead of replacing it. In lesson 1, original lines 194-206 use a supervisor's
   warning to motivate reconsidering the stipulated known SD; generated p. 4 reduces the scene to a
   transition. Lesson 2's original lines 207-209 and lesson 3's original lines 261-273 also provide
   personal bridges to the next tutorial, reduced to brief endings on pp. 4 and 6. All three
   original `Key Takeaways` sections (lesson 1 lines 188-192, lesson 2 lines 200-205, lesson 3
   lines 254-259) are absent as sections. Some core points are folded into the steps, but their
   explicit recap is lost. Preserve the new statistical cautions while restoring the personal task
   progression and concise takeaways in the author's existing voice.

## Lesson-by-lesson source map

### 1. Microbial diversity Z-test

Original source: `2025_Artifacts/Microbes_1_Z-Test_Tutorial_Fall_2025.md`.
Generated source: `tutorial_data/microbes_1_z_test.md`.
Current PDF: `tutorial_output/microbes_1_z_test/microbes_1_z_test.pdf` (4 pages).

| Original heading / lines | Generated location | Review |
| --- | --- | --- |
| Title, image, and `Part 1 Scenario` (1-16) | Title and Scenario, p. 1 | The ecological setting and Shannon richness/evenness explanation remain, with a better-defined formula and an explicit warning that the artifacts do not establish field provenance or causation. The original Busse Woods photo is omitted. The new normal-curve image appears before the hypothesis explanation. |
| Steps 1-2: copy sheet and enter known values (18-37) | Steps 1-2, pp. 2-3 | Copying data is replaced by opening the generated workbook; benchmark 4.0 and stipulated SD 0.6 remain. Generated workbook has 24 numeric observations in B2:B25, blank labels and answer cells, and headers in A1:D1. The instructions correctly state the existing data and counts. |
| Steps 3-4: mean, n, Z (39-57) | Steps 3-4, p. 2 | Formulas and cells are retained. The explanation is much shorter and more precise about standard-error units. Ranges through row 101 allow later practice even though the workbook initially ends at row 25. |
| Step 5: tail choice (59-85) | Step 5, p. 3 | Original two-tail and higher-tail examples are corrected and reorganized. The selected lower alternative and all three hypothesis pairs are now explicit. The old heading's example mistakenly paired a lower/equal null with a higher alternative under the label of the general one-tail case; the correction is appropriate. |
| Step 6: p-values and curve explanation (87-135) | Step 6 and substeps 6.1-6.3, pp. 1, 3 | All three tails remain. The long repeated derivation of `NORM.S.DIST` is condensed to correct `NORM.DIST(..., TRUE)` direction explanations. The curve image is retained with more accurate alt text, but is separated from the formula step and placed on p. 1. |
| Step 7: IF decisions (137-163) | Step 7, pp. 3-4 | The three formulas remain. The explanation of `IF` as a programming concept is mostly removed, which reduces repetition. The original explanation used D13 where alpha is D14 in one formula (line 161); the generated formula correctly uses D14. |
| Step 8: interpretation (165-180) | Step 8, p. 4 | The fill-in response remains. A worked result is newly supplied: Z about  -1.65817, lower p about  0.04864, two-tail p about  0.09728. This usefully reconciles different tail decisions but makes the answer visible before student work; consider placing the result in instructor notes or after the blank. Causal attribution and "failure to reject means equal" wording are corrected. |
| Practice and Key Takeaways (182-192) | Practice: Explore sensitivity, p. 4 | Sensitivity practice remains, with stronger instructions to use hypothetical data and avoid treating it as new evidence. The distinct recap is removed; most concepts are integrated into the steps. |
| `Part 2 Setup` / supervisor email / transition (194-208) | Final transition, p. 4 | The supervisor email and explanation of why the SD assumption merits reconsideration are removed. The one-line bridge loses narrative continuity. The shift from Z to t is preserved as a next step. |

### 2. Microbial diversity benchmark t-test

Original source: `2025_Artifacts/Microbes_2_T-Test_Tutorial_Fall_2025.md`.
Generated source: `tutorial_data/microbes_2_t_test.md`.
Current PDF: `tutorial_output/microbes_2_t_test/microbes_2_t_test.pdf` (4 pages).

| Original heading / lines | Generated location | Review |
| --- | --- | --- |
| Title, Z-vs-T image, and `Part 2 Scenario` (1-22) | Title and Scenario, p. 1 | The benchmark question and unknown-SD distinction remain. The Z-vs-T visual is omitted although its asset remains. The new text correctly distinguishes stipulated known SD from estimated sample SD and avoids claiming the data are real field evidence. |
| Steps 1-2: copy data and benchmark (23-39) | Steps 1-2, pp. 1-2 | Generated workbook already includes the data and benchmark; 24 observations appear in rows 2:25. The population mean remains 4.0, and SD is now explicitly unknown. Student actions are clear. |
| Steps 3-5: summaries, t, df (41-74) | Steps 3-5, p. 2 | Mean, sample SD, count, statistic and n-1 df formulas/cells remain. The new df explanation is concise. The original says fewer than 30 is a reason to use t; the migration correctly centers the decision on unknown population SD rather than treating n<30 as a rule. |
| Step 6: tail choice (76-83) | Step 6, p. 2 | The lower alternative is selected. The new text says each direction has its own null and keeps the tail interpretations separate. |
| Step 7: T.DIST / T.TEST manual and direct approaches (85-150) | Step 7 and substeps 7.1-7.3, p. 3 | Manual p-value routes remain in a cleaner layout, with `T.DIST.2T`, cumulative `T.DIST`, and direction-specific tail formulas. The original `T.DIST.RT` alternative is replaced by `1 - T.DIST(...)` and `T.DIST(-D8,...)`. The direct `T.TEST` comparison from the original is not retained in this lesson's generated steps; this removes a useful alternate calculation practice. Google Sheets formula execution was not observed, so compatibility is unverified. |
| Step 8: IF decisions (152-175) | Step 8, pp. 3-4 | Decision formulas and alpha remain. A long explanation of the IF construct is condensed. |
| Step 9: interpretation (177-192) | Step 9, p. 4 | Result is newly supplied: t about  -1.10438, df = 23, lower p about  0.14043; the lower test fails to reject. This clearly contrasts with the Z result while correctly avoiding an equality claim. As in lesson 1, students see the worked answer before completing the interpretation; consider relocating it after the response blank or into instructor notes. |
| Practice and Key Takeaways (194-205) | Practice: Explore sensitivity, p. 4 | Practice remains and is more explicit about before/after comparisons and keeping hypothetical values separate. The standalone recap is removed, though df convergence and unknown SD reappear in the new sensitivity notes. |
| `Part 3 Setup` transition (207-209) | Final transition, p. 4 | The original narrative about uncertainty after the t result is reduced to a short instruction to compare two years. |

### 3. Microbial diversity two-sample t-test

Original source: `2025_Artifacts/Microbes_3_Two-Sample_T-Test_Tutorial_Fall_2025.md`.
Generated source: `tutorial_data/microbes_3_two_sample_t_test.md`.
Current PDF: `tutorial_output/microbes_3_two_sample_t_test/microbes_3_two_sample_t_test.pdf` (6 pages).

| Original heading / lines | Generated location | Review |
| --- | --- | --- |
| Title and `Part 3 Scenario` (1-13) | Title and Scenario, p. 1 | Comparing 2014 with 2024 remains. The generated scenario is more disciplined: it asks about means and explicitly says the test does not establish an environmental mechanism. The same 24 named locations appear in both years; the new independence caveat makes this an explicit unresolved design choice (see finding 1). Original before/after photos are omitted. |
| Steps 1-2: copy data and organize columns (15-35) | Steps 1-2, pp. 1-2 | Both year columns and statistical names remain. Generated workbook includes 24 paired-name rows, D1/E1 headers, blank calculations and F/G alternatives. The student is asked to label F1/G1 and retain the raw observations. |
| Step 3: statistics (37-55) | Step 3, p. 2 | Both means, sample SDs and counts are retained. Current counts are correctly identified as 24. |
| Step 4: Welch t-statistic (57-67) | Step 4, p. 2 | Welch formula and direction are retained and clarified: 2024 minus 2014, negative favors lower 2024 mean. Its independent-sample premise needs confirmed design. |
| Step 5: Welch df and examples (69-100) | Step 5 and table, pp. 3-4 | Welch-Satterthwaite formula and all six numerical examples are retained. The new text removes a misleading "pooled" description and states that df alone does not determine the p-value. The original t-vs-normal distribution graphic is omitted even though its asset remains; this was a useful visual counterpart to the examples. |
| Step 6: tails (102-111) | Step 6, p. 3 | All directions remain, with a clear lower-tail primary choice and separate nulls. The former instruction to test both directions for a "complete analysis" is corrected to discourage tail shopping. |
| Step 7: manual p-values and T.TEST (113-201) | Step 7 and substeps, pp. 3-4 | The beta identity and direct `T.TEST` route remain, with sign handling for one-tail requests made explicit. Formula sequence depends on E16 before E17/E18; instructions explain the dependency. These are dense pages with long formulas, but the current PDF remains readable at normal zoom. Google Sheets execution was not observed. |
| Step 8: IF decisions and Step 9 interpretation (202-247) | Steps 8-9, p. 5 | Decision/interpretation cells remain. Result is newly supplied: t about  -1.91452, df about  39.49524, lower p about  0.03141, two-tail p about  0.06282. This is internally consistent with Welch independent samples. It also foregrounds the unresolved pairing concern because using the same locations as pairs changes the result materially. |
| Practice and Key Takeaways (248-259) | Practice: Explore sensitivity, p. 5 | Change/add/compare/connect activities are retained in streamlined form. The distinct four-point recap is removed; the t/Z relationship remains in the new practice note. |
| `Part 4 Setup` / F-test transition (261-275) | Final transition, p. 6 | The forest-homogenization motivation and original narrative are removed. The generated transition properly cautions that lower spread alone does not demonstrate homogenization, a strong correction; it would benefit from one sentence connecting the next variance test to the observed data. |

## Workbook walkthrough

The generated XLSX files were opened read-only with `openpyxl`; original workbook values were also
read from the matching source sheets. For lessons 1 and 2, each generated sheet contains the same
24 Shannon values and location names as the first 24 observed rows in the source workbook. The
original source sheet's remaining rows through 101 are blank. For lesson 3, both years' 24 values
and all location names match the source workbook row by row. Generated workbooks leave answer cells
blank, as intended.

Following each lesson as a novice works mechanically through the current file: select the named
sheet, enter the instructed labels and formulas, and leave missing observations blank. Ranges through
row 101 support the later sensitivity task. Lesson 2 adds its `Alternate Values` heading in E1;
lesson 3 supplies D1/E1 and asks the student to add F1/G1. The written count checks help catch
mistakes. No prefilled formula or result is present to disclose a hidden discrepancy.

The main conceptual interruption occurs in lesson 3 before formulas: the workbook's matching
location labels suggest repeated sites, but the tutorial tells students to assume independent
samples. A novice has no evidence in the workbook with which to decide whether that assumption is
true. The text says to verify the actual sampling design, but the original artifacts do not provide
that design information. This blocks an evidence-based choice of test until provenance is supplied.

## Visual and verification evidence

The images below are contact sheets made from direct renders of the current bundled PDFs, not the
older contact sheets elsewhere under `tutorial_output/verification/pdf/`.

- `tutorial_output/verification/teaching_review/microbes_early/microbes_1_z_test-current-pdf-contact.png`
- `tutorial_output/verification/teaching_review/microbes_early/microbes_2_t_test-current-pdf-contact.png`
- `tutorial_output/verification/teaching_review/microbes_early/microbes_3_two_sample_t_test-current-pdf-contact.png`
- `tutorial_output/verification/teaching_review/microbes_early/source_lines.txt`
- Current DOCX/PDF text extracts and page PNGs are stored in the same evidence folder.

The current PDFs have 4, 4, and 6 pages respectively; the old contact sheets show a different
version and page count and were excluded from this review. DOCX text was extracted directly and
agrees with the current PDF text for the reviewed content. No LibreOffice command was run in this
review. No Google Docs/Sheets import or live formula calculation was performed. Numerical checks
above use the values in the generated workbook and SciPy; they assess the specified statistical
models, not the validity of the unknown field sampling design.
