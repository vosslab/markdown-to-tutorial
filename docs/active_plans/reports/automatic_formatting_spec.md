# Automatic formatting specification review

Review date: 2026-10-22. Status: one literal-action rendering finding requires correction.

## Scope and authority

Reviewed [automatic_tutorial_formatting.md](../automatic_tutorial_formatting.md) and the manager's
approved formula, spacing, font, style, blank-answer, and wording contract against
[TUTORIAL_SPEC.md](../../TUTORIAL_SPEC.md), the changed parser/compiler/DOCX modules, and focused
semantic and DOCX tests. Applied repository, Python, pytest, and Markdown style rules.

The parser owns formula recognition and neutral formula roles; the existing validator remains the
formula-validation authority. DOCX applies the green `188038` Roboto Mono formatting. This matches
the approved architecture. No new author color syntax or configuration is introduced.

## Finding

Literal action payloads can lose Markdown operators in the rendered document:

```markdown
- **Enter C2:** "=A2*B2*3"
- **Label D2:** =A2*B2*3
```

Each compiles without errors and retains the literal text value `=A2*B2*3`. Native DOCX instead
renders `Enter C2: "=A2B23"` and `Label D2: =A2B23`. The literal safeguard disables formula
recognition but leaves the stars available to Markdown emphasis parsing. This appears to expose
an existing literal-rendering gap rather than a regression in formula storage, but it conflicts
with the preserved copy-text and literal-value contract now documented for this work.

Required correction: preserve literal action payload characters while retaining a nonformula
role. Confirm compiled value, native DOCX text, and absence of green formula styling. Avoid adding
formula grammar or changing ordinary narrative quotation behavior to solve this problem.

## Passing evidence

- `source source_me.sh && python3 -m pytest tests/test_tutorial_docx.py tests/test_tutorial_semantics.py -q`:
  15 passed in 0.32 seconds.
- Temporary parser probes preserve multiplication, spaces, functions, quoted string operands,
  comparison operators, unary signs, powers, percent, and sentence punctuation. Strong wrappers,
  formulas following prose, and linked formulas retain their boundaries and surrounding markup.
- Prose such as `alpha = 0.05`, `x=3`, comparisons, and URL query strings remains ordinary text.
- Bare Enter formulas, including `= A2*B2*3`, retain their source text and green DOCX styling.
- Code inspection and the focused DOCX contract test cover inline formulas, explicit code spans,
  nested-list links, formula fences, tutorial table cells, unchanged compiled tokens, compact list
  continuations, and unchanged body spacing. Existing style coverage protects the six standard
  paragraph styles and three required font families.
- Temporary XLSX export and verified readback preserve a workbook seed JSON value
  `"=A2*B2*3"` as exact literal text with type `s`, the adjacent bare formula as exact formula text
  with type `f`, and the instructed answer destination as blank.

## Boundaries and remaining evidence

Workbook tables and Enter/Replace actions have scalar semantics; ordinary tutorial tables have
narrative GFM semantics. A quoted formula inside an ordinary tutorial table appropriately receives
the same formula treatment as a quoted formula in prose. The documentation's JSON literal
safeguard should identify scalar contexts explicitly; a broad quoted-table heuristic is unwarranted.

The recognizer is a boundary scanner, not a complete Excel grammar. Existing optional code spans
remain appropriate for ambiguous or extended narrative expressions. Formula validity continues
through the existing validator. No architectural drift or additional formula authoring burden was
found in the reviewed supported paths.

No LibreOffice process was invoked. Full-suite, all-12 rebuild, PDF appearance, and original-PDF
color comparison evidence belong to the separate build and visual review lanes. Google import
behavior remains unverified. This review does not accept the outstanding literal-action mismatch.
