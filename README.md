# markdown-to-tutorial

Turn student-authored Markdown into polished science tutorials, editable Word documents, and Excel
workbooks. Keep the author's words and students' calculations; let the compiler handle presentation
and reference maintenance.

## Screenshots

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

## Quick start

Install the Python requirements in [docs/INSTALL.md](docs/INSTALL.md), then build a small template:

```bash
source source_me.sh
python3 make_tutorial.py lint templates/calculated_column.md
python3 make_tutorial.py build templates/calculated_column.md --format docx,xlsx
```

Open `tutorial_output/calculated_column/calculated_column.docx` and
`tutorial_output/calculated_column/calculated_column.xlsx`. You get formatted instructions and
three supplied observations, with column C reserved for the squared values.

For PDF output, install LibreOffice and the fonts listed in [docs/INSTALL.md](docs/INSTALL.md), then
run `python3 make_tutorial.py build templates/calculated_column.md --format all`.

Copy a template to start your own lesson:

- [templates/calculated_column.md](templates/calculated_column.md) - Data, a new formula, and fill-down.
- [templates/statistical_summary.md](templates/statistical_summary.md) - A compact summary calculation.
- [templates/anova_worksheet.md](templates/anova_worksheet.md) - An ANOVA worksheet construction activity.

Use plain ASCII Markdown, straight quotes, and ordinary Excel formulas. Readable named entities
such as `&alpha;` are supported. No programming or replacement formula language is required.

## Write instructions in context

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

## What the project provides

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

## Move cells, keep instructions coordinated

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

## Documentation

- [docs/FORMATTING_GUIDE.md](docs/FORMATTING_GUIDE.md) - Compare Markdown syntax with cropped output examples.
- [docs/INSTALL.md](docs/INSTALL.md) - Install Python requirements, LibreOffice, and the required fonts.
- [docs/AUTHORING_GUIDE.md](docs/AUTHORING_GUIDE.md) - Fill in templates, write instructions, and design worksheets.
- [docs/USAGE.md](docs/USAGE.md) - Build, preview coordinated worksheet edits, import, and validate calculations.
- [docs/TUTORIAL_CATALOG.md](docs/TUTORIAL_CATALOG.md) - Browse all 12 lesson sources and data notes.
- [docs/TUTORIAL_SPEC.md](docs/TUTORIAL_SPEC.md) - Read the complete source and output contract.
- [docs/GOOGLE_SHEETS_VALIDATION.md](docs/GOOGLE_SHEETS_VALIDATION.md) - Review the separate Google validation scope and evidence.

The source code is licensed under the [MIT License](LICENSE.MIT).
