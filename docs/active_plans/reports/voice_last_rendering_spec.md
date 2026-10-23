# Final rendering specification review

Date: 2026-10-22. Decision: **ACCEPT** the final quoted-label, semantic pagination,
terminal list-break, heading-style, and two localized source corrections. No concrete
specification defect remains in this reviewed implementation. This is implementation/source
acceptance; the rebuilt student PDFs and workbooks still require their separate final review.

## Scope and contract

Reviewed the current [instructional_voice_restoration.md](../instructional_voice_restoration.md),
[TUTORIAL_SPEC.md](../../TUTORIAL_SPEC.md), repository rules, correction reports, production
code, and focused regressions. Waited for the pagination owner to release the final renderer
and tests before verification. Only this report was written; no production or lesson source
was edited, and no LibreOffice command ran.

The final implementation respects authored source as the wording authority:

- Quoted LABEL payloads use Markdown entity/emphasis decoding as prose. The alpha entity
  becomes U+03B1, and `Two-Tail Decision` retains italic formatting. Quotes and punctuation
  already inside these label bindings remain visible and part of the workbook text.
- Enter/Replace quoted scalars retain raw JSON copy text until the existing scalar decoder
  interprets it. Literal code and formula-looking label bytes remain protected. Formula
  roles are removed from text labels, preventing accidental formula validation or styling.
- Label pagination examines only the next sibling list paragraph and, when appropriate,
  that instruction's first nested formula. The entry must occupy the adjacent column on
  the same row and sheet. Heading/list boundaries and a different row break the match.
  Existing parent-to-first-child keeping completes a three-paragraph cluster without
  chaining subsequent formula explanations or retaining a whole Step on one page.
- The final two adjacent paragraph body blocks are paired by setting `keep_with_next`
  only on the predecessor. A table boundary prevents pairing. This is the requested small
  general closing-paragraph rule, with no source rewriting or document ancestry state.
- Terminal list hardbreak removal works on a copied child-token list. It preserves
  internal breaks and token contents, including formulas. Closing emphasis/link tokens
  can follow the removable terminal break. The compiled AST is not mutated.
- Heading sizes/weight live in the renderer style definitions. Informational headings
  remain authored prose, while structural prefixes retain canonical numbering. There is
  no heuristic rewriting of narrative paragraphs or new configuration/fallback framework.

The bounded token patterns and existing local renderer state satisfy the plan's small
semantic-layer and KISS requirements. No ancestry map, document-wide action search, hidden
formula inventory, or source-normalization workaround was introduced for pagination.

## Independent verification

After owner release, ran:

```bash
source source_me.sh && python3 -m pytest tests/test_tutorial_bindings.py tests/test_tutorial_semantics.py tests/test_tutorial_docx.py tests/test_tutorial_workbook.py tests/test_pyflakes_code_lint.py tests/test_function_typing.py -q
```

Result: **177 passed in 0.99 seconds**. Coverage includes natural quoted label markup,
JSON assignment/replay fidelity, literal code and formula preservation, sibling/nested
pagination, list boundary barriers, final paragraph pairing, heading semantics, workbook
roles, code lint, and function annotations. Scoped `git diff --check` also passed.

A separate in-memory parser-to-DOCX probe rendered a strong-wrapped list item containing
an internal authored hardbreak and a terminal hardbreak, followed by a strong-wrapped
formula item with a terminal break. Its paragraphs were `Strong` + newline + `continued`
and `Use =SUM(1,2)`. The single internal native DOCX break survived; both terminal blank
lines disappeared. Bold remained active on both content runs, and the formula retained
exact text and green `188038` styling. A deep-copied token comparison was equal after
rendering, independently confirming no compiled-token mutation.

Independent compilation of the two corrected current lesson sources confirmed:

- Microbes 1 D14 has one Enter action with scalar kind `number` and value `0.05`;
  the visible instruction binds `0.05`, with its sentence period outside the binding.
- Microbes 5 G1 is explicitly a blank seed with value `None`. The current source does
  not place a period in that spacer cell.
- Both sources compile without errors. These checks confirm the current intended
  semantics; the source owners' before/after comparisons establish the narrow edit deltas.

## Reviewed fingerprints and limits

| Reviewed file | SHA-256 |
| --- | --- |
| `tutorial_lib/semantic_bindings.py` | `e490c62e63a55467bcf92fd8bbbd92b14ae83c5a501c4ecd6e30c096aa0b318a` |
| `tutorial_lib/compiler.py` | `944b21f34670c433171025abfb6cb6aed3d0dd67fd2940f0300ff1efbde1d8c3` |
| `tutorial_lib/docx_renderer.py` | `ad138c283a502719dfe06705600cbfd59f13b4385e5b388b2cad126057807a48` |
| `tutorial_lib/docx_inline.py` | `71b10b8c11c25ec49443bebc64c29f92d96199d297229081bcd8db98f9caecfb` |
| `tutorial_lib/docx_styles.py` | `c9f85b841167b30177dd7d237fe80cc20879fc13fb4fd6e7842de06fcea4da46` |
| `tutorial_data/microbes_1_z_test.md` | `f11f071cae9b664383f4e83bdaa5838004b9e48ffd61ad758c31c7fc41f150c0` |
| `tutorial_data/microbes_5_anova.md` | `9e5004a388494c8e7e28e4e9e6d2557466df9de1b90f4338caa2d4eb300fa512` |

Final artifact reviewers must confirm these sources/code produced the rebuilt bundles,
that Babies labels display decoded markup, that label/instruction/formula groups remain
together where needed, that Caffeine no longer gains terminal blank list lines, and that
Microbes 2 no longer ends with an isolated next-tutorial link. No PDF pagination, Google
Docs/Sheets behavior, or student-learning outcome is claimed by this review.
