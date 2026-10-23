# Babies source grouping recovery

## Scope and evidence

This recovery addresses the concrete failed-source findings in
[voice_babies_source_spec.md](voice_babies_source_spec.md), using the three read-only Fall 2025
Fried Foods Markdown lessons as wording authority. The active instructional voice plan and repository
Markdown/Python/repository rules were read. Only the three canonical Babies sources and this report
were edited. No original artifact was edited and no LibreOffice command was run.

## Recovered original instruction groups

- **Babies 1:** Restored Step 3's nested `Enter:` and explanation bullets, including original
  "we will use" and the separate unused-sample-SD bullet. Restored Step 4's conceptual formula
  `(sample mean - population mean) / [ population standard deviation / sqrt(sample size) ]` before
  the bound spreadsheet formula. Restored numbered two-tail/one-tail parents with child action
  bullets in 5.2. Restored nested decision instructions, emphasis, "enter the formula", the
  `Explanation:` parent and its three bullets. Restored child interpretation example bullets and
  "write a brief interpretation". The setup parameter asides are child bullets as in the original.
- **Babies 2:** Restored the scenario's two child bullets and D2's "it should say". Restored
  nested formula entries under Steps 3-6; Step 7 again has its introductory instruction, `Enter:`
  bullet and `Here, E5...` explanation. Restored numbered 8.2 parents and each branch's nested entry,
  formula explanation and `Explanation:` bullets. The right-tail explanation again explicitly
  describes observing a value as extreme or more extreme in the greater-than direction.
  Restored the nested and emphasized IF decision instructions.
- **Babies 3:** Restored the complete 6.2 syntax introduction, syntax bullet, "Here's how you'll
  set up the formula" group and nested Range1/Range2/Tails/Type walkthrough. The Tails group
  retains separate one-/two-tailed choice bullets. Each alternative retains its formula and an
  `Explanation:` group; the two-tail group separately explains both data ranges, the tails argument
  and Welch type argument. The one-tail group explains the tails argument, magnitude behavior and
  signed IF guard. Restored original `Important Notes:` case/punctuation. Also restored the original
  nested formula bullets in the mean/SD/size instructions and the retained decision entry.

The z lesson's narrative transition is now the H3 informational heading `Setup for the T-Test:`.
It preserves the original section hierarchy while avoiding historical Part 2 structural metadata.
Its statistical-reference heading is H4 to maintain valid hierarchy. Offline compilation confirms
that the transition is an informational heading and does not increment Part/Step numbering.

## Narrow exceptions retained

- Historical Part/Step numbers use the approved standalone numbering. Technical worksheet headings,
  workbook tables and explicit semantic region/action metadata support generated standalone files.
- Setup describes the generated XLSX and actual sheets; copying supplied data remains a reset
  exercise. The original combined instructor workbook's third tab is described as historical.
  Old setup screenshots are not treated as current generated-workbook instructions.
- Population **parameter**, standard errors for the z statistic, sample **standard deviation** and
  `STDEV.S` correct original terminology. Known population SD determines z versus estimated-SD t;
  the original automatic n=30 rule remains corrected. Independence, approximate normality and
  outlier checks remain explicit. The national 7.5 lb value remains a fictional teaching benchmark.
- Estimating the mean constrains deviations to sum to zero, leaving n-1 independent deviations;
  this narrowly replaces the misleading original assertion that the mean is one fixed observation.
- Current supported normal/t formulas and cells remain unchanged. The t right-tail walkthrough uses
  `1 - T.DIST(E9, E10, TRUE)` rather than unsupported `T.DIST.RT`, with correct E9/E10 references
  and signed-statistic clarification. Two-tail/right-tail doubling remains direction-qualified.
- Welch uses type **3**, not the original incorrect type 2 description. Both data ranges end at 101.
  The Joe-greater branch retains the IF mean-difference guard because one-tail `T.TEST` uses magnitude.
  The implementation's `Alternative` branch markers remain alongside recovered authored prose.
- Both alternatives are explained, but students must prespecify the test. Causal claims remain
  qualified; failure to reject does not prove equal means. The national-comparison outcome remains
  nonsignificant, so Joe does not regain eligibility. Original humor remains around that correction.
- The duplicated original two-sample 6.3/7 decision entry stays consolidated. F6/G6 still share one
  numbered instruction. Original explanation is retained in the single decision sequence.
- Deliberate practice ranges still extend beyond the 24 supplied observations to row 40 or 101.

## Verification and remaining acceptance work

Directly reread original/current paragraphs and groups at every failed-source anchor. An offline
word comparison using `difflib.SequenceMatcher` additionally removed link wrappers and Markdown
punctuation and inspected original replacement/deletion runs of at least 12 words. The remaining
long runs concern standalone workbook setup, the corrected n=30 premise and consolidated duplicate
instructions; none represents a new unexplained prose deletion. This check supplements direct
reading; it does not establish generated-page fidelity.

All three sources pass `source source_me.sh && python3 make_tutorial.py lint <source>`. Remaining
warnings concern intentional spare practice rows; notes concern optional Google cell mappings.
Compiled action counts remain 64 label/enter operations (32 each) plus three worksheet directives.
No formula, scalar, worksheet coordinate or supplied data was changed by this recovery.

Reviewed source SHA-256 values:

| Source | SHA-256 |
| --- | --- |
| Babies 1 | `da64c65d64e160d9b7dc311b73afc7e28fefb38efdb45d9a34d9ed2704c1d5c1` |
| Babies 2 | `446256332bb144cc1ecbd2d0202043dc980a484ceee4ed28db4d624a6f76e96d` |
| Babies 3 | `c58d36f92c826a7625f5e371c65bad5ab5dca25148301117d69ac1504217db5f` |

Fresh independent source specification review and current-output build/page/workbook review remain
required. This report makes no PDF, workbook rendering, Google behavior or overall completion claim.
