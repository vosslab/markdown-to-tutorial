# Voice core corrections specification recheck

Review date: 2026-10-22. Decision: **ACCEPT** the reviewed emphasis, heading/hardbreak,
and destination-reference corrections against the approved semantic binding contract.
No blocking defect was found. This supplements the original
[voice_core_spec_review.md](voice_core_spec_review.md).

## Scope and rules

Read the restoration plan, AGENTS.md, Python/Markdown/repository/pytest style rules,
the three correction reports, and their production and focused test surfaces. Reviewed
`scalar_payload`, `_compile_bindings`, terminal hardbreak restoration, formula boundary
scanning, structural heading recognition, and reference validation. Only this report was
written. Python commands used `source source_me.sh && python3`; all checks were offline
and none invoked LibreOffice.

The approved contract requires authored visible text and emphasis to survive independently
of executable values. The implementation resolves that boundary without rewriting lesson
prose or extending table/legacy scalar syntax. The hardbreak correction restores an actual
authored backslash-newline omitted by block parsing; it does not introduce automatic prose
wrapping. Destination references are exempted only for an exact write target in the same
paragraph, while formula dependencies continue through ordered validation. These choices
fit the plan's "Fix the design, not the symptom" and actual-needs requirements.

## Independent evidence

Final focused command, after the destination-reference owner released its files:

```bash
source source_me.sh && python3 -m pytest tests/test_tutorial_bindings.py tests/test_tutorial_semantics.py tests/test_tutorial_docx.py tests/test_tutorial_workbook.py tests/test_pyflakes_code_lint.py tests/test_function_typing.py -q
```

Result: **174 passed in 0.93 seconds**. The four behavior modules account for 36 tests;
the remaining checks cover code lint and function annotations. Coverage includes nested
emphasis, raw and bold JSON strings, escaped literal stars, formula operators, native DOCX
breaks at list and paragraph boundaries, literal code backslashes, and heading diagnostics.

A separate disposable combined probe compiled and rendered:

- A `***Sample Size***` label, which became the workbook string `Sample Size` and a
  DOCX run with both bold and italic formatting.
- A bold `=IF(A2<>B2,"A_*B",A2*3*4)` formula. Replay retained the exact source formula
  in C2 and translated it to `=IF(A3<>B3,"A_*B",A3*3*4)` in C3. DOCX retained the
  original formula text, including quoted punctuation and multiplication operators.
- A bold JSON string containing embedded quotes, a backslash path, and literal stars.
  Replay decoded the intended cell string; DOCX retained the visible JSON copy text and
  escapes without interpreting the literal stars as authored emphasis.
- Four paragraph-terminal authored breaks. DOCX contained four native `w:br` elements;
  paragraph text ended in newlines without literal terminal backslashes. Semantic `label:`,
  `enter:`, `fill:`, and `select:` destinations created no external relationships.
- Informational `Step-by-Step Tutorial:` preserved as written. The focused heading
  regression separately rejects `Step2: Calculate`, `Step 2 Calculate`, and `Step:`.

Independent destination-validation probes confirmed all of the following:

| Instruction case | Observed unavailable input |
| --- | --- |
| Mention I2 while assigning `=A2` to I2 | None |
| Mention I2 while assigning `=A99` to I2 | A99 |
| Assign `=J2` to I2 before assigning 4 to J2 | J2 |
| Assign 4 to J2 before assigning `=J2` to I2 | None |
| Assign I2, then read missing J2 in another paragraph | J2 |
| Select missing J2 | J2 |

Thus the correction removes the demonstrated destination-mention false positive while
preserving genuine missing inputs, Select checks, and ordered formula dependencies.

## Review boundary

The correction reports are accepted for their implementation claims:
[voice_binding_emphasis_fix.md](voice_binding_emphasis_fix.md),
[voice_heading_hardbreak_fix.md](voice_heading_hardbreak_fix.md), and
[voice_target_reference_fix.md](voice_target_reference_fix.md). Their earlier test totals
describe earlier checkpoints; the 174-test result above is this review's final targeted run.

This is specification acceptance of the reviewed core corrections. Separate quality review
must still compare original lessons, restored sources, generated student pages, and workbook
regions. This report does not accept all twelve sources, PDF layout, final calculation
artifacts, whole-suite integration, Google behavior, or student outcomes.
