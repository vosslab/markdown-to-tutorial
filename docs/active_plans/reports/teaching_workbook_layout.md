# Student workbook layout

## Demonstrated problem

The previously generated caffeine 1 workbook has blank `D4`, width 12, no wrapping, and no
reserved row height. Entering "Sample standard deviation" beside the occupied numeric results
clips the label. The same issue affects caffeine 3's 51-character `H11` label and the collection's
initially blank statistic and decision destinations.

## Shared sizing policy

The XLSX writer now anticipates authored text while preserving blank student destinations:

- Include all Label, literal Enter, and literal Replace text when estimating column widths.
- Include quoted formula text operands as conservative estimates, covering the existing IF
  decision strings. This neither calculates formulas nor claims the strings are actual results.
- Consider every alternative branch, retaining the existing width bounds of 12 through 48.
- Apply top alignment and wrapping to blank entry cells, including numeric result destinations.
- Reserve row height for text that needs multiple lines at the final bounded column width.

Seeds and authored formula semantics remain unchanged. The writer adds no student answers,
formatting configuration, formula evaluator, or lesson-specific layout exceptions.

## Verification

`source source_me.sh && python3 -m pytest tests/test_tutorial_workbook.py
tests/test_function_typing.py tests/test_pyflakes_code_lint.py -q`: **144 passed**.
The existing workbook test file now protects blank preservation, branch-dependent label sizing,
the width cap, wrapping, row height, literal entries, and quoted IF decision text.

Fresh XLSX files were generated from the actual caffeine 1, caffeine 3, and microbes 1 sources.
Each initial workbook passed typed-seed verification. Temporary populated copies replayed the
authored actions through the shared case preparer, retaining the generated cell styles and
dimensions. LibreOffice Calc exported these copies to PDF outside the sandbox, using a private
profile for each workbook. Only the evidence copies received cropped print areas.

Inspected all three rendered images:

| Workbook | Destination | Generated dimensions | Observed completed state |
| --- | --- | --- | --- |
| Caffeine 1 | D4 | Width 27, wrapped | Full sample-standard-deviation label and both numeric results visible |
| Caffeine 3 | H11 | Width 48, wrapped, row 33 points | Entire two-tailed quadratic label and adjacent p-value visible |
| Microbes 1 | D15:D17 | Width 36, wrapped | Full Reject and Fail to Reject decisions visible beside their labels |

Calc fits caffeine 3's label on one rendered line; the reserved second-line height is conservative
space for other spreadsheet font metrics. These are layout estimates, not measured glyph widths.

Evidence is retained under
`tutorial_output/verification/teaching_review/workbook_layout/`: initial and populated XLSX,
populated PDFs, rendered PNGs, and `report.json`. The temporary verification script was removed.
No main lesson bundles were rebuilt. Google Sheets import appearance remains unverified.
