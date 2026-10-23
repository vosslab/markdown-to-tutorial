# Microbes 4 and 5 original-paragraph recovery

This recovery rebuilt the Tutorial bodies directly from the read-only 2025 originals, rather than
editing the already shortened migration. The original instructional paragraphs, explanations,
numbered groups, nested action groups, emphasis, and descriptive heading words return. Workbook
source tables and current formula destinations remain unchanged. Semantic bindings wrap existing
visible text in the restored instructions.

## Deliberate exceptions

- Copy-data groups now open the delivered workbook instead of copying a legacy Google tab. The
  original source-workbook URL remains a reference. Existing observation counts and row-101 practice
  buffers remain; blanks are not zeros.
- F: distinguish variance from mean and species composition; keep the advisor's enthusiasm and
  questions, while removing causal conclusions the variance test cannot support. Add one concise
  independent-normal assumption paragraph and the repeated-site caveat. Explain F below/above 1,
  numerator-first degrees of freedom, both-tail minimum, and conditional F.TEST tail recovery.
- F: correct the claim that increasing df makes an F distribution normal; preserve the surrounding
  df explanation. Correct p-value, nonrejection, directional/two-tail inference, and increased-sample
  certainty statements in place. Preserve historical-thesis narrative, with narrow culture-detection
  and identification corrections and one method-confounding paragraph.
- ANOVA: preserve each original calculation/explanation paragraph. Correct the premature F/p-value
  paragraph in Step 10 to explain calculating F after mean squares. Correct I10 to I11 and M3 to M2,
  bound whole-column formulas to the existing row-101 practice ranges, and repair column A versus
  B:F descriptions, stray list item 5, and Step 8's incoherent item 2.
- ANOVA: state the right-tail omnibus mean hypothesis; replace claims of each-year decline,
  environmental causality, random-chance probabilities, or equality after nonrejection only where
  they occurred. Add one independent/common-variance/residual-normality assumption paragraph and
  one combined repeated-site/method-confounding paragraph.
- Original Step-by-Step Tutorial and Explanation headings remain informational. The F closing
  transition keeps its original Part 5 Setup title and its original Moving to ANOVA heading, with
  a structural Step prefix so the transition Part is nonempty. Semantic links preserve strong/code
  formatting; quoted entry labels keep their visible quotes outside the action payload.

## Direct original-to-current paragraph ledger

This compares original narrative paragraph blocks with current narrative blocks after removing
semantic-link wrappers, Markdown emphasis/code delimiters, harmless legacy escaping, and whitespace.
Lists, headings, tables, images, and URL-only paragraphs are excluded from this narrative count;
original nested/list structures were checked separately against the source during reconstruction.
An exact row means the whole original paragraph is retained. A corrected row points to its closest
current paragraph; each corresponds to the technical/scientific exceptions above, not permission
for general rewriting. All line numbers refer to the current source files, not generated output.

### microbes_4_f_test

19 of 44 original narrative paragraphs remain exact under the normalization above.
The remaining paragraphs retain their original location and instructional purpose with the documented
corrections. No original narrative paragraph is replaced by an unrelated summary.

| Original line and opening | Current line | Status |
| --- | --- | --- |
| 7: After comparing the microbial diversity in Busse Woods between 2014 | 51 | Corrected |
| 9: Excited by this idea, you present your findings to your | 53 | Corrected |
| 13: While the Two Sample T-test compared the means of microbial | 57 | Corrected |
| 39: Now, let us calculate the statistics needed for both datasets. | 96 | Exact |
| 56: Now, we will calculate the F-statistic to compare the variances | 113 | Exact |
| 64: The F-statistic is used to compare the variances of two | 121 | Corrected |
| 66: It is important to note that sample means are not | 123 | Exact |
| 68: This calculation will help determine whether the spread (variability) in | 125 | Corrected |
| 72: In an F-test, degrees of freedom are used differently than | 129 | Exact |
| 74: Step-by-Step Tutorial: | 131 | Exact |
| 83: In the F-test, the degrees of freedom (DF) represent the | 140 | Corrected |
| 85: These degrees of freedom are used to interpret the F-statistic, | 144 | Corrected |
| 87: In biological studies, where sample sizes are often small, the | 146 | Corrected |
| 91: In an F-test, you are testing whether the variances between | 150 | Exact |
| 98: For an F-test, you are no longer testing the mean | 157 | Corrected |
| 102: Now that you are working with two samples (2014 and | 161 | Exact |
| 104: You will perform both two-tailed and one-tailed tests (lower and | 163 | Exact |
| 108: The function F.DIST is used to calculate the cumulative distribution | 167 | Corrected |
| 118: The function F.TEST simplifies the F-test process by directly comparing | 177 | Exact |
| 124: The F.TEST function returns the p-value, which tells you whether | 183 | Exact |
| 128: This test checks if the variance in microbial diversity has | 187 | Exact |
| 142: In this two-tailed F-test, you are testing whether the variance | 201 | Exact |
| 146: This test evaluates whether the variance in microbial diversity is | 220 | Corrected |
| 156: In this one-tailed F-test, you are testing if the variance | 215 | Corrected |
| 161: This test evaluates whether the variance in microbial diversity is | 220 | Exact |
| 177: In this one-tailed F-test, you are assessing whether the variance | 236 | Exact |
| 179: The formula F.DIST.RT(E6^2 / E5^2) specifically tests if 2024 has | 238 | Corrected |
| 181: By testing both directions (with swapped ratios), you can confirm | 285 | Corrected |
| 185: In hypothesis testing, the decision to reject or fail to | 244 | Corrected |
| 206: The IF statement simplifies decision-making by evaluating whether the p-value | 265 | Corrected |
| 208: This automated process ensures that you can efficiently assess whether | 267 | Corrected |
| 212: You have just conducted the F-test to compare the variance | 271 | Exact |
| 222: The interpretation depends on comparing the p-value to the significance | 281 | Corrected |
| 224: If the p-value is greater than 0.05, you fail to | 220 | Corrected |
| 226: By interpreting the results of the F-test, you can assess | 285 | Corrected |
| 243: After conducting the F-test comparing microbial diversity in 2014 and | 309 | Corrected |
| 245: As you think about this, an idea strikes. You recall | 311 | Exact |
| 247: Without DNA sequencing, these students used plate counts and staining | 313 | Corrected |
| 249: These methods, while labor-intensive, provided valuable estimates of microbial diversity. | 315 | Corrected |
| 251: Inspired by this, you explore three theses from 1994, 2004, | 319 | Corrected |
| 253: With all the data in hand, you can now analyze | 321 | Exact |
| 257: ANOVA allows for the comparison of multiple groups simultaneously, unlike | 325 | Exact |
| 259: This analysis will reveal whether diversity declines started earlier or | 220 | Corrected |
| 261: ...Ask the instructor for the next tutorial link. | 329 | Exact |

### microbes_5_anova

21 of 34 original narrative paragraphs remain exact under the normalization above.
The remaining paragraphs retain their original location and instructional purpose with the documented
corrections. No original narrative paragraph is replaced by an unrelated summary.

| Original line and opening | Current line | Status |
| --- | --- | --- |
| 7: After successfully rejecting the null hypothesis using the F-test, you | 53 | Corrected |
| 9: To analyze how microbial diversity has shifted over time, you | 55 | Corrected |
| 13: ANOVA is ideal for comparing more than two groups, making | 59 | Corrected |
| 40: In this step, we will set up a traditional ANOVA | 85 | Exact |
| 72: The first step in an ANOVA test is to calculate | 117 | Exact |
| 76: We will set up another table to organize the group | 121 | Exact |
| 109: This step focuses on calculating the group statistics: the means, | 154 | Exact |
| 111: These statistics will feed into the next step, where we | 156 | Exact |
| 115: In this step, you will calculate the grand mean, which | 160 | Exact |
| 124: In this step, you will calculate the Degrees of Freedom | 169 | Exact |
| 134: The Degrees of Freedom (DF) reflect the number of independent | 179 | Exact |
| 140: The relationship between these degrees of freedom is: DF Total | 185 | Exact |
| 144: In this step, you will calculate the Regression Sum of | 189 | Exact |
| 153: The SSR quantifies the variation between the group means and | 198 | Exact |
| 155: The SUMPRODUCT function multiplies corresponding elements from two arrays and | 200 | Corrected |
| 159: In this step, you will calculate the Error Sum of | 204 | Exact |
| 167: The SSE quantifies the variability within the groups that is | 212 | Exact |
| 171: In this step, you will calculate the Total Sum of | 216 | Exact |
| 179: The Total Sum of Squares (SST) measures the overall variance | 224 | Exact |
| 184: The relationship between these terms is: SST = SSR + | 229 | Exact |
| 186: By calculating the SST, you quantify the total variability in | 231 | Exact |
| 190: The mean square (MS) is calculated by dividing the sum | 235 | Exact |
| 199: The mean squares (MS) are the average variability per degree | 244 | Exact |
| 203: Now that you have calculated the F-statistic, the next step | 248 | Corrected |
| 211: The F-statistic is the ratio of the between groups variance | 256 | Corrected |
| 215: Now that the F-statistic has been calculated, we can determine | 260 | Corrected |
| 223: The F.DIST.RT function calculates the right-tailed probability of the F-distribution. | 268 | Exact |
| 229: The result of this function gives us the P-value, which | 274 | Corrected |
| 233: In hypothesis testing, the decision to reject or fail to | 278 | Corrected |
| 245: The IF statement evaluates whether the p-value (in M3) is | 289 | Corrected |
| 247: This process simplifies the interpretation of your ANOVA results, ensuring | 291 | Exact |
| 251: Now that you have calculated the ANOVA results, the next | 295 | Corrected |
| 261: The interpretation hinges on comparing the p-value to the significance | 305 | Corrected |
| 263: If the p-value is greater than 0.05, you would fail | 307 | Corrected |

## Validation and remaining output review

`source source_me.sh && python3 make_tutorial.py lint` passes both files with zero errors after
the shared compiler fixes landed. Both files compile into action models: 36 F actions and 51 ANOVA
actions including worksheet selection; formulas target the existing cells. Original Step-by-Step
headings and code-format destination references no longer produce false diagnostics.

Workbook role regions are disjoint: ANOVA L2:M2 carries the F/p-value results, H14:I14 the decision,
and H16:I16 the interpretation; alpha H13:I13 is calculation. F p-values D16:G18 and decisions
D22:E24 are results, alpha D20:E20 is calculation, and D26:E26 is interpretation. Source data tables
remain intact. No workbook-cell moves were made.

Remaining warnings are intentional spare rows through 101 (F: 10 unavailable-input plus 10
range-overshoot; ANOVA: 18 plus 18), two ANOVA SUMPRODUCT compatibility notes, and the optional
unmapped-Google-link note for each lesson. Their source ranges are documented practice buffers.

This is source-comparison evidence, not rendered fidelity acceptance. No LibreOffice command was
run, no output bundle was rebuilt, and no PDF/workbook visual or spreadsheet-engine calculation
claim is made here. Fresh output review remains part of the manager's integration phase.
