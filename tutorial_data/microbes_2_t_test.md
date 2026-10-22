# Microbial diversity benchmark t-test

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The
ecological story is a hypothesis for practice; the supplied artifacts do not establish a real
field-study provenance or a causal effect of urbanization.

## Workbook

### Sheet: Microbial T-Test

| "Sample Location" | `"2024\nShannon\nIndex "` | "Statistical Names" | "Values" |
| --- | --- | --- | --- |
| "Andrews Park" | 2.413 |  |  |
| "Beisner Road Entrance" | 3.853 |  |  |
| "Boat Launch Area" | 2.645 |  |  |
| "Busse Lake" | 4.871 |  |  |
| "Debra Park" | 2.357 |  |  |
| "Elk Pasture" | 4.281 |  |  |
| "Forest Central Grove" | 3.433 |  |  |
| "Forest North Grove" | 2.876 |  |  |
| "Forest South Grove" | 4.415 |  |  |
| "Forest West Grove" | 3.46 |  |  |
| "Lake Boating Center" | 2.64 |  |  |
| "Large Event Area" | 5.009 |  |  |
| "Main Dam" | 4.885 |  |  |
| "Main Pool" | 2.805 |  |  |
| "Marshall Park" | 4.733 |  |  |
| "Model Airplane Field" | 4.452 |  |  |
| "Nature Preserve" | 2.749 |  |  |
| "Ned Brown Meadow" | 3.635 |  |  |
| "North Pool" | 4.371 |  |  |
| "Osborn  Park" | 4.906 |  |  |
| "Salt Creek Trail" | 3.985 |  |  |
| "South Pool" | 3.849 |  |  |
| "Wildlife Refuge" | 3.521 |  |  |
| "Woodland Meadow" | 4.982 |  |  |

## Tutorial

### Part 2: Scenario

- **Worksheet:** Microbial T-Test

![Z-test versus t-test.](assets/microbes_2_t_test_image1.png)

Now, you face a more realistic challenge. Without knowing the true **population standard
deviation**, you must rely on the **sample standard deviation** from your collected data.
Determined to reach a solid conclusion, you open your spreadsheet again to calculate the sample
mean and SD and perform a **one-sample t-test**.

Revisit the same benchmark question with an **unknown population SD**. Estimate it from the sample
and use a one-sample t-test. The main question remains lower: H0: mean >= 4.0; H1: mean < 4.0.
Two-tail uses equality versus inequality; higher uses mean <= 4.0 versus mean > 4.0. Compare the
result with Part 1 without treating either outcome as proof about urbanization.

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

Assume a representative independent sample and a normally distributed population for the
one-sample t model. Inspect observations for outliers and distribution shape.
Larger samples cannot repair biased sampling or dependence.

#### Step 1: Set Up Your Google Sheet for the T-Test

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


#### Step 2: Set Up the Known Population Values

Retain the benchmark mean **4.0**. Unlike Part 1, the population SD is now treated as **unknown**
and estimated from the observations. This changes the standard error and the reference distribution.

- **Label C2:** Population Mean
- **Enter D2:** 4.0

#### Step 3: Calculate the Sample Statistics

`AVERAGE` gives the sample mean, `STDEV` gives the **sample** standard deviation (using n - 1), and
`COUNT` gives the number of numeric observations. The current count is **24**.

- **Label C4:** Sample Mean
- **Enter D4:** `=AVERAGE(B2:B101)`
- **Label C5:** Sample Standard Deviation
- **Enter D5:** `=STDEV(B2:B101)`
- **Label C6:** Sample Size
- **Enter D6:** `=COUNT(B2:B101)`

#### Step 4: Calculate the T-Statistic

The **t-statistic** divides the sample mean minus the benchmark by the estimated standard error,
sample SD / square root of n. Its sign has the same interpretation as Z, but estimating the SD adds
uncertainty.

- **Label C8:** T-Statistic
- **Enter D8:** `=(D4 - D2) / (D5 / SQRT(D6))`

#### Step 5: Calculate the Degrees of Freedom

The one-sample t-test uses **n - 1 degrees of freedom** because the sample mean is estimated from
the same observations. For 24 observations, this is **23**. At low degrees of freedom the t
distribution has heavier tails than the normal; it approaches the normal as degrees of freedom
increase.

- **Label C9:** Degrees of Freedom
- **Enter D9:** `=D6 - 1`

#### Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)

For the main question, use the **one-tailed lower** alternative selected in the scenario.
The two-tailed alternative asks about a difference in either direction; the higher alternative
asks about an increase. Each has its own null hypothesis. Keep these interpretations separate.


#### Step 7: Calculate the P-Values

`T.DIST(x, df, TRUE)` returns the cumulative probability to the left of x. `TRUE` requests a
cumulative probability; `FALSE` would request a density, which is not a p-value. `T.DIST.2T`
directly returns a two-tail probability beyond the absolute statistic.

- **Label E1:** Alternate Values

##### Substep 7.1: Two-Tailed Test:

The **two-tailed** alternative includes extremes in both directions. Double the smaller tail; using
the absolute Z or t statistic makes this the upper tail beyond its magnitude. Compare alternate
methods where provided.

- **Label C10:** P-Value (Two-Tailed)
- **Enter D10:** `=T.DIST.2T(ABS(D8), D9)`
- **Enter E10:** `=2 * (1 - T.DIST(ABS(D8), D9, TRUE))`

##### Substep 7.2: One-Tailed Test (for lower values):

The **one-tailed lower** alternative uses the probability to the left of the signed statistic. For a
positive statistic, this probability is large; do not force it to be the smaller tail.

- **Label C11:** P-Value (One-Tailed, Lower)
- **Enter D11:** `=T.DIST(D8, D9, TRUE)`

##### Substep 7.3: One-Tailed Test (for higher values):

The **one-tailed higher** alternative uses the probability to the right of the signed statistic.
Subtract the cumulative probability from one. For a negative statistic, this probability is large.
By symmetry, T.DIST of the negated statistic gives the same higher probability.

- **Label C12:** P-Value (One-Tailed, Higher)
- **Enter D12:** `=1 - T.DIST(D8, D9, TRUE)`
- **Enter E12:** `=T.DIST(-D8, D9, TRUE)`

#### Step 8: Decision Using an IF Statement

Compare each p-value with alpha using `IF`. The condition p <= alpha selects **Reject the Null
Hypothesis**; otherwise select **Fail to Reject the Null Hypothesis**. Interpret the lower-tail
decision for the main question.

- **Label C14:** Significance Level (alpha)
- **Enter D14:** 0.05
- **Label C15:** Two-Tail Decision
- **Enter D15:** `=IF(D10 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label C16:** One-Tail Decision (Lower)
- **Enter D16:** `=IF(D11 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label C17:** One-Tail Decision (Higher)
- **Enter D17:** `=IF(D12 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

#### Step 9: Interpret the Results

Read the **lower-tail p-value in D11**. The original data give t about **-1.10438**, df **23**, and
lower p about **0.14043**. Fail to reject at 0.05: evidence is insufficient to conclude the
population mean is below 4.0. The two-tail p is about **0.28085**, and the higher-tail p is about
**0.85957**. Unlike the known-SD Z exercise, this test estimates SD from the sample; a
nonsignificant result does not prove equality or unchanged biodiversity.

- **Label C19:** Interpretation

- **Explain:** Write your interpretation in `D19`. Include the p-value, tail and alternative, alpha, and the evidence-based conclusion. If p > alpha, state that evidence is insufficient; do not claim equality or absence of an effect.

#### Practice: Explore sensitivity

Save a separate practice copy after recording the original result. Treat modified observations
as hypothetical examples, not newly collected evidence.

- **Change:** Modify a few values in columns B. Compare the mean, SD or variance, statistic, p-value, and decision before and after. Explain which quantities changed and why.
- **Add:** Enter hypothetical numeric observations in blank cells within rows 2:101 of the raw-data columns. Check the updated counts; leave unobserved entries blank. Compare adding values near a group mean with adding extreme values.
- **Compare:** Discuss how sample size, effect size, variability, and assumptions influence the result. More observations can reduce standard errors under the model, but do not guarantee a smaller p-value or repair biased or dependent observations.
- **Connect:** Explain why larger degrees of freedom make the t distribution approach the normal distribution. This does not make a sample SD a known population SD or turn the study into a Z-test.

#### Key Takeaways

- **One-sample t-test:** Use this test to compare a population mean with a benchmark when the population
  SD is unknown and estimated from the sample.
- **T-distribution:** It accounts for the extra uncertainty from estimating SD.
- **Degrees of freedom:** As they increase, the t-distribution approaches the normal distribution;
  the population SD is still unknown.
- **Lower-tail test:** This asks whether the population mean Shannon Index is below **4.0**;
  insufficient evidence does not establish equality.

#### Moving to two samples

The t-test has not confirmed the lower-than-benchmark conclusion from your Z-test. As you
reconsider your report, your advisor suggests a new approach: "We also have data from **2014**.
Compare those observations with **2024**, rather than only comparing with a benchmark."
The next tutorial uses Welch's two-sample t-test to answer that new question.

Ask the instructor for the next tutorial link.
