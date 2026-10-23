# Student workbook visual acceptance review

Reviewed 2026-10-22. Status: **accepted for the reviewed renderer scope**.

## Evidence method

This report supersedes the earlier rejected review. Its former completed-state
evidence was invalid because `devel/validate_libreoffice.write_case` created
new unstyled workbooks from calculation writes. That process proves calculations,
not presentation retention.

The current review rebuilt fresh student starter XLSX files in
`/tmp/student_workbook_visual_refresh/starters/`. For each priority lesson, a
disposable completed view began with that exact styled starter workbook. The
temporary review helper copied only cell values, formulas, and `data_type` from the
matching Calc scenario, preserving the starter's fills, borders, dimensions,
fonts, and wrapping. It then changed only print settings in the disposable
copy. That helper has since been removed; its temporary files under `tests/_temp/`
are not part of the current repository.

LibreOffice rendered those copies outside the sandbox with
`render_artifact_libreoffice.sh`. Final proof is under
`/tmp/student_workbook_visual_refresh/renders/`:

| Lesson | Starter | Styled completed state |
| --- | --- | --- |
| Caffeine 3 | `caffeine3_starter_v2.webp` | `caffeine3_completed_v2.webp` |
| Microbes 4 | `microbes4_starter_v2.webp` | `microbes4_completed_v2.webp` |
| Microbes 5 | `microbes5_starter_v2.webp` | `microbes5_completed_v2.webp` |

All 12 sources also rebuilt successfully as fresh XLSX starter bundles before
the final targeted visual pass. Existing lesson warnings concern intentional
practice-range capacity and formula-engine coverage; none are new workbook
serialization failures.

## Accepted presentation behavior

The workbook renderer now separates blank learner construction from empty
design space:

- Supplied data has accessible blue headers, light source stripes, and thin
  internal rules.
- Formula and label targets retain pale, role-specific emphasis, while
  fill-down targets use thin rules instead of a medium colored bar in every
  row.
- A genuine learner label task at the top of a declared area gets a dark,
  blank future-header cell. No label is supplied, but the completed table
  gains a consistent header automatically when the learner types the
  instructor-authored text.
- A contiguous run of two or more learner labels is also recognized as a
  table header below an area top. In the completed ANOVA sheet, the `H6:M6`
  sample-name row is now one coherent header rather than a mixture of plain
  and dark cells.
- An intentionally empty interpretation region remains an open, subtly pink
  writing panel with a clear outer edge. No prompt or conclusion is invented.

The completed Caffeine 3 view demonstrates readable quadratic-result labels,
formula values, column widths, and the preserved response panel. Microbes 4
retains its F-test organization and alternate-value columns after completion.
Microbes 5 shows a recognizable completed ANOVA table with aligned main and
sample-summary headers. In all reviewed files, the student labels, formulas,
and results were absent from the starter and present only in the disposable
completed state.

## Verification

`source source_me.sh && python3 -m pytest tests/test_tutorial_workbook.py -q`
passed: **13 passed**.

The focused contracts protect blank learner work, future-header styling,
contiguous internal headers, thin entry rules, and usable empty interpretation
space. The calculation validator is a separate proof lane and is not repeated
by this visual review.

## Limits

This is LibreOffice evidence for native XLSX output. It does not establish
Google Sheets import fidelity or actual student comprehension. The completed
views use valid Calc scenario values, but they are visual state fixtures rather
than a simulation of every interactive spreadsheet action. Temporary files
under `/tmp/student_workbook_visual_refresh/` support review only.
