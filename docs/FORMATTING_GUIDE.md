# From Markdown to formatting

Copy a pattern, replace the words with your own, and build your tutorial. The compiler supplies
fonts, colors, spacing, and numbering. You decide what the lesson says and what students do.

The formatting examples come from [examples/formatting_demo.md](examples/formatting_demo.md),
with cropped views of the actual output. The later walkthrough connects the table and actions,
then adds a column and a row in [examples/adding_rows_and_columns.md](examples/adding_rows_and_columns.md).
Write plain ASCII: straight quotes, ordinary hyphens, and readable symbols such as `&alpha;`.

## Find a practical pattern

New to Markdown and spreadsheets? Start with [STUDENT_GUIDE.md](STUDENT_GUIDE.md) for the
three-part BIOL 318 course. Use this index when you know the task you want to perform.
The visual examples below remain useful for seeing how source becomes a document and workbook.

| Task | Reference |
| --- | --- |
| Write headings, paragraphs, lists, links, and scientific symbols | [reference/MARKDOWN.md](reference/MARKDOWN.md) |
| Place observations, supplied labels, and blank student work | [reference/WORKSHEETS.md](reference/WORKSHEETS.md) |
| Calculate count, mean, sample SD, and fixed-reference deviations | [reference/FORMULAS.md](reference/FORMULAS.md) |
| Connect visible instructions to Enter, Fill, Select, and Replace | [reference/ACTIONS.md](reference/ACTIONS.md) |
| Add observations or move a worksheet layout | [reference/CHANGES.md](reference/CHANGES.md) |
| Diagnose wrong ranges, targets, table rows, and seeded answers | [reference/MISTAKES.md](reference/MISTAKES.md) |

The reference uses the course's small synthetic root-length dataset. Each page links back to a
course exercise and working source. Copy a small pattern, then check its actual output.
For every supported rule, use [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md).

## Headings and nested instructions

Use `Part:` and `Step:` to organize the lesson. The compiler adds their numbering. Indent a bullet
under a numbered item to keep related details together.

```markdown
### Part: Explore a curved relationship

- **Worksheet:** Sleep and scores

The data suggest that exam performance may rise and then fall as sleep changes. A squared predictor
lets a regression model describe that curve without changing the original observations.

#### Step: Inspect the observations

1. Read the supplied headings before changing the worksheet.
   - The first two columns contain the observations.
   - The third column is blank because you will construct its calculation.
2. Notice that the predictor is called **hours of sleep**, not *sleep quality*.
```

The Step heading sits farther left than the body text. Colors, sizes, and spacing distinguish the
levels without author-written formatting commands.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Numbered Part and Step headings with indented prose and nested instructions](screenshots/syntax_headings.webp)
<!-- screenshots:end -->

## Emphasis and scientific symbols

Use `**bold**` for emphasis, `*italics*` for a distinction, and backticks for literal spreadsheet
text. Type `&alpha;` to show the Greek letter while keeping the source ASCII.

```markdown
##### Explanation: Why square a value?

If a student sleeps 6 hours, squaring the value gives 36. The `^2` tells a spreadsheet to multiply
the value by itself. In a regression equation, the squared term can have coefficient &alpha; while
the ordinary sleep-hours term has its own coefficient.
```

The smaller explanation heading separates the reasoning from the task. Long prose receives full
justification automatically, using an estimated line count; no alignment syntax is needed.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Explanation heading above prose with monospace exponent notation and a rendered alpha](screenshots/syntax_text.webp)
<!-- screenshots:end -->

## Formulas and spreadsheet actions

Keep ordinary Excel formulas in your instructions. The text inside square brackets is visible;
`(enter:C2)` records where the student enters it. The destination stays hidden in the document.

```markdown
#### Step: Calculate squared sleep hours

1. In cell C2, enter:
   [`=A2^2`](enter:C2)
2. [Fill C2:C4](fill:C2:C4) down to calculate the remaining rows.
3. Check that the value beside 9 hours of sleep is 81.
```

Put the formula on its own indented line after the introduction to give it a prominent green block.
A formula within a sentence stays inline. The workbook leaves C2:C4 blank for
students to calculate. These action links also let the compiler check the calculation sequence.
Keep the destination visible in your sentence so students know where to work.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Formula entry and fill-down instructions with a prominent green spreadsheet formula](screenshots/syntax_actions.webp)
<!-- screenshots:end -->

## Tables in the tutorial

A table inside `## Tutorial` becomes a document table. It does not add cells to the workbook.

```markdown
| Model feature | What to record |
| --- | --- |
| Linear term | How the response changes in a straight-line model. |
| Squared term | How the curve bends as sleep changes. |
```

The compiler supplies the header styling, borders, and alternating row shading.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Rendered tutorial table with an emphasized header and readable row styling](screenshots/syntax_table.webp)
<!-- screenshots:end -->

## Tables in the workbook

Put the labels and data students should receive under `## Workbook`. The first table starts at A1;
`At: E1` places the next table where you choose. Empty entries stay empty.

```markdown
## Workbook

### Sheet: Sleep and scores

| Hours of sleep | Exam score | Sleep hours squared |
| --- | --- | --- |
| 5 | 72 | |
| 7 | 88 | |
| 9 | 81 | |

- **Region A1:B4:** source
- **Region C1:C4:** calculation

#### At: E1

| Model feature | Why it matters |
| --- | --- |
| Linear term | Describes a steady change. |
| Squared term | Allows a curved relationship. |
```

This is the starting workbook, with supplied headings and blank calculation cells. The author
chooses the arrangement and content; the compiler adds presentation. A region description does
not create a heading: write the heading in the table itself.

Numbers display three decimal places by default. The blank calculation cells use that format too,
so student-entered results match. Stored values keep their full precision; this is display
formatting, not rounding the data.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Starting worksheet with labeled observations, blank squared values, and a model-feature reference table](screenshots/syntax_workbook.webp)
<!-- screenshots:end -->

## Connect a table to actions

The connection is the **worksheet name and cell address**. A heading such as "Sleep hours squared"
does not automatically connect to a formula. You choose its column, then use that column's address
in the instructions.

For the workbook table above, the first table starts at A1. Its header occupies row 1; the first
observation occupies row 2. The Markdown separator line (`| --- | --- | --- |`) does not occupy a
spreadsheet row.

| Spreadsheet row | Column A | Column B | Column C |
| --- | --- | --- | --- |
| 1 | Hours of sleep | Exam score | Sleep hours squared |
| 2 | 5 | 72 | Blank for the student's formula |
| 3 | 7 | 88 | Blank for fill down |
| 4 | 9 | 81 | Blank for fill down |

Read this instruction as three connected pieces:

```markdown
1. In cell C2, enter:
   [`=A2^2`](enter:C2)
```

- `A2` inside the Excel formula is the **input**: the first sleep-hours value, 5.
- `C2` after `enter:` is the **destination**: the empty squared-hours cell in the same row.
- `In cell C2` is what the reader sees, so it must name that same destination.

The part's `- **Worksheet:** Sleep and scores` selects the worksheet for these actions. Its name
must match `### Sheet: Sleep and scores` in the Workbook section.

The table creates the starting worksheet. The action creates an instruction and records what the
student should enter; it does **not** put the answer into the starting worksheet. Putting `=A2^2`
directly in the Workbook table would supply that formula in advance instead.

## Add a calculation column

Suppose you want a second calculation: sleep hours minus 7. As the tutorial author, add a fourth
column to the Workbook table. It becomes column D. Supply its heading and leave its values blank:

```markdown
| Hours of sleep | Exam score | Sleep hours squared | Hours minus 7 |
| --- | --- | --- | --- |
| 5 | 72 | | |
| 7 | 88 | | |
| 9 | 81 | | |

- **Region A1:B4:** source
- **Region C1:D4:** calculation
```

Extend the calculation region through D so both calculation columns receive the same styling.
Keep the existing column-C instructions, then add this step under the same Tutorial part:

```markdown
#### Step: Compare with 7 hours

1. In cell D2, enter:
   [`=A2-7`](enter:D2)
2. [Fill D2:D4](fill:D2:D4) down to calculate the remaining rows.
```

Both formulas read from column A, but one writes to C and the other to D. The author has added the
column and supplied its heading; the tutorial user enters and fills its formula.

## Add another observation

Now add a fourth observation, 6 hours and a score of 79, at the bottom of that same Workbook table:

```markdown
| Hours of sleep | Exam score | Sleep hours squared | Hours minus 7 |
| --- | --- | --- | --- |
| 5 | 72 | | |
| 7 | 88 | | |
| 9 | 81 | | |
| 6 | 79 | | |

- **Region A1:B5:** source
- **Region C1:D5:** calculation
```

The new observation is on spreadsheet row 5. The first formulas stay `=A2^2` in C2 and `=A2-7` in
D2. Extend **both** fill instructions to row 5, including the visible wording and the link target:

```markdown
2. [Fill C2:C5](fill:C2:C5) down to include all four observations.
```

```markdown
2. [Fill D2:D5](fill:D2:D5) down to include all four observations.
```

After the tutorial user fills down, C5 contains `=A5^2` and displays `36.000`; D5 contains `=A5-7`
and displays `-1.000`. In the generated starting workbook, those cells are still blank.

The complete version is [examples/adding_rows_and_columns.md](examples/adding_rows_and_columns.md).
Build it with:

```bash
source source_me.sh
python3 make_tutorial.py build docs/examples/adding_rows_and_columns.md --format docx,xlsx
```

These examples show the edits explicitly so you can understand the connections. Manually changing
a Markdown table does not automatically rewrite its Tutorial instructions. For larger layout
changes, the worksheet-edit command can preview coordinated changes; see
[USAGE.md](USAGE.md#maintain-a-worksheet-after-a-layout-decision). Review its notices, including any
visible wording or worked numbers that still need updating.

## Try the complete example

Run from the repository root:

```bash
source source_me.sh
python3 make_tutorial.py lint docs/examples/formatting_demo.md
python3 make_tutorial.py build docs/examples/formatting_demo.md --format all
```

Open the DOCX, PDF, and XLSX in `tutorial_output/formatting_demo/`. PDF export requires LibreOffice
and the fonts listed in [INSTALL.md](INSTALL.md). On this macOS host, agent commands that invoke
LibreOffice must run outside the sandbox.

The screenshots show local PDF rendering and a printed view of the XLSX. Page wrapping can differ
in other applications; these are not Google Docs or Google Sheets screenshots.

For writing a complete lesson, use [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md). For all supported
syntax and its rules, see [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md).

## Refresh the screenshots

For maintainers, refresh all documentation artifacts and screenshots after changing renderer styles:

```bash
source source_me.sh && python3 devel/refresh_documentation.py
```

The repository-owned capture helpers locate semantic content automatically, so crops follow style
changes without hand-adjusting coordinates. To rebuild only this guide's syntax examples, run:

```bash
source source_me.sh && python3 devel/capture_syntax_examples.py
```

See [INSTALL.md](INSTALL.md) for the optional capture dependencies. Both commands invoke
LibreOffice; on this macOS host, agents must run them outside the sandbox with
`sandbox_permissions="require_escalated"`. Human terminal commands use the syntax above.
The [capture receipt](screenshots/syntax_capture_receipt.json) records the source and image hashes.
The narrow crops keep each feature readable; they intentionally omit unrelated page content.
