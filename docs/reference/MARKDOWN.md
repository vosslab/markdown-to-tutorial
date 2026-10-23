# Write readable Markdown

Use this page when you want to turn plain notes into readable tutorial instructions.
Markdown is text with a few punctuation marks that describe structure. Write the content;
the compiler supplies the document's fonts, colors, spacing, and numbering.

Start the guided lesson at [../STUDENT_GUIDE.md](../STUDENT_GUIDE.md).
Return to the task index at [../FORMATTING_GUIDE.md](../FORMATTING_GUIDE.md).

## Start with short paragraphs

Separate paragraphs with a blank line. A line break in your editor is useful for keeping
source readable, but does not by itself begin a new paragraph in the document.

```markdown
The five root lengths are synthetic practice data, measured in millimeters.

Compare the individual measurements before calculating a summary.
```

Use ordinary sentences to explain why a calculation matters. A formula alone does not tell
another student what to look for or how to interpret the result.

## Organize a tutorial

A complete source has a Workbook section for supplied cells and a Tutorial section for
student instructions. Inside Tutorial, use Part and Step headings:

```markdown
## Tutorial

### Part: Describe root lengths

- **Worksheet:** Roots

#### Step: Inspect the measurements

1. Read the root lengths in cells A2:A6.
2. Notice that the measurement unit is millimeters.
   - Row 1 contains the heading.
   - Rows 2 through 6 contain five measurements.
```

The compiler numbers Parts and Steps. You supply their names. Keep action instructions inside
a Step, and use indentation to place supporting details under the instruction they explain.

<!-- screenshots:begin (managed by screenshot-docs) -->
![A rendered Part and Step with numbered instructions and nested details](../screenshots/syntax_headings.webp)
<!-- screenshots:end -->

The crop uses the older Sleep-and-scores example to show the same heading structure.
Notice how the heading levels remain distinct even though the source contains no font settings.
A bullet such as `- **Worksheet:** Roots` binds the Part to the worksheet named Roots.

## Emphasize a distinction

```markdown
Read the **root length** heading before calculating the *sample* standard deviation.
Use `A2:A6` for the five observations. The symbol &alpha; can appear in an explanation.
```

- `**bold**` emphasizes a phrase.
- `*italics*` marks a distinction.
- Backticks display literal text such as a cell address or formula.
- Named HTML entities such as `&alpha;` provide scientific symbols in ASCII source.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Rendered emphasis, literal exponent notation, and a Greek alpha in explanatory prose](../screenshots/syntax_text.webp)
<!-- screenshots:end -->

The crop uses the older sleep example to show the same punctuation. Notice the different
appearance of literal spreadsheet text and ordinary prose. Keep straight quotation marks and
ordinary hyphens in source. Use named entities rather than pasting non-ASCII scientific symbols.

## Link to another resource

Ordinary links show clickable text and point to a file or web address:

```markdown
Read [WORKSHEETS.md](WORKSHEETS.md) to map a table to cells.
```

The link destination is relative to the file containing it. From this reference folder,
`WORKSHEETS.md` is a neighbor, while `../STUDENT_GUIDE.md` goes up one folder.

A local image uses the same pattern with an exclamation mark:

```markdown
![A tutorial table with a header row](../screenshots/syntax_table.webp)
```

<!-- screenshots:begin (managed by screenshot-docs) -->
![A tutorial table with a header row](../screenshots/syntax_table.webp)
<!-- screenshots:end -->

Write alternative text that explains what the reader should learn from the image. Use an
existing image file at the stated path; an image link does not create the image.

## Recognize special action links

```markdown
1. In cell E2, enter:
   [`=COUNT(A2:A6)`](enter:E2)
```

This looks like a link in source, but `enter:E2` records a spreadsheet action. The printed
instruction shows the formula. See [ACTIONS.md](ACTIONS.md) for the visible wording and hidden target.

## Avoid a common mix-up

A table under Tutorial explains information in the document. A table under Workbook supplies
starting spreadsheet cells. Moving a table between those sections changes its purpose.
See [WORKSHEETS.md](WORKSHEETS.md) before designing the starting sheet.

Practice writing instructions in [../learn/PART_1_CREATE.md](../learn/PART_1_CREATE.md#step-write-plain-markdown).
Compare the working source in
[../examples/authoring_course/root_02_write.md](../examples/authoring_course/root_02_write.md).
For the complete grammar, see [../TUTORIAL_SPEC.md](../TUTORIAL_SPEC.md#document-structure).
