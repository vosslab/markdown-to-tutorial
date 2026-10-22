# Microbial diversity two-sample t-test

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The
ecological story is a hypothesis for practice; the supplied artifacts do not establish a real
field-study provenance or a causal effect of urbanization.

## Workbook

### Sheet: Two Sample T-Test

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

### Part 3: Scenario

- **Worksheet:** Two Sample T-Test

![Forest scenes labeled Before and After, showing a change in tree cover.](assets/microbes_3_two_sample_t_test_image1.png)

These forest scenes illustrate the environmental concerns in the story; they are not evidence
about the supplied Shannon Index observations or their causes.

After reanalyzing the data with a t-test, you are less certain about the benchmark comparison.
Rather than discarding the results, your advisor suggests comparing **2014** with **2024**.
You will compare the two population means directly, instead of comparing one mean with **4.0**.

Use **Welch's independent-samples t-test** to compare the two means. Main H0: 2024 mean >= 2014 mean; H1:
2024 mean < 2014 mean. Two-tail uses equal versus unequal means; higher uses 2024 mean <= 2014 mean
versus >. The question concerns population means rather than an environmental mechanism.

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
Larger samples cannot repair biased sampling or dependence.

#### Step 1: Set Up Your Google Sheet for the Two Sample T-Test

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

Inspect columns **A:C**: location, 2014 Shannon Index, and 2024 Shannon Index. Use **D** for labels,
**E** for the primary calculations, and **F:G** for alternate p-value calculations. These alternates
are checks of the same hypotheses, not additional independent evidence.

- **Label F1:** Alternate Values 1
- **Label G1:** Alternate Values 2

#### Step 3: Calculate the Sample Statistics

Calculate each year's **mean**, **sample SD**, and **sample size**. `STDEV` uses the sample variance
denominator n - 1. Both current counts should be **24**. The sample summaries will supply the
standard error and Welch degrees of freedom.

- **Label D2:** 2014 Sample Mean
- **Enter E2:** `=AVERAGE(B2:B101)`
- **Label D3:** 2024 Sample Mean
- **Enter E3:** `=AVERAGE(C2:C101)`
- **Label D5:** 2014 Sample Standard Deviation
- **Enter E5:** `=STDEV(B2:B101)`
- **Label D6:** 2024 Sample Standard Deviation
- **Enter E6:** `=STDEV(C2:C101)`
- **Label D8:** 2014 Sample Size
- **Enter E8:** `=COUNT(B2:B101)`
- **Label D9:** 2024 Sample Size
- **Enter E9:** `=COUNT(C2:C101)`

#### Step 4: Calculate the T-Statistic

Use **2024 mean minus 2014 mean** throughout. Divide this difference by the square root of (2014
sample variance / 2014 n + 2024 sample variance / 2024 n). This is the **Welch t-statistic**; it
does not assume equal population variances. A negative statistic favors a lower 2024 mean.

- **Label D11:** T-Statistic
- **Enter E11:** `=(E3 - E2) / SQRT((E5^2/E8) + (E6^2/E9))`

#### Step 5: Calculate the Degrees of Freedom

Use the **Welch-Satterthwaite approximation** to account for uncertainty in both sample variance
estimates. Preserve the noninteger degrees of freedom in E13. With equal sample sizes and equal
variances this reduces to n1 + n2 - 2; otherwise it generally differs. Smaller degrees of freedom
give heavier t tails for a fixed statistic.

- **Label D13:** Degrees of Freedom
- **Enter E13:** `=((E5^2/E8) + (E6^2/E9))^2 / ((E5^4/((E8^2)*(E8-1))) + (E6^4/((E9^2)*(E9-1))))`

Compare these **Welch df examples**. The same formula responds to both unequal variances and unequal
sample sizes; degrees of freedom alone do not determine the p-value.

| Name | Sample 1 Variance | Sample 1 Size | Sample 2 Variance | Sample 2 Size | Welch Degrees of Freedom |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Both variances and sizes equal | 0.5 | 50 | 0.5 | 50 | 98.00 |
| Larger Sample 1 size, same variance | 0.5 | 50 | 0.5 | 25 | 48.11 |
| Much larger Sample 1 size, same variance | 0.5 | 50 | 0.5 | 10 | 12.87 |
| Same sample size, smaller Sample 2 variance | 0.5 | 50 | 0.4 | 50 | 96.80 |
| Same sample size, much smaller Sample 2 variance | 0.5 | 50 | 0.2 | 50 | 82.79 |
| Both variances and sizes unequal | 0.5 | 50 | 0.3 | 25 | 60.19 |

![Standard normal and t-distribution density curves: t with 3 degrees of freedom has heavier tails than t with 23 degrees of freedom, which lies closer to the normal curve.](assets/t_distributions.png)

The t-distribution approaches the standard normal as degrees of freedom increase. These curves
compare reference distributions, not the observed microbial data; there is no cutoff at n = 30.

#### Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)

For the main question, use the **one-tailed lower** alternative selected in the scenario.
The two-tailed alternative asks about a difference in either direction; the higher alternative
asks about an increase. Each has its own null hypothesis. Keep these interpretations separate.


#### Step 7: Calculate the P-Values

Use `BETADIST(x, a, b)` to calculate the t-tail probability from your statistic and **unrounded**
Welch df. It evaluates a cumulative beta probability on the default interval 0 to 1. The identity
is: two-tail t probability = beta cumulative probability at df / (df + t^2), with shape parameters
df / 2 and 0.5. This calculates the same t-distribution probability while preserving fractional df;
some spreadsheet `T.DIST` functions truncate df to an integer. You do not need to derive the beta
identity to interpret the t-test. At t = 0 the beta input is 1, giving two-tail p = 1.

`T.TEST(array1, array2, tails, type)` calculates a p-value directly from observations:
use tails **2** or **1**, and type **3** for
independent unequal-variance (Welch) samples. Type 1 is paired; type 2 assumes equal variances. A
one-tail `T.TEST` returns the small tail associated with the magnitude, so use the statistic's
**sign** to obtain the requested direction. Compare this direct calculation with your calculation
from t and df; retain E13 unrounded.

- **Label D16:** P-Value (Two-Tailed)
- **Label D17:** P-Value (One-Tailed, Lower)
- **Label D18:** P-Value (One-Tailed, Higher)

##### Substep 7.1: Two-Tailed Test:

The **two-tailed** alternative includes extremes in both directions. Double the smaller tail; using
the absolute Z or t statistic makes this the upper tail beyond its magnitude. Compare alternate
methods where provided.

- **Enter E16:** `=BETADIST(E13 / (E13 + E11^2), E13 / 2, 0.5)`
- **Enter F16:** `=2 * MIN(E17, E18)`
- **Enter G16:** `=T.TEST(C2:C101, B2:B101, 2, 3)`

F16 checks that the two-tailed probability equals twice the smaller directional tail. It will
update after you enter E17 and E18 below; it reuses the same calculation rather than providing an
independent method. G16 compares the manual calculation with the direct test on the observations.

##### Substep 7.2: One-Tailed Test (for lower values):

The **one-tailed lower** alternative uses the probability to the left of the signed statistic. For a
positive statistic, this probability is large; do not force it to be the smaller tail. Half of E16
is the smaller tail; the IF selects that half for a negative statistic and its complement for a
positive statistic. At zero, both one-tail probabilities are 0.5. The IF around T.TEST likewise
selects the requested tail using the sign of E11; simply requesting tails = 1 does not specify
lower or higher.

- **Enter E17:** `=IF(E11 <= 0, E16 / 2, 1 - E16 / 2)`
- **Enter G17:** `=IF(E11 <= 0, T.TEST(C2:C101, B2:B101, 1, 3), 1 - T.TEST(C2:C101, B2:B101, 1, 3))`

##### Substep 7.3: One-Tailed Test (for higher values):

The **one-tailed higher** alternative uses the probability to the right of the signed statistic.
For a positive statistic, use half of E16; for a negative statistic, use its complement, which is
large.
By symmetry, the higher and lower probabilities sum to one. The IF around T.TEST
selects the requested tail using the sign of E11; simply requesting tails = 1 does not specify lower
or higher.

- **Enter E18:** `=IF(E11 >= 0, E16 / 2, 1 - E16 / 2)`
- **Enter F18:** `=1 - E17`
- **Enter G18:** `=IF(E11 >= 0, T.TEST(C2:C101, B2:B101, 1, 3), 1 - T.TEST(C2:C101, B2:B101, 1, 3))`

#### Step 8: Decision Using an IF Statement

Use `IF` to compare each primary p-value in column E with alpha. A lower-tail rejection supports a
lower 2024 population mean under the working model; a higher-tail rejection supports the reverse. A
two-tailed rejection supports a difference without specifying its direction in advance.

- **Label D21:** Significance Level (alpha)
- **Enter E21:** 0.05
- **Label D22:** Two-Tail Decision
- **Enter E22:** `=IF(E16 <= E21, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label D23:** One-Tail Decision (Lower)
- **Enter E23:** `=IF(E17 <= E21, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label D24:** One-Tail Decision (Higher)
- **Enter E24:** `=IF(E18 <= E21, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

#### Step 9: Interpret the Results

Use the **lower-tail result in E17**. The original data give t about **-1.91452**, Welch df about
**39.49524**, and lower p about **0.03141** using fractional df. Reject the lower directional null
at 0.05; the working model supports a lower 2024 mean. The two-tail p is about **0.06282**, which
fails to reject. The beta calculation and direct Welch test retain fractional df and should agree
apart from numerical precision. The comparison cannot attribute a difference to urbanization or
climate change.

- **Label D26:** Interpretation

- **Explain:** Write your interpretation in `E26`. Include the p-value, tail and alternative, alpha, and the evidence-based conclusion. If p > alpha, state that evidence is insufficient; do not claim equality or absence of an effect.

#### Practice: Explore sensitivity

Save a separate practice copy after recording the original result. Treat modified observations
as hypothetical examples, not newly collected evidence.

- **Change:** Modify a few values in columns B:C (2014 and 2024). Compare the mean, SD or variance, statistic, p-value, and decision before and after. Explain which quantities changed and why.
- **Add:** Enter hypothetical numeric observations in blank cells within rows 2:101 of the raw-data columns. Check the updated counts; leave unobserved entries blank. Compare adding values near a group mean with adding extreme values.
- **Compare:** Discuss how sample size, effect size, variability, and assumptions influence the result. More observations can reduce standard errors under the model, but do not guarantee a smaller p-value or repair biased or dependent observations.
- **Connect:** Explain why larger degrees of freedom make the t distribution approach the normal distribution. This does not make a sample SD a known population SD or turn the study into a Z-test.

#### Key Takeaways

- **Welch's two-sample t-test:** Use it to compare two population means under the independent-samples
  model without assuming equal variances.
- **T-distribution:** It accounts for uncertainty from estimating both population variances.
- **Degrees of freedom:** Welch df depend on sample sizes and variances; larger df bring the reference
  distribution closer to the normal distribution.
- **Comparing years:** Comparing the 2014 and 2024 means answers a different question from the benchmark test.
  It does not identify an environmental cause.

#### Moving to the F-test

While reviewing your spreadsheet, you notice that the **2024 Shannon Index values** appear more
similar to one another than the **2014** values. You bring this observation to your advisor:
"We compared the means. Has the variability also changed?" Your advisor suggests an **F-test**
to compare variances. Lower index spread alone does not demonstrate community homogenization;
the next tutorial examines the spread of the indices.

Ask the instructor for the next tutorial link.
