# Quoted label markup correction

Date: 2026-10-22. Scope: the LABEL presentation/scalar boundary exposed by the Babies PDF
review. No lesson source is changed by this correction.

## Reproduction and contract

The authored bindings `["Significance Level (&alpha;)."](label:D14)` and
`["*Two-Tail Decision*."](label:D16)` reached PDF as literal entity/asterisk characters.
The shared binding decoder preserved all leading-quote payloads as raw scalar syntax. The
compiler then replaced their Markdown children with one literal token. This protection belongs
to JSON Enter/Replace assignments, but incorrectly applied to prose LABEL bindings.

The decoder now receives the binding kind. LABEL quotes are ordinary visible punctuation,
so their contents follow Markdown text/entity/emphasis decoding. Their workbook values are
`"Significance Level (` followed by U+03B1 and `)."`, and `"Two-Tail Decision."` respectively.
The DOCX retains those quotes and punctuation; its inner `Two-Tail Decision` run is italic.
There is no JSON string interpretation for labels.

Enter/Replace JSON strings retain their source copy text, including entity-looking text,
Markdown punctuation, and JSON escapes. Their decoded workbook values still follow JSON
semantics. Strong emphasis enclosing the complete JSON payload remains presentation formatting.
Bare formula-looking labels retain operator bytes and stay literal text. Quoted formula-looking
labels use the formula-aware Markdown tokenization for operator preservation, with inferred
formula roles removed. Explicit label code spans keep literal entity/asterisk bytes.

This follows the repository's "Fix the design, not the symptom" rule: no entity substitution,
global HTML unescape, source rewrite, or alternate renderer path is introduced. The source
capture and existing formula scanner remain unchanged.

## Verification

The added permanent regression in `tests/test_tutorial_bindings.py` compiles the two actual
quoted-label shapes alongside literal code, bare/quoted formula-looking labels, JSON Enter,
and strong-wrapped JSON Replace. It checks action values, workbook replay writes, editable
DOCX paragraph text and italic/bold runs, and absence of inferred formula roles/checks. The
existing regression continues to cover escaped stars and nested emphasis.

Command: `source source_me.sh && python3 -m pytest tests/test_tutorial_bindings.py
tests/test_tutorial_semantics.py tests/test_tutorial_docx.py tests/test_tutorial_workbook.py
tests/test_pyflakes_code_lint.py tests/test_function_typing.py -q` (one shell command).

Result: **175 passed in 0.93 seconds**. No LibreOffice command was run. This verifies the
compiler/replay/DOCX contract; refreshed canonical PDFs and their visual acceptance remain with
the build and quality reviewers.

## Authoring and handoff

The authored quotes and terminal periods remain part of both the visible label and its cell
value under the existing text-label contract. Excluding them would be a separate authoring
change: bind only the desired label phrase and place instructional quotes/punctuation outside
the link. No such source change is necessary to fix markup leakage or has been made here.

Production edits are limited to `scalar_payload` in `tutorial_lib/semantic_bindings.py` and
its caller/literal-rendering guard in `_compile_bindings` in `tutorial_lib/compiler.py`.
The integration owner must rebuild all twelve canonical outputs after this correction and
record current source/artifact hashes before final acceptance. Fresh specification and quality
reviews should specifically confirm decoded alpha, italic label text, retained punctuation,
literal code/formula safeguards, and unchanged JSON assignment display and replay semantics.
