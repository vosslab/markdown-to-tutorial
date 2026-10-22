# Teaching review: Microbes lessons 4 and 5

Reviewed the original Fall 2025 Markdown against the regenerated DOCX, PDF, and XLSX for both
lessons. I extracted the DOCX text, searched the PDF text, inspected the rendered PDF contact sheets,
and checked the XLSX sheet names, headers, and seeded data. PDF page numbers below are the printed
numbers (the cover is unnumbered). The XLSX files intentionally contain raw data and blank result
cells for students to complete; I reviewed formulas in the instructions rather than expecting them
to be prefilled.

## Lesson 4: two-sample F-test

| Original heading | Generated location | Review |
| --- | --- | --- |
| `Microbial Diversity Two Sample F-Test Tutorial` and `Part 4 Scenario` (original lines 1-10) | PDF page 1; `Part 4: Scenario` | Retains the 2014/2024 spread question and the transition from the t-test. Replaces the original claim that the data show homogenization/resilience loss with a bounded teaching scenario, Shannon-index explanation, sampling-design caveat for the same named sites, and normality/independence assumptions. No material scientific explanation is lost; the causal story is appropriately qualified. |
| `Why Use an F-Test Now?` (line 11) | Scenario, PDF page 1; `Step 4: Calculate the F-Statistic`, page 2 | Its mean-versus-variance rationale is retained in the scenario and ratio explanation. The original link between lower index variance and community homogenization is explicitly corrected: index spread does not establish taxonomic homogenization. |
| `Step 1: Copy the Data` (line 15) | `Step 1: Open the workbook`, page 2 | Copying from the course sheet is replaced by using the generated workbook, which already contains all 24 paired-row observations. The original course workbook is still referenced as provenance. Students are told not to overwrite raw data and that blank cells are not zero. |
| `Step 2: Organize Your Sheet` (line 23) | `Step 2: Organize Your Sheet`, page 2 | Columns A:C and the D:G results area are explained; means are correctly identified as unnecessary. Instructions to label D1/E1 are omitted because those labels are already seeded in the XLSX; F1/G1 remain student-entered. The workbook headers are readable, though D1/E1 prefill is not called out explicitly. Smallest clarity improvement: say that D1/E1 are already present and only F1/G1 need labels. |
| `Step 3: Calculate the Sample Statistics` (line 37) | `Step 3: Calculate the Sample Statistics`, page 2 | SD and count formulas retain the original cells and ranges. It adds the expected sample size of 24 and explains practice capacity through row 101. Clear and in order. |
| `Step 4: Calculate the F-Statistic` and `Explanation: F-Statistic` (lines 54-68) | `Step 4: Calculate the F-Statistic`, page 2 | Keeps the 2024/2014 variance ratio and clarifies what below/above one means. It avoids the original conflation of an observed F ratio with significance and disclaims causal or species-composition conclusions. |
| `Step 5: Calculate the Degrees of Freedom` and `Explanation` (lines 70-87) | `Step 5: Calculate the Degrees of Freedom`, page 2 | Retains n - 1 for both groups, adds the crucial numerator/denominator ordering (2024 df first, 2014 second), and removes the inaccurate claim that the F distribution approaches a normal distribution. |
| `Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)` (line 89) | `Step 6: Determine the Type of Test`, page 3 | Retains lower, higher, and two-sided alternatives, with explicit null directions. It identifies the lower 2024 variance alternative as the planned question and says to decide before seeing results. |
| `Step 7: Calculate the P-Values`, `Explanation of F.DIST Inputs`, `Explanation of F.TEST Inputs`, and substeps 7.1-7.3 (lines 100-181) | `Step 7` and substeps 7.1-7.3, PDF pages 3-4 | The three tails and built-in `F.TEST` comparison remain. The critical correction is present: two-tailed p is twice the smaller tail (capped at one); directional p-values cannot be assumed to equal half of `F.TEST`, and the ratio/df swap is explicit. Formula cells follow the earlier statistics/df cells. No substantive omission found. |
| `Step 8: Decision Using an IF Statement` (line 183) | `Step 8`, PDF page 4 | Retains the decision formulas and alpha. It explicitly keeps the decision tied to the variance question. |
| `Step 9: Interpret the Results` (line 210) | `Step 9`, PDF page 4 | Supplies the correct example ratio and tail p-values, states the lower-variance conclusion under the model, and limits it to Shannon-index spread. The original overstated ecological conclusions are removed. |
| `Practice Task` and `Key Takeaways` (lines 228-239) | `Practice: Explore sensitivity`, PDF page 5; transition to lesson 5 | Practice for changing/adding observations and comparing sample size, spread, assumptions, and decisions is retained and made hypothetical. The separate numbered takeaways are not retained as a recap; their main ideas appear in the tutorial and closing transition. If a recap is desired, add a short three-point summary of variance, tail choice, and assumptions. |

## Lesson 5: one-way ANOVA

| Original heading | Generated location | Review |
| --- | --- | --- |
| `Microbial Diversity ANOVA Tutorial` and `Part 5 Scenario` (original lines 1-10) | PDF page 1; `Part 5: Scenario` | Retains the five years and why an omnibus comparison is useful. Replaces the original assertion that the preceding F-test proved a decline/homogenization with the precise all-means-equal versus at-least-one-differs hypotheses. Adds right-tail framing, model assumptions, and cautions that neither a time trend nor cause follows from ANOVA. The narrative change is necessary because the original conclusion was not supported by the F-test. |
| `Why Use ANOVA Now?` (line 11) | Scenario, PDF page 1 | The rationale that ANOVA compares more than two means and uses between/within variation is retained in the scenario and steps 6-11. The original wording that an omnibus ANOVA determines a long-term trend is explicitly corrected. |
| `Step 1: Copy the Data` (line 15) | `Step 1: Open the workbook`, PDF page 2 | The generated workbook replaces the old copy-tab workflow and already has the five columns. The 2014 series difference from Part 3/4 is called out. Counts and intact-source-data instructions are clear. |
| `Step 2: Organize Your Sheet into an ANOVA Table Layout` (line 38) | `Step 2`, PDF page 2 | Retains all table headings and cell locations, adds a visible blank ANOVA-table scaffold in the rendered PDF, and explicitly protects A:F raw data and explains the G1 separator. Clear. |
| `Step 3: Calculate the Group Statistics` (line 70) | `Step 3`, PDF pages 2-3 | Retains all five means, sample variances, and counts; states expected group sizes (10, 15, 20, 24, 24) and total 93. The formula list continues onto the next page, but remains in numerical/year order. |
| `Step 4: Calculate the Grand Mean` (line 113) | `Step 4`, PDF page 3 | Retains the grand-mean formula and adds the needed unequal-group-size explanation. |
| `Step 5: Calculate the Degrees of Freedom (DF)` (line 122) | `Step 5`, PDF page 3 | Retains between/within/total df formulas and adds k=5, N=93, expected 4/88/92, plus the additive check. |
| `Step 6: Calculate the Regression Sum of Squares (SSR)` (line 142) | `Step 6`, PDF page 3 | Retains the weighted between-group calculation. It explains why group sizes weight squared deviations and says to preserve year order. |
| `Step 7: Calculate the Error Sum of Squares (SSE)` (line 157) | `Step 7`, PDF page 4 | Retains the within-group variance decomposition and explains it as variation within groups, without assigning a biological cause. |
| `Step 8: Calculate the Total Sum of Squares (SST)` (line 169) | `Step 8`, PDF page 4 | Retains SST = SSR + SSE and explains the partition. |
| `Step 9: Calculate the Mean Square (MS)` (line 188) | `Step 9`, PDF page 4 | Retains between/within division by df and notes total MS is unnecessary. |
| `Step 10: Calculate the F-Statistic` (line 201) | `Step 10`, PDF page 4 | Retains MS-between/MS-within and adds that a large F is evidence against equal means but does not identify the differing group. |
| `Step 11: Calculate the P-Value` (line 213) | `Step 11`, PDF page 4 | Retains `F.DIST.RT(L2, I2, I3)` and makes the right-tail-only meaning explicit, distinguishing this from the preceding two-variance test. |
| `Step 12: Decision Using an IF Statement` (line 231) | `Step 12`, PDF pages 4-5 | Retains alpha and the IF formula, correcting the reference to M2. The page break separates the formula from its setup (alpha and labels finish on page 4; I14 formula begins page 5). It remains understandable, but the smallest layout repair is to keep all four entries together or add a "continued" cue. |
| `Step 13: Interpret the Results` (line 249) | `Step 13`, PDF page 5 | Replaces the original causal/trend template with the computed F, df, and p-value; explains failure to reject as insufficient evidence, not equality; and says significant ANOVA needs follow-up comparisons. Student response cell and expected interpretation elements are specified. |
| `Practice Task` and `Key Takeaways` (lines 265-275) | `Practice: Explore sensitivity`, PDF page 5 | Retains change/add/compare practice and adds safeguards for hypothetical data and assumptions. The separate takeaway list is omitted; its useful ideas (omnibus scope, p-value, sample size) are integrated into explanations. A short recap could help novices, but no necessary instruction is missing. |

## Workbook and sequence check

The F-test workbook sheet is `Two Sample F-Test`; raw headers and all 24 2014/2024 rows are present.
The ANOVA sheet is `30 Year ANOVA Test`; the five original columns and unequal counts are present.
Result areas are blank for student entry as the tutorials state. Formula dependencies follow instruction
order in both lessons: source statistics before F/df/p-values and, for ANOVA, group summaries before
grand mean, df, sums of squares, mean squares, F, and right-tail p. Cell addresses match the generated
instructions. The existing validation manifests note formulas are not recalculated by an external
spreadsheet engine; this review checked sequence and references, not live Google Sheets/Excel behavior.

Rendered PDFs are legible at normal page scale in the contact sheets and preserve the lesson icon and
table/diagram elements. Dense formula pages and the ANOVA decision page break are the only visible
novice-friction items found. I found no additional consequential content omission or formula-order
error that warrants a lesson correction.
