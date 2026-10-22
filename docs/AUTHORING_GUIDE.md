# Authoring guide

Each tutorial source is one Markdown file with a `Workbook` section for spreadsheet data and a
`Tutorial` section for student-facing instructions. The converter produces an editable DOCX, an
XLSX workbook, and a PDF from the DOCX.

## Start a source

Use exactly one title, then the two required sections:

```markdown
# Comparing two groups

## Workbook

### Sheet: Measurements

| Group A | Group B |
| --- | --- |
| 12.4 | 11.8 |
| 10.9 | 12.1 |

#### At: D1

| Statistic | Result |
| --- | --- |

## Tutorial

### Part: Compare the groups

- **Worksheet:** Measurements

#### Step: Calculate the means

- **Label D2:** Group A mean
- **Enter E2:** `=AVERAGE(A2:A3)`
- **Interpret:** Use `E2` as the sample mean for Group A.
```

A table directly under a sheet declaration begins at A1. Put `#### At: <cell>` directly before
each additional table to set its top-left address. Table headers are workbook cells. A table's
assigned range cannot overlap another table.

## Write instructions

Use `### Part:`, `#### Step:`, and `##### Substep:` headings. The converter generates numbering;
you can include legacy numbers when migrating existing materials. Put the worksheet name in a
`**Worksheet:**` item within each part.

Every list item should begin with a bold action and colon. Decide who supplies each label: seed it
in the Workbook table for students to inspect, or leave it blank and ask students to type it with
`Label`. Do not seed a label and ask students to re-enter it. `Label`, `Enter`, and `Replace` record
student assignments for validation but leave those answers blank in the generated workbook.
`Select` records a cell/range reference; `Choose` records a menu path. Other bold openings, such as
`**Compare:**` and `**Explain:**`, remain ordinary instructions.

Give each list item actual content. A bold, colon-terminated label by itself is incomplete unless
the item has a substantive continuation, a nonempty fenced instruction, a valid action, or a
substantive descendant. An empty child does not complete its parent. The linter checks parsed list
structure and points to the source line. Repeated identical assignments still receive a redundancy
warning.

Put a formula in one code span after `Enter` or `Replace`. Use backticks around cell references in
prose when they should become linked references. An A1-shaped string without backticks is left as
ordinary text unless it is the target of a recognized action.

After entering a formula in the first row, use `- **Fill C2:C26:** Down` to teach copying it
through the remaining rows. For adjacent formula columns, use `- **Fill E2:F26:** Down`.
Enter a formula in every cell of the selected first row first; each column copies its own source.
Relative references move with the destination row, while `$` anchors stay fixed. The source
formulas must exist and match in every incoming alternative. Otherwise, place Fill inside each
alternative. Only `Down` is supported, and the range must contain at least two rows. Generated
instructions stay concise, and the student workbook leaves the fill destinations blank.

Workbook presentation uses a frozen first row and readable widths of at least 12 characters,
including blank entry columns. When a task needs number formatting, teach the explicit spreadsheet
menu action in the instructions; the generator does not infer number formats from values. Use native
editable tables for worked examples that must match the current workbook. Keep original source
images and assets intact; a historical screenshot may remain as provenance only when it cannot be
mistaken for the current workbook or procedure.

## Check and build

Run lint while editing, then build the desired outputs:

```bash
source source_me.sh
python3 make_tutorial.py lint tutorial_data/babies_1_z_test.md
python3 make_tutorial.py build tutorial_data/babies_1_z_test.md
```

The default build exports PDF using LibreOffice. Use `--format docx,xlsx` for iteration without
PDF conversion. Read source-located diagnostics and the generated `validation.json`; formula
checking is static and does not calculate values or establish statistical correctness.

For the full syntax, numbering rules, worksheet metadata, formula checks, and unsupported content,
see [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md). For command options, see [USAGE.md](USAGE.md).
