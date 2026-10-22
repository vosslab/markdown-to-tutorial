# Established teaching review

## Verdict

The rebuilt Babies 1-3 and Microbes 1-5 bundles meet the established-teaching specification. The
current PDFs preserve the original sequence, scenarios, examples, and voice where those remain
supportable; current DOCX text agrees with the PDFs. The focused changes restore task context,
explicitly correct statistical errors, and bound ecological claims without rewriting the lessons
into a new teaching style. No blocking content, calculation-order, workbook-start-state, figure, or
numbering defect was found. Babies 2 ends with two short paragraphs on a lightly occupied final page;
this is a minor pagination opportunity only.

This is an independent review of the current outputs on disk. Earlier review reports were used as
leads; conclusions below were checked against the direct Fall 2025 sources and current artifacts.
The generated PDFs were rendered anew with `pdftoppm`: 45 pages across these eight bundles. Every
page was reviewed in its fresh contact sheet, and figures, worked formulas, and endings were viewed
at full size. No LibreOffice command was run. The generated DOCX text was extracted independently.
All eight generated XLSX files were opened read-only with `openpyxl`; every worksheet had zero
prefilled formulas, raw observations were present, and the answer/calculation areas matched the
visible instruction order. Current PDF page counts differ from the older inventory: Babies 1-3
have 7, 7, and 3 pages; Microbes 1-5 have 5, 5, 7, 5, and 6 pages.

This report's artifact snapshot predates the coordinating agent's final pagination-only rebuild.
The source-level SPEC verdict is complete; final pagination on the rebuilt PDFs is covered by the
separate quality/HCI review.

## Lesson findings

| Lesson | Direct source and current generated evidence | Finding and verdict |
| --- | --- | --- |
| Babies 1: Z-test | Fall 2025 guide, Markdown Parts 1 and 2, Steps 1-6, Practice, and Takeaways; original PDF pp. 1-6. Current source `tutorial_data/babies_1_z_test.md`; generated PDF pp. 1-7: scenario/setup pp. 1-2, summaries and statistic p. 3, tail choice and p-values p. 4, decisions/results p. 5, practice and story p. 6, comic and references p. 7. | Keeps Joe's hospital premise, known-SD Z-test, two-tail comparison, practice, and protest comic. The assigned claim is explicitly right-tailed and the lesson tells students to preselect and report that branch, resolving the earlier post-hoc-choice risk. It corrects the original claim that n below 30 alone invalidates a Z-test: population SD and distribution assumptions now explain the Z/t distinction. The known benchmark and population SD appear before the calculations. Workbook sheets contain all 24 observations; D1/E1 labels are seeded and the remaining stated cells are blank. **Accept.** |
| Babies 2: one-sample t-test | Fall 2025 guide, Part 2, "Why Use a T-Test Now?", Steps 1-10, Practice, Takeaways, and Joe's Redemption; original PDF pp. 1-5. Current source `tutorial_data/babies_2_t_test.md`; generated PDF pp. 1-7: challenge/setup pp. 1-2, summary statistics p. 3, t/df and p-values pp. 4-5, decisions and ending p. 6, story close/reference p. 7. | Keeps the same benchmark and Joe story while correcting the sample-size misconception and explaining estimated SD, df, and uncertainty. Joe's assigned higher-than-benchmark alternative is selected before p-values; both tails remain a comparison exercise, and reporting is tied to the preselected branch. The observed right-tail result (about 0.154) correctly replaces the original unsupported redemption. The standalone workbook has the 24 data and explicit "not used" entry; the referenced calculation sequence matches the blank cells. The two closing paragraphs and reference on p. 7 leave considerable white space, but no sentence is stranded or lost. **Accept; minor layout note.** |
| Babies 3: two-sample t-test | Fall 2025 guide, Part 3, prior/new scenario, Steps 0-8, and example interpretation; original PDF pp. 1-4. Current source `tutorial_data/babies_3_two_sample_t_test.md`; generated PDF pp. 1-3: pre-calculation hypothesis/setup p. 1, summaries and test formulas p. 2, interpretation p. 3. | Preserves Joe-versus-Green-Veggies rivalry and both groups' 24 observations. The generated introduction is simpler and hypothesis choice now precedes visible means/SDs, addressing the original order conflict. It corrects the source's mistaken claim that T.TEST type 2 is Welch: the two-sided formula uses type 3; directional formulas account for the observed sign and the function's absolute-statistic behavior. The calculated example is bounded to the observed data and does not infer a dietary cause. The workbook begins with raw columns A:C and an empty F:H calculation area; the instructions seed labels, group means/SDs/sizes, then p-value and decision in dependency order. **Accept.** |
| Microbes 1: Z-test | Direct Fall 2025 Markdown Part 1, Steps 1-8, Practice, Takeaways, and Part 2 transition (source lines 5-204). Current source `tutorial_data/microbes_1_z_test.md`; generated PDF pp. 1-5: Busse Woods scenario/photo p. 1, workbook/statistics p. 2, Z and normal-curve/tail explanation p. 3, tail-specific probabilities and decisions p. 4, practice/takeaways/advisor transition p. 5. | Restores the specific soil-diversity task, Busse Woods image, lower-tail illustration, three-point recap, and supervisor's unknown-SD question. The illustration is correctly labeled as a tail example, not the dataset result. It retains the stipulated known SD and benchmark, and corrects the source's n=30 cutoff implication. The lesson distinguishes tail-specific alternatives and limits inference to diversity summaries rather than urbanization causality. The 24 raw observations are present and D1's headers/remaining formula cells follow the visible sequence. **Accept.** |
| Microbes 2: one-sample t-test | Direct Fall 2025 Markdown Part 2, "Why Use a T-Test Now?", Steps 1-9, Practice, Takeaways, and Part 3 transition (source lines 5-217). Current source `tutorial_data/microbes_2_t_test.md`; generated PDF pp. 1-5: Z-vs-t art and scenario p. 1, setup p. 2, statistics and tail-specific p-values p. 3, decisions/results p. 4, practice/takeaways/advisor transition p. 5. | Restores the continuing benchmark task, neutral Z-versus-t image, recap, and advisor's two-year comparison. It states that the population SD is unknown, corrects the n=30 cutoff, and does not promise a one-sample T.TEST implementation absent from the original. The lower-tail question remains primary while other tails are explicitly comparative. The workbook contains the original 24 observations; the blank calculation area and the visible D2, D4-D6, D8-D12, D14-D17, and D19 sequence align. **Accept.** |
| Microbes 3: two-sample t-test | Direct Fall 2025 Markdown Part 3, Steps 1-9, Welch example table, Practice, Takeaways, and Part 4 transition (source lines 1-271). Current source `tutorial_data/microbes_3_two_sample_t_test.md`; generated PDF pp. 1-7: scenario/forest image p. 1, setup and summaries pp. 2-3, Welch example table and distribution figure p. 4, tail formulas pp. 5-6, results/recap/next-test bridge p. 7. | Restores the advisor task, forest context image, distribution comparison, four takeaways, and variance-question transition. The new t curves are labeled by df and explicitly have no n=30 cutoff; the forest image is not presented as data evidence. Welch df remains fractional and the unequal-variance calculation is used. Since the source rows name the same locations, the lesson clearly marks independence as a hypothetical assumption and says matched repeated measures require a dependent-data method; it does not silently switch this exercise to a paired test. The full-size formula table and chart are legible. The workbook's two data groups precede blank calculations, then means, SDs, sizes, t, df, tail probabilities, decisions, interpretation. **Accept.** |
| Microbes 4: F-test | Direct Fall 2025 Markdown Part 4, Steps 1-9, Practice, Takeaways, and Part 5 transition (source lines 1-255). Current source `tutorial_data/microbes_4_f_test.md`; generated PDF pp. 1-5: T-vs-F image and variance scenario p. 1, data/statistics p. 2, statistic/df/tail setup p. 3, probabilities/decision/results p. 4, practice/recap/ANOVA bridge p. 5. | Restores the personal observation/advisor task, title art, recap, and older-thesis bridge. It corrects the interpretation boundary: an F-test compares variances of Shannon-index values and cannot establish homogenization, resilience, or species-composition change. The same-site independence assumption is explicitly hypothetical; the directional and two-tail F probabilities preserve numerator/denominator ordering. The actual workbook headers already in D1/E1 are readable and called out; calculation cells are blank. The sequence computes SDs and counts before the ratio, df, p-values, and decisions. **Accept.** |
| Microbes 5: ANOVA | Direct Fall 2025 Markdown Part 5, Steps 1-13, Practice, and Takeaways (source lines 1-275). Current source `tutorial_data/microbes_5_anova.md`; generated PDF pp. 1-6: ANOVA scenario/title art p. 1, method history and result-table setup p. 2, group statistics p. 3, grand mean/df/sums of squares pp. 4-5, decision/interpretation/practice/takeaways p. 6. | Restores the advisor's return to older theses, ANOVA title image, and four takeaways. It corrects the unsupported trend/homogenization inference and identifies the single right-tail omnibus test; rejection still requires follow-up comparisons. It distinguishes the older culture-based hypothetical series from 2014/2024 sequencing and warns that method is confounded with year. The source's 2014 series difference from Parts 3/4 is called out. Full-size page 2 shows the workbook setup; the starting sheet has raw data in A:F, G1 as a separator, and blank H:M results. The student sequence is valid: group summaries and counts, grand mean, df, SSR/SSE/SST, mean squares, F, right-tail p, decision, interpretation. Unequal counts 10/15/20/24/24 are stated. **Accept.** |

## Workbook walkthrough

Every current XLSX opens with the source observations and no pre-entered formulas. Labels already
present in the original/generated templates are identified in the corresponding lesson; other
labels and formula cells are blank, so students can follow the visible instruction sequence. Babies
1-2 preserve the supplied national comparison data on both tabs, with the separate test tab ready
for entries. Babies 3 has 24 values per group in A:C and a blank F:H calculation area. Microbes 1-2
have the 24 observations in A:B and empty result columns. Microbes 3-4 have 24 rows in A:C and empty
results; their formulas use the stated ranges through row 101. Microbes 5 has five raw-data columns
with the stated unequal group counts; G1 remains a separator and the H:M results area is empty.

The visible instruction order respects formula dependencies in all eight workbooks. In particular,
Babies 3 chooses the alternative before group summaries; Microbes 3 derives Welch df after group
statistics and before p-values; Microbes 4 calculates numerator/denominator df in the stated year
order; and Microbes 5 builds group counts and statistics before the weighted grand mean and ANOVA
components. I found no unresolved destination, reference, numbering, or truncated-formula mismatch.

## Retained evidence

Ignored evidence is in `tutorial_output/verification/teaching_review/established_spec/`:

- `*_contact.png`: newly rendered contact sheets covering every current PDF page.
- `pages/`: every page rendered at 125 dpi; `fullsize/`: critical figures, formula pages, and endings
  rendered at 200 dpi.
- `text/`: PDF text from all current PDFs, original Babies PDFs, and extracted text from all eight
  generated DOCX files. `docx_pdf_text_check.txt` records that every normalized DOCX token is also
  present in its corresponding current PDF extraction.
- `artifact_inventory.txt` records current PDF page counts and DOCX/XLSX/PDF SHA-256 values;
  `workbook_inventory.txt` records worksheet dimensions, populated-cell counts, and zero formulas.

The originals are the direct files in `2025_Artifacts/`; migrated Markdown was compared with the
matching `tutorial_data/` lesson source. Generated XLSX inspection used the files under
`tutorial_output/<lesson>/`. No tests, source edits, or workbook edits were made in this review.
