# Caffeine original comparison

Independent comparison of the original lesson, the three authored Markdown lessons, and their
generated PDFs/XLSX workbooks. The source outline is
`/Users/vosslab/nsh/SLIDES/djot-slide-builder/Tutorial_Outline.md`; original line numbers below
refer to that file. The original XLSX export is `/private/tmp/caffeine_source.xlsx`. No original
PDF was present in the source repository or workspace, so PDF review covers the current generated
artifacts only. This is a cognitive walkthrough of the learner's tasks, not a student study.

## Restore the original voice

The current lessons retain the academy setting and several jokes, but some effective source lines
were shortened or rewritten. The source's voice can return alongside the newer accuracy checks.

| Original source anchor | Current destination | Recommendation |
| --- | --- | --- |
| L86-L92: "where the coffee is strong, the students are exhausted" and "too much caffeine" | `caffeine_2_linear_regression.md`, opening L3-L5 | Restore the original scenario paragraph verbatim. Keep the current standalone regression definition and the notice that students become points on the plot. |
| L100-L108: research question and explicit H0/H1 for a nonzero slope | `caffeine_2_linear_regression.md`, L61 and L165-L170 | Restore the question and hypotheses near the opening scenario, where students first learn what they are investigating. Keep the current explicit two-tailed direction and model-assumption note at the test. |
| L179-L197: equation symbols explained in plain language; "Don't let the symbols scare you." | `caffeine_2_linear_regression.md`, L115-L118 | Restore the source's brief symbol-by-symbol explanation and warm lead-in. Preserve the current equation and percentage-point units. |
| L223-L229: hypothetical "45 + (5 x hours of sleep)" with explicit warning that values are hypothetical | `caffeine_2_linear_regression.md`, L143-L146 | The current text already preserves this material accurately; retain it. |
| L313-L327: "plot twist," upside-down-U story, line "not connecting the dots," and the pivot to a curve | `caffeine_3_quadratic_regression.md`, L3-L6 and L76-L84 | Restore the original transition and joke structure. Replace only the unsupported 2-hour/14-hour examples with language tied to the observed range. Keep the important point that a significant positive linear slope can coexist with a poor description of curvature. |
| L340: "Create a SQUARED Sleep-Hours Column" | `caffeine_3_quadratic_regression.md`, L88 | Restore the exact numbered-step heading and emphasis. |
| L342 and L347: "To let our regression model curve, we need to square our predictor variable (x)." and "Don't worry, they didn't sleep for 36 hours!" | `caffeine_3_quadratic_regression.md`, L90-L109 | Restore both original sentences verbatim around the learner's formula/fill action. The current PDF keeps a changed version of the 36-hour joke; the source wording is more conversational. |
| L351-L367: quadratic equation, symbol meanings, and "That extra x^2 term is what gives the model its curve." | `caffeine_3_quadratic_regression.md`, L115-L122 | Restore the original explanatory rhythm and direct link between the squared term and curvature. Keep the current accurate note that the model remains linear in its coefficients. |
| L393-L402: "Did quadratic regression actually improve our model, or did we just make the equation more complicated for fun?" | `caffeine_3_quadratic_regression.md`, L181-L196 | Restore the opening question verbatim. Keep the current training-R-squared caveat and residual/new-data follow-up. |
| L404-L410: "your reward is hopefully a better understanding ... and maybe a snack (no coffee)" and closing water/browser-tabs joke | `caffeine_3_quadratic_regression.md`, L200-L218 | Restore the source's celebratory wording and "PLEASE get some sleep!" ending. Retain the current range and causation qualifications. |

The descriptive-stats introduction already preserves the source's academy-warmup premise and credits
Tania and Roohana. Keep its corrected promise to calculate both variables. Restore the source heading
"Part 0: Warm up - Tania + Roohana" (original L32) if the author wants the original contributor
credit visible as a section heading as well as in the current introduction.

## Keep the useful corrections

These changes repair errors in the source and should remain while its voice returns:

- In tutorial 1, calculate mean, median, and sample standard deviation for both sleep and scores.
  Original L61-L76 repeatedly labels sleep-column formulas as score calculations and asks for a
  median exam score after using the sleep range. The current paired-column formulas and `STDEV.S`
  are right; make the explanations lively without restoring those mismatches.
- Describe the linear result as statistically significant but incomplete for the observed curve.
  The source's "data is giving absolutely NOTHING linear" (L315) conflicts with the recovered data:
  the positive slope is about 3.18 percentage points per hour and the two-tailed p-value is about
  0.00196. The current distinction between evidence of a nonzero slope and model shape is correct.
- Keep references within the observed 3-to-11.5-hour range when describing the data. Original L315
  uses 2 and 14 hours, which were not observed. The current final question about 16 hours is useful
  as an explicitly labeled extrapolation exercise.
- Keep a test for the quadratic coefficient, its two-tailed alternative, and the assumption and
  model-selection cautions. The original asks about a quadratic term but never supplies an
  executable coefficient test.
- Keep the corrected LINEST input ranges and scalar extraction. Original L377 and L381 contain a
  malformed response range and a non-adjacent array construction; current `B2:B26` and adjacent
  `E2:F26` predictors avoid including scores as predictors and make the coefficient order explicit.
- Keep the current `A2:A26` sleep and `B2:B26` score mapping. Original L126-L142 mixes the Data tab
  with the regression tab and then describes the roles inconsistently.

## Group learner actions

The original Step 9 is one numbered sequence of four actions (L340-L347): add the column, label it,
enter `=A2^2`, and fill down. The current quadratic lesson needs extra actions for its explicit
adjacent predictor table and checks, but eight separate instruction bullets at L93-L109 break one
small task into a long visual checklist. Group related setup, formula/fill, and verification actions
into a few compact units after the shared authoring syntax contract is settled. Keep each required
cell address and the check that the last row matches the same student.

Apply the same grouping to repeated `Label` / `Enter` pairs in the regression lessons: keep the
formula destinations and distinguish student-entered formulas from expected checks, but place the
small sets for one calculation together. The current PDFs expose the cost of splitting each item:
the linear test-statistics page renders as a long bullet list, and the descriptive-statistics PDF
places only a handful of final reflection and closing lines on page 3, leaving most of it empty.
This is a focused pagination and working-memory issue, not a request for a new validation framework.

## Preserve useful visual structure

The original workbook uses six task-specific tabs, including two reflection tabs. On the three
analysis sheets, data headers are blue (`#6D9EEB`), regression measure/result headers are orange
(`#FF9900`), and statistics/test blocks have separate theme fills. Each generated workbook now has
one `Sleep and scores` tab and no filled cells. Consolidating the tabs is compatible with the new
self-contained tutorial files, but the current sheet loses the original color cues that distinguish
data, calculated values, and inferential statistics. A small, consistent set of section fills in the
single-sheet layout can retain that meaning without recreating six tabs.

The current PDFs preserve the embedded story art and render the lessons in the expected order. The
quadratic PDF's equation page places the chaotic bathroom illustration directly above the concise
equation explanation; its neighboring page begins the formula-entry sequence. That pairing supports
the plot-twist story, while the surrounding learner actions can be grouped more compactly.
