# Heading and hardbreak repair

## Actual reproduction

Markdown-It already recognizes a backslash followed by a newline within a paragraph.
Its block parser removes the terminal newline from an inline paragraph token, however.
Thus `* First\` followed by the next list item produced a text child ending in a literal
backslash. The restored Caffeine sources use this form repeatedly at list-item and
paragraph boundaries. The DOCX renderer correctly renders `hardbreak` tokens; the defect
was in the token stream supplied to it.

The separate near-miss heading check used a word boundary after `Step`, which also
matched the hyphen in `Step-by-Step Tutorial:`. This informational heading was therefore
incorrectly diagnosed as malformed structural syntax.

## Changes

- Restore the terminal newline before inline parsing only for an inline token ending in
  an odd number of backslashes whose mapped physical source line actually ends in a
  newline. This preserves ordinary escape parsing, literal code, and original source
  text while producing the expected hardbreak token at paragraph/list boundaries.
- Recognize backslash-newline as a narrative formula boundary, retaining the formula
  role and exact copy text instead of falling back to ordinary Markdown parsing.
- Require whitespace, colon, digit, or end after a structural near-miss prefix. Digits
  retain malformed `Step2` diagnostics; hyphenated informational headings remain prose.

## Verification

`source source_me.sh && python3 -m pytest tests/test_tutorial_bindings.py
tests/test_tutorial_semantics.py tests/test_tutorial_docx.py tests/test_function_typing.py
tests/test_pyflakes_code_lint.py -q` passed **161 tests**.

The focused regression verifies actual DOCX paragraph text and five native `w:br`
elements for ordinary text, list items, strong text, and formulas. It also verifies
formula green styling and exact formula backslashes, literal code backslashes,
ordinary escaped slashes, and quoted text. The heading regression accepts
`Step-by-Step Tutorial:` and rejects malformed `Step2: Calculate`, `Step 2 Calculate`,
and `Step:` headings.

Both real Caffeine 2 and Caffeine 3 sources compile without errors. Their inline ASTs
contain **zero text nodes ending in a literal backslash**; Caffeine 2 contains 59
hardbreak tokens and Caffeine 3 contains 17. No tutorial source was modified here.

This verification did not invoke LibreOffice. Rebuilt PDF visual review remains with
the parent integration workflow. Legacy action raw scalar extraction is unchanged;
these repairs address the actual restored natural-prose and semantic-binding sources.
