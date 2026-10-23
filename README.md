# markdown-to-tutorial

Create a biology tutorial for classmates in one plain-text file. Write the lesson and design the
spreadsheet; the compiler formats your work as editable Word, PDF, and Excel files.

## Start here

**Writing your first tutorial? Start with the [student guide](docs/STUDENT_GUIDE.md).** Its three
short Parts guide you through one Roots lesson: write the source, add `COUNT`, `AVERAGE`, and
`STDEV.S`, then optionally extend it with deviations and a classmate check. You can explore the
lesson and examples before installing anything.

1. **Make your first tutorial.** Follow [docs/learn/PART_1_CREATE.md](docs/learn/PART_1_CREATE.md),
   then continue to Part 2. Keep editing `my_roots_tutorial.md` throughout.
2. **Find a checkpoint.** The [student guide](docs/STUDENT_GUIDE.md) links to eight complete source
   examples, from the first observation lesson through the optional classmate review.
3. **Look up a topic.** Use the guide's focused references for Markdown, worksheets, formulas,
   actions, worksheet changes, and common mistakes. Start with the [formatting guide](docs/FORMATTING_GUIDE.md)
   to see source syntax beside its rendered result.
4. **Build your files.** After installation, follow [Build your files](#build-your-files). Open the
   document and workbook, then follow your instructions as a classmate would.

If you are **using a tutorial for an assignment**, start with the document and workbook provided
for that lesson. The authoring guide is for students making tutorials.

## See the finished materials


Actual output from the Microbes and Dr. Caffeine lessons: prominent formulas, varied heading
indents, justified explanations, and scientific worksheets with purposeful color.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Microbes F-test instructions with a prominent green formula display and justified explanation](docs/screenshots/microbes_4_formula_instruction.webp)
![Caffeine squared-column step with inset body text, Excel formula, and the author's 36-hours aside](docs/screenshots/caffeine_3_fill_down_instructions.webp)
![Completed ANOVA demonstration showing styled table headers, summary calculations, and a decision; not the student starter](docs/screenshots/microbes_5_completed_anova.webp)
<!-- screenshots:end -->

The ANOVA image is a **completed demonstration**, populated from the lesson's instructions in a
disposable copy to show its table formatting. It is not the student starting workbook. Some current
lessons still defer headings to learner actions; this demonstration does not establish that those
starting worksheets have the right instructional structure.

The illustrated lesson opening and capture details are in
[docs/screenshots/README.md](docs/screenshots/README.md).

Built for BIOL 318 students writing tutorials for classmates. Authors establish the labels and
worksheet structure, write ordinary Excel formulas, and decide what learners complete. The compiler
preserves their prose and adds formatting. The collection includes 12 lessons; PETase uses
explicitly synthetic data.

DOCX, XLSX, and PDF output is verified locally. Google Docs and Sheets import and execution remain
unverified; Google may also wrap text differently.

## Choose a starting example

Start small and adapt a copy. You choose the scientific question, worksheet arrangement, and
learning activities.

| I want to... | Open this file |
| --- | --- |
| Start with labeled data and one formula column | [docs/examples/formatting_demo.md](docs/examples/formatting_demo.md) |
| Understand how to add a column or another observation | [docs/examples/adding_rows_and_columns.md](docs/examples/adding_rows_and_columns.md) |
| Teach students to construct a calculated column | [templates/calculated_column.md](templates/calculated_column.md) |
| Teach a summary calculation | [templates/statistical_summary.md](templates/statistical_summary.md) |
| Plan an ANOVA table-building activity | [templates/anova_worksheet.md](templates/anova_worksheet.md) |

The templates include some label-entry exercises. Keep those only when constructing the labels is
part of your lesson; otherwise, supply the labels in the Workbook table, as the first example does.
For complete lesson ideas, browse [docs/TUTORIAL_CATALOG.md](docs/TUTORIAL_CATALOG.md).

## What you write

Your Markdown file has two main sections:

- **Workbook:** the tables, labels, and data students see when they open the spreadsheet.
- **Tutorial:** your explanations and the instructions students follow to complete the work.

For example, this instruction asks the reader to enter a formula in C2:

```markdown
1. In cell C2, enter:
   [`=A2^2`](enter:C2)
```

The formula reads the value in A2 and squares it. The `enter:C2` part connects the instruction to
the destination cell; it is hidden in the finished document. C2 stays blank for the reader to fill.
The [docs/FORMATTING_GUIDE.md](docs/FORMATTING_GUIDE.md#connect-a-table-to-actions) walkthrough shows
how that address comes from the Workbook table.

Use straight quotes, ordinary keyboard characters, and ordinary Excel formulas. For a Greek letter,
you can type a readable name such as `&alpha;`. The tool handles fonts, colors, spacing, and the
default three-decimal number display. Your explanations stay in your own words.

<details>
<summary>More examples: a full lesson source and the original Caffeine instructions</summary>


Keep the student's explanation in your own voice. Semantic links attach a cell action to the words
students already read; the destination stays hidden in the generated document. This excerpt is from
the [Caffeine 3 lesson](tutorial_data/caffeine_3_quadratic_regression.md):

```markdown
#### Step: **Create a SQUARED Sleep-Hours Column**

To let our regression model curve, we need to square our predictor variable (x).

1. Use blank column C in your spreadsheet.\
2. Label it [Sleep Hours Squared (x^2)](label:C1)\
3. If the sleep hours are in cell A2, enter: [=A2^2](enter:C2)\
4. Press Enter, then [drag the little blue square all the way down to the bottom](fill:C2:C26) to
   make sure it applies to all students! Basically, we're taking each student's hours of sleep
   and multiplying that number by itself. If someone slept 6 hours, their squared sleep value is
   36! Don't worry, they didn't sleep for 36 hours!
```

Workbook region roles identify starting data, calculations, results, and interpretation. A clearly
bounded bare formula such as `=SUM(A1:A3)` receives automatic styling; it does not declare a cell
action.

<details>
<summary>Full runnable authoring example</summary>

The following small source builds as written. A semantic link binds the visible wording to a checked cell target while keeping the authored paragraph intact.

```markdown
# Squared sleep hours

## Workbook

### Sheet: Sleep

| Hours slept | Exam score |
| --- | --- |
| 6 | 80 |
| 8 | 92 |

- **Region A1:B3:** source
- **Region C1:C3:** calculation
- **Region E1:F2:** results
- **Region H1:I2:** interpretation

#### At: E1

| Measure | Result |
| --- | --- |
| Mean squared hours | |

#### At: H1

| Prompt | Response |
| --- | --- |
| What might a curve capture? | |

## Tutorial

### Part: Prepare the predictor

- **Worksheet:** Sleep

#### Step: Square sleep hours

Use column C for the squared predictor. In C1, label [Sleep hours squared (x^2)](label:C1); in C2, enter [=A2^2](enter:C2), then [fill the formula through row 3](fill:C2:C3). Each value stays paired with the same student's score.

#### Step: Summarize the predictor

In F2, enter [=AVERAGE(C2:C3)](enter:F2). Then explain what a curved pattern could capture in I2.
```

</details>

</details>

## What the tool handles


- **Your words, professionally presented.** Editable headings, prominent green formula displays,
  styled tables, and long-paragraph justification, without LLM rewriting.
- **Styled scientific worksheets.** Colors, table headers, borders, and response areas follow
  the authored structure. Calculation cells remain blank where the lesson assigns learner work.
- **One source, three outputs.** Markdown supplies DOCX instructions, XLSX workbooks, and PDF copies.
- **Less coordinate bookkeeping.** Preview column/row insertions, range moves, and data resizing
  across the worksheet specification and explicit instructional references.
- **Approachable starting points.** Three student templates, 12 complete lessons, and a simple
  XLSX-to-Markdown draft importer.
- **Checks with clear limits.** Lint checks source structure and references; a separate Calc
  validation checks numerical results.

## Build your files

This step uses a terminal. The publishing tool currently runs through commands; it does not have a
web form or an upload button. First follow [docs/INSTALL.md](docs/INSTALL.md) to install Python and
the required packages. Then open a terminal in the project folder and try the small example:

```bash
source source_me.sh
python3 make_tutorial.py lint docs/examples/formatting_demo.md
python3 make_tutorial.py build docs/examples/formatting_demo.md --format docx,xlsx
```

`lint` checks the source for problems. `build` makes the files. Open:

- `tutorial_output/formatting_demo/formatting_demo.docx` - the formatted instructions.
- `tutorial_output/formatting_demo/formatting_demo.xlsx` - the labeled worksheet, with calculation
  cells left blank.

For your own lesson, replace `docs/examples/formatting_demo.md` with the path to your copy.
The output folder uses your file's name. Read reported problems, rebuild after edits, and check
that someone following the instructions can find the right cells and complete the calculations.
A successful build does not establish that the scientific explanation or statistical test is correct.

For a PDF too, install LibreOffice and the fonts in [docs/INSTALL.md](docs/INSTALL.md), then run:

```bash
python3 make_tutorial.py build docs/examples/formatting_demo.md --format all
```

## When your worksheet changes

Use the row-and-column walkthrough in [docs/FORMATTING_GUIDE.md](docs/FORMATTING_GUIDE.md#add-a-calculation-column)
first. For larger moves, a command can help update connected references. Review the changes before
applying them; visible wording and worked numerical examples may still need your attention.

<details>
<summary>Optional: preview a coordinated worksheet edit</summary>


After choosing a new layout, preview a column insertion using ordinary spreadsheet coordinates:

```bash
python3 make_tutorial.py worksheet-edit templates/calculated_column.md \
  --sheet Data insert-columns --at A --count 1
```

This prints a diff and leaves the source unchanged. In this template, inserting column A moves
the data to B:C, the learner's first formula cell from C2 to D2, and its formula from `=A2^2` to
`=B2^2`. The fill action's target moves to D2:D4; the preview flags its displayed
`Fill C2:C4` wording for author review.

Explicit worksheet references stay coordinated. Ambiguous bare references and worked numerical
explanations are flagged for author review rather than guessed at or rewritten. See
[docs/USAGE.md](docs/USAGE.md#maintain-a-worksheet-after-a-layout-decision) for applying a reviewed edit.

</details>

## What to read next

| Your question | Where to look |
| --- | --- |
| What should I type, and how will it look? | [docs/FORMATTING_GUIDE.md](docs/FORMATTING_GUIDE.md) |
| How do I write a complete lesson? | [docs/AUTHORING_GUIDE.md](docs/AUTHORING_GUIDE.md) |
| Can I see other biology tutorials? | [docs/TUTORIAL_CATALOG.md](docs/TUTORIAL_CATALOG.md) |
| How do I install the software? | [docs/INSTALL.md](docs/INSTALL.md) |
| How do I build files or change worksheet locations? | [docs/USAGE.md](docs/USAGE.md) |

For detailed reference, [docs/TUTORIAL_SPEC.md](docs/TUTORIAL_SPEC.md) describes all supported syntax.
[docs/GOOGLE_SHEETS_VALIDATION.md](docs/GOOGLE_SHEETS_VALIDATION.md) explains the separate spreadsheet
calculation checks and their limits. Neither is required reading before starting your first draft.

The source code is licensed under the [MIT License](LICENSE.MIT).
