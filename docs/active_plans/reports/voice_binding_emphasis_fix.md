# Binding emphasis correction

Date: 2026-10-22. Scope: the binding scalar regression discovered during source restoration
under [instructional_voice_restoration.md](../instructional_voice_restoration.md).

## Finding and correction

The concrete reproduction `[**Sample Size**](label:D5)` produced `action-scalar` with
`Only plain text or one complete code span is allowed`. The raw semantic-link capture was
correct; the compiler reused table scalar decoding, which deliberately rejects emphasis.
The earlier [voice_core_spec_review.md](voice_core_spec_review.md) did not exercise this
authored emphasis case.

Binding assignments now use a binding-specific decoder in `tutorial_lib/semantic_bindings.py`.
Complete enclosing Markdown emphasis is removed before interpreting a scalar. Plain formatted
text uses its visible content; raw JSON strings and bare formulas retain their escapes,
quotes, underscores, multiplication operators, and other syntax. Labels remain text even when
their contents resemble formulas. The compiler preserves authored emphasis tokens for DOCX,
and literal JSON contents cannot create Markdown emphasis or inferred formula styling.

This follows the repository's "Fix the design, not the symptom" and "Keep it simple (KISS)"
principles: binding presentation and executable values are decoded at their shared semantic
boundary. No lesson prose is rewritten, and table/legacy scalar acceptance is unchanged.

## Verification

The durable regression in `tests/test_tutorial_bindings.py` compiles a compact authored example
through action values, replay writes, and editable DOCX runs. It checks a nested bold/italic
label, an italic numeric scalar, a bold formula containing multiplication and a quoted
underscore, raw and bold JSON strings containing literal Markdown characters and a backslash,
and escaped literal stars beside ordinary bold text. The original source remains intact;
rendered prose retains emphasis and excludes Markdown delimiter characters from cell values.

Command: `source source_me.sh && python3 -m pytest tests/test_tutorial_bindings.py
tests/test_tutorial_semantics.py tests/test_tutorial_docx.py tests/test_tutorial_workbook.py
tests/test_pyflakes_code_lint.py tests/test_function_typing.py -q` (one shell command).

Result: **170 passed in 0.91 seconds**. The four behavior modules account for 32 passing tests;
the remaining checks cover repository pyflakes and function annotations. No LibreOffice command
was run.

A read-only compile of all twelve canonical lesson sources found no `action-scalar` errors.
At that checkpoint, the actively edited Microbes sources still had region, heading, and
assignment diagnostics. This checkpoint is not final whole-corpus acceptance.

## Review handoff

Changed production surface: `scalar_payload` in `tutorial_lib/semantic_bindings.py` and the
binding-only value/literal-rendering branch in `_compile_bindings` in `tutorial_lib/compiler.py`.
The Markdown adapter and raw payload capture are unchanged. Fresh review should confirm that
raw JSON/formula syntax is retained, emphasis-only wrappers do not enter spreadsheet values,
literal strings stay literal, and DOCX runs retain intended author formatting. Artifact builds,
PDF inspection, final source lint, and whole-suite integration remain with their owning lanes.
