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
- **Enter E2:** =AVERAGE(A2:A3)
- **Interpret:** Use `E2` as the sample mean for Group A.
```

A table directly under a sheet declaration begins at A1. Put `#### At: <cell>` directly before
each additional table to set its top-left address. Table headers are workbook cells. A table's
assigned range cannot overlap another table.

## Write instructions

Use `### Part:`, `#### Step:`, and `##### Substep:` headings. The converter generates numbering;
you can include legacy numbers when migrating existing materials. Put the worksheet name in a
`**Worksheet:**` item within each part.

Write instructions as ordinary prose and numbered or nested lists that read naturally. Attach cell
actions to the words already present with semantic links, for example:

```markdown
1. In D5, type [**Sample Mean**](label:D5); in E5, enter [=AVERAGE(B2:B26)](enter:E5).
2. [Select C2:C26](select:C2:C26), then [fill down](fill:C2:C26) to copy the first-row formula.
```

Keep each value or formula once in the visible instructions; multiple linked actions may appear
within one paragraph. The link destination carries the operation while the link text remains the
student-facing wording. Links render without exposing semantic URIs. Ordinary GFM numbered and
nested lists retain their grouping. Do not add bold action labels to every list item.
Name each destination cell or range in the visible instruction or its parent item; a hidden link
target does not tell the student where to type. Label links decode ordinary Markdown emphasis and
entities as label text; quoted labels retain their visible quotes. Enter/Replace quoted scalars
follow JSON rules and retain their copy text until scalar decoding.

Legacy `**Label D2:**`, `**Enter E2:**`, `**Replace E2:**`, `**Select:**`, and `**Fill C2:C26:**`
openings remain supported. `Label`, `Enter`, and `Replace` record assignments for validation but
leave student answers blank in the generated workbook. Do not seed a label and ask students to
re-enter it. `Choose` records a menu path. Other bold openings, such as `**Compare:**` and
`**Explain:**`, remain ordinary instructions.
Write menu segments with ASCII `>` separators; the DOCX renders them in bold Roboto Mono.

Give each list item actual content. A bold, colon-terminated label by itself is incomplete unless
the item has a substantive continuation, a nonempty fenced instruction, a valid action, or a
substantive descendant. An empty child does not complete its parent. The linter checks parsed list
structure and points to the source line. Repeated identical assignments still receive a redundancy
warning.

After `Enter` or `Replace`, write a formula directly, such as `- **Enter C2:** =A2^2`. Backticks
around an expression remain optional when they make the intended formula boundary clearer. In a
Workbook cell or `Enter`/`Replace` payload, a JSON double-quoted value such as `"=not a formula"` is
literal text. Tutorial prose and ordinary Tutorial tables use narrative semantics: a bounded
spreadsheet formula remains a formula when quoted as an example. In an action payload, formula
recognition runs before Markdown interprets arithmetic characters. Complete spreadsheet expressions
such as `=SUM(A1:A3)` and `=A1+B1` in prose are recognized when their boundaries are clear; statistical
equations, comparison operators, and URLs remain prose. Use backticks around cell references in prose
when they should become linked references. An A1-shaped string without backticks is left as ordinary
text unless it is the target of a recognized action.

Formula roles are recognized in action payloads, code spans, formula fences, and workbook tables.
The renderer preserves the authored formula text and formats formulas in Roboto Mono with dark green
(`#188038`). No author color markup is needed. In GFM tables, escape a literal pipe as `\|` as
required by the table syntax.

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
Generated DOCX uses Google Docs' Normal text, Title, Subtitle, and Heading 1-3 styles. PDF export
requires locally installed PT Sans, PT Sans Narrow, and Roboto Mono; setup does not install fonts.

For the full syntax, numbering rules, worksheet metadata, formula checks, and unsupported content,
see [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md). For command options, see [USAGE.md](USAGE.md).
