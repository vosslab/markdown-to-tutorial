# Write spreadsheet formulas

Use this page when you need a count, mean, sample standard deviation, or repeated calculation.
These are ordinary Excel formulas. The compiler records them; the spreadsheet application
calculates their numerical values.

Find the course at [../STUDENT_GUIDE.md](../STUDENT_GUIDE.md) and the task index at
[../FORMATTING_GUIDE.md](../FORMATTING_GUIDE.md).

## Begin with equals

A formula begins with `=`. The cell address identifies an input, and the action target identifies
where the student types the formula:

```markdown
1. In cell E2, enter:
   [`=COUNT(A2:A6)`](enter:E2)
```

`A2:A6` means the range from A2 through A6, including both ends. For the Roots practice data,
those cells contain 12, 15, 18, 20, and 25. The heading in A1 is outside the range.

<!-- screenshots:begin (managed by screenshot-docs) -->
![An instruction to enter the count formula in cell E2](../screenshots/course_count_action.webp)
<!-- screenshots:end -->

Notice that E2 is named in the printed instruction. The target in the Markdown link is hidden
from the printed document, so it cannot replace that visible cue.

## Choose a summary

For the five synthetic root lengths, use these formulas in the summary table:

| Question | Destination | Formula | Expected display |
| --- | --- | --- | --- |
| How many numeric measurements? | E2 | `=COUNT(A2:A6)` | 5.000 |
| What is their mean length? | E3 | `=AVERAGE(A2:A6)` | 18.000 |
| How variable is this sample? | E4 | `=STDEV.S(A2:A6)` | 4.950 |

`COUNT` counts numeric cells. `AVERAGE` gives the arithmetic mean. `STDEV.S` calculates the
sample standard deviation; the suffix `.S` is part of the function name.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Roots summary showing count, mean, and sample standard deviation](../screenshots/course_statistics.webp)
<!-- screenshots:end -->

Check both a result and its input range. A plausible number can still describe the wrong cells.
For example, `=AVERAGE(A2:A5)` leaves out the longest root and gives 16.250.

## Use arithmetic operators

Use `+` for addition, `-` for subtraction, `*` for multiplication, `/` for division, and `^`
for powers. Parentheses group a calculation, as in `=(A2-E3)^2`.

A deviation compares one observation with the mean. After expanding to six observations, with
30 in A7, the mean is 20.000. The first deviation is 12 minus 20, or -8.000.

```markdown
1. In cell B2, enter:
   [`=A2-$E$3`](enter:B2)
2. [Fill B2:B7](fill:B2:B7) down to calculate all six deviations.
```

Column B has a supplied heading and blank student work cells in the Workbook source.

## Keep the mean fixed

A relative reference changes when you fill a formula down. A fixed reference with dollar signs
keeps its column and row:

| Formula cell | Formula after filling |
| --- | --- |
| B2 | `=A2-$E$3` |
| B3 | `=A3-$E$3` |
| B7 | `=A7-$E$3` |

The observation follows the current row; every deviation uses the same mean cell.
With `=A2-E3`, filling into B3 would read E4 instead of the mean.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Deviation formula with a changing observation reference and a fixed mean reference](../screenshots/course_fixed_formula.webp)
<!-- screenshots:end -->

Notice both dollar signs. Fixing only the row or only the column is a mixed reference; use both
for this exercise so the mean stays fixed during copying in either direction.

## Distinguish fill from moving

Dollar signs control copying and filling. They do not mean a cell stays at the same address
when the worksheet layout changes. Inserting a new column A moves the mean from E3 to F3.
The corresponding deviation formula becomes `=B2-$F$3` in C2.
See [CHANGES.md](CHANGES.md) for the full coordinated edit.

## Read display precision

Generated numeric, formula, and blank work cells display three decimal places by default.
For example, the sample SD displays 4.950 while retaining its underlying precision.
This is display formatting, not rounding the stored measurements or formula results.

Keep percentages and scientific notation as explicit lesson choices. Type a numeric observation
such as `12`, rather than adding its unit to each cell; put the unit in the column heading.

Practice the summary in [../learn/PART_2_STATISTICS.md](../learn/PART_2_STATISTICS.md#step-count-the-measurements), using
[../examples/authoring_course/root_04_calculate.md](../examples/authoring_course/root_04_calculate.md).
Practice fixed references in [../learn/PART_3_IMPROVE.md](../learn/PART_3_IMPROVE.md).
For action syntax, see [ACTIONS.md](ACTIONS.md); for exact scalar rules, see
[../TUTORIAL_SPEC.md](../TUTORIAL_SPEC.md#cell-values-and-types).
