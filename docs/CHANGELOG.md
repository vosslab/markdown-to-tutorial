# Changelog

## 2026-10-22

### Plan Scope and Execution

- Expand the tutorial converter plan from two pilots to all three Fried Foods/babies tutorials,
  five Microbes tutorials, and the three-part Dr Caffeine set; repair PETase with an explicitly
  synthetic Bradford dataset because the legacy source contains unrelated Microbes material.
- Add [tutorial_execution_ledger.md](archive/tutorial_execution_ledger.md) to track
  foundation, implementation, migration, and review work. Live Google calculation was attempted
  but unavailable without credentials; Google Docs/Sheets import remains unverified.
- Keep completion agent-led: focused DOCX/XLSX behavior checks and PDF visual assessment establish
  local evidence; Google import is optional and reported only with observed evidence. Agents resolve
  scientific migration issues from authoritative sources and document corrections.

### Additions and New Features

- Add [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md) defining the single-source Markdown tutorial/workbook
  format, list actions, worksheet tables, numbering, validation, DOCX/XLSX/PDF outputs,
  simple XLSX import, and Google import acceptance boundaries.
- Add [tutorial_converter_plan.md](archive/tutorial_converter_plan.md) with component
  contracts, six implementation milestones, dependencies, verification, risks, and migration scope.
- Implement source-located compilation, static reference/assignment checks, native XLSX import
  and export, editable DOCX, LibreOffice PDF conversion, and staged three-output CLI bundles.
- Migrate all 12 lessons and extracted original images. Correct mean-test assumptions, signed
  t-test tails, Welch variance handling, F-test directions, ANOVA group sizes, regression ranges,
  coefficient ordering, and unsupported narrative conclusions; document provenance and corrections.
- Add independent SciPy/NumPy expectations and optional real Google Sheets developer tooling.
  Cover 12 lessons, 13 scenarios, 254 final formula values, and 8 synthetic directional checks.

### Implementation Documentation

- Add [INSTALL.md](INSTALL.md), [USAGE.md](USAGE.md), and [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md)
  for the current install and CLI workflow, plus a concise README description. Update
  [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md) to reflect the available CLI and autonomous local completion
  policy. Keep the active execution ledger aligned with observed files and current workstream status.
- Add [TUTORIAL_CATALOG.md](TUTORIAL_CATALOG.md) with indexed links to all 12 sources, build outputs,
  and explicit synthetic PETase provenance. Consolidate observed evidence in
  [implementation_validation.md](active_plans/reports/implementation_validation.md).

### Decisions and Failures

- Record the user's list-first authoring and Google import priorities in
  [HUMAN_GUIDANCE.md](HUMAN_GUIDANCE.md). Record the planned seed-data/student-action separation and
  source-located validation model in [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md). Keep the original
  artifacts and adjacent projects unchanged.

### Developer Tests and Notes

- Rename the application package from `tutorial_lib/` to `sheetlesson/` while retaining the
  `tutorial.py` executable, so shell completion distinguishes the library from the command.
  Update active imports, developer tools, tests, documentation, and the execution ledger; do not
  provide a compatibility alias. Compiler quality review accepted the secure XML parsing,
  flattened helper imports, malformed-formula diagnostics, and literal payload handling; record
  its seven behavior tests and 12 lint checks in the ledger. XML behavior review accepted 12 tests,
  pending hygiene review; workbook import checks passed 137 and 66 checks.
- Extend the repository bootstrap `PYTHONPATH` with both the repository root and `devel/` so the
  root package and shared flat developer-tool helpers import under the required sourced environment.
  Keep the extension after loading `~/.bashrc`, which clears `PYTHONPATH`.
- Reject converter output that has a PDF signature but cannot be parsed as a document with pages.
  Use the declared `pypdf` dependency before publication and retain the previous bundle on failure.
  The focused build tests pass with a regression for a successful converter writing only `%PDF-`.
- Document the macOS agent lane: invoke builds using the LibreOffice wrapper with
  `sandbox_permissions="require_escalated"`; human terminal commands remain ordinary commands.
- Google Docs/Sheets import verification has not been performed. Documentation checks for the
  implementation-facing updates passed local link and ASCII checks. The oversized human-guidance
  bullet is split into focused entries. Existing non-ASCII content in two legacy sources remains
  preserved; report it separately from changed-source verification.
- Build all 12 bundles and visually assess the initial 87 PDF pages. Repair nested-list and table
  pagination findings; final rebuilt-PDF verification remains in progress. Record exact evidence in
  [pdf_validation.md](active_plans/reports/pdf_validation.md).
- Prepare all 13 Sheets cases with independent expectations, then attempt authorized live execution.
  Missing ADC returns exit 2 and creates no Google files; no live calculation or import is claimed.
- Preserve original archival Unicode through an explicit ASCII-check scope rule for
  `2025_Artifacts/**` in the existing layered test registry. New tutorials, code, and documentation
  remain checked; all original SHA fingerprints match and the scoped ASCII checks pass (120).
- Complete source-edit checks for inserted steps and formulas, table relocation, worksheet rename,
  failed-build preservation, and all 12 final PDF reviews. The final sourced Python suite passes
  1272 tests; archive the completed plan and ledger under `docs/archive/`.
- Remove redundant `tests/_temp/pdf_review/` rasters after preserving visual evidence in
  `output/verification/pdf/`; retain deterministic verification reports under `output/verification/`.
