# Babies, Caffeine, and PETase tutorial readiness

Path note (2026-10-22): paths and command examples below use the current repository layout.
Recorded observations belong to their stated snapshots; renamed output manifests retain their
original contents until the final rebuild and verification refresh.

Editorial review completed 2026-10-22 for the seven assigned lessons. Evidence was compared with
the read-only 2025 originals and the existing babies, caffeine, and PETase migration reports.
The report does not alter or replace those migration/calculation records.

## Readiness

All seven sources are ready for the root agent's fresh review. Their procedure sequences lead from
the supplied data through the requested calculations to a written interpretation. Cell references
match the worksheets declared in each source, and the supplied workbook labels remain the starting
state. Students are asked to label cells that the authored workbook leaves blank.

The three caffeine lessons form a continuous sequence: summarize both variables, inspect their
paired pattern and fit a straight line, then test whether a quadratic model better describes the
observed curve. The conclusion distinguishes association from cause and treats p-values, R-squared,
residuals, and prediction limits with appropriate qualifications. Their retained images are story
illustrations; the lessons tell students to use their own calculated results as evidence.

The babies lessons preserve the national z-test, one-sample t-test, and independent two-sample Welch
test sequence. Their scenarios identify the test alternatives and the final lessons state what the
supplied results support. The one-sample t-test now introduces t through estimated population
variability rather than a sample-size cutoff. PETase preserves its scenario while plainly labeling
all supplied numbers as synthetic; its Bradford work leads from blank correction and calibration to
dilution-corrected BSA-equivalent total protein, with explicit limits on claims about PETase yield or
activity.

No numeric data or formulas were changed, and no new calculations were added in this editorial pass.
The national tutorial's existing spare ranges, the babies practice-input warnings, and the caffeine
LINEST/INDEX compatibility notes remain documented migration/compiler observations.

## Editorial changes

- Addressed fresh-review findings: the two mutually exclusive babies test alternatives now each
  label `F5` with the chosen tail and direction; the caffeine quadratic-term p-value now explains
  the exploratory limitation when the model follows a pattern noticed in the same data, and calls
  for confirmation using independent data with the model specified in advance.

- Removed obsolete Google Sheets copying, renaming, tab, and layout screenshots from the active
  babies z-test procedure. Replaced its useful population-value table example with native Markdown.
  Kept the title, normal-curve, and story illustrations. Replaced the old completed-table screenshot
  from the babies one-sample t-test with a native table that marks supplied cells and student entries.
- Reworded the seeded babies `D1`/`E1` headers as inspection guidance. For the t-test, `E3` is
  already seeded with `not used`; the procedure now asks students to inspect it rather than repeat
  its value. Calculation labels remain student-entered where the workbook leaves them blank.
- Corrected the one-sample t-test introduction so it does not imply that fewer than 30 observations
  alone determines whether to use t. The surrounding lessons retain the relevant assumptions.
- Left all original screenshot binaries untouched in the read-only artifact collection and local
  asset directory; the active lessons no longer reference the obsolete UI images.

## Validation

Ran `source source_me.sh && python3 make_tutorial.py lint` separately on each of the seven assigned
Markdown sources. All seven passed offline lint. Expected diagnostics remain: Google cell mappings
are intentionally absent or unverified; babies formulas use spare rows and include free-response
cells; caffeine regression functions include conservative `INDEX`/`LINEST` compatibility warnings.
Lint does not verify Google Sheets import, UI navigation, or live formula calculations.

No empty Guide headings were found. Screenshot references remaining in babies lessons are the
conceptual normal-curve and story illustrations, not Google UI. Caffeine illustrations are similarly
identified in the lesson as illustrations, not evidence from the workbook.
