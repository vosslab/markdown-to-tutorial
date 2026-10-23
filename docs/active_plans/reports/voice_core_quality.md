# Voice core quality review

Review date: 2026-10-22. Decision: **ACCEPT** the compiler, parser, semantic binding,
validation, DOCX, and workbook style changes against
[the restoration plan](../instructional_voice_restoration.md) and the accepted core
specification. No actionable quality finding was identified.

## Review scope

Reviewed the changed core implementation and call paths in `tutorial_lib/compiler.py`,
`parser.py`, `semantic_bindings.py`, `formulas.py`, `model.py`, `validation.py`,
`docx_inline.py`, `docx_renderer.py`, `docx_styles.py`, and `workbook.py`, along with the
focused tests and the approved plan. The review focused on meaning remaining independent of
presentation, source formulas not being copied into a second inventory, ordered actions in a
paragraph, explicit raw formula/JSON contexts, terminal authored hardbreaks, and whether the
new style behavior stays local and understandable.

## Findings

None. The core has a clear boundary: semantic links compile to ordered `Action` records, while
renderers keep the authored inline content as the visible text. Validation groups actions by
token and applies them in their original order, so multiple writes in one paragraph retain
replay order. Formula checks derive from those action records; there is no duplicate formula
inventory. Formula scanning is limited to recognizing copy text and leaves formula validation
to the existing validation path. JSON and formula-looking literal payloads are kept out of
Markdown interpretation where needed. The hardbreak adjustment is source-span-local and only
restores an authored terminal backslash-newline. Workbook roles are a closed set, with explicit
regions checked for overlap before rendering.

The DOCX changes retain authored headings and emphasis while removing only the structural prefix
identified during compilation. List spacing and formula appearance are applied through small style
helpers. Workbook styling follows the existing table geometry, answer-cell targets, and explicit
role declarations; no prose rewriting or style permission layer was introduced. These choices
meet the plan and the repository principles of KISS, Ground requirements in actual needs, and
Reviews should simplify.

## Evidence and limits

A disposable in-memory probe compiled and rendered one prose sentence containing Enter, Label,
and Enter bindings. It confirmed action order and scalar values, exactly one formula-check entry
per formula, preserved visible prose and formula copy text, and no hyperlink relationships for
semantic destinations. The repository bootstrap was used (`source source_me.sh && python3`).

The accepted core-specification report records 174 focused tests passing. This review did not
rerun the full suite or invoke LibreOffice; PDF appearance and workbook visual acceptance remain
with the artifact-review lane. The reported unrelated report-image suite failure is outside this
code review's changed surface.

## Open questions

None for the reviewed core contract. This acceptance does not establish lesson voice fidelity,
PDF layout, live spreadsheet behavior, or student outcomes; those remain covered by their separate
review workstreams.
