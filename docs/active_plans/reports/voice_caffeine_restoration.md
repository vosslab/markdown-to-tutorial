# Caffeine voice restoration

Restored the three canonical lessons against the read-only original
`/Users/vosslab/nsh/SLIDES/djot-slide-builder/Tutorial_Outline.md`, not the previous migration.
The comparison report guided corrections; the original supplied the wording. Original embedded
image payloads and planning notes after the lesson were excluded. The recovered original workbook
at `/private/tmp/caffeine_source.xlsx` was not changed.

## Pilot proof

The former heading `Square the predictor`, paraphrased explanation, and repeated Label / Enter /
Fill / Do / Check bullets were replaced by the original `Create a SQUARED Sleep-Hours Column`
heading, original introductory paragraph, and exactly four numbered instructions:

1. Use blank column C in your spreadsheet.
2. Label it `[Sleep Hours Squared (x^2)](label:C1)`
3. If the sleep hours are in cell A2, enter: `[=A2^2](enter:C2)`
4. Press Enter, then `[drag the little blue square all the way down to the bottom](fill:C2:C26)`
   to make sure it applies to all students! Basically, we're taking each student's hours of sleep
   and multiplying that number by itself. If someone slept 6 hours, their squared sleep value
   is 36! Don't worry, they didn't sleep for 36 hours!

The canonical source retains the original curly punctuation as HTML character references; this
report uses plain punctuation for compact readability. The original introductory paragraph is
unchanged: "To let our regression model curve, we need to square our predictor variable (x)."
Original item 1 was "Add a new column to your spreadsheet." Its sole replacement avoids shifting
the existing fixed cells. The original 36-hour joke and all remaining item-4 words are retained.
Adjacent E/F predictor staging moved to the original Calculate Quadratic Regression step as one
paragraph with multiple bindings, outside the four-item pilot.

## Restoration and technical exceptions

| Lesson | Original material restored | Required exceptions and additions |
| --- | --- | --- |
| Descriptive | Warm up - Tania + Roohana; original orientation, setup, descriptive explanations, questions, and congratulations | One generated Sleep and scores tab replaces references to six original tabs and placeholder screenshots/template link. Correct sleep-versus-score formula descriptions and units; use STDEV.S; add matching exam-score calculations. Small entry/submission instructions complete the draft. |
| Linear | Scenario paragraphs, research question and hypotheses, all seven descriptive step headings, student-as-dot joke, scatterplot questions, symbol explanation, hypothetical example, decision paragraphs, coffee jokes, final reflection | Generated workbook eliminates copying between tabs. Retain A/B mapping and scalar INDEX/LINEST extraction into existing H cells; update t formula to those cells and incorrect intercept reference D6 to E6. Add two-tailed entry direction, model assumptions, retained numerical checks and standalone submission instructions. |
| Quadratic | Plot-twist paragraph structure, receipts/disconnect humor, research question and hypotheses, four-item squared-column sequence, equation breakdown, LINEST coefficient-order explanation, original comparison question/paragraph, celebration and closing water/browser-tabs joke | Replace NOTHING linear claim with significant positive slope that misses curvature; replace unobserved 2/14-hour examples with observed range. Qualify apparent optimal-sleep claim to these data. R2 alone cannot diagnose model shape, so correct that clause. Reserve blank C instead of inserting a column; fix malformed/nonadjacent LINEST ranges using unchanged E/F predictors and scalar outputs. Add missing inference, chart-setting, prediction, standalone setup and submission instructions. |

All sound source paragraphs were restored directly, including long conversational paragraphs;
they were not shortened to match the migration. The original prose's case and emphasis remain in
descriptive headings; standalone numbering is generated from Part/Step/Substep prefixes.
The original "Does Sleep Affect Exam Scores?" subtitle remains bold text above the lesson because
the required document structure reserves H2 exclusively for Workbook and Tutorial.
Math notation uses supported y-hat/coefficient descriptions and HTML superscripts, preserving
the equations and symbol-by-symbol explanation. Typographical corruption `B**efore` and
`t-stastistic` were corrected. Draft placeholders and incompatible tab references were completed.
Nested lists retain the author's instructional grouping. UI menu instructions remain ordinary
prose and bold text, with no Choose-action requirement.

The misleading original scatterplot/model comparison screenshots 06 and 13 remain replaced by
the existing accurate plots of the actual observations. Original story illustrations remain.
Quadratic exploratory model-selection cautions, independent-error/normality/variance assumptions,
two-tailed alternatives and answer directions, causation cautions, observed-range restriction and
16-hour extrapolation question remain. New additions received a humanizer check; original prose
was exempt from stylistic rewriting.

## Workbook and verification

No seeds were added and all formula answer cells remain unseeded. Regions declare meaning, not
editing permission. Source A1:B26 remains blue-source data; descriptive D1:F4 and quadratic
C1:C26/E1:F26 are calculation regions. Linear D1:E14 is calculation; G1:H5 and J2:K10 are results.
Quadratic H1:I11 and L1:M4 are results. Dedicated blank interpretation regions are D6:F8,
M2:O12, and L7:N16 respectively. All declared rectangles are disjoint within each workbook.

The compiler confirms all 25 A/B pairs unchanged in each lesson. Compared with Git HEAD's
pre-restoration lessons, all explicit formula destinations and exact formula strings are
unchanged: six descriptive, ten linear, fifteen quadratic. C2:C26 and E2:F26 fill actions remain.
The pilot has exactly four numbered items. No compiler, renderer, oracle, tests, original source,
or generated output was edited by this workstream.

Each lesson passes `source source_me.sh && python3 make_tutorial.py lint <source>` against the
current shared compiler. Remaining messages are the existing unmapped Google-link note and
INDEX/LINEST compatibility warnings. This is offline compilation evidence only: LibreOffice
builds, generated PDF/workbook inspection, Google import/calculation, and final fresh review
belong to integration and are not claimed here. An initial lint invocation with three positional
paths was rejected by the CLI; separate supported one-file invocations all passed.
