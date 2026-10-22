# Converter teaching quality review

## Verdict

Accept the focused Fill Down and student-workbook sizing changes. No blocking correctness,
design, or maintainability issue was found in the reviewed implementation. This review changes
only this report; other agents own product code, lesson content, and shared ledgers.

## Design assessment

- Fill remains one authored action with generated Enter children. Reusing ordinary assignment,
  conflict, reference, entry-cell, and branch-state handling avoids a second execution model.
  The existing Translator dependency supplies spreadsheet reference translation; a new formula
  evaluator would add unnecessary complexity.
- Every incoming branch must supply an identical formula per source column. Branch-local Fill
  permits different formulas, and shared replay filters the parent branch before expanding its
  generated children. The tests check both joined and branch-local execution choices.
- Children are translated before being applied to state, then applied in row and column order.
  Same-row references to earlier filled columns become available to subsequent calculations.
  Original source spans remain attached to generated diagnostics. DOCX renders the concise
  authored item, while XLSX preserves blank answers and styles the generated destinations.
- Workbook sizing reads literal Label, Enter, and Replace text across all alternatives and
  possible quoted formula text operands. It bounds widths at 12 through 48, wraps blank answer
  cells, and reserves height for anticipated multiline text. This is a small shared policy
  tied directly to the demonstrated classroom problem, without lesson-specific exceptions,
  author configuration, or added validation infrastructure.

## Independent verification

Command:

```bash
source source_me.sh && python3 -m pytest tests/test_tutorial_fill.py \
  tests/test_tutorial_semantics.py tests/test_sheets_validation.py \
  tests/test_tutorial_docx.py tests/test_tutorial_workbook.py -q
```

Result: **26 passed in 0.39 seconds**. These checks exercise mixed and absolute anchors,
quoted sheet names, unchanged string literals, downstream range availability, selected branch
writes, destination conflicts, invalid sources/directions/ranges, blank student workbooks, and
concise native DOCX output. The workbook test verifies label width, all-alternative sizing,
quoted IF decision strings, wrapping, reserved row height, and preservation of layout after
values are entered beside occupied result cells. They protect durable behavior rather than
requiring a permanent test for each lesson or destination.

Additional direct probes independently confirmed:

- `Enter C2 =A2)` followed by `Fill C2:C3 Down` returns both `formula-syntax` and
  `fill-formula` diagnostics instead of raising the tokenizer exception.
- The resulting invalid document is rejected by shared case preparation, workbook export,
  and DOCX export, each with a controlled ValueError before writing an artifact.
- The current caffeine quadratic lesson compiles without errors: its two Fill actions generate
  24 and 48 children, ending in `=A26^2` and `=C26` respectively. Shared replay contains 105 writes.
- The current PETase lesson compiles without errors: its five Fill actions generate 6, 12, 2,
  2, and 2 children. Endpoints preserve the expected absolute references and chained dependencies:
  `=B8-$B$2`, `=C8-I8`, `=(B15-$B$2-$G$3)/$G$2`, `=E15*C15`, and `=F15*D15`.
  Shared replay contains 38 writes.

## Small maintenance note and limits

The malformed-formula regression also asserts the third-party exception wording
`pop from empty list`. The useful contract is the source-located diagnostic and blocked export;
that exact upstream message is incidental and could be removed during routine test maintenance.
It is not a product defect or an approval blocker.

Width and height are estimates, not font measurements or evaluation of possible formula results.
The current numeric Fill lessons do not require row-height estimates for long text produced by
generated formulas. Future filled text formulas would need separate representative layout
evidence. This review performed offline compilation, replay preparation, DOCX, and XLSX checks;
it did not invoke LibreOffice, recalculate formulas in a live spreadsheet, or verify Google
Sheets appearance. Actual populated Calc render evidence is assessed in the separate
[teaching_workbook_spec_review.md](teaching_workbook_spec_review.md).
