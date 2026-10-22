# Established lessons: cognitive walkthrough

## Finding

The eight lessons support completion of their assigned analyses from the supplied blank student
workbooks. I found one substantive teaching mismatch: Babies 1's story celebrates a conclusion its
Z-test does not support. The correction needs one sentence, preserving Joe's mistake, the award,
the committee letter, and the protest scene. No other task-completion blocker emerged.

This is a fresh expert cognitive walkthrough, not a student experiment or an observation of the
Google Sheets interface. I applied the HCI and humanizer skills to the actual rebuilt DOCX, PDF,
and XLSX files. The accepted established-teaching specification was the scope boundary; I did not
replace the author's narrative or require a different instructional style.

## Task and evidence

The learner is a BIOL 318/418 student who can open a supplied workbook and enter a formula but
is learning which statistical question, calculation, and interpretation belong together. The task
starts with the generated XLSX and the finished lesson, and ends with the original-data analysis
and an interpretation in the stated cell. Success requires the correct worksheet, untouched raw
observations, the stated tail, usable intermediate calculations, and a conclusion supported by the
result. Practice changes follow the original analysis.

At each decision I asked whether the student could recognize the immediate goal, find the named
worksheet/cell, select the correct action, recognize the expected result, and recover using the
checks actually stated. I read every generated DOCX in instruction order, checked its workbook
destinations and dependencies, and populated ignored copies from those visible instructions. Both
Babies 3 alternatives were walked separately; the other lessons calculate their comparison tails
in one path. Interpretation cells were filled in the copies. The action ledgers retain the
referenced-cell state before formula entry. This was not a replay of the compiler's action list.

I reused the final rebuild's Calc results for the numeric response, comparing those numbers with
the visible formulas and prose. I did not run a new spreadsheet engine or claim that writing
formulas with openpyxl recalculates them. All eight original workbooks were inspected directly:
their raw observations are present and their calculation areas have no prefilled formulas.
The existing Calc evidence is final-state execution evidence; intermediate Google Sheets behavior
and measured student comprehension remain unobserved.

All 44 current PDF pages were freshly rendered and viewed in contact sheets. The restored figures,
Welch table, long formulas, and important page transitions were also viewed at readable page size.
Current page counts are Babies 1-3: 6, 7, 3; Microbes 1-5: 5, 5, 7, 5, 6. These are the rebuilt
outputs, not the older 45-page set described in the specification report.

## Completed walkthroughs

| Lesson | Visible path and workbook evidence | Recognition, feedback, recovery, and judgment |
| --- | --- | --- |
| Babies 1 | PDF pp. 1-5, Steps 1-7; `Part 1 National Z-Test`, data B2:B25, supplied D1/E1, E2/E3 then E5:E9, E11/E12, E14/E16/E17, interpretation E19. n=24, mean=7.80792, Z=1.00565; right p=0.15729, two-tail p=0.31458; both fail to reject. | The named working tab, copy/reset explanation, seeded-header check, and after-entry table make setup recognizable. Sample SD is explicitly unused. Right-tail reporting is fixed by Joe's claim, while both comparison results remain available. The IF explanation supplies the correct decision. **Substantive mismatch on p. 6:** Joe celebrates as though the result proved heavier babies. Make his misreading explicit; see the minimal fix below. The hospital, normal curve, and protest figures remain visible. |
| Babies 2 | PDF pp. 1-7, Steps 1-10; `Part 2 National T-Test`, the same 24 observations, D1/E1 and E3="not used" supplied. E2 then E5:E7, E9/E10, E12/E13, E15/E17/E18, interpretation E20. t=1.04305, df=23; right p=0.15388, two-tail p=0.30776; both fail to reject. | The standalone-workbook instruction resolves the original return-to-Part-1 handoff. The check table explains E3, so a student does not substitute the national SD into t. The df discussion and signed-tail warning explain what the formulas mean. The closing story explicitly gives p about 0.154 and denies Joe's preferred ending. Accept. The lightly occupied final page and remaining original emotional language do not obstruct the task. |
| Babies 3 | PDF pp. 1-3, Steps 0-8; `Fried Foods vs Green Veggies`, complete A1:C25 and blank F:H. Each path records its alternative before summaries. G2/H2 means 8.05792/7.65667, SDs 1.47634/0.75585, n=24/24. Separate G5 formulas yield two-tail p=0.24410 or Joe-greater p=0.12205; G7 fails to reject and G8 states the chosen conclusion. | The learner can identify the independent groups and Welch type 3. The two alternatives intentionally share F5/G5; the instruction to use the preselected alternative makes these choices rather than consecutive overwrites. The sign-aware right-tail formula avoids a false directional conclusion. The final caution distinguishes insufficient evidence from equality and diet causation. Accept both branches. The old 6.2/6.3 numbering is cosmetic; no action is missing. |
| Microbes 1 | PDF pp. 1-5, Steps 1-8; `Microbial Z-Test`, A:B data with supplied C1/D1. D2/D3 precede D5/D6, D8, D10:D12, D14:D17, interpretation D19. n=24, Z=-1.65817; lower p=0.04864 rejects, two-tail p=0.09728 does not. | The benchmark, known SD, lower alternative, and count check precede formulas. The lower-tail figure is explicitly an illustration rather than this result. The worked interpretation identifies both different decisions and their different questions, giving a novice a useful discrepancy check. Practice keeps SD fixed and separates hypothetical changes from evidence. Busse Woods context, recap, and supervisor transition survive. Accept. |
| Microbes 2 | PDF pp. 1-5, Steps 1-9; `Microbial T-Test`, A:B data and C:D blank calculations. D2, D4:D6, D8/D9 precede D10:D12 and alternate E10/E12; then D14:D17 and interpretation D19. n=24, t=-1.10438, df=23; lower p=0.14043, two-tail p=0.28085, higher p=0.85957; all fail to reject. | Each destination is named, sample SD and df precede their uses, and the equivalent alternate probabilities are explained. The numeric ending makes the change from the stipulated-SD Z result understandable rather than promising confirmation. The image, advisor's next question, and four takeaways remain. Accept. |
| Microbes 3 | PDF pp. 1-7, Steps 1-9; `Two Sample T-Test`, complete A:C and D:E headers. E2/E3, E5/E6, E8/E9 precede E11=-1.91452 and E13=39.49524; E16/E17/E18 give 0.06282/0.03141/0.96859; E22/E23/E24 then E26. All alternate checks match these results. | The sign convention is explicit, fractional df are preserved, the beta method is explained, and direct Welch calculations offer a stated check. F16 initially references empty E17/E18, but the lesson specifically says it updates after those entries; this is explained deferred feedback, not a hidden dependency failure. Repeated table headers make the pp. 3-4 Welch examples readable, and the df curves are clearly reference distributions. The contextual forest image is bounded by its caption. Accept. |
| Microbes 4 | PDF pp. 1-5, Steps 1-9; `Two Sample F-Test`, A:C observations and supplied D1/E1. E5/E6 and E8/E9 precede E11=0.42265, E13/E14=23/23, E16:E18=0.04413/0.02207/0.97793; E20/E22:E24 precede interpretation E26. G16/G17 and F18/G18 agree with their primary values. | The student is told why means are unnecessary and why numerator df comes from 2024. Reciprocal-ratio and complement checks support error recovery without implying independent evidence. The conclusion concerns index variance, rather than taxonomic homogenization. The title figure, spread question, recap, and older-thesis transition are present. Accept. |
| Microbes 5 | PDF pp. 1-6, Steps 1-13; `30 Year ANOVA Test`, A:F observations, G1 separator, empty H:M results. Group table I7:M9 gives counts 10/15/20/24/24; grand mean I11=4.14244 precedes sums of squares. I2:I4=4/88/92; SSR/SSE/SST=4.73937/118.62881/123.36818; L2=0.87893, M2=0.47999; I14 fails to reject and I16 interprets. | Each table header and destination is named before use. The count total, df identity, and weighted-grand-mean explanation help diagnose common mistakes. Sums of squares precede mean squares and the F ratio; the right tail is distinguished from Part 4's variance test. The final numeric interpretation prevents a false time-trend claim. The older-thesis context and method/year confounding are explained rather than erased. Accept. |

## Minimal correction and accepted limits

Babies 1, p. 6, opening of "Looking ahead": change the opening sentence so Joe explicitly mistakes
the higher sample mean for proof despite the nonsignificant Z result. For example:

> Joe mistook the higher sample mean for proof, ignoring the nonsignificant Z-test result, and was
> certain that his hospital's babies were the heaviest in town.

This repairs recognition of a correct result without replacing the author's story. The coordinator
has assigned the sentence correction and its rebuild; the snapshot reviewed here precedes that
small change. No other content rewrite is needed from this walkthrough.

The ecological sampling provenance is unknown. The hypothetical independence assumption is
acceptable for this method exercise; it does not verify independence or authorize real field-study
inference. The same-site warning and culture-versus-sequencing qualification are necessary limits,
not unresolved reasons to block the teaching task. Babies 2's large-sample t/Z comparison is
ordinary teaching shorthand in its known-versus-estimated-SD context; it needs no extra rewrite.

No timed success rate, observed novice behavior, accessibility conformance, Google account flow,
or Google Sheets recalculation is claimed. Exact cells, original-data numeric results, visible
checks, readable current PDFs, and coherent interpretation support this expert-inspection finding.

## Retained evidence

Ignored evidence is under `tutorial_output/verification/teaching_review/established_quality/`:

- `manifest.txt`: SHA-256 values for the inspected DOCX/PDF/XLSX files and current page counts.
- `*_docx.txt`, `*_pdf.txt`, `*_workbook.txt`: actual artifact text and occupied-cell inventories.
- `*_page_*.png`, `*_contact.png`: freshly rendered current pages and whole-lesson contact sheets.
- `*_action_ledger.txt`, `*_visible_entries.xlsx`: nine visible-instruction walkthrough paths,
  including both Babies 3 branches and completed interpretation entries.
- `*_existing_calc_results.txt`: relevant existing Calc results, extracted without rerunning it.
- `original_prose.txt`: direct Fall 2025 source prose with embedded image data definitions removed
  for comparison; the original artifacts remain unchanged.

No product source, original artifact, permanent test, or shared documentation was edited in this
review. The report and ignored review evidence are the only deliverables.
