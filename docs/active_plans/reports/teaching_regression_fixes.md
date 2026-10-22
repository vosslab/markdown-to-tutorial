# Regression teaching corrections

Date: 2026-10-22. Scope: three caffeine lessons and the PETase lesson only. The caffeine draft
is a foundation for three independently usable lessons, not a quality benchmark. Read the full
four lesson sources, the original caffeine prose without embedded image definitions, the original
PETase scenario and teaching sections, and the independent
[teaching_regression_review.md](teaching_regression_review.md).

## Focused lesson changes

| Lesson section | Before | After and reason |
| --- | --- | --- |
| Caffeine 1 introduction | Warm-up attribution absent; title shortens the academy name. | Restore Tania and Roohana and the All-Nighter Academy name; state the descriptive-statistics assignment. |
| Caffeine 1 workspace and calculations | Assumes formula-entry knowledge; no simple recovery check. | Explain cell selection, equals sign, Enter, and formula-bar inspection once; use the mean's observed-range bound as a check. |
| Caffeine 1 ending | Reflection followed immediately by continuation. | Add a brief to Dr. Caffeine using all six statistics, a same-mean/different-spread transfer question, and a concrete submission task. |
| Caffeine 2 setup and ending | Has a valid full workflow but no entry reminder, numeric recovery check, or collected deliverable. | Keep that workflow; add a short entry reminder, slope/R-squared check with range recovery, an overclaim to critique, and the requested chart/calculations/conclusion. |
| Caffeine 3 squared predictors | Two fills are buried in 72 repeated descendant Enter instructions. | Retain three seed formulas, use `Fill C2:C26: Down` and `Fill E2:F26: Down`, and teach selection, relative references, keyboard/handle fill, and endpoint checks. |
| Caffeine 3 interpretation | Coefficient order is explained, but b1 could be mistaken for a constant hourly effect. | Clarify that b1 alone is not a constant score change in a quadratic model. |
| Caffeine 3 comparison comic | Image prints quadratic R-squared .88; actual data give .847. | Retain the original image; place the specific .847 explanation beside it instead of repeating broad disclaimers at every introduction. |
| Caffeine 3 ending | Has a qualified verdict but no transfer task or collected deliverable. | Ask about unsupported 16-hour extrapolation and specify the equations, chart, prediction, test, and verdict to submit. |
| All caffeine progression | Hyperlinks target Markdown files absent from generated document folders. | Name the next/prerequisite lesson by its readable title. Each workbook still includes all 25 original pairs. |
| PETase introduction | Opens with migration history and loses the learner's new-hire role. | Keep a concise synthetic-data disclosure; restore the direct startup assignment to estimate protein concentrations and recovered masses. |
| PETase assay bridge | Blue dye binding is compressed into one sentence. | Restore acidic free dye, protein-bound blue dye, measurement wavelength, and matching treatment of standards/unknowns; preserve total-protein/BSA-equivalent qualifications. |
| PETase repeated formulas | Enumerates every repeated blank correction, fitted/residual pair, and three-sample calculation. | Use five explicit Fill ranges, explain anchored references and rectangular fill, retain endpoint checks, and add a compact numerical recovery check. |

Story, humor, images, observed sleep range, data, statistical formulas, test directions, and scientific
limitations remain. The original caffeine equation example is still explicitly hypothetical.
The original PETase source turns into unrelated microbial t-test instructions after its Bradford
setup; that source-contamination history belongs in this report and
[petase_migration.md](petase_migration.md), not in a student's opening task. The replacement numbers
remain synthetic and never support a claim about actual PETase production or activity.

Applied the requested humanizer guidance through targeted edits: preserve the academy humor and
startup role, keep bold instruction openings, and avoid broad synonym replacement. Additional words
address task entry, formula copying, recovery, interpretation, or completion. No new student formula
or seeded observation was introduced.

## Numbering and standalone sequence

Compiled the current sources and wrote fresh temporary DOCX files directly through the repository
renderer. Reopened each DOCX and confirmed every compiled Part/Step/Substep display appears in its
paragraph text:

- Caffeine 1: Part 1, Steps 1-5.
- Caffeine 2: Part 1, Steps 1-7; substeps 3.1-3.2 and 6.1-6.4.
- Caffeine 3: Part 1, Steps 1-7.
- PETase: Part 1, Steps 1-6; Part 2, Steps 1-5, following the compiler's per-Part reset.

Current source headings contain semantic `Part:`, `Step:`, and `Substep:` prefixes, with no manual
ordinal prefixes or stale literal references to the original draft's moved steps. All three caffeine
lessons start their own sequence. Their prerequisites are conceptual knowledge, not a saved answer
workbook. None links the student to an unavailable `.md` file.

## Source and calculation checks

Ran each source separately with `source source_me.sh && python3 make_tutorial.py lint <source>`.
All four passed with zero errors. Caffeine 1 and PETase have zero warnings; caffeine 2 and 3 retain
six and twelve existing INDEX/LINEST compatibility warnings, respectively. Each has the existing
unmapped-Google note. These are offline checks, not live Google validation.

One temporary check compares each staged pre-edit source against the current source. It compiles
both, collects Label/Enter actions plus generated Fill descendants, and requires exact equality
of every destination, scalar kind, and value. The old untyped prose `Fill:` wrappers are renamed
to plain `Copy:` in memory for this comparison; their explicit descendant formulas are unchanged.
All seeded workbook cell coordinates and values are also compared exactly.

| Lesson | Identical final Label/Enter destinations | Current explicit fills |
| --- | --- | --- |
| Caffeine 1 | 12 | None |
| Caffeine 2 | 23 | None |
| Caffeine 3 | 105 | C2:C26; E2:F26 |
| PETase | 38 | C2:C8; I2:J8; E13:E15; F13:F15; G13:G15 |

All four seeded-cell comparisons passed. Temporary DOCX/XLSX files and the JSON containing exact
heading sequences and equality results are under
`tutorial_output/verification/teaching_review/regression_fixes/`. The one-time checker is
`/private/tmp/regression_source_check.py`; no permanent tests or validation infrastructure were added.
Workbook label sizing belongs to the parallel workbook-layout correction.

## Verified instructional facts

Checked primary documentation on 2026-10-22:

- [Bio-Rad Quick Start Bradford manual](https://www.bio-rad.com/webroot/web/pdf/lsr/literature/4110065A.pdf),
  sections 1.1-1.2 and 2.1: acidic free dye is predominantly red near 470 nm; protein-bound blue
  dye is measured at 595 nm. Protein-dependent response and consistent assay treatment support the
  lesson's BSA-equivalent qualification. No universal Bradford working interval was added.
- [Google Sheets shortcuts](https://support.google.com/docs/answer/181110?hl=en): Fill down uses
  Ctrl+D on Windows and Command+D on Mac. The final lesson text uses these verified shortcuts,
  not an assumed Edit > Fill menu path.
- [Google trendline instructions](https://support.google.com/docs/answer/6075154?hl=en): equation,
  polynomial-degree, R-squared, and legend guidance support the chart actions. Added the missing
  legend reminder to the caffeine regression lessons.

No PDF build or new live Sheets session was performed in this source-correction workstream.
Final PDF pagination, image placement, workbook label readability, and independent classroom-quality
acceptance require the coordinator's fresh rebuild and reviewers.
