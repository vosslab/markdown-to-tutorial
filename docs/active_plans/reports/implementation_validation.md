# Implementation validation

Updated 2026-10-22 for the current tutorial layout and readiness snapshot. This report separates
the delivered local behavior from unavailable Google evidence.

## Current implementation

One Markdown source defines workbook seed data and list-authored student instructions. The current
entry point is `make_tutorial.py`; application modules are in `tutorial_lib/`, authored lessons
and assets in `tutorial_data/`, and generated bundles/evidence in ignored `tutorial_output/`.
There are no old-name compatibility aliases.

The parser/compiler resolves worksheet declarations, numbering, assignments, alternatives, cell
references, and static formula coverage. It rejects structurally incomplete label-only list items
with source-located diagnostics. DOCX output keeps instructions, formulas, images, tables, and
references editable. XLSX output preserves typed seed data while student answer cells remain blank.
The workbook freezes panes at `A2` and keeps columns at least 12 characters wide. Word output uses
a native `PAGE` footer. Builds stage the selected formats and verify that PDFs are readable before
publishing a bundle.

At the XLSX storage boundary, recognized modern function-name tokens receive the OOXML `_xlfn.`
prefix. Readback removes that prefix only for known tokens. Authored formula math, spacing, strings,
and references remain unchanged; unknown functions remain outside the checked vocabulary.

## Current evidence

All 12 tutorial sources passed independent content quality review. Focused specification and
quality reviews accepted the compiler/rendering contracts (19 checks) and formula boundary (12
checks). The portable statistical formula review accepted the implementation with no blockers.
Independent SciPy/NumPy expectations cover 12 lessons, 13 scenarios, 254 values, and eight model
direction checks. LibreOffice Calc `26.2.6.3` evaluated all 254 final-state values successfully;
15 additional signed Welch probes passed. The detailed evidence and exact hashes are in
[local_calculation_readiness.md](local_calculation_readiness.md).

All 12 current DOCX/XLSX/PDF bundles rebuilt successfully. The source, asset, and artifact hashes
match their manifests, and every generated file reopened. See
[readiness_execution.md](readiness_execution.md) and
[readiness_visual.md](readiness_visual.md). The 12 current PDFs contain 65 pages; every contact
sheet was inspected and difficult pages were reviewed at full size, with no blocking visual issue.
The final repository suite passed 1309 tests; direct module checks covered the new formula I/O
source. Integrated implementation and content reviews accepted the current work with no blockers.
The final source snapshot, local calculation report, and one rebuilt babies t-test bundle are
recorded in [readiness_execution.md](readiness_execution.md) and
[local_calculation_readiness.md](local_calculation_readiness.md). The suite evidence is in
[test_validation.md](test_validation.md).

## Google boundary

Fourteen worksheet mappings remain absent and Application Default Credentials were unavailable
for live execution. No workbook was created by the live attempt. Google import, formula execution,
effective values, spill behavior, and live navigation remain unverified. Offline static checks and
local Calc execution do not establish Google Sheets behavior.
