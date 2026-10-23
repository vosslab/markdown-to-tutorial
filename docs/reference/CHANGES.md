# Revise a workbook

Use this page after you make a deliberate layout decision. Inspect the Markdown, generated document,
and generated workbook together. The compiler can coordinate marked cell references; it cannot
rewrite your scientific explanation.

Return to [../AUTHORING_GUIDE.md](../AUTHORING_GUIDE.md) or
[../FORMATTING_GUIDE.md](../FORMATTING_GUIDE.md).

## Change a row or column

When a source table changes, review all of these places:

- The Workbook table and its region declarations.
- Formula input ranges and fixed references.
- Action targets and visible cell references.
- Explanations, expected values, and any associated image.

For example, adding a new root value to the formatting example means changing the table and every
formula that should include it. A successful build cannot decide whether the new data belong in a
particular analysis.

## Preview a coordinated layout edit

The optional worksheet editor previews a reviewed structural change. Run it from the repository
root on your own source file:

```bash
source source_me.sh
python3 make_tutorial.py worksheet-edit my_tutorial.md \
  --sheet Data insert-columns --at A --count 1
```

The preview leaves the source unchanged. Read the displayed diff and notices before considering
`--write`.

The helper updates table placement, declared regions, marked formula references, action targets,
and explicit cell instructions. It is an optional maintenance tool, not the normal authoring workflow.

An observation resize updates both the displayed range and target in links such as
`[Fill D2:D6](fill:D2:D6)`. Write standalone column references in uppercase, such as `column D`
or `columns D-F`, so the editor can distinguish them from ordinary words such as `column is`.
Review the complete diff, including action text, before applying it. Your explanations and
numerical conclusions still need your judgment after a data change.

## Rebuild after every structural change

```bash
source source_me.sh
python3 make_tutorial.py lint my_tutorial.md
python3 make_tutorial.py build my_tutorial.md --format all
```

Open the document and starter workbook. Check the first and last affected rows, blank work cells,
ranges, and changed headings. See [MISTAKES.md](MISTAKES.md) for common diagnostics and
[../USAGE.md](../USAGE.md) for the full command reference.
