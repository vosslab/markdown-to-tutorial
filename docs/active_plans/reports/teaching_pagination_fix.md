# Result label pagination fix

The DOCX renderer now sets native `keep_with_next` on a Label paragraph when the immediately
following sibling list paragraph is Enter or Replace for the next column in the same worksheet
and row. Both targets must be single cells. It does not join whole lists, infer page numbers, or
cross prose, chart, heading, nested-list, or list-boundary tokens. Existing parent/child list
pagination remains in place.

Files changed: [docx_renderer.py](../../../tutorial_lib/docx_renderer.py) and
[test_tutorial_docx.py](../../../tests/test_tutorial_docx.py).

## Evidence

`source source_me.sh && python3 -m pytest tests/test_tutorial_docx.py -q` passes: 3 tests.
The durable regression check compiles authored instructions, exports DOCX, and inspects native
paragraph XML. It verifies that the adjacent result label stays with its entry, a summary header
is not joined, intervening prose breaks the pair, and the result entry is not locked to the
following instruction.

Direct DOCX-only exports of the current lesson sources were opened with python-docx:

| Source | Label keep-with-next | Immediately following entry | Entry keep-with-next |
| --- | --- | --- | --- |
| caffeine_2_linear_regression | G2: Slope = true | H2: LINEST formula | unset |
| caffeine_3_quadratic_regression | H5: Quadratic R-squared = true | I5: LINEST formula | unset |
| petase_1_linear_regression | F3: Intercept (A595) = true | G3: INTERCEPT formula | unset |

These temporary exports were outside the main bundle directories and did not invoke LibreOffice.
PDF pagination still needs the coordinator's rebuilt-bundle visual verification.
