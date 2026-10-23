# Student publishing implementation

This ledger records completion evidence for the approved plan for student-designed tutorials,
automatic reference maintenance, and DOCX/XLSX presentation.

| Workstream | Scope | Owner | Status |
| --- | --- | --- | --- |
| Worksheet edits | CLI and source edits | Fresh repair and verification reviewers | Complete: real Caffeine insert A, grow 25 to 50, shrink 25 to 10, and ANOVA H:M to J:O previews, writes, and exports pass; learner prose and math are preserved |
| DOCX presentation | Step heading indent, prose alignment, hard breaks | Inherited presentation expert | Complete: specification and quality reviews, broad 94-page review, final two-page correction review, and integration accepted |
| XLSX presentation | Formatting rules, future headers, empty response panels | Fresh workbook polish expert | Complete: specification, quality, visual, and integration reviews accepted; three styled completed workbooks reviewed |
| Authoring | ASCII, templates, mismatch validation | Authoring workstream | Complete: 12 lessons and 3 templates; lint reports 0 errors |
| Documentation | Guidance, decisions, and this ledger | Documentation workstream | Complete |
| Reviews | Independent quality reviews | `root` to coordinate | Complete: editor, DOCX, workbook, and integration reviews accepted |
| Acceptance | Full build, formula calculation, visual verification | `root` | Complete: all 12 lessons and 3 templates compile without errors; 41 focused tests and 1,828 full-suite tests pass; 12 bundles contain 36 outputs matching manifest fingerprints |

Mechanical documentation updates use a small model; cross-module correctness and implementation
work use inherited experts.

The worksheet editor passes real preview, write, and export checks for column insertion, data growth
and shrinkage, and ANOVA column moves. The accepted operations preserve learner-facing prose and
formulas. A correction removed generic prep/copula guessing and preserves ambiguous prose with
line-numbered notices. The leaf `--write` path reports invalid columns clearly. The final editor
specification-quality review and integration review are accepted.

The workbook's final specification and quality reviews are accepted. Its visual report covers three
completed styled workbooks, future headers that remain blank and continuous, thin rules, and
open-response panels. See the [workbook visual report](reports/student_workbook_visual.md). Final
DOCX specification and quality reviews are accepted. See the
[document visual report](reports/student_document_visual.md).

## Acceptance evidence

- The accepted [integration review](reports/student_publishing_integration.md) verifies the source,
  generated outputs, and implementation against the approved plan.
- All 12 lessons and 3 templates compile without errors; the focused integration rerun passes 41
  tests and the full repository suite passes 1,828 tests.
- All 12 canonical bundles contain 36 DOCX/XLSX/PDF outputs whose source and artifact fingerprints
  match their `validation.json` records. Calc passes 13 scenarios and 254 comparisons.
- DOCX visual review accepts all 94 PDF pages and the final two-page correction. Workbook visual
  review accepts starter and completed-state evidence for Caffeine 3, Microbes 4, and Microbes 5.
- Final editor specification-quality, DOCX, workbook, and integration reviews are accepted.

## Independent calculation oracle

The independent calculation validator passed 13 scenarios and 254 Calc comparisons; its report is at
`/tmp/student_publishing_validation/calc/run-8c24gbyv/report.json`. The prepared oracle at
`/tmp/student_publishing_validation/tutorial_expectations.json` also includes 8 synthetic direction
checks. Validator output is unstyled and is not visual evidence. An earlier workbook visual report
incorrectly relied on that output and was superseded by fresh workbook screenshots and review.

The current full suite passed 1,828 tests in 4.93 seconds with `source source_me.sh && python3 -m pytest -q`.
Earlier Bandit, typing, and ASCII-fixture failures are resolved. The numeric calculation check passed
13 scenarios and 254 comparisons with the prior formulas unchanged.

DOCX step headings use zero left indent and native paragraph indents, including a 0.2-inch body indent.
Justify prose when its estimated natural wrapping exceeds two lines; preserve hard breaks as left
aligned, and keep the corrected formula introduction justified. The fresh specification re-review
accepted these rules.
The broad 94-page PDF review and final two-page correction review accepted the presentation. The
canonical build verified all 12 bundles and 36 outputs against manifests and source/output SHA-256
fingerprints. Final integration and the editor spec-quality review are accepted; see the
[integration review](reports/student_publishing_integration.md).

The count of naturally wrapped lines is estimated from font metrics and paragraph width. Google Docs
and Sheets import fidelity and live Google calculation remain unverified. Ambiguous unmarked
references still receive author review, and no student study was performed.
An accidental review write to Caffeine was restored to prior SHA-256
`671e14419101d4397556c3f3ac986c28373ce5562f3a3961504b35ba96327d1f` and rebuilt and verified; interim
failures are resolved historical evidence.
