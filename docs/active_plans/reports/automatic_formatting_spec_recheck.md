# Automatic formatting spec recheck

Review date: 2026-10-22. Status: the literal-action rendering finding is resolved.

## Finding recheck

Rechecked the approved [automatic formatting plan](../automatic_tutorial_formatting.md),
[formatting specification review](automatic_formatting_spec.md), and formula/literal rules in
[TUTORIAL_SPEC.md](../../TUTORIAL_SPEC.md). `tutorial_lib.formulas._preserve_literal_payload`
now replaces the parsed action payload with its authored raw text after the bold action label.
Formula recognition remains disabled for JSON literal `Enter`/`Replace` values and `Label`
payloads.

## Evidence

- Compiled `Enter C2` and `Replace C2` with JSON `"=A2*B2*3"`, plus `Label D2` with
  `=A2*B2*3`. The three action scalars were text with the exact value `=A2*B2*3`; none
  generated a formula check.
- Native DOCX output preserved each action's exact visible payload, including every `*`, and
  rendered these scalar payloads with ordinary text formatting and no formula green.
- Explicit code spans around JSON and Label literals retained their payload text and code font,
  without formula green.
- The existing native DOCX contract covers quoted formula examples in prose and ordinary Tutorial
  tables, plus bare formulas in prose, actions, links, code spans, and fences. All eight expected
  formula runs retain their exact text, Roboto Mono, and green `188038` formatting.
- The DOCX contract snapshots compiled tokens before rendering and confirms rendering leaves them
  unchanged. Semantic tests continue to cover scalar classification and blank student answer
  destinations; workbook tests pass unchanged.
- `source source_me.sh && python3 -m pytest tests/test_tutorial_docx.py tests/test_tutorial_semantics.py -q`:
  16 passed. `source source_me.sh && python3 -m pytest tests/test_tutorial_workbook.py -q`:
  10 passed.

## Review outcome

The correction matches the plan and the documented distinction between literal action scalars and
narrative examples. It does not change formula grammar, workbook scalar classification, or workbook
generation scope. Existing focused tests cover the changed rendering contract and core semantic and
workbook behavior. No additional plan drift was found. No LibreOffice process was invoked.
