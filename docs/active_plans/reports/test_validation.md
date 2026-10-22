# Final execution validation

Verified on 2026-10-22 with Python 3.12.15 through `source source_me.sh && python3`.
This report records execution evidence; external Google compatibility is not inferred from it.

## Bundle verification

All 12 sources were built sequentially with `python3 tutorial.py build tutorials/<name>.md`.
LibreOffice ran outside the macOS sandbox through approved escalated execution. All builds
returned exit 0. Five Microbes lessons were rebuilt again after their final source corrections.
The final inventory checked every source SHA256 against its manifest and every artifact SHA256
against its ownership manifest. All 36 artifacts were nonempty and readable: DOCX ZIP integrity
and document parsing, XLSX workbook reopening, and PDF page-tree parsing passed.

Raw build logs, `artifact_inventory.json`, and `artifact_checks.log` are retained in
`output/verification/final_verification/`. The inventory lists all 36 paths, sizes, fingerprints, and
PDF page counts. Each bundle is `output/<stem>/<stem>.docx`, `.xlsx`, and `.pdf`, with its
`validation.json` ownership report.

| Tutorial stem | PDF pages |
| --- | ---: |
| babies_1_z_test | 8 |
| babies_2_t_test | 6 |
| babies_3_two_sample_t_test | 4 |
| caffeine_1_descriptive_statistics | 3 |
| caffeine_2_linear_regression | 8 |
| caffeine_3_quadratic_regression | 9 |
| microbes_1_z_test | 8 |
| microbes_2_t_test | 7 |
| microbes_3_two_sample_t_test | 12 |
| microbes_4_f_test | 9 |
| microbes_5_anova | 8 |
| petase_1_linear_regression | 6 |

The 88 pages passed independent final visual review; see [pdf_validation.md](pdf_validation.md).

## Editable source exercise

A verification source in `output/verification/final_verification/` was built before and after inserting a
Step, changing an authored formula from `=A2*2` to `=A2*3`, and changing a workbook seed from 3
to 4. Both builds produced all three formats. The compiled Step sequence changed from `1,2` to
`1,2,3`; the new instruction and formula appeared in extracted DOCX and PDF text; the reopened
XLSX contained the changed seed. The original tutorial sources were untouched by this exercise.
`source_edit_contract.json` records the first exercise. `move_rename_contract.json` records a
second exercise that moved the table from A1 to D4, relocated a student entry from C2 to F5,
updated formula and selection references from A2 to D5, and renamed worksheet `Data` to
`Observations`. Reopened XLSX confirmed the moved seed and renamed sheet. Reopened DOCX confirmed
updated worksheet labels, formulas, cell hyperlink target, and an internal heading link to an
emitted bookmark. These checks exercise source-to-artifact propagation, not spreadsheet formula
evaluation.

## Calculation and Sheets preparation

The independent calculation command produced expectations for all 12 tutorials, 13 scenarios,
254 formula cells, and eight synthetic direction checks. The Sheets dry run consumed that exact
expectations file and prepared all 13 cases without API requests:

```bash
source source_me.sh && python3 -m devel.check_tutorial_calculations -o output/verification/final_verification/oracles
source source_me.sh && python3 -m devel.validate_google_sheets tutorials/*.md --dry-run --expectations output/verification/final_verification/oracles/tutorial_expectations.json -o output/verification/final_verification/sheets_dry_run
```

The direct script invocation initially failed to import `sheetlesson`; module invocation worked.
The earlier live attempt's missing credentials remain documented in
[calculation_validation.md](calculation_validation.md). No repeated live request was made.
Google import, calculation, navigation, and spill behavior remain unverified.

## Tests and limits

The full suite passed all 1272 tests after the final source, import, and documentation fixes.
The captured run is `output/verification/final_verification/pytest_final.log`; it used Python
3.12.15 via `source source_me.sh && python3 -m pytest -q`. The build contract tests exercise
previous-bundle preservation when conversion fails or produces an unreadable PDF. Earlier full
runs exposed temporary report-link, XML-security, typing, and support-import findings; those were
fixed and the final run is green. No live Google execution was performed during this final
verification.
