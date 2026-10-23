# Find an authoring mistake

Use this page when a build reports a problem or a result does not match the intended calculation.
Start with the source, cell addresses, and actual spreadsheet results. A successful build cannot
establish that you selected the scientifically appropriate inputs.

Find the course at [../STUDENT_GUIDE.md](../STUDENT_GUIDE.md) and the topic index at
[../FORMATTING_GUIDE.md](../FORMATTING_GUIDE.md).

## Establish the intended result

For the five synthetic root lengths 12, 15, 18, 20, and 25 mm, check these facts first:

| Item | Intended value or address |
| --- | --- |
| Observations | A2:A6 |
| Count | E2 displays 5.000 |
| Mean | E3 displays 18.000 |
| Sample SD | E4 displays 4.950 |
| Starter summary values | E2:E4 blank |

<!-- screenshots:begin (managed by screenshot-docs) -->
![Five-observation Roots summary with the intended numerical results](../screenshots/course_statistics.webp)
<!-- screenshots:end -->

Notice the input rows as well as the results. Match your source to the correct checkpoint;
a six-observation example has a different mean and standard deviation.

## Missing equals becomes text

Compare these two action values:

```markdown
1. In cell E3, enter:
   [`AVERAGE(A2:A6)`](enter:E3)
```

```markdown
1. In cell E3, enter:
   [`=AVERAGE(A2:A6)`](enter:E3)
```

The first value is text because it lacks the leading equals sign. The second is a formula.
A word that resembles a function does not make text execute. Check the formula bar in your
spreadsheet application, and preserve the leading `=` in both source and student entry.

## Plausible numbers can be wrong

`=AVERAGE(A2:A5)` produces 16.250 instead of 18.000 because it omits the root length 25 in A6.
The formula is ordinary valid spreadsheet syntax, so check its meaning rather than expecting
the compiler to infer your intended sample.

Trace the first and last inputs. Compare the count with the number of observations in the table.
For a six-observation source ending at A7, all three summary ranges must also end at row 7.

## Check the destination separately

In this instruction, the visible destination and hidden target disagree:

```markdown
1. In cell E3, enter:
   [`=AVERAGE(A2:A6)`](enter:E2)
```

The formula inputs are correct, but `enter:E2` records the count cell as the destination.
Compare the visible sentence, link target, and worksheet layout. Correct them to name the same
cell. A temporary lint run of that changed action reports:

```text
error [action-visible-target] Visible cell E3 disagrees with enter target E2
  Correction: Use cell E2 in the instruction or change the binding target
```

Read the reported source location before changing another formula.

## A short fill misses work

After adding 30 in A7, filling B2:B6 leaves B7 without a deviation. The desired range is B2:B7:

```markdown
2. [Fill B2:B7](fill:B2:B7) down to include all six observations.
```

A shorter fill can be syntactically valid. Inspect the final row in the completed workbook,
not just the first formula. Update both the visible range and the hidden fill target.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Completed expanded worksheet including the final deviation in row 7](../screenshots/course_expanded_complete.webp)
<!-- screenshots:end -->

Check that row 7 contains the final observation and a deviation of 10.000 mm.

## Keep table rows rectangular

This table has a missing second cell in the last row:

```markdown
| Root length (mm) | Deviation (mm) |
| --- | --- |
| 12 | |
| 15 |
```

Write `| 15 | |` instead. The blank work cell still needs its table boundary. Lint reports
malformed tables; repair the source row rather than relying on a Markdown viewer to pad it.
A temporary lint run with the same missing-cell mistake in the summary table reports:

```text
error [ragged-table] Table rows have different cell counts
  Correction: Give every authored row the same number of cells
```

The header row occupies a spreadsheet row; the separator does not.

## Keep answers out of starters

Putting `=AVERAGE(A2:A6)` into the Workbook's E3 supplies that formula to students.
An identical Enter action then repeats the supplied answer. A temporary lint run reports:

```text
warning [assignment-redundant] Identical assignment repeats a prior value
  Correction: Remove the redundant instruction
```

A different Enter value at an already populated target is an assignment conflict.
Leave E3 blank when the student is supposed to calculate the mean. Use Replace only when
changing an existing value is an intentional lesson task.

## Check again after repair

Run lint, rebuild, and inspect the starter plus a separately completed workbook. Read the exact
reported diagnostic in your own run; this page describes causes rather than inventing error text.
Practice repairs in [../learn/PART_3_IMPROVE.md](../learn/PART_3_IMPROVE.md#step-check-and-share).
For input and destination patterns, see [ACTIONS.md](ACTIONS.md).
For the complete checks, see [../TUTORIAL_SPEC.md](../TUTORIAL_SPEC.md#validation-and-diagnostics).
