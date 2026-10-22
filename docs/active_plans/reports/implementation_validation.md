# Implementation validation

Updated: 2026-10-22. Final local integration checks and rebuilt PDF assessment are complete.
This report distinguishes locally observed behavior from external application compatibility.

## Delivered behavior

One Markdown source defines native worksheet data and list-authored student instructions.
The source-located parser/compiler resolves worksheets, numbering, assignments, alternatives,
cell references, and static formula coverage. DOCX includes editable instructions, formulas,
images, tables, and references. XLSX contains typed seed data while student answer cells remain
blank. The CLI lints, builds selected formats, and imports simple XLSX into a Markdown draft.
Builds stage outputs and validate PDF readability before publishing a bundle.

All 12 migrated lessons have built DOCX, XLSX, PDF, and `validation.json` bundles under
`output/<source-stem>/`. The initial 87-page pass found three pagination issues involving a nested
list, a split table row, and missing continuation headers. Renderer corrections were rebuilt and
accepted in the final 88-page visual review recorded in [pdf_validation.md](pdf_validation.md).

## Migration and scientific evidence

The collection contains 3 babies, 5 Microbes, 3 Dr. Caffeine, and 1 synthetic PETase lesson.
[TUTORIAL_CATALOG.md](../../TUTORIAL_CATALOG.md) links every source.

- Babies retain original observations, story, practice tasks, and extracted images. Corrections
  distinguish known population SD from estimated SD, use Welch type 3, preserve signed tail
  direction, and align the fictional story's conclusion with the supplied nonsignificant data.
- Microbes retain original data and teaching sequence. Corrections include Welch degrees of
  freedom, directional variance tails and reciprocal degrees of freedom, actual ANOVA group sizes,
  mean-test assumptions, and careful ecological interpretation. Fresh review repaired incomplete
  Z/F prose and the misleading sample-size explanation for choosing t.
- Dr. Caffeine retains all 25 recovered sleep/score pairs and 14 illustrations. Corrections repair
  malformed ranges, use scalar INDEX/LINEST extraction, make coefficient order explicit, and
  replace unsupported narrative claims with the observed linear and quadratic results.
- PETase retains recoverable background and images but clearly labels every seeded measurement
  as synthetic. Bradford estimates total protein relative to BSA, with dilution and volume
  corrections; it does not establish PETase abundance, activity, or fermentation productivity.

Detailed provenance, scientific references, and migration checks are in
[babies_migration.md](babies_migration.md), [microbes_migration.md](microbes_migration.md),
[caffeine_migration.md](caffeine_migration.md), and [petase_migration.md](petase_migration.md).
The migration does not overwrite original artifacts or sibling source projects.

## Independent numerical evidence

SciPy/NumPy expectations cover all 12 lessons, 13 scenarios, and 254 expected final formula cells.
Eight synthetic checks verify sign-sensitive Z/t/Welch tails and reciprocal variance ratios.
The independent generator consumes seed data and explicit curriculum mappings rather than
evaluating spreadsheet formulas. See [calculation_validation.md](calculation_validation.md).

The actual Sheets runner prepared all 13 cases with the generated expectation file without API
requests. A user-authorized live attempt then returned exit 2 because Application Default
Credentials were unavailable. No Google workbook was created. Real Sheets calculation, effective
values, spill behavior, import fidelity, and live navigation remain unverified.
The live attempt's preserved report is `output/validation/sheets-live/report.json`; the command
used the module launcher `python3 -m devel.validate_google_sheets --live`.

## Review and final checks

Workbook, DOCX, and build implementations have passed independent specification and quality
reviews after corrections. The parser/compiler specification review passed, with its final quality
review still active. All 12 sources passed their specification review after content corrections.
Sheets tooling and independent numerical expectations passed specification and quality review.

The final artifact check verified 12 current bundle manifests and 36 readable DOCX/XLSX/PDF
artifacts. The first editable-source exercise changed seed A2 from 3 to 4, changed `=A2*2` to
`=A2*3`, and inserted a step; the rebuilt XLSX, DOCX, and PDF reflected those edits. A second
exercise moved a worksheet table from A1 to D4, updated action/formula references from C2/A2 to
F5/D5, and renamed `Data` to `Observations`. Reopened XLSX and DOCX reflected the new cells, sheet
scope, action link, formula, and heading bookmark. Evidence is in `output/verification/final_verification/`
(`artifact_inventory.json`, `artifact_checks.log`, `source_edit_contract.json`, and
`move_rename_contract.json`).

The final sourced-environment repository suite passed 1272 tests. The build regressions include
preservation of an existing bundle after conversion failure or unreadable PDF output. Independent
specification and quality reviews accepted the compiler hygiene and focused contract coverage; the
integration review's final-suite condition is now satisfied. Final test details and the captured log
are in [test_validation.md](test_validation.md) and `output/verification/final_verification/pytest_final.log`.
Original historical artifacts remain intact, including their existing content.

The existing layered test registry now excludes `2025_Artifacts/**` only from ASCII compliance.
This preserves imported historical Unicode as source evidence while retaining ASCII checks for
new tutorials, application code, and documentation. All archival source fingerprints matched;
the scoped ASCII run passed 120 checks. This policy is explicit in
[DESIGN_DECISIONS.md](../../DESIGN_DECISIONS.md).

Local warnings expose deliberate spare practice rows, free-response/forward references,
unsupported static function coverage, and absent Google tab mappings. A successful build does
not silently convert these into verified formula results.
