# Microbial diversity two-sample F-test

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The
ecological story is a hypothesis for practice; the supplied artifacts do not establish a real
field-study provenance or a causal effect of urbanization.

## Workbook

### Sheet: Two Sample F-Test

| "Sample Location" | `"2014\nShannon\nIndex "` | `"2024\nShannon\nIndex "` | "Statistical Names" | "Values" |
| --- | --- | --- | --- | --- |
| "Andrews Park" | 4.417 | 2.413 |  |  |
| "Beisner Road Entrance" | 5.359 | 3.853 |  |  |
| "Boat Launch Area" | 1.984 | 2.645 |  |  |
| "Busse Lake" | 6.923 | 4.871 |  |  |
| "Debra Park" | 1.412 | 2.357 |  |  |
| "Elk Pasture" | 4.677 | 4.281 |  |  |
| "Forest Central Grove" | 4.26 | 3.433 |  |  |
| "Forest North Grove" | 2.633 | 2.876 |  |  |
| "Forest South Grove" | 3.429 | 4.415 |  |  |
| "Forest West Grove" | 2.965 | 3.46 |  |  |
| "Lake Boating Center" | 4.728 | 2.64 |  |  |
| "Large Event Area" | 6.944 | 5.009 |  |  |
| "Main Dam" | 5.404 | 4.885 |  |  |
| "Main Pool" | 4.612 | 2.805 |  |  |
| "Marshall Park" | 5.028 | 4.733 |  |  |
| "Model Airplane Field" | 5.949 | 4.452 |  |  |
| "Nature Preserve" | 3.907 | 2.749 |  |  |
| "Ned Brown Meadow" | 4.305 | 3.635 |  |  |
| "North Pool" | 4.665 | 4.371 |  |  |
| "Osborn  Park" | 4.241 | 4.906 |  |  |
| "Salt Creek Trail" | 4.351 | 3.985 |  |  |
| "South Pool" | 3.791 | 3.849 |  |  |
| "Wildlife Refuge" | 4.079 | 3.521 |  |  |
| "Woodland Meadow" | 6.565 | 4.982 |  |  |

## Tutorial

### Part 4: Scenario

- **Worksheet:** Two Sample F-Test

![T-test versus F-test.](assets/microbes_4_f_test_image1.png)

After comparing the two years' means, you notice that the **2024 Shannon Index values** appear
more similar to one another. You present this observation to your advisor, who suggests an
**F-test**: the t-test compared means; now you will compare variances.

A classical two-sample F-test compares population variances. A lower variance means
indices vary less across observations; it does not establish that species composition has become
more uniform.

The Shannon Index combines **richness** (the number of taxa detected) and **evenness**
(their relative abundances). It is calculated as **H = -sum(p_i ln(p_i))**, where p_i
is the proportion assigned to taxon i and ln is the natural logarithm. Higher values indicate
greater diversity at the chosen taxonomic
resolution; the index has no universal upper bound independent of community size and log base.
In the teaching scenario, soil microbial diversity at Busse Woods is estimated using SSU rRNA
sequencing. Urbanization motivates the questions, but these tests compare diversity summaries;
they cannot identify an environmental cause.

Choose the hypothesis and significance level **before inspecting results**. Use alpha = 0.05
throughout. Calculating all three tails is a comparison exercise, not permission to select the
smallest p-value. A p-value is a probability of a result at least as extreme in the specified
tail or tails, under the null model and its assumptions. It is not the probability that the null
hypothesis is true. Failure to reject means insufficient evidence for the alternative.

The source lists the **same 24 named locations in both years**. For this method exercise,
make the **hypothetical assumption of independent samples** within and across years. Matching row labels do not establish
independence. If these represent repeated measurements at matched sites, use a paired method
for means or a variance comparison that accounts for dependence; the independent F-test is
not a paired variance test. Verify the actual sampling design before applying either method
to field-study inference.

Assume a representative independent sample and a normally distributed population for the
two-sample model. Inspect observations for outliers and distribution shape.
The classical variance F-test is especially sensitive to nonnormality.
Larger samples cannot repair biased sampling or dependence.

#### Step 1: Open the workbook

The generated workbook already contains the observations. Calculation labels are deliberately
left for you to enter, so constructing the results table remains part of the exercise. Open the
XLSX workbook in Google Sheets, then inspect the named worksheet before entering formulas.

- **Open:** Open the generated XLSX workbook in Google Sheets and select the worksheet named above.
- **Inspect:** Check the raw-data headers and counts. Keep the source observations intact while calculating the original results.

Each current-year dataset has 24 observations in rows 2:25. Formula ranges end at row 101 to
leave room for later practice. `AVERAGE`, `STDEV`, `VAR.S`, and `COUNT` ignore empty cells;
blank observations are not zeroes. Enter numeric practice data only within the stated ranges.
The original course workbook is retained as a [source
reference](https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit).


#### Step 2: Organize Your Sheet

Inspect columns **A:C** for locations and the two years of observations. Use **D** for labels, **E**
for primary values, and **F:G** for alternate tail calculations. The F-test compares spread, so
sample means are not needed.

Headers **D1 (Statistical Names)** and **E1 (Values)** are already present. Inspect them, then
add the two alternate-value headings below.

- **Label F1:** Alternate Values 1
- **Label G1:** Alternate Values 2

#### Step 3: Calculate the Sample Statistics

Calculate the **sample standard deviation** and **sample size** for each year. Squaring each SD in
the next step yields its sample variance. Both current sample sizes should be **24**.

- **Label D5:** 2014 Sample Standard Deviation
- **Enter E5:** `=STDEV(B2:B101)`
- **Label D6:** 2024 Sample Standard Deviation
- **Enter E6:** `=STDEV(C2:C101)`
- **Label D8:** 2014 Sample Size
- **Enter E8:** `=COUNT(B2:B101)`
- **Label D9:** 2024 Sample Size
- **Enter E9:** `=COUNT(C2:C101)`

#### Step 4: Calculate the F-Statistic

Form the variance ratio **2024 / 2014**. F below one means the observed 2024 variance is lower; F
above one means it is higher. Statistical significance also depends on degrees of freedom. A
difference in Shannon-index spread does not establish taxonomic homogenization: communities can have
the same index and different species.

- **Label D11:** F-Statistic
- **Enter E11:** `=E6^2 / E5^2`

#### Step 5: Calculate the Degrees of Freedom

Each variance estimate has **n - 1 degrees of freedom**. Because 2024 is the numerator, its df in
**E14** must be the first df argument in the F distribution. The 2014 denominator df in **E13** is
second. Keep this ordering when practice changes sample sizes.

- **Label D13:** Degrees of Freedom for 2014
- **Enter E13:** `=E8 - 1`
- **Label D14:** Degrees of Freedom for 2024
- **Enter E14:** `=E9 - 1`

#### Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)

The main alternative is **2024 population variance < 2014 population variance** (one-tailed lower);
its null is >=. The two-tailed null is equality, against inequality. The higher-tail null is <=,
against >. These hypotheses concern variance, not the direction of the mean difference.

#### Step 7: Calculate the P-Values

`F.DIST(F, numerator_df, denominator_df, TRUE)` gives the lower tail; `F.DIST.RT` gives the upper
tail. `F.TEST(array1, array2)` returns twice the smaller tail for the equality-of-variances
comparison. Do not automatically halve its result for a preselected direction: determine which tail
is smaller first.

- **Label D16:** P-Value (Two-Tailed)
- **Label D17:** P-Value (One-Tailed, Lower)
- **Label D18:** P-Value (One-Tailed, Higher)

##### Substep 7.1: Two-Tailed Test:

For the **two-tailed variance** alternative, double the smaller of the lower and upper
probabilities, capped at one. Compare the explicit calculation in E16 with the built-in F.TEST in
G16.

- **Enter E16:** `=MIN(1, 2 * MIN(F.DIST(E11, E14, E13, TRUE), F.DIST.RT(E11, E14, E13)))`
- **Enter G16:** `=F.TEST(C2:C101, B2:B101)`

##### Substep 7.2: One-Tailed Test (for lower values):

For the **one-tailed lower variance** alternative, use the direct F cumulative probability. G17
recovers the same tail from F.TEST: halve its two-tail p only when the direct lower probability is
<= 0.5; otherwise subtract that half from one. This remains valid with unequal sample sizes.

- **Enter E17:** `=F.DIST(E11, E14, E13, TRUE)`
- **Enter G17:** `=IF(F.DIST(E11, E14, E13, TRUE) <= 0.5, F.TEST(C2:C101, B2:B101)/2, 1 - F.TEST(C2:C101, B2:B101)/2)`

##### Substep 7.3: One-Tailed Test (for higher values):

For the **one-tailed higher variance** alternative, use F.DIST.RT. F18 checks the same probability
using the reciprocal variance ratio and **swapped degrees of freedom**. G18 is the complement of
G17. All three calculations should agree.

- **Enter E18:** `=F.DIST.RT(E11, E14, E13)`
- **Enter F18:** `=F.DIST(E5^2 / E6^2, E13, E14, TRUE)`
- **Enter G18:** `=1 - G17`

#### Step 8: Decision Using an IF Statement

Compare each p-value with **alpha = 0.05** using `IF`. The lower-tail decision answers the main
question. These decision formulas compare variances; they say nothing about whether the population
means differ.

- **Label D20:** Significance Level (alpha)
- **Enter E20:** 0.05
- **Label D22:** Two-Tail Decision
- **Enter E22:** `=IF(E16 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label D23:** One-Tail Decision (Lower)
- **Enter E23:** `=IF(E17 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label D24:** One-Tail Decision (Higher)
- **Enter E24:** `=IF(E18 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

#### Step 9: Interpret the Results

Read **E17**, the lower-tail p-value. Original F is about **0.42265**, with numerator and
denominator df **23, 23**. Lower p is about **0.02207**, so reject the lower directional null at
0.05: the independent normal-population model supports lower 2024 variance of Shannon indices. The
two-tail p is about **0.04413** and also rejects equality; higher p is about **0.97793** and fails
to reject. This result concerns index spread across observations, not community composition,
ecological resilience, or an environmental cause.

- **Label D26:** Interpretation

- **Explain:** Write your interpretation in `E26`. Include the p-value, tail and alternative, alpha, and the evidence-based conclusion. If p > alpha, state that evidence is insufficient; do not claim equality or absence of an effect.

#### Practice: Explore sensitivity

Save a separate practice copy after recording the original result. Treat modified observations
as hypothetical examples, not newly collected evidence.

- **Change:** Modify a few values in columns B:C (2014 and 2024). Compare each sample SD, sample size, variance ratio, p-value, and decision before and after. The F-test compares variance; sample means are not part of its calculation. Explain which spread and count changes affect the ratio and its degrees of freedom.
- **Add:** Enter hypothetical numeric observations in blank cells within rows 2:101 of the raw-data columns. Check the updated counts; leave unobserved entries blank. Compare adding values near a group mean with adding extreme values.
- **Compare:** Discuss how sample size, effect size, variability, and assumptions influence the result. More observations can reduce standard errors under the model, but do not guarantee a smaller p-value or repair biased or dependent observations.

#### Key Takeaways

- **F-test:** Use it to compare two population **variances**, rather than means.
- **Tail choice:** The variance ratio and its degrees of freedom determine the reference distribution; select
  the lower, higher, or two-tailed alternative before inspecting results.
- **Assumptions:** The classical test assumes independent normal observations and is especially sensitive to
  nonnormality. Larger samples cannot repair dependence or biased sampling.
- **Spread:** The F-test complements the **t-test** by asking about the spread of Shannon Index values.
  Spread alone does not describe species composition or ecological resilience.

#### Moving to ANOVA

With the two-year comparison complete, you recall older student theses in the lab. In this
teaching story, the **1994, 2004, and 2009** projects used culture-based methods before the later
sequencing datasets. You bring these records to your advisor and propose comparing all five
years with **ANOVA**. Method differences need attention, and the omnibus test will ask whether
at least one population mean differs, rather than establish a declining trend.

Ask the instructor for the next tutorial link.
