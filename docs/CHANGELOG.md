# Changelog

## 2026-10-22

### Readiness implementation and current evidence

- Complete the focused result-label pagination SPEC review: the renderer meets the adjacent
  same-row, next-column Label/Enter-or-Replace contract; three affected DOCX exports carry
  `keep_with_next` only on the label paragraphs. The referenced standalone SPEC file was absent,
  so the review records the supplied contract and DOCX evidence in
  [the pagination review](active_plans/reports/teaching_pagination_spec.md). Rebuilt PDF visual
  verification remains pending.
- Consolidate the active executable layout and entry points: `make_tutorial.py`, `tutorial_lib/`,
  `tutorial_data/`, and ignored `tutorial_output/`; do not provide old-name aliases. Expand the
  README with a working quick start and links to the installation, usage, authoring, and format
  guides.
- Define the formula I/O boundary: recognized modern function tokens receive `_xlfn.` only for
  XLSX storage and are normalized on readback. This preserves authored formula math and text.
- Record local final-state formula execution separately from offline static checks and Google
  execution. LibreOffice Calc passed 254 independent expected values over 13 scenarios, including
  15 signed Welch probes. Fourteen Google worksheet mappings remain absent and live credentials
  were unavailable; this result is not Google validation.
- Refresh execution evidence after the coordinated rename: 12 lessons and all 36 DOCX/XLSX/PDF
  artifacts were checked. After final whitespace cleanup, the babies t-test DOCX/XLSX/PDF bundle was
  rebuilt from its current source; the source and all artifact fingerprints are current, and its six
  pages were re-rendered and reviewed. All 65 current PDF pages have no blocking visual findings.
  Calc passed 254 comparisons across 13 scenarios, the repository suite passed 1309 tests, and
  integrated implementation/content reviews accepted the result. Archive the completed plan; 14
  Google worksheet mappings remain absent and Google behavior remains unverified.
- Complete first-pass source corrections for all 12 lessons after direct original-to-generated
  comparisons; restore Babies task ordering and standalone setup, Microbes narrative and statistical
  boundaries, independently usable Caffeine lessons, and PETase's qualified synthetic Bradford task.
  Fresh visual review then found three misleading Caffeine figures and recurring label/step page
  splits. Those corrections, rebuild, and quality closeout remain open; see the
  [teaching quality summary](active_plans/reports/teaching_quality_summary.md).
- Clarify the review standard: preserve established Babies/Microbes teaching experience and voice,
  correcting verified errors, typos, and format faults with minimal wording changes. Treat Caffeine
  as a draft foundation and complete all three parts as polished standalone classroom lessons.
- Complete focused Fill/layout specification reviews; the full all-12 generated-XLSX walkthrough
  remains in progress.
  Shared Fill handling reports malformed source formulas through controlled diagnostics; label
  sizing includes quoted formula text such as IF decisions while preserving blank answer cells.
  Follow-up group artifact reviews and final quality/HCI inspection remain pending. Review reports
  name ignored `tutorial_output/` artifacts as code paths instead of broken links.
- Complete an independent established-teaching SPEC review of the current Babies 1-3 and Microbes
  1-5 DOCX/PDF/XLSX bundles. The report records direct source-to-output evidence, formula-free
  starting workbooks, and fresh renders of all current PDF pages; 45 pages were reviewed.

### Behavior or Interface Changes

- Apply the final user-selected layout: `make_tutorial.py`, `tutorial_lib/`, `tutorial_data/`,
  and default generated `tutorial_output/`. Move tracked sources with Git, retain prior staged
  edits, and move generated evidence intact. Update imports, discovery, defaults, active commands,
  documentation links, and readiness ownership without compatibility aliases. Historical changelog
  entries and archived plans retain their snapshot names. Existing generated manifest contents
  remain historical until the final rebuild.

### Readiness Contract and Status Reconciliation

- Clarify in the specification and authoring guide that labels are either seeded for inspection or
  left blank for student `Label` actions; preserve the existing warning for identical repeated
  assignments. Reject label-only instruction items from parsed structure, including cases where an
  empty child would otherwise obscure the missing instruction. Keep the existing authoring schema.
- Set the readiness output contract to freeze panes at A2, use a 12-character minimum width for
  columns including blank entry cells, and include a native Word PAGE footer field. Keep number
  formats as explicit authored menu tasks when needed; do not infer arbitrary styles or promise full
  spreadsheet formatting fidelity.
- Replace misleading worked examples with native editable tables while retaining original assets.
  Record focused preproduction decisions without adding compatibility paths or stubs.
- Earlier ledger status snapshot was superseded by current review evidence below and in the active
  readiness plan. Content, compiler, export, local formula execution, fresh builds, and visual review
  are complete; final repository-suite and closeout remain open.
- Verify documentation links with `tests/test_markdown_links.py` (71 passed) and run the repository
  character check on each edited Markdown file.

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

### Fixes and Maintenance

- Synchronized shared style guides, tests, and repository support files from the starter template.

### Decisions and Failures

- Record the user's list-first authoring and Google import priorities in
  [HUMAN_GUIDANCE.md](HUMAN_GUIDANCE.md). Record the planned seed-data/student-action separation and
  source-located validation model in [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md). Keep the original
  artifacts and adjacent projects unchanged.

### Developer Tests and Notes

- Document the macOS sandbox restriction for every direct or indirect LibreOffice invocation,
  including PDF exports, conversion tests, and ODP imports; use repository scripts outside it.
- Validate the final naming layout with CLI help, a `tutorial_lib.compiler` import, explicit
  `pyflakes devel/validate_libreoffice.py`, and the full repository suite (1305 passed).

- Earlier naming experiment (superseded by the final layout recorded above): rename the application
  package from `tutorial_lib/` to `sheetlesson/` while retaining the
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
- Earlier snapshot only: source-edit checks, failed-build preservation, and 12 PDF reviews were
  recorded with the then-current 1272-test suite. The later coordinated rename and readiness work
  require fresh verification; see current reports under `active_plans/reports/`.
- Historical review rasters and verification paths were moved with the selected output directory.
  Current evidence is under `tutorial_output/verification/`.
