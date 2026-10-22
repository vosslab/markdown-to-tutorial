# Fill invalid-formula fix

`Fill` now converts the openpyxl tokenizer `IndexError` raised by a malformed source such as
`=A2)` into the existing source-located `fill-formula` diagnostic. The exception is caught only
around `Translator` construction and translation, alongside the existing tokenizer and translator
errors. Ordinary formula validation still reports `formula-syntax`, and the document remains
invalid and export-blocked.

The existing invalid-source test now covers `Enter C2 =A2)` followed by `Fill C2:C3 Down`. It
checks for both diagnostics and verifies that the fill error points to a source line.

## Validation

```bash
source source_me.sh && python3 -m pytest tests/test_tutorial_fill.py -q
```

Result: 3 passed. This focused check is offline and does not invoke LibreOffice.
