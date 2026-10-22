# Fresh Fill specification review

Verdict: fix required before specification approval.

This review inspected the current implementation against the efficient authoring contract:
enter the first formula once, then author one `**Fill C2:C26:** Down` or rectangular
`**Fill E2:F26:** Down` action. It did not rely on an earlier approval and changed no product
files. The remaining issue concerns invalid-source handling, rather than lesson calculations.

## Required correction

An invalid source formula ending in an unmatched closing parenthesis crashes compilation:

```markdown
- **Enter C2:** `=A2)`
- **Fill C2:C3:** Down
```

The observed exception is `IndexError: pop from empty list`. Ordinary Enter validation already
handles that tokenizer failure as a `formula-syntax` diagnostic, but the Translator invocation
in [tutorial_lib/validation.py](../../../tutorial_lib/validation.py) catches only TokenizerError
and TranslatorError. Fill must preserve the ordinary diagnostic behavior instead of aborting
the compiler. Include this tokenizer failure in the narrow translation error handling, or
otherwise reject that invalid source without constructing a Translator. Recheck this exact
case after the correction.

## Verified contract

- The compiler recognizes literal `Down`, rejects reversed ranges and ranges with only one
  row, and accepts both requested range shapes.
- Source formulas must exist in every incoming branch and be identical per column. Different
  branch-local formulas are accepted when Fill is inside each alternative. The focused branch
  test verifies selected execution writes for both alternatives.
- Translation preserves mixed and absolute anchors, quoted sheet names, and string literals.
  Generated children receive ordinary conflict, reference, and availability checks in row order.
  A generated `=A1048577` produces an `invalid-address` error, and a destination containing a
  different value produces an `assignment-conflict` error.
- Translation builds children before applying them to instruction state. Failed compilation
  cannot be replayed because `prepare_cases` rejects documents containing errors. The reported
  exception still needs correction so failure reaches that controlled diagnostic path.
- Shared `prepare_cases` supplies translated child writes to both execution engines. The DOCX
  test finds one authored Fill instruction without generated Enter lines, and the XLSX test
  confirms blank answer cells with destination styling.

The actual caffeine source compiles without errors and expands `C2:C26` to 24 children and
`E2:F26` to 48 children. Final formulas are `=A26^2`, `=A26`, and `=C26` respectively.

The actual PETase source compiles without errors and uses five Fill actions. Its verified
endpoints are `=B8-$B$2`, `=$G$2*A8+$G$3`, `=C8-I8`,
`=(B15-$B$2-$G$3)/$G$2`, `=E15*C15`, and `=F15*D15`.

## Evidence

Run from the repository root:

```bash
source source_me.sh && python3 -m pytest tests/test_tutorial_fill.py \
  tests/test_tutorial_semantics.py tests/test_sheets_validation.py \
  tests/test_tutorial_docx.py tests/test_tutorial_workbook.py -q
```

Observed: 26 passed in 0.40 seconds.

Additional direct `compile_source` probes used a minimal declared Data sheet and the two
instructions above. Formula `=A1048576` followed by Fill produced `invalid-address`; formula
`=A2)` followed by Fill raised the exception. Direct `compile_document` and `prepare_cases`
calls on both real lesson sources produced the expansion counts and endpoint formulas above.

These are offline compiler, replay-preparation, native DOCX, and student XLSX checks. No live
spreadsheet calculation or rendered PDF check was performed by this reviewer.
