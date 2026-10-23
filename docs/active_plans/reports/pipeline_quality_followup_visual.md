# Pipeline quality follow-up: native visual evidence

The final native rebuild and refresh completed on 2026-10-23. All screenshots and
native receipts are current. The earlier Part 1 instructional-table content loss is
resolved in the rebuilt PDF; the original finding and final proof are retained below.

## Commands and scope

- `source source_me.sh && python3 devel/refresh_documentation.py`: passed. Every
  LibreOffice stage ran outside the sandbox, sequentially, as required by AGENTS.md.
- `source source_me.sh && python3 tutorial_output/followup_visual_check.py`: passed.
  Disposable XLSX copies use existing source example conclusions and the existing
  native Calc capture helper. Original starter files were not filled.
- `source source_me.sh && python3 tutorial_output/followup_review_pages.py`: passed.
  Poppler rendered every page of all three Parts and the published Roots capstone.
  Current source, artifact, and screenshot receipt hashes passed all 131 comparisons.
- All 25 screenshot assets were inspected in contact views. SHA-256 comparison with
  HEAD found 24 byte-identical assets and one changed asset,
  `microbes_5_completed_anova.webp`; its larger interpretation region was inspected.

The temporary scripts, page PNGs, contact sheets, disposable workbooks, native sample
PDFs, and machine-readable checks live under ignored `tutorial_output/`. They add no
permanent capture machinery. GFM review is assigned separately; this report covers
native artifacts.

## Whole-document inspection

| Artifact | Pages | Result |
| --- | --- | --- |
| Part 1: Create | 6 | Source fences readable; repaired table has all five body rows |
| Part 2: Statistics | 6 | All pages inspected; formulas, images, and checks legible |
| Part 3: Improve | 7 | All pages inspected; moved formulas and long command readable |
| Published root_statistics.pdf | 1 | All Steps and formulas visible on one page |

The Workbook source preambles are now literal source examples in the compiled PDFs.
They consume most of the opening pages before the instructional Steps. Part 2 places
its Part heading near the end of page 1 and starts the first Step on page 2. Part 3
ends with a short page of final checks and navigation. These are pacing limitations,
with no clipped code, missing screenshot, or lost navigation observed. Broad
pagination changes remain outside this focused repair.

The initial material Part 1 finding was reported immediately to the manager: the Markdown
table headed `Spreadsheet location | Supplied content` contains five data rows in
`docs/learn/PART_1_CREATE.md`, but its compiled PDF page 5 shows only the header.
Page 6 starts `3.1: Try designing the blanks`; PDF text extraction confirms the table
rows are absent. This is content loss, not merely a table split. No product or source
edits were made by this capture worker. This describes the initial failed artifact;
the final rebuild resolves it as documented below.

## Workbook response-space proof

| Starter target | Blank | Font/wrap | Row height | Source example visible |
| --- | --- | --- | --- | --- |
| Microbes 4 E26 | Yes | 10 pt, wrapped | 123 pt | Entire lower-tail example |
| Microbes 5 I16 | Yes | 10 pt, wrapped | 123 pt | Entire right-tail example |

The existing example conclusions at source lines 277 and 301 were copied as rendered
plain text, preserving words and placeholders. No numerical answer was invented.
Both native Calc sample PDFs contain every word; both rendered images show the
complete six-line conclusion with spare vertical room. Label-side cells D26 and H16
remain blank in the original starters, as specified by the source workbook tables;
labels are later authored actions. The completed ANOVA screenshot retains its
`Interpretation` label and blank response cell.

The eight-line minimum is shared across authored interpretation rows. The Caffeine
L7:N16 region retains its ten-row shape; no rows or source content were added.
Course capture independently checks blank Roots summary/deviation cells and numeric
display format `0.000`, and compares completed authored results with Python statistics.

## Evidence and limits

- `tutorial_output/followup_visual/review_metadata.json`: page counts and receipt checks.
- `tutorial_output/followup_visual/asset_comparison.json`: 25 screenshot comparisons.
- `tutorial_output/followup_visual/samples.json`: exact copied text, blankness, row
  height, wrap/font, native PDF paths, and whole-text extraction checks.
- `docs/screenshots/{capture,syntax_capture,course_capture}_receipt.json`: current
  maintained capture receipts.

This is an expert native-artifact walkthrough. It does not establish student
usability, live GitHub rendering, Google Sheets import fidelity, or student outcomes.
The Part 1 table finding is resolved in the final native rebuild below.

## Final rebuild and direct PDF proof

All 12 canonical lessons were rebuilt sequentially using the existing CLI:

```bash
source source_me.sh && for lesson in tutorial_data/*.md; do python3 make_tutorial.py build "$lesson" || break; done
source source_me.sh && python3 devel/refresh_documentation.py
```

Both commands completed successfully. Every LibreOffice invocation ran outside the
sandbox. The refresh rebuilt the three canonical documentation examples, captured
all 25 screenshots, rebuilt the published Roots capstone, and composed each guide
with its explicit practice-workbook checkpoint before building the three Parts.
The checkpoint is `root_05_variation` for Parts 1 and 2 and `root_06_grow` for Part 3.
The guides' Workbook source examples remain literal fenced examples.

| Canonical PDF | Pages |
| --- | --- |
| babies_1_z_test | 6 |
| babies_2_t_test | 6 |
| babies_3_two_sample_t_test | 5 |
| caffeine_1_descriptive_statistics | 3 |
| caffeine_2_linear_regression | 10 |
| caffeine_3_quadratic_regression | 7 |
| microbes_1_z_test | 9 |
| microbes_2_t_test | 9 |
| microbes_3_two_sample_t_test | 12 |
| microbes_4_f_test | 11 |
| microbes_5_anova | 10 |
| petase_1_linear_regression | 6 |

All 94 canonical pages, all 19 course-Part pages, and the one-page published capstone
were rendered and inspected in contact sheets. All six actual table-bearing pages
were also inspected at full size: Microbes 3 page 4, Microbes 5 page 3, Part 1 pages
4 and 6, Part 2 page 6, and Part 3 page 5. Headers and body labels fit, and table
rows remain visible. The long Part 3 command fits by wrapping within its code box.
The earlier pacing limitations remain, including short final pages; this focused
repair does not claim a pagination redesign.

Part 1 page 6 now displays `Spreadsheet location | Supplied content` and all five
body rows together: A1, A2:A6, D1:E1, D2:D4, and E2:E4. Page 5 no longer strands
the header. Full-size inspection confirms both text columns are legible, including
the complete sample-standard-deviation label and blank-result explanation. The
owning renderer change sets header-cell paragraph `keep_with_next`; this final
review verifies its resulting PDF rather than inferring success from DOCX content.

The disposable final audit additionally compares every nonempty DOCX table cell
against normalized rendered PDF text. All 106 cells across six tables are present;
none are missing. This text-presence check supplements the page-image inspection.

Final reconciliation passed:

- All 12 canonical `tutorial_data/*.md` SHA-256 hashes match their pre-rebuild values.
- All 102 source, asset, and output hash comparisons in the 15 canonical/Part bundle
  manifests match their current files.
- All 131 screenshot, source, and published-artifact receipt comparisons match.
- All 25 maintained screenshots were regenerated: 24 are byte-identical to HEAD;
  `microbes_5_completed_anova.webp` is the sole changed asset and was inspected at
  full size. Its headings, results, decision, and expanded blank interpretation area fit.
- Microbes 4 E26 and Microbes 5 I16 remain blank, wrapped, 10 pt, and 123 pt tall.
  All other starter values match the existing disposable native-rendered samples.
  Both sample images were re-inspected; each complete six-line source conclusion
  fits with spare vertical room. This reuses the existing native response-space proof
  without another LibreOffice export of equivalent samples.
- The course capture rechecked blank starter results/deviations and `0.000` numeric
  display. Formula evaluation was not rerun as a separate Calc suite: this repair
  changes document table pagination, not lesson formulas.

Current machine-readable evidence is under ignored `tutorial_output/followup_visual/`:
`final/audit.json`, `final/manifest_reconciliation.json`, `review_metadata.json`,
`final_refresh.log`, and `final_audit.log`. Final page/contact images are WebP at
quality 90 under `final/`. Disposable scripts remain under ignored `tutorial_output/`;
no permanent test or capture framework was added.

The rebuild retained pre-existing diagnostic warnings about intentionally extended
input ranges and functions outside the offline formula checker. Native build and
visual acceptance do not resolve those source diagnostics or establish live GitHub,
Google Sheets, student-usability, or learning-outcome acceptance.
