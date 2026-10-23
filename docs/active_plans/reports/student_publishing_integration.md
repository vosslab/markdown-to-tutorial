# Student publishing integration review

Reviewed 2026-10-22. Status: **accepted**.

## Decision

The implementation satisfies the approved student-publishing plan as one coherent
system. It preserves the educational boundary: authors and learners work with
ordinary A1 coordinates and Excel formulas, authors decide worksheet structure and
learner activities, and the compiler supplies consistent presentation and limited,
explicit maintenance support. No LLM-generated prose or new author-facing formula
language was introduced.

## Cross-component contract review

- Active lesson files and the three starter templates are ASCII Markdown, accept
  readable named entities, and reject numeric character references. The compiler
  preserves instructor prose and diagnoses only an explicit visible cell/action
  mismatch.
- The Workbook section remains the student starting state. Tutorial actions remain
  blank in the generated workbook, including learner labels, formulas, and written
  responses. The spreadsheet renderer adds headers, restrained color, thin rules,
  and response panels without inventing instructional content.
- Worksheet maintenance uses preview-first, familiar operations for an author-made
  layout decision. Inserts, moves, and observation resizing update declared geometry,
  action targets, explicit references, and marked spreadsheet formulas. Atomic
  writes require the source to match the preview. Ambiguous bare coordinates and
  worked numerical explanations are retained and reported for author review.
- Native DOCX keeps major Step headings left of the 0.2-inch body indent, gives
  subordinate headings distinct positions, justifies naturally long prose, and
  leaves deliberate hard-break displays and formula blocks left aligned. Formulas
  have a distinct, editable green presentation.

## Evidence

- The latest full repository suite passed **1,828 tests**.
- A focused integration rerun passed **41 tests** across ASCII/source validation,
  worksheet edits, DOCX presentation, and workbook presentation. All 12 lessons
  plus all three templates compile with no errors.
- The 12 canonical bundles contain all 36 declared DOCX/XLSX/PDF artifacts. Each
  current source fingerprint and artifact fingerprint matches its bundle
  `validation.json` record.
- The separate calculation lane passed 13 Calc scenarios and 254 comparisons.
- The document review accepted all 94 PDF pages; the workbook review accepted styled
  starter and completed-state evidence for Caffeine 3, Microbes 4, and Microbes 5.
  Their methods and limits are recorded in
  [student_document_visual.md](student_document_visual.md) and
  [student_workbook_visual.md](student_workbook_visual.md).

## Limits retained deliberately

Google Docs and Google Sheets import fidelity, live Google calculation, and student
learning outcomes remain unverified. DOCX wrapping is estimated before import, so
Google Docs can choose different exact line breaks. The worksheet editor supports
the documented structural operations; it intentionally does not guess about
ambiguous prose or rewrite an author's scientific interpretation.
