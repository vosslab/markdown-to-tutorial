# Microbial diversity Z-test

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The
ecological story is a hypothesis for practice; the supplied artifacts do not establish a real
field-study provenance or a causal effect of urbanization.

## Workbook

### Sheet: Microbial Z-Test

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

### Part 1: Scenario

- **Worksheet:** Microbial Z-Test

![Busse Woods, with wooded shorelines around the lake.](assets/microbes_1_z_test_image1.png)

Busse Woods is the setting for your microbial diversity investigation.

You are analyzing microbial diversity in soil samples from different locations in **Busse Woods
Forest Preserve**. Urbanization around Busse Woods is raising concerns about soil health and
biodiversity. Your task is to compare the current diversity with a benchmark for similar ecosystems.

Compare the current population mean Shannon Index with the stipulated benchmark **4.0**, assuming a
known population SD **0.6**. The main question is whether the mean is **lower**: H0: mean >= 4.0;
H1: mean < 4.0. For the two-tail comparison use H0: mean = 4.0 versus H1: mean != 4.0; for higher
use H0: mean <= 4.0 versus H1: mean > 4.0.

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
known-SD Z model. Inspect observations for outliers and distribution shape.
Larger samples cannot repair biased sampling or dependence.

#### Step 1: Find Your Copy of the Spreadsheet

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

The benchmark mean is **4.0** and the population standard deviation is **0.6**, both stipulated for
this exercise. A Z-test requires the population SD to be known; do not estimate it from the current
sample.

- **Label C2:** Population Mean
- **Enter D2:** 4.0
- **Label C3:** Population Standard Deviation
- **Enter D3:** 0.6

#### Step 3: Calculate the Sample Mean

`AVERAGE` calculates the sample mean and `COUNT` counts numeric observations. Use the same
observation range for both; the current count should be **24**.

- **Label C5:** Sample Mean
- **Enter D5:** `=AVERAGE(B2:B101)`
- **Label C6:** Sample Size
- **Enter D6:** `=COUNT(B2:B101)`

#### Step 4: Calculate the Z-Statistic

The **Z-statistic** is the sample mean minus the benchmark, divided by the standard error,
population SD / square root of sample size. It expresses the difference in **standard-error units**.
Negative values favor the lower alternative.

- **Label C8:** Z-Statistic
- **Enter D8:** `=(D5 - D2) / (D3 / SQRT(D6))`

#### Step 5: Determine the Type of Test (One-Tailed or Two-Tailed)

For the main question, use the **one-tailed lower** alternative selected in the scenario.
The two-tailed alternative asks about a difference in either direction; the higher alternative
asks about an increase. Each has its own null hypothesis. Keep these interpretations separate.


#### Step 6: Calculate the P-Values

![A standard normal curve with the lower-tail area shaded to the left of a negative Z value.](assets/microbes_1_z_test_image2.png)

The shaded area illustrates a lower-tail probability, not the result for this dataset.

`NORM.DIST(z, 0, 1, TRUE)` returns the standard normal cumulative probability to the left of z.
The **0** sets the mean, **1** sets the standard deviation, and **TRUE** selects cumulative
probability. Use it to construct the following tail probabilities.

##### Substep 6.1: Two-Tailed Test:

The **two-tailed** alternative includes extremes in both directions. Double the smaller tail; using
the absolute Z or t statistic makes this the upper tail beyond its magnitude. Compare alternate
methods where provided.

- **Label C10:** P-Value (Two-Tailed)
- **Enter D10:** `=2 * (1 - NORM.DIST(ABS(D8), 0, 1, TRUE))`

##### Substep 6.2: One-Tailed Test (for lower values):

The **one-tailed lower** alternative uses the probability to the left of the signed statistic. For a
positive statistic, this probability is large; do not force it to be the smaller tail.

- **Label C11:** P-Value (One-Tailed, Lower)
- **Enter D11:** `=NORM.DIST(D8, 0, 1, TRUE)`

##### Substep 6.3: One-Tailed Test (for higher values):

The **one-tailed higher** alternative uses the probability to the right of the signed statistic.
Subtract the cumulative probability from one. For a negative statistic, this probability is large.

- **Label C12:** P-Value (One-Tailed, Higher)
- **Enter D12:** `=1 - NORM.DIST(D8, 0, 1, TRUE)`

#### Step 7: Make a Decision Using an IF Statement

An `IF` formula evaluates whether p <= alpha. It returns **Reject the Null Hypothesis** when true
and **Fail to Reject the Null Hypothesis** otherwise. Use the matching p-value for each tail; the
lower decision answers the main question.

- **Label C14:** Significance Level (alpha)
- **Enter D14:** 0.05
- **Label C15:** Two-Tail Decision
- **Enter D15:** `=IF(D10 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label C16:** One-Tail Decision (Lower)
- **Enter D16:** `=IF(D11 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label C17:** One-Tail Decision (Higher)
- **Enter D17:** `=IF(D12 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

#### Step 8: Interpret the Results

Use the **lower-tail p-value in D11** and the decision in D16. The original observations give Z
about **-1.65817** and lower p about **0.04864**: reject the directional null at 0.05. Under the
stated model, there is evidence that the population mean Shannon Index is below 4.0. The two-tail p
is about **0.09728**, so the two-tailed comparison fails to reject. These different decisions answer
different hypotheses; neither establishes an effect of urbanization.

- **Label C19:** Interpretation

- **Explain:** Write your interpretation in `D19`. Include the p-value, tail and alternative, alpha, and the evidence-based conclusion. If p > alpha, state that evidence is insufficient; do not claim equality or absence of an effect.

#### Practice: Explore sensitivity

Save a separate practice copy after recording the original result. Treat modified observations
as hypothetical examples, not newly collected evidence.

- **Change:** Modify a few values in column B. Compare the sample mean, Z-statistic, p-value, and decision before and after. The stipulated population SD in D3 stays fixed at 0.6; this Z-test does not calculate a sample SD or variance. Explain how changing the mean and count changes the standard error and result.
- **Add:** Enter hypothetical numeric observations in blank cells within rows 2:101 of the raw-data columns. Check the updated counts; leave unobserved entries blank. Compare adding values near a group mean with adding extreme values.
- **Compare:** Discuss how sample size, effect size, variability, and assumptions influence the result. More observations can reduce standard errors under the model, but do not guarantee a smaller p-value or repair biased or dependent observations.

#### Key Takeaways

- **Flexibility:** The range B2:B101 lets you explore how adding or removing observations changes
  the result. More observations do not guarantee a smaller p-value.
- **Z-statistics:** Compare the sample mean with a benchmark in standard-error units, using a
  known population SD.
- **Dynamic calculations:** Google Sheets recalculates the statistic and p-values as you modify
  your practice data.

#### Moving to the t-test

As you prepare your report, your supervisor sends a question: "The population SD was stipulated
for this exercise. What if we did not know it? Recalculate using the sample SD and a t-test."
You open your spreadsheet again to see how estimating SD changes the result. The reason for this
change is the unknown population SD, rather than a sample-size cutoff.

Ask the instructor for the next tutorial link.
