# Microbes and PETase voice comparison

## Finding

The migration kept the statistical work and added useful scientific limits, but it changed the
teaching voice across all six lessons. The original Microbes sequence uses a continuing Busse Woods
story, explanatory headings such as **Why Use a T-Test Now?**, and numbered spreadsheet directions
with nested cell-entry instructions. The current files replace much of that with compressed method
statements, repeated generic headings, and action-label bullets. The PETase lesson has the same
compression, although it also had material scientific overclaims that must stay corrected.

Restore the original paragraph wording, headings, and instruction grouping wherever they remain
factually sound. Keep the actual cell/formula work, original-data results, and required scientific
corrections. Do not use the earlier approval of a rewritten version as evidence that the voice is
good.

## Source-to-current actions

| Lesson | Original source to restore | Current location and action | Keep as a correction |
| --- | --- | --- | --- |
| Microbes 1 Z-test | `2025_Artifacts/Microbes_1_Z-Test_Tutorial_Fall_2025.md` lines 5-13 and the original ordered steps beginning at 18. The opening establishes the Busse Woods question, explains the Shannon Index, and tells students why they are doing the Z-test. | `tutorial_data/microbes_1_z_test.md` lines 40-74 compress the scenario into short declarations and a block of hypothesis/method caveats. Restore the original narrative and Google Sheets direction grouping around the accurate test instructions. | Retain the explicit lower-tail research question, correct Shannon Index limits, p-value meaning, and caution that this teaching data do not show an environmental cause. The original description calls 4.0 a benchmark; avoid presenting it as independently verified field provenance. |
| Microbes 2 one-sample t-test | `2025_Artifacts/Microbes_2_T-Test_Tutorial_Fall_2025.md` lines 5-21: “Now, you face a more realistic challenge,” followed by the two reasons for a t-test and their explanation. Preserve the “Why Use a T-Test Now?” heading and the ordered setup at lines 23 onward. | `tutorial_data/microbes_2_t_test.md` lines 40-73 flatten this into a short scenario, a compact hypotheses paragraph, and repeated assumptions text. Restore the original explanatory progression and nested spreadsheet directions. | Keep the distinction between known and estimated population SD, accurate hypotheses, and the statement that neither result proves urbanization caused a change. Correct the source's overstatement that a t-test is specifically for small samples / automatically more accurate. |
| Microbes 3 two-sample t-test | `2025_Artifacts/Microbes_3_Two-Sample_T-Test_Tutorial_Fall_2025.md` lines 5-13 sets up the shift from the benchmark test to comparing 2014 and 2024 and has the heading “Why Use a Two Sample T-Test Now?” Lines 15 onward use numbered directions and nested cell instructions. | `tutorial_data/microbes_3_two_sample_t_test.md` lines 40-80 replaces the two explanatory paragraphs with abbreviated scenario and formal hypothesis declarations. Restore the original story and heading structure, then keep the corrected independent-samples exercise clear in that structure. | The source workbook repeats the same 24 named sites across years. Keep the current explicit statement that independence is hypothetical; if rows are repeated sites, use a paired mean method. Do not restore the original causal claims or assert the t-test proves decline. |
| Microbes 4 two-sample F-test | `2025_Artifacts/Microbes_4_F-Test_Tutorial_Fall_2025.md` lines 5-13 has the advisor conversation, the “Why Use an F-Test Now?” explanation, then numbered directions. | `tutorial_data/microbes_4_f_test.md` lines 40-79 reduces the scene to a two-sentence handoff followed by generic method/assumption exposition. Restore the original explanatory voice and ordered instruction grouping, while anchoring the task to comparing variances. | Do not restore the source's claim that the t-test “confirmed” a decrease, or that lower Shannon-index variance means more uniform species composition. Retain the hypothetical independence disclosure for the repeated sites and the classical F-test's normality sensitivity. |
| Microbes 5 ANOVA | `2025_Artifacts/Microbes_5_ANOVA_Tutorial_Fall_2025.md` lines 5-13 has a 30-year story transition and “Why Use ANOVA Now?” explanation; the calculations are grouped under numbered steps. | `tutorial_data/microbes_5_anova.md` lines 40-88 compress the story and add a long provenance/method caveat before Step 1. Restore the original story and heading cadence; keep limitations in the relevant explanation and interpretation, not as a replacement for the scene. | The source says the prior F-test rejected and established decline/uniformity. The result does not support that premise. Keep the current five-group null, one right-tail F p-value, method-change confounding, and warning that ANOVA does not establish trend or cause. |
| PETase regression | `2025_Artifacts/PETase_1_Linear_Regression_Tutorial_Fall_2025.md` lines 5-47 supplies the original headings “Background: PET and Plastic Waste,” “Engineering Yeast to Produce PETase,” “Your Task,” “How the Bradford BSA Assay Works,” and “Why Use Linear Regression Now?” Restore these headings, paragraph pacing, startup/student framing, and numbered sheet directions from line 48 onward. | `tutorial_data/petase_1_linear_regression.md` lines 10-51 compresses the background, strain story, assay, and regression into short textbook paragraphs. Restore the valid narrative and section grouping around the actual calibration task. The source later contains a copied Microbes section beginning around line 188; leave that contamination out. | Keep the synthetic-data disclosure, partial-purification language, Bradford's total-protein limitation, BSA-equivalent units, and the requirement for separate PETase abundance/activity evidence. Do not restore unsupported claims that the engineered variant has severalfold higher activity or industrially realistic stability, or that total Bradford protein identifies which strain makes most PETase. |

The first five Microbes source files follow the same voice pattern: Part number and scenario, a short
reason-for-method heading, then practical steps with explicit locations. Restore those structures
consistently while preserving legitimate technical changes in place. In the spreadsheet directions,
bring back numbered steps and nested “type/enter/check” instructions where the original supplies
them; keep corrected workbook names, cell references, and formulas from the current version.

## PDF and workbook evidence

I compared all six original Markdown sources with their six current Markdown lessons, generated
PDFs, and XLSX sheet structure. Original PDF exports for these six lessons were not present, so the
voice comparison uses the Fall 2025 Markdown as the original and the generated PDF as the rendered
current artifact. Current PDFs are letter size: Microbes 1, 2, 4, and 5 are 5 pages each; Microbes 3
and PETase are 7 and 5 pages. Each current workbook has one expected lesson sheet with the raw data
and calculation area.

The opening-page comparison shows how the current PDF carries the same compressed prose into the
rendered artifact. In the Microbes 3 page, the image and caveat, short story, formal hypotheses, and
Shannon explanation are all packed into page 1. PETase uses the same compact paragraphs between its
figures. The source's longer paragraphs and explicit “why this test” headings offer a more
recognizable teaching rhythm; retain those while checking that restored prose still paginates
cleanly.

The opening-page comparison was inspected locally. Its raster images and extracted PDF openings
are in ignored `tutorial_output/verification/voice_microbes_petase_original_comparison/` files, so
they are not repository-linked evidence and cannot be resolved by the Markdown-link checker. PDF
extraction used Poppler. LibreOffice was not invoked.

## Scope

This is an expert inspection of source and rendered artifacts, not a student study or usability
test. It identifies restoration targets; it does not propose replacement prose or authorize
gratuitous scientific rewriting. No original, tutorial source, workbook, or permanent test was
edited.
