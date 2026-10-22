# Tutorial converter execution ledger

Updated: 2026-10-22

This ledger tracks the completed plan [tutorial_converter_plan.md](tutorial_converter_plan.md).
Local completion uses behavior checks and agent PDF assessment, without human milestone signoff.
Report Google behavior only when directly observed. Final integration and rebuilt PDF assessment
are complete.

| Workstream | Status | Evidence or remaining work |
| --- | --- | --- |
| Foundation and shared model | Implemented; specification and quality reviews accepted | Seven behavior tests and 12 lint checks passed; secure XML parsing, flat helper imports, malformed-formula diagnostics, and literal payload handling reviewed. |
| Workbook | Accepted by specification and quality review | XLSX export/import and round-trip behavior checks exist; import checks passed 137 and 66. |
| XML parsing | Behavior and hygiene reviews accepted | 12 behavior tests passed; no distinct hygiene findings remained. |
| Renderer | Accepted; final PDF review passed | DOCX instructions, formulas, images, references, tables, and pagination repairs are implemented. |
| Build | Accepted; final integration passed | CLI, format subsets, staged bundles, PDF validation, and previous-output protection are implemented. |
| Babies | Migrated, built, source review accepted | All 3 lessons, original data, and 12 extracted images; corrections documented. |
| Microbes | Migrated, built, source review accepted | All 5 lessons; statistical and post-freeze prose corrections documented. |
| Dr. Caffeine | Migrated, built, source review accepted | All 3 lessons with 25 original data pairs and 14 original illustrations. |
| PETase | Repaired, built, source review accepted | Explicit synthetic Bradford calibration; original source has unrelated Microbes data. |
| Independent calculations and Sheets tooling | Accepted by specification and quality review | 12 lessons, 13 scenarios, 254 expected final formula values, 8 synthetic directional checks. |
| Optional real Google calculation | Attempted; unavailable | Authorized live attempt returned exit 2 without ADC. No Google workbook was created. |
| Final integration | Complete | All 12 bundles rebuilt; final 88-page visual review accepted; 1272 repository tests passed; editable-source, table-move, worksheet-rename, and previous-bundle preservation contracts verified. Package is `sheetlesson/` beside `tutorial.py`. |

## Evidence and inventory

- [TUTORIAL_CATALOG.md](../TUTORIAL_CATALOG.md) indexes all 12 source lessons.
- [implementation_validation.md](../active_plans/reports/implementation_validation.md) records implementation
  behavior, review boundaries, and final verification status.
- [pdf_validation.md](../active_plans/reports/pdf_validation.md) records visual assessment and pagination findings;
  use its latest evidence for final render status.
- [calculation_validation.md](../active_plans/reports/calculation_validation.md) records independent numerical
  methods, results, commands, and Google execution limits.
- Migration reports: [babies_migration.md](../active_plans/reports/babies_migration.md),
  [microbes_migration.md](../active_plans/reports/microbes_migration.md),
  [caffeine_migration.md](../active_plans/reports/caffeine_migration.md), and
  [petase_migration.md](../active_plans/reports/petase_migration.md).

Bundles are generated under `output/<source-stem>/`. Original artifacts and sibling source projects
are inputs, not migration write targets. Existing user modifications to historical files predate
this work and remain intact. No Google import or live formula execution is claimed.
