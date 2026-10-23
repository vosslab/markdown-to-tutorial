# Fix authoring problems

Use this page after lint reports a problem or an output differs from the source you intended.
Start with the source line named by the diagnostic. A successful build proves structure, not the
scientific suitability of the tutorial.

Return to [../AUTHORING_GUIDE.md](../AUTHORING_GUIDE.md) or
[../FORMATTING_GUIDE.md](../FORMATTING_GUIDE.md).

## Check the workbook owner

| Symptom | Likely cause | Correction |
| --- | --- | --- |
| A table is missing from the spreadsheet | It is under `## Tutorial` | Move a supplied-cell table under `## Workbook` |
| The starter already has an answer | A formula is in Workbook | Leave the work cell blank and use `enter:` |
| A student instruction overwrites content | `enter:` targets a supplied cell | Use a blank cell or intentional `replace:` |
| A table shifts or fails to parse | Rows have different cell counts | Add the missing empty cell boundary |
| A second table starts at A1 | It lacks `#### At: <cell>` | Put an At heading directly above it |

## Check the visible and hidden address

Type this wrong Markdown:

```markdown
1. In cell E2, enter [`=AVERAGE(A2:A6)`](enter:E3).
```

The visible instruction says E2 and the action target says E3. Keep both addresses identical.
The formula input range remains separate from the destination.

## Check formula and text values

A formula starts with `=`. Without it, `AVERAGE(A2:A6)` is text. In a Workbook table,
`"=AVERAGE(A2:A6)"` is also text because the quotes request a literal string.

Use a complete rectangular table. An empty work cell needs both pipes:

```markdown
| Root length (mm) | Squared length (mm^2) |
| --- | --- |
| 12 | |
| 15 | |
```

## Check links and images

Use relative paths for repository files. Ensure the linked heading, image, or document exists.
GitHub renders the same ordinary Markdown links and fenced examples that authors see in these
references. A compiler build reports unsupported raw HTML and source-structure problems; inspect
the rendered GitHub page when a link or Markdown appearance matters.

## Rebuild and inspect

```bash
source source_me.sh
python3 make_tutorial.py lint my_tutorial.md
python3 make_tutorial.py build my_tutorial.md --format all
```

Read the full diagnostic and correction before editing unrelated lines. Open the document and
workbook after a repair. See [../TUTORIAL_SPEC.md](../TUTORIAL_SPEC.md) for every diagnostic class.
