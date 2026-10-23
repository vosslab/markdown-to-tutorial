# Microbes 1-3 original prose recovery

Recovery validation on 2026-10-22: all three `make_tutorial.py lint` commands pass using
`source source_me.sh && python3`. Remaining diagnostics are the intentional B2:B101/C2:C101
practice-range spare rows and Microbes 3 F16's forward references to E17/E18; that formula's
original instructional location is retained and its update order explained. Google mappings are
optional and absent. No LibreOffice command or deliverable build was run by this source editor.

Direct compiler inspection confirms 25, 29 and 38 actions respectively, including 9, 13 and 19
formula entries. All three alpha entries are numeric 0.05. Labels have clean cell values while
their original quotation marks, punctuation and bold appearance remain outside semantic spans.
The three Welch p-value labels D16:D18 are actions. Each workbook declares six disjoint semantic
regions. Microbes 1 retains eight original numbered steps and three p-value substeps; Microbes 2
and 3 each retain nine steps and three p-value substeps. Each retains the original three practice
items and its original three or four numbered takeaways.

The omission review compared every original non-setup prose paragraph with the restored body,
including all tail-probability walkthroughs, IF explanations, interpretation explanations,
practice and takeaway lists, the supervisor's email, the advisor's suggestions and all transitions.
The Step 1 setup paragraph and tab-copy instructions are the only instructional block replaced
for the generated-workbook workflow. Original base64 image data are represented by the current
extracted images. Scientific exceptions below change the incorrect sentence/phrase and keep the
surrounding original paragraphs. Rendered-product review remains the integrator's next step.

The Tutorial bodies below were rebuilt from the original 2025 Markdown, not from the
previous abbreviated restoration. Original paragraphs, numbered groups, nested instruction
bullets, explanations, practice tasks, takeaways, and next-part story sections are retained.
Workbook tables remain the current complete 24-location observations. This report records
the exact sentence/phrase exceptions as well as structural and technical adaptations.

## microbes_1_z_test.md

### Exact wording exceptions

- Original: leading to a decline in microbial diversity
  Restored correction: leading to a possible decline in microbial diversity
- Original: we can determine if external pressures, such as pollution or habitat fragmentation, are reducing the biodiversity of the soil
  Restored correction: we can ask whether microbial diversity is lower than the benchmark; this comparison cannot identify an environmental cause
- Original: with typical values ranging from 1.5 to 4.5 in ecological studies
  Restored correction: with no universal upper bound independent of community size and logarithm base
- Original: The primary goal of this study
  Restored correction: The primary goal of this exercise
- Original: which represents the average microbial diversity for similar ecosystems
  Restored correction: which is stipulated for similar ecosystems in this exercise
- Original: The known population standard deviation for microbial diversity in similar ecosystems is 0.6.
  Restored correction: The population standard deviation for microbial diversity in similar ecosystems is stipulated to be known and equal to 0.6.
- Original: to investigate whether urbanization has significantly reduced the microbial diversity at **Busse Woods**
  Restored correction: to investigate whether microbial diversity at **Busse Woods** is lower than the benchmark
- Original: Microbial diversity in the forest preserve is consistent with the known average (Shannon Index \= 4.0).
  Restored correction: The population mean microbial diversity in the forest preserve is at least the benchmark (Shannon Index >= 4.0).
- Original: Microbial diversity in the forest preserve is significantly different from the known average.
  Restored correction: The population mean microbial diversity in the forest preserve is lower than the benchmark (Shannon Index < 4.0).
- Original: (the known average microbial diversity for similar ecosystems)
  Restored correction: (the stipulated benchmark for similar ecosystems)
- Original: (the known population standard deviation for microbial diversity in ecosystems)
  Restored correction: (the stipulated known population standard deviation)
- Original: mean of weights
  Restored correction: mean of Shannon Index values
- Original: into units of standard deviation
  Restored correction: into units of standard error
- Original: which is the probability that the microbial diversity is significantly lower than the benchmark
  Restored correction: which is the probability, under the null model, of a Z-statistic this low or lower
- Original: representing the probability of microbial diversity being **higher** than the benchmark
  Restored correction: representing the probability, under the null model, of a Z-statistic this high or higher
- Original: meaning the microbial diversity is considered similar to the benchmark
  Restored correction: meaning there is insufficient evidence of a difference; this does not establish equality
- Original: This could suggest a reduction in biodiversity due to urbanization or other environmental pressures.
  Restored correction: This comparison does not identify whether urbanization or other environmental pressures caused a difference.
- Original: This could indicate that environmental factors, such as urbanization, have negatively affected the biodiversity in the area.
  Restored correction: This does not establish that environmental factors, such as urbanization, caused the difference.
- Original: In this case, you conclude that microbial diversity in Busse Woods is either **equal to or within the expected range** for ecosystems similar to the benchmark. This suggests that the biodiversity in the forest preserve may not have been significantly impacted by external factors.
  Restored correction: This does not establish equality with the benchmark or rule out an effect of external factors.
- Original: whether microbial diversity in Busse Woods has been affected based on your hypothesis test results
  Restored correction: whether the data provide evidence of lower microbial diversity in Busse Woods based on your hypothesis test results
- Original: Think about how a larger sample size leads to more robust conclusions, while extreme individual values might skew the results.
  Restored correction: Think about how a larger representative independent sample can reduce the standard error, while extreme individual values might skew the results; more data do not guarantee a smaller p-value or repair biased sampling.
- Original: B2:B100
  Restored correction: B2:B101
- Original: the diversity was significantly different from the benchmark
  Restored correction: the diversity was significantly lower than the benchmark in the preselected lower-tail test
- Original: More importantly, your sample size was relatively small (N <= 30). For smaller samples, a Z-test is not reliable. You should be using a T-test, which accounts for the extra uncertainty when estimating the population standard deviation from your sample data.
  Restored correction: The key question is whether the population standard deviation is truly known, not whether N is below 30. If it is unknown, you should be using a T-test, which accounts for the extra uncertainty when estimating the population standard deviation from your sample data.
- Original: This new approach will take into account the smaller sample size and the uncertainty in estimating the population standard deviation.
  Restored correction: This new approach will take into account the uncertainty in estimating the population standard deviation.
- Original: The **T-test** adjusts for the extra uncertainty when using a small sample, making it a more robust test for this kind of ecological data.
  Restored correction: The **T-test** adjusts for the extra uncertainty when estimating the population standard deviation from the sample, under the stated sampling assumptions.
- Original: NORM.S.DIST(ABS(D8))
  Restored correction: NORM.DIST(ABS(D8), 0, 1, TRUE)
- Original: NORM.S.DIST(-ABS(D8))
  Restored correction: NORM.DIST(-ABS(D8), 0, 1, TRUE)
- Original: NORM.S.DIST(D8)
  Restored correction: NORM.DIST(D8, 0, 1, TRUE)
- Original: NORM.S.DIST(-1)
  Restored correction: NORM.DIST(-1, 0, 1, TRUE)
- Original: gives the cumulative probability of observing a Z-statistic that's at least as extreme as the one **you've calculated**, but for only **one side** of the distribution
  Restored correction: gives the cumulative probability to the left of the absolute Z-statistic **you've calculated**
- Original: To calculate the **upper tail** probability (the area to the right of the positive Z-value), we subtract this cumulative probability from **1**.
  Restored correction: The complement of this illustrated cumulative probability is the area to the right of -1. For our two-tailed calculation, instead subtract the cumulative probability at **ABS(D8)** from **1** to obtain the upper tail beyond the positive magnitude.
- Original: IF(D11 <= D13,
  Restored correction: IF(D11 <= D14,
- Original: IF(D12 <= D13,
  Restored correction: IF(D12 <= D14,
- Original: \[is/is not\] significantly lower
  Restored correction: \[provides/does not provide\] sufficient evidence of a population mean lower
- Original: indicating that microbial diversity in Busse Woods \[provides/does not provide\]
  Restored correction: indicating that the data \[provide/do not provide\]
- Original: D14: **"0.05."**
  Restored correction: D14: numeric 0.05 with punctuation outside the action

### Technical and structural exceptions

- Retained current title, workbook data, worksheet name, formula/cell destinations and source assets.
- Step 1 replaces obsolete create/copy-tab instructions with generated-workbook open/select/inspect instructions; original data-column description and source workbook link remain.
- Original heading levels and accidental heading markers become semantic Part/Step/Substep prefixes; descriptive wording and explanatory subheads remain. Standalone Part numbering starts at 1. The next-lesson Setup heading keeps its descriptive words as an informational heading, omitting its historic numbered Part prefix.
- Formula actions use current validated formulas in their original instruction locations; semantic links wrap original visible label/value/formula spans without splitting paragraphs.
- Added one scenario-assumption paragraph, explicit directional hypotheses, source-range/count note, and separate-copy practice instruction.
- Added disjoint source, calculation, result and interpretation workbook regions.

### Omission review

- All original non-setup prose paragraphs and original instruction groups originate in the restored body. No explanation, practice, takeaway, email, advisor dialogue or transition section was intentionally omitted.
- Base64 image definitions are replaced by current extracted image files. Original empty image headings are removed.
- Scientific sentence/phrase replacements are enumerated above rather than described as blanket permission to rewrite.

## microbes_2_t_test.md

### Exact wording exceptions

- Original: (the known average microbial diversity for similar ecosystems)
  Restored correction: (the stipulated benchmark for similar ecosystems)
- Original: The T-test is specifically designed to handle smaller **sample sizes** and the uncertainty that comes from estimating the population standard deviation.
  Restored correction: The T-test accounts for the uncertainty that comes from estimating the population standard deviation; a small sample size alone does not determine which test to use.
- Original: indicating possible biodiversity loss due to urbanization
  Restored correction: without identifying the cause of any difference
- Original: In short, two reasons:
  Restored correction: The defining reason and a related consideration:
- Original: * **Small Sample Size**
  Restored correction: * **Small Sample Size** makes the uncertainty from estimating SD especially important; it is not a separate criterion for choosing a t-test.
- Original: This uncertainty makes the **T-test** the best fit. The **sample size** in your study is small (fewer than 30 samples), and the **T-test** accounts for extra variability from smaller datasets, providing a more accurate result under these conditions.
  Restored correction: This uncertainty makes the **T-test** appropriate under the stated assumptions. The **sample size** in your study is small (24 samples), and the t-distribution accounts for the uncertainty from estimating the population standard deviation; it cannot repair biased or dependent observations.
- Original: one of the values-typically the mean-is fixed based on the rest of the data
  Restored correction: the deviations from the estimated sample mean must sum to zero, leaving only n - 1 independently varying deviations
- Original: In this step, we will calculate p-values, which help us understand how likely it is that the difference between the sample data and the benchmark is due to random chance.
  Restored correction: In this step, we will calculate p-values: probabilities, under the null model and its assumptions, of results at least as extreme in the specified tail or tails. A p-value is not the probability that the null hypothesis is true or that chance caused the difference.
- Original: **T.DIST** for flexible cumulative probability, and **T.TEST** for a direct statistical test
  Restored correction: **T.DIST** for flexible cumulative probability
- Original: **cumulative** is set to **FALSE**
  Restored correction: **cumulative** is set to **TRUE**
- Original: This test will help you determine if environmental factors, such as urbanization, have reduced biodiversity.
  Restored correction: This test compares diversity with the benchmark without identifying an environmental cause.
- Original: The **T.DIST.RT** function is typically used for **right-tailed tests**, but in this case, it is useful for testing **lower values**. **T.TEST** simplifies the process by allowing a one-tailed test with tails set to **1**.
  Restored correction: Use the signed T-statistic so that a positive statistic gives a large lower-tail probability. T.TEST requires two samples and is not used for this one-sample benchmark test.
- Original: `=T.DIST.RT(D8, D9)`
  Restored correction: `=1 - T.DIST(D8, D9, TRUE)`
- Original: `=1 - T.DIST(D8, D9, TRUE)`

#### Explanation for One-Tailed Test (Higher)
  Restored correction: `=T.DIST(-D8, D9, TRUE)`

#### Explanation for One-Tailed Test (Higher)
- Original: **T.DIST.RT(x, degrees\_freedom):** x is the **T-statistic**, and **degrees\_freedom** is in **D9**. This function calculates the p-value for values **greater than** the **T-statistic**, testing for an increase in diversity.
  Restored correction: **1 - T.DIST(x, degrees\_freedom, TRUE):** x is the signed **T-statistic**, and **degrees\_freedom** is in **D9**. Subtract the cumulative probability from one to test for an increase in diversity.
- Original: The **T.DIST.RT** function calculates the probability
  Restored correction: The complement of **T.DIST** calculates the probability
- Original: implying the microbial diversity is **similar to the benchmark** and no significant deviation is found
  Restored correction: meaning there is insufficient evidence of a difference; equality with the benchmark is not established
- Original: This process helps determine whether the data supports the conclusion that **urbanization** and **environmental factors** have affected microbial diversity at Busse Woods.
  Restored correction: This process helps determine whether the data support a difference in microbial diversity at Busse Woods relative to the benchmark; it does not establish an environmental cause.
- Original: The goal is to determine if the diversity has declined due to **urbanization** or other **environmental pressures**.
  Restored correction: The goal is to determine if diversity is lower than the benchmark, without attributing a difference to an environmental cause.
- Original: This implies that factors such as **urbanization**, **pollution**, or **climate change** may have contributed to a **decline in biodiversity** in the area.
  Restored correction: This does not establish that **urbanization**, **pollution**, or **climate change** caused the difference.
- Original: In this scenario, microbial diversity in **Busse Woods** is either **equal to** or within the expected range for ecosystems similar to the benchmark, suggesting that biodiversity may not have been significantly affected by external factors.
  Restored correction: This does not establish equality with the benchmark or rule out an environmental effect.
- Original: whether microbial diversity in **Busse Woods** has been impacted by environmental changes
  Restored correction: whether the data provide evidence that microbial diversity in **Busse Woods** is lower than the benchmark
- Original: and/or the sample size is small
  Restored correction: under the stated sampling assumptions
- Original: As the **sample size increases**, the **one-sample T-test** results begin to resemble those of the **z-test**.
  Restored correction: As the **sample size increases**, the t reference distribution approaches the normal reference distribution.
- Original: making the T-test and Z-test results more similar
  Restored correction: making their reference probabilities more similar when the standardized statistics are comparable; the population SD remains unknown
- Original: This **longitudinal analysis** will allow you to draw meaningful conclusions about how these factors have impacted **Busse Woods' microbial communities**.
  Restored correction: This comparison over time will test for a difference in the mean Shannon Index; it cannot establish how environmental factors affected **Busse Woods' microbial communities**.
- Original: This analysis could reveal whether **urbanization** and **climate change** are contributing to the loss of biodiversity in the area.
  Restored correction: This analysis could reveal a difference in mean diversity, without identifying whether **urbanization** or **climate change** caused it.
- Original: \[is/is not\] significantly lower
  Restored correction: \[provides/does not provide\] sufficient evidence of a population mean lower
- Original: indicating that microbial diversity in **Busse Woods** \[provides/does not provide\]
  Restored correction: indicating that the data \[provide/do not provide\]
- Original: Discuss when the **one-sample T-test** results start to resemble those of a **z-test**.
  Restored correction: Discuss how the t reference distribution approaches the normal distribution as degrees of freedom increase; this does not make the population SD known or guarantee a smaller p-value.

### Technical and structural exceptions

- Retained current title, workbook data, worksheet name, formula/cell destinations and source assets.
- Step 1 replaces obsolete create/copy-tab instructions with generated-workbook open/select/inspect instructions; original data-column description and source workbook link remain.
- Original heading levels and accidental heading markers become semantic Part/Step/Substep prefixes; descriptive wording and explanatory subheads remain. Standalone Part numbering starts at 1. The next-lesson Setup heading keeps its descriptive words as an informational heading, omitting its historic numbered Part prefix.
- Formula actions use current validated formulas in their original instruction locations; semantic links wrap original visible label/value/formula spans without splitting paragraphs.
- Added one scenario-assumption paragraph, explicit directional hypotheses, source-range/count note, and separate-copy practice instruction.
- Added disjoint source, calculation, result and interpretation workbook regions.

### Omission review

- All original non-setup prose paragraphs and original instruction groups originate in the restored body. No explanation, practice, takeaway, email, advisor dialogue or transition section was intentionally omitted.
- Base64 image definitions are replaced by current extracted image files. Original empty image headings are removed.
- Scientific sentence/phrase replacements are enumerated above rather than described as blanket permission to rewrite.

## microbes_3_two_sample_t_test.md

### Exact wording exceptions

- Original: and/or the sample size is small
  Restored correction: under the stated sampling assumptions
- Original: The **Two Sample T-test** will help you assess whether urbanization and other environmental factors are contributing to a decline in microbial biodiversity.
  Restored correction: The **Two Sample T-test** will help you assess whether the population mean microbial diversity differs between the two years.
- Original: This test is ideal when comparing two groups or time periods, especially when working with relatively small sample sizes.
  Restored correction: Welch's version of this test compares two independent groups without assuming equal population variances; small sample size alone is not the criterion for choosing it.
- Original: A larger **T-statistic**
  Restored correction: A larger absolute **T-statistic**
- Original: while a smaller **T-statistic**
  Restored correction: while a smaller absolute **T-statistic**
- Original: compensates for unequal sample sizes by assigning more weight to the larger sample
  Restored correction: accounts for unequal sample sizes through the variance divided by sample size for each group
- Original: a pooled degrees of freedom value
  Restored correction: an approximate Welch degrees of freedom value
- Original: Pooled Degrees of Freedom
  Restored correction: Welch Degrees of Freedom
- Original: With more degrees of freedom, the test is more precise.
  Restored correction: For the same statistic, more degrees of freedom give lighter tails.
- Original: As degrees of freedom increase, the test becomes more reliable. This allows for better conclusions about differences between groups.
  Restored correction: More degrees of freedom bring the reference distribution closer to normal; they do not guarantee reliable sampling or a significant result.
- Original: In the case of a **two-tailed test**, you would multiply the one-tailed cumulative probability by 2 to account for both tails of the distribution.
  Restored correction: In the case of a **two-tailed test**, you would multiply the smaller one-tailed probability by 2 to account for both tails of the distribution.
- Original: Use **2** for a two-sample T-test with equal or unequal variances (independent groups).
  Restored correction: Use **3** for Welch's two-sample T-test with unequal variances (independent groups). Type 2 assumes equal variances; type 1 is paired.
- Original: A p-value less than 0.05 suggests that the difference is not due to random variation and is likely significant.
  Restored correction: A p-value less than or equal to the preselected 0.05 is statistically significant under the null model; it is not the probability that random variation caused the difference.
- Original: This would indicate that the difference between the **2014** and **2024 Shannon Index** values is unlikely to have occurred by chance.
  Restored correction: This indicates that a result at least as extreme has a probability no greater than 0.05 under the specified null model.
- Original: implying that the diversity has not changed significantly over time
  Restored correction: meaning that the evidence is insufficient to conclude a difference in mean diversity over time
- Original: whether **environmental factors** have impacted microbial diversity in Busse Woods
  Restored correction: whether the mean microbial diversity in Busse Woods differs between years
- Original: You are specifically testing whether diversity has declined due to **urbanization** or other **environmental pressures**.
  Restored correction: You are specifically testing whether the 2024 population mean is lower than the 2014 population mean; this does not identify an environmental cause.
- Original: This implies that **environmental factors** like **urbanization** or **climate change** may have reduced biodiversity in the area.
  Restored correction: This does not establish that **environmental factors** like **urbanization** or **climate change** caused the difference.
- Original: In this case, the microbial diversity in **Busse Woods** is either **equal to** or within the expected range for ecosystems similar to **2014**, suggesting that the biodiversity may not have been significantly affected by external factors.
  Restored correction: This does not establish equality between the population means or rule out an environmental effect.
- Original: whether **microbial diversity** in **Busse Woods** has been affected based on your hypothesis test results
  Restored correction: whether the data provide evidence of lower **microbial diversity** in **Busse Woods** based on your hypothesis test results
- Original: As the **sample size increases**, the **two-sample T-test** results start to resemble those of the **z-test**.
  Restored correction: As the Welch degrees of freedom increase, the t reference distribution approaches the normal reference distribution.
- Original: leading to more similar results between the two tests
  Restored correction: leading to more similar reference probabilities for comparable standardized statistics; the population variances remain unknown
- Original: to assess the impact of environmental factors such as **urbanization** or **climate change** on biodiversity
  Restored correction: to assess differences in population means without identifying an environmental cause
- Original: What you are suggesting points to a potential **homogenization** of microbial communities, which could be an effect of **urbanization** or other **environmental pressures**.
  Restored correction: What you are suggesting points to a possible decrease in the spread of Shannon Index values; that alone does not establish **homogenization** of microbial community composition or an effect of **urbanization**.
- Original: providing insights into whether **environmental pressures** have made microbial communities more **uniform**. This could suggest that **Busse Woods** has not only lost biodiversity but has also become more **homogenized**, possibly reducing its **ecological resilience**.
  Restored correction: without identifying whether **environmental pressures** caused a change. Similar Shannon Index values alone do not demonstrate similar community composition, **homogenization**, or reduced **ecological resilience**.
- Original: \[is/is not\] significantly lower
  Restored correction: \[provides/does not provide\] sufficient evidence of a population mean lower
- Original: indicating that microbial diversity in **Busse Woods** \[provides/does not provide\]
  Restored correction: indicating that the data \[provide/do not provide\]
- Original: A **p-value** helps determine if the observed difference in diversity could have occurred by random chance.
  Restored correction: A **p-value** is the probability, under the null model and its assumptions, of a result at least as extreme in the specified tail or tails; it is not the probability that chance caused a difference or that the null hypothesis is true.
- Original: Discuss when the **two-sample T-test** results start to resemble those of a **z-test**.
  Restored correction: Discuss how the t reference distribution approaches the normal distribution as degrees of freedom increase; this does not make the population variances known or guarantee a smaller p-value.
- Original: The `T.DIST.2T` function automatically calculates the p-value for both tails, accounting for deviations in either direction. The more manual method using `T.DIST` requires calculating the cumulative probability for one tail, subtracting it from 1 to capture the upper tail, and then multiplying by 2 to account for both tails.
  Restored correction: The `BETADIST` formula calculates the p-value for both tails while retaining fractional Welch degrees of freedom. The second method doubles the smaller directional tail from E17 and E18; it updates once those formulas are entered.
- Original: This calculates the p-value for the two-tailed test using the absolute value of the T-statistic and degrees of freedom.
  Restored correction: This calculates the two-tailed t probability using the squared T-statistic and unrounded Welch degrees of freedom: BETADIST(df / (df + t^2), df / 2, 0.5).
- Original: This calculates the cumulative probability for one tail and then multiplies it by 2 to account for both tails.
  Restored correction: This doubles the smaller directional tail from E17 and E18; enter those formulas below before comparing the result.
- Original: This calculates the cumulative probability for values less than or equal to the T-statistic, focusing on the lower tail.
  Restored correction: This selects half the two-tailed probability when t <= 0, and its complement otherwise, giving the probability at or below the signed statistic.
- Original: This calculates the one-tailed p-value automatically, testing whether microbial diversity has significantly decreased.
  Restored correction: The IF uses the sign of E11 to select the lower tail; T.TEST with tails = 1 alone returns the smaller tail and does not specify direction.
- Original: This calculates the probability of obtaining a T-statistic greater than or equal to the observed value, focusing on the upper tail.
  Restored correction: This selects half the two-tailed probability when t >= 0, and its complement otherwise, giving the upper-tail probability.
- Original: This calculates the cumulative probability for the lower tail, which is then subtracted from 1 to get the probability for the upper tail.
  Restored correction: This subtracts the lower-tail probability from one to obtain the upper-tail probability.
- Original: This calculates the one-tailed p-value automatically, testing whether microbial diversity has significantly increased.
  Restored correction: The IF uses the sign of E11 to select the higher tail; T.TEST with tails = 1 alone does not specify direction.
- Original: E16: =T.DIST.2T(ABS(E11), E13)
  Restored correction: E16: =BETADIST(E13 / (E13 + E11^2), E13 / 2, 0.5)
- Original: F16: =2 * (1 - T.DIST(ABS(E11), E13, TRUE))
  Restored correction: F16: =2 * MIN(E17, E18)
- Original: G16: =T.TEST(C2:C101, B2:B101, 2, 2)
  Restored correction: G16: =T.TEST(C2:C101, B2:B101, 2, 3)
- Original: E17: =T.DIST(E11, E13, TRUE)
  Restored correction: E17: =IF(E11 <= 0, E16 / 2, 1 - E16 / 2)
- Original: G17: =T.TEST(C2:C101, B2:B101, 1, 2)
  Restored correction: G17: =IF(E11 <= 0, T.TEST(C2:C101, B2:B101, 1, 3), 1 - T.TEST(C2:C101, B2:B101, 1, 3))
- Original: E18: =T.DIST.RT(E11, E13)
  Restored correction: E18: =IF(E11 >= 0, E16 / 2, 1 - E16 / 2)
- Original: F18: =1 - T.DIST(E11, E13, TRUE)
  Restored correction: F18: =1 - E17
- Original: G18: =1 - T.TEST(C2:C101, B2:B101, 1, 2)
  Restored correction: G18: =IF(E11 >= 0, T.TEST(C2:C101, B2:B101, 1, 3), 1 - T.TEST(C2:C101, B2:B101, 1, 3))

### Technical and structural exceptions

- Retained current title, workbook data, worksheet name, formula/cell destinations and source assets.
- Step 1 replaces obsolete create/copy-tab instructions with generated-workbook open/select/inspect instructions; original data-column description and source workbook link remain.
- Original heading levels and accidental heading markers become semantic Part/Step/Substep prefixes; descriptive wording and explanatory subheads remain. Standalone Part numbering starts at 1. The next-lesson Setup heading keeps its descriptive words as an informational heading, omitting its historic numbered Part prefix.
- Formula actions use current validated formulas in their original instruction locations; semantic links wrap original visible label/value/formula spans without splitting paragraphs.
- Added one scenario-assumption paragraph, explicit directional hypotheses, source-range/count note, and separate-copy practice instruction.
- Added disjoint source, calculation, result and interpretation workbook regions.

### Omission review

- All original non-setup prose paragraphs and original instruction groups originate in the restored body. No explanation, practice, takeaway, email, advisor dialogue or transition section was intentionally omitted.
- Base64 image definitions are replaced by current extracted image files. Original empty image headings are removed.
- Scientific sentence/phrase replacements are enumerated above rather than described as blanket permission to rewrite.
