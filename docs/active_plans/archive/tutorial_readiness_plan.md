# Tutorial readiness completion plan

Updated: 2026-10-22. Status: complete. Final artifact, calculation, visual, suite, and integrated
review checks passed. Google Sheets evidence remains unavailable and is explicitly out of scope for
local completion.

## Goal and evidence

Deliver 12 accurate, usable single-source lessons whose current DOCX, XLSX, and PDF outputs support
the student workflow. The initial suite, oracle, and PDF reports are snapshot evidence; current
readiness evidence is summarized in [readiness_execution.md](../reports/readiness_execution.md),
[implementation_validation.md](../reports/implementation_validation.md), and
[test_validation.md](../reports/test_validation.md). The contract is
[TUTORIAL_SPEC.md](../../TUTORIAL_SPEC.md).

The readiness work repaired incomplete ANOVA instructions and labels, scientific contradictions,
historical screenshots that differed from current steps, missing workbook defaults, and document
readability. Fourteen worksheet Google mappings remain absent and live credentials were unavailable.
Local Calc execution does not establish Google behavior.

## Settled decisions

- Fix defects at their authoring or rendering source. Remove obsolete paths and incomplete scaffolds;
  do not add compatibility aliases or stubs.
- Keep the existing schema and action directives. The demonstrated instruction gaps fit current
  Markdown.
- Give each label one owner: seed it for inspection, or leave the cell blank for a student `Label`
  action. Identical repeated assignments retain their warning.
- Reject label-only list items without substantive continuation, a nonempty fenced instruction, a
  valid action, or a substantive descendant. An empty child does not rescue its parent. Diagnose
  from parsed Markdown structure and source locations.
- Freeze workbook panes at `A2` and set a minimum 12-character column width, including blank entry
  columns. Teach number formats as explicit menu tasks where needed; do not infer formats.
- Replace misleading worked-example screenshots with native editable tables. Preserve source
  assets and keep historical images only when they cannot be mistaken for current instructions.
- Include a native Word `PAGE` footer. These targeted changes do not promise full spreadsheet
  formatting fidelity.
- Keep generated snapshots and verification evidence under ignored `tutorial_output/`.
- Do not invent Google IDs or claim import/execution without observation. Report local Calc
  execution separately from Google evidence.

## Work ledger

| Work | Status | Evidence or remaining work |
| --- | --- | --- |
| Lesson content | Complete; independent content review accepted | All 12 sources passed content quality review. See [microbes_readiness.md](../reports/microbes_readiness.md) and [other_readiness.md](../reports/other_readiness.md). |
| Parser and instruction validation | Implemented; focused spec and quality checks accepted | Source-located AST checks reject incomplete label-only items and retain substantive descendants. |
| DOCX/XLSX readability | Implemented; focused spec and quality checks accepted | PAGE footer, frozen `A2`, minimum widths, and blank student assignments verified. |
| Formula storage and local execution | Implemented; focused reviews accepted | Recognized formula tokens receive `_xlfn.` only at XLSX storage. Calc passed 254 final values in 13 scenarios and 15 signed probes; see [local_calculation_readiness.md](../reports/local_calculation_readiness.md). |
| Google evidence | Limitation recorded | All 14 worksheet mappings are absent and live credentials unavailable. No Google import or execution claim. |
| Repository layout and fresh artifacts | Complete | Use `make_tutorial.py`, `tutorial_lib/`, `tutorial_data/`, and `tutorial_output/`; no aliases. Twelve fresh bundles and 36 artifacts match current fingerprints. |
| PDF visual review | Complete | All 65 current PDF pages were reviewed; the final rebuilt babies t-test PDF was re-rendered and all six pages rechecked. See [readiness_visual.md](../reports/readiness_visual.md). |
| Final suite and closeout | Complete | The full suite passed 1309 tests, the new formula I/O module passed direct checks, and integrated implementation/content reviews accepted the result with no blockers. See [test_validation.md](../reports/test_validation.md). |

## Completion checks

1. An independent walkthrough covers all lessons from their generated initial workbooks: labels,
   targets, formulas, selections, menus, interpretations, and alternatives.
2. Fresh DOCX/XLSX readback confirms formulas, seed values and addresses, blank student assignments,
   and source references. Representative source edits, renumbering, table moves, sheet renames, and
   previous-bundle preservation are checked where affected.
3. Independent numerical expectations cover revised assignments and alternatives. Any engine report
   names the engine and evaluated cells; expected mathematics alone is not formula execution.
4. Fresh builds follow the last content/style edits. Record fingerprints, page counts, all-page
   contact sheets, and full-size examples; repair clipping and pagination defects.
5. Run focused changed-contract checks and the final repository suite using
   `source source_me.sh && python3 -m pytest tests/`. Keep one-time evidence outside permanent tests.
6. Separate local completion from unavailable Google mapping, import, calculation, spill, and
   navigation checks. The local checks passed; external Google behavior remains unverified.

## File scope

The readiness work edits authored sources/assets in `tutorial_data/`, affected modules in
`tutorial_lib/`, focused tests, and current reports under `docs/active_plans/reports/`. Canonical
contract and decision docs are maintained in the root `docs/` directory. Human-stated guidance is
recorded in [HUMAN_GUIDANCE.md](../../HUMAN_GUIDANCE.md).
