# Semantic pagination and terminal list-break fix

## Change

The DOCX renderer now keeps a semantic label with an immediately adjacent sibling entry when the
targets are single cells in the same row and worksheet, with the entry one column to the right. It
recognizes the entry either in the next sibling paragraph or in the first nested list item beneath
that sibling's short instruction. The lookahead is limited to the adjacent list-token pattern and
its first nested formula paragraph. Later explanations remain separate paragraphs and can paginate
independently.

Redundant hardbreaks at the ends of list paragraphs are removed from a copied inline-token list
before rendering. Internal hardbreaks remain intact, and the compiled source tokens are unchanged.
When the final two DOCX body blocks are both paragraphs, the preceding paragraph keeps the final
paragraph with it so short closing instructions do not occupy a page alone.

## Evidence

`source source_me.sh && python3 -m pytest tests/test_tutorial_docx.py -q` passed: **10 passed**.
The focused DOCX XML checks cover direct semantic pairs, a nested formula entry, a different-row
negative case, a heading barrier, the boundary between the nested formula and following explanation,
terminal list hardbreak removal with both plain and emphasized text, preservation of internal
hardbreaks, and a final closing paragraph.

A direct DOCX export of `tutorial_data/babies_2_t_test.md` confirms that the D13 label paragraph has
`keepNext`; the E13 destination instruction also keeps its first nested formula paragraph with it.
The formula and its following explanation have no `keepNext`, so the remaining explanation can
flow to the next page. This reproduces the intended page-break protection at the DOCX XML level.

No LibreOffice command or PDF export was run. Fresh bundle generation and rendered PDF inspection
remain with the integration review.
