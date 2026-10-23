# Babies source fidelity specification review

Verdict: **FAIL - source restoration remains incomplete.** This is an independent source review,
not acceptance of the restoration summary or generated PDF layout. Much of the original prose has
returned, but good explanatory content and list hierarchy remain missing, and one transition heading loses its hierarchy.

## Evidence and method

Reviewed all prose, instructions, headings, and nested groups in these direct pairs:

- `2025_Artifacts/Fried_Foods_1_Z-Test_Tutorial_Guide_Fall_2025.md` versus
  `tutorial_data/babies_1_z_test.md`.
- `2025_Artifacts/Fried_Foods_2_T-Test_Tutorial_Guide_Fall_2025.md` versus
  `tutorial_data/babies_2_t_test.md`.
- `2025_Artifacts/Fried_Foods_3_Two-Sample_T-Test_Tutorial_Fall_2025.md` versus
  `tutorial_data/babies_3_two_sample_t_test.md`.

Read the active instructional voice plan, repository rules, Markdown/Python styles, original
comparison report, and numbering contract in `docs/TUTORIAL_SPEC.md`. Original Markdown is the
wording authority; the restoration report is not evidence of fidelity. An offline Python
`difflib.SequenceMatcher` word comparison removed embedded image data, workbook inventory, action
link wrappers, and Markdown decoration to expose prose deletions/replacements. Direct line review
then checked grouping that word comparison cannot detect. Python ran through
`source source_me.sh && python3`. `compile_document` checked actual generated heading numbers.
No LibreOffice commands or PDF review were performed.

Reviewed source hashes:

| Source | SHA-256 |
| --- | --- |
| Babies 1 | `df9fbe42b807359485ddd6608841a50f9e18a94df01695aebce5055a942553f4` |
| Babies 2 | `2d7879bc3ddb3b2591c8d417e5ff2db72f83704693bf7b12218b5100b9ace568` |
| Babies 3 | `dbcf313f5b837df0a5da46aa5ad5b7b1112ad696a592f0ef5a4d56d3bc8ecd3b` |

Sources are being edited concurrently. Line references describe this reviewed state; headings and
quoted text are the durable anchors. This reviewer edits only this report.

## Required corrections

### 1. Preserve descriptive heading hierarchy

Standalone Part/Step/Substep numbering is approved; historical Part 2/3 and Step 0 numbers are not
required. Offline compilation confirms coherent standalone sequences for all three lessons.

The z lesson's original `Part 2 Setup:` is now a bold paragraph, absent from compiled headings.
Restore it as an informational heading with a standalone-valid title/prefix and the original
transition's hierarchy. It remains a narrative setup for the next lesson, not a workbook operation.

Two-sample `Important Notes:` became `Important notes`; preserve original case and punctuation.
A generic Markdown style preference does not authorize changing an existing author's heading.
These case/punctuation differences are minor; the missing transition heading is substantive.

### 2. Restore the z lesson's conceptual formula and nested explanation groups

Original z Step 4, line 71:

> Formula: (sample mean - population mean) / [ population standard deviation / sqrt(sample size) ]

This correct conceptual formula is entirely absent from current lines 167-170. Restore it before
the spreadsheet entry, in the original nested group. It explains the statistic in words and is
not a duplicate spreadsheet action/formula listing.

Original Step 3 uses nested `Enter:` and explanation bullets under each numbered E5/E6/E7
instruction. Current lines 145-162 concatenate formula and explanation as unmarked continuation
text. Restore the original nested actions and explanation grouping, keeping `STDEV.S` and the
correction from "sample mean" to "sample standard deviation". Restore original E5 wording
"we will use" instead of the unnecessary shortened "use".

Original 5.2 has numbered top-level branches `1. Two-Tailed Test` and `2. One-Tailed Test`, each
with two child bullets. Current lines 198-203 reverse this to top-level bullets and numbered
children. Restore authored numbering/nesting around the existing correct semantic bindings.

Original Step 6 items 4 and 6 each contain a nested "Using the **two-tailed test** p-value ...,
enter the formula:" instruction, followed by its formula. Current lines 223-229 flatten these
into a sentence and formula continuation, removing emphasis and "the formula". Item 7 originally
reads `Explanation:` followed by three explanation bullets; current lines 230-233 merge everything
into one item. Restore the original numbered parent and nested explanations.

Original Step 7's two example interpretations are child bullets, not numbered children. Current
lines 239-244 number them. Restore their authored grouping; "write a brief interpretation" also
became "write your own brief interpretation" without a technical reason.

### 3. Restore one-sample t instruction groups and the complete right-tail explanation

Original Steps 3-6 each place `Enter:` and any formula explanation in nested bullets beneath the
numbered cell instruction. Current lines 165-187 flatten these. Original Step 7 similarly has
"calculate the degrees of freedom using:" followed by a nested entry and nested "Here, E5 is the
sample size..." explanation. Current lines 192-193 collapse all three into one paragraph. Restore
the source grouping and wording while keeping semantic links around the existing visible actions.

Original 8.2 uses numbered parent items `1. Determine the Type of Test` and
`2. Calculate the P-Value`. Current lines 226-231 turn both into bullets. Restore the numbered
parents and original nested `Enter:`, formula explanation, and `Explanation:` bullets in each branch.

Original right-tail branch includes:

> Explanation: The T.DIST.RT function tests the probability of observing a value as extreme or
> more extreme in one direction (greater than the population mean).

Current lines 243-247 replace the entire formula explanation group with a signed-statistic warning,
losing the original extreme-or-more-extreme explanation. Keep `=1 - T.DIST(E9, E10, TRUE)` and its
signed-statistic clarification, but restore the original explanatory sentence narrowly adapted to
that supported formula (and correct E9/E10 references). Neither formula portability nor sign
correction requires dropping the explanation of what the p-value measures.

Original Step 9's two decision entries have nested "Using the **two-tailed test** p-value ...,
enter the formula:" / one-tailed counterparts. Current lines 267-276 flatten them as in the z
lesson. Restore source grouping and emphasis.

Original scenario's "This time, he must:" has two bullets; current lines 122-124 turn these into a
numbered list. Restore the source bullets. The original setup item D2 says "it should say";
current line 153 says "enter" despite using a label binding. Retain the original visible wording.

### 4. Restore the two-sample 6.2 function walkthrough comprehensively

The two-sample 6.1 explanatory paragraphs and nested example hypotheses are now substantially
restored. Accept that portion as a faithful restoration; do not replace it with shorter summaries.
The following adjacent 6.2 changes still fail:

- Original lines 80-88 begin "The syntax of the T.TEST function is:", then a syntax bullet,
  then "Here's how you'll set up the formula:" with nested Range1, Range2, Tails, and Type entries.
  Current lines 161-166 replace this with "Its syntax is" and a flatter shorthand list.
- Original Tails entry says "This specifies if the test is **one-tailed** or **two-tailed**", then
  separate child bullets "Enter **1** for a **one-tailed test**" and
  "Enter **2** for a **two-tailed test**." Current source compresses this to
  "Tails: Enter 1 for a one-tailed test or 2 for a two-tailed test." Restore original explanation,
  emphasis, and nesting.
- Original Type entry begins "This specifies the type of t-test. Use **2** to indicate that you
  are performing a **two-sample t-test with unequal variances** (Welch's t-test)." Restore that
  sentence with **3** substituted for **2**, rather than the current shortened "Use 3 for ...".
- Original two-tail branch has a formula bullet and `Explanation:` with three nested bullets:
  ranges for each hospital, meaning of the first 2, and meaning of the final type argument.
  Current lines 168-171 omit the ranges explanation entirely and compress the argument
  explanations into one sentence. Restore the original three-bullet explanation, correcting the
  final argument to 3. Retain current valid ranges B2:B101 and C2:C101.
- Original one-tail branch's `Explanation:` group should remain a group, with only its incorrect
  directional claim corrected. Keep the signed conditional formula and clear explanation of
  `T.TEST` magnitude behavior. Restore the explanation of the `1` tails argument and explain the
  `IF` guard without compressing away the authored walkthrough.

Keep branch headings compatible with the implemented alternative-branch model. The required
`Alternative` marker is a technical adaptation; it does not justify deleting good branch prose.
Keep combined F6/G6 label/value instruction as one numbered item, as in original lines 107/115.
Current lines 198-199 do preserve that combined group. Do not split it into separate action entries.

## Changes that should remain

The following are justified narrow exceptions or useful retained original content, not failures:

- Known population SD versus estimated SD, standard errors rather than standard deviations for the
  sample-mean statistic, no automatic n=30 rule, small-sample assumptions, and no causal conclusion.
- The corrected one-sample t ending and two-sample Joe transition: the supplied national comparison
  does not show a significant increase. Restore surrounding humor, not a false victory.
- Standalone generated workbook setup, actual sheet names, seeded headings, copied-data reset
  instructions, and flexible blank practice ranges.
- Correct supported normal/t formulas, signed right-tail handling, Welch type 3, corrected ranges
  and cell references. Never restore type 2 while describing unequal variances.
- Prespecified alternatives and qualification of the relationship between one-tail/two-tail p-values.
- Removing duplicated original two-sample 6.3/7 decision entries is justified. Preserve the useful
  wording in the single retained decision step; entering the same action twice is unnecessary.
- Most original opening/narrative prose, the z-statistic note, one-sample degrees-of-freedom
  explanation, all three practice bullets, and two-sample 6.1/important-notes prose are present.
  Do not rewrite these because they could be shorter or because the scenario is fictional.

One scientific sentence in the restored degrees-of-freedom block merits a narrow correction:
"one of the values (usually the mean) is fixed based on the rest of the data" conflates the mean
with an observation. Explain that estimating the mean constrains the deviations to sum to zero,
leaving n-1 independent deviations. Preserve the rest of the original paragraph.

## Acceptance boundary

Recheck all original paragraphs and list groups after the concrete fixes above, using final source
hashes. Then build and inspect actual student pages and workbooks in the authorized LibreOffice
lane. This source report makes no PDF layout or workbook-rendering acceptance claim. The separate
bold-label parsing work is deliberately not duplicated as a finding here.
