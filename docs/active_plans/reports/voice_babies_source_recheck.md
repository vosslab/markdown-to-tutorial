# Babies source fidelity recheck

Verdict: **ACCEPT - the concrete source findings in `voice_babies_source_spec.md` are resolved.**
This review rechecked the current canonical Markdown directly against the Fall 2025 Fried Foods
Markdown sources. It makes no claim about rendered DOCX/PDF pages or workbooks; the separate
material-quality review remains necessary.

## Scope and method

Read `docs/active_plans/instructional_voice_restoration.md`, `docs/TUTORIAL_SPEC.md`,
`docs/active_plans/reports/voice_babies_source_spec.md`, and
`docs/active_plans/reports/voice_babies_recovery.md`. Compared the three original Markdown lessons
under `2025_Artifacts/` with `tutorial_data/babies_1_z_test.md`,
`tutorial_data/babies_2_t_test.md`, and `tutorial_data/babies_3_two_sample_t_test.md`, focusing on
each exact prose and grouping finding in the source specification. The original Markdown is the
wording authority. The recovery report was used as a locator only; each finding below was confirmed
against the source text itself. Current source hashes match those reported in the recovery map.

## Recheck results

### Babies 1: z test

- The conceptual statistic formula is present as its own nested `Formula:` item before the
  spreadsheet entry (`babies_1_z_test.md:165-170`): "(sample mean - population mean) / [ population
  standard deviation / sqrt(sample size) ]". It is distinct from the cell formula and explanation.
- Step 3's numbered cell instructions retain nested `Enter:` and explanation bullets; E5 says
  "we will use," and E7 retains the note that the sample standard deviation is not used
  (`:148-164`).
- The p-value branches are numbered parents 1 and 2, with their cell instructions nested below
  (`:199-204`). The decision entries retain nested formula instructions and the numbered
  `Explanation:` parent with three child bullets (`:225-240`). The two interpretation examples are
  child bullets under item 2 (`:243-248`).
- The transition at `:269` is an H3 informational heading, `Setup for the T-Test:`. It preserves
  the transition's heading role while avoiding historical structural Part numbering. The active
  plan and tutorial numbering contract allow standalone numbering; historical Part 2/3 numbers are
  not a blocker.

### Babies 2: one-sample t test

- The scenario's "This time, he must:" instructions are bullets (`babies_2_t_test.md:120-124`),
  and D2 retains "it should say" (`:147`). Steps 3-7 preserve nested entries and explanations,
  including the degree-of-freedom introduction and its separate entry/explanation children
  (`:165-193`).
- The p-value subsection keeps numbered parent branches and nested entries/explanations
  (`:228-252`). The right-tail branch uses the signed formula `=1 - T.DIST(E9, E10, TRUE)` and
  retains the full explanation that it tests "the probability of observing a value as extreme or
  more extreme in **one direction** (greater than the population mean)" (`:245-252`). Its cell
  references are E9 and E10. This preserves the original teaching point while correcting the
  unsupported `T.DIST.RT` usage and the source's incorrect cell references. The decision
  instructions retain nested, emphasized test-specific formula directions (`:267-280`).

### Babies 3: two-sample t test

- Section 6.2 restores the syntax introduction, syntax bullet, "Here's how you'll set up the
  formula," and nested Range1/Range2/Tails/Type walkthrough (`babies_3_two_sample_t_test.md:160-171`).
  Tails retains its explanatory sentence and separate one- and two-tail child bullets (`:167-169`).
  Type explains unequal variances and Welch's test with the corrected type argument 3 (`:170-171`).
- The two-tail branch retains nested explanation bullets for both hospital ranges, the first `2`,
  and the final `3` (`:172-180`). The one-tail branch retains an explanation group for the `1`
  argument, `T.TEST` magnitude behavior, and the signed `IF` guard (`:181-191`). The semantic
  `Alternative` wrappers preserve the implemented branch model while the authored branch
  explanations remain nested beneath it.
- `Important Notes:` retains the original capitalization and colon (`:196`). The F6/G6 combined
  label/value direction remains one numbered item (`:209-212`), consistent with the original.

## Approved exceptions and boundary

Technical changes documented in the source specification remain narrow and supported by the
current lessons: `STDEV.S`, corrected cell references and formulas, Welch type 3, ranges through
row 101, right-tail sign handling, and corrected scientific explanations. The repeated two-sample
decision entry remains consolidated, and setup text describes the generated standalone workbook.
These are the documented exceptions, not unexplained deletions. The approved standalone Part/Step
numbering resolves the old-numbering concern.

No concrete source-spec failure remains in the three current Markdown files. This ACCEPT does not
cover rendered material quality, LibreOffice output, workbook appearance or calculation, or the
overall plan milestone; those require their separate review lanes.

## Source hashes

| Source | SHA-256 |
| --- | --- |
| Babies 1 | `da64c65d64e160d9b7dc311b73afc7e28fefb38efdb45d9a34d9ed2704c1d5c1` |
| Babies 2 | `446256332bb144cc1ecbd2d0202043dc980a484ceee4ed28db4d624a6f76e96d` |
| Babies 3 | `c58d36f92c826a7625f5e371c65bad5ab5dca25148301117d69ac1504217db5f` |
