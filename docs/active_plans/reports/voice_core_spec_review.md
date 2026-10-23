# Voice core specification review

Review date: 2026-10-22. Scope: the shared compiler/action model, semantic bindings,
validation, DOCX rendering, and workbook role rendering for
[instructional_voice_restoration.md](../instructional_voice_restoration.md).

## Decision

Accept the reviewed core implementation against the approved M1-M2 contract. No blocking
correctness defect or architectural drift was found. This is a focused implementation review;
source restoration, full artifact rebuild, calculation, and visual acceptance remain separate
M3-M5 work.

## Rules and plan

Read AGENTS.md, the repository's Markdown/Python/pytest/repository style guides, the current
changelog entry, and the restoration plan. Python checks used `source source_me.sh && python3`.
No LibreOffice command was run. No production source, test, configuration, or lesson was edited.

The plan explicitly approves semantic links, a common Action representation, ordered actions
within paragraphs, legacy compatibility, heading-prefix metadata, and closed workbook meaning
roles. The implementation follows those boundaries without introducing a prose rewriting layer,
permission model, duplicate formula inventory, or new theme configuration. Per the repository's
"Reviews should simplify" and "Ground requirements in actual needs" principles, this review
does not require speculative formula grammar or additional infrastructure.

## Evidence

- Focused permanent coverage: `tests/test_tutorial_bindings.py`,
  `tests/test_tutorial_semantics.py`, `tests/test_tutorial_docx.py`, and
  `tests/test_tutorial_workbook.py`: **31 passed in 0.51 seconds**. Tests cover compact numbered
  instructions, shared legacy replay, ordered assignments, scalar fidelity, invalid targets,
  region conflicts, heading emphasis/prefix parsing, DOCX text, and workbook seed integrity.
- The permanent Caffeine-style four-item fixture compiles to a native numbered DOCX group with
  one visible formula, preserved prose, emphasized title runs, and an ordinary external link.
  Semantic `label:`, `enter:`, `fill:`, and `select:` destinations do not become DOCX external
  relationships. The fixture is evidence for the presentation contract, not an original-source
  or completed-lesson comparison.
- Additional disposable source-to-DOCX/XLSX probes exercised multiple same-paragraph actions:
  Enter C2, Enter D2, Replace C2, Replace D2 with `=A2^2`, then Fill D2:D3. Replay retained every
  write in order, including translated `=A3^2`; student workbook destinations stayed blank.
- Two explicit alternatives each performed three bindings in one paragraph before two common
  replacements. Both replay cases retained their distinct branch writes and the common writes;
  validation reported no erroneous assignment or replacement conflict.
- Bare bound formulas `=IF(A2>0,"A*B",A2*3*4)` and `=A2<>B2` retained their exact operators,
  quotes, scalar values, visible DOCX text, and replay formulas.
- JSON-quoted literal bindings covered formula-looking unknown-sheet text, Markdown emphasis
  characters, HTML-looking text, a backslash, embedded quotes, comparison operators, and an
  A1-looking unknown-sheet reference. They generated no formula checks, preserved exact visible
  JSON copy text and surrounding prose, and retained the ordinary external hyperlink.
- Real Markdown region declarations compiled through XLSX writing and workbook verification:
  default source and calculation cells plus explicit results and interpretation cells received
  distinct fills. Answer destinations remained blank, and workbook verification passed.
- Assignment bindings to A0, XFE1, A1048577, reversed ranges, multi-cell ranges, and an unknown
  worksheet all produced errors. Permanent tests also reject malformed literal payloads,
  unsupported region roles, overlapping explicit regions, and invalid region coordinates.

## Limits and follow-through

The repository was under active parallel lesson migration during review. Whole-corpus lint,
the complete suite, original-to-current comparisons, LibreOffice exports, spreadsheet calculation,
and final rendered page inspection were intentionally left to the integration and materials
review lanes. Actual per-lesson role declarations need those source/workbook reviews.

The already identified obsolete yellow-fill expectation in `tests/test_tutorial_fill.py` belongs
to its separate correction lane and is not a new finding here. Authoring-document updates were
still in progress and are not accepted by this core review. No claim is made about Google import,
live spreadsheet execution, or student outcomes.
