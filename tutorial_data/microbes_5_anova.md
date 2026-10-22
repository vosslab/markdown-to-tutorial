# Microbial diversity ANOVA

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The
ecological story is a hypothesis for practice; the supplied artifacts do not establish a real
field-study provenance or a causal effect of urbanization.

## Workbook

### Sheet: 30 Year ANOVA Test

| `"Sample\nID"` | `"1994\nShannon\nIndices"` | `"2004\nShannon\nIndices "` | `"2009\nShannon\nIndices "` | `"2014\nShannon\nIndices "` | `"2024\nShannon\nIndices "` | "." |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.0 | 3.66 | 4.96 | 5.43 | 1.754 | 2.413 |  |  |  |  |  |  |  |
| 2.0 | 3.98 | 5.12 | 5.43 | 3.173 | 3.853 |  |  |  |  |  |  |  |
| 3.0 | 5.0 | 3.78 | 3.82 | 2.226 | 2.645 |  |  |  |  |  |  |  |
| 4.0 | 5.0 | 3.73 | 4.026 | 5.345 | 4.871 |  |  |  |  |  |  |  |
| 5.0 | 3.56 | 5.0 | 6.099 | 2.598 | 2.357 |  |  |  |  |  |  |  |
| 6.0 | 5.0 | 5.54 | 6.461 | 5.588 | 4.281 |  |  |  |  |  |  |  |
| 7.0 | 5.0 | 4.91 | 2.551 | 4.504 | 3.433 |  |  |  |  |  |  |  |
| 8.0 | 6.21 | 4.26 | 2.713 | 1.927 | 2.876 |  |  |  |  |  |  |  |
| 9.0 | 3.22 | 3.85 | 3.786 | 4.552 | 4.415 |  |  |  |  |  |  |  |
| 10.0 | 3.62 | 5.0 | 3.104 | 2.623 | 3.46 |  |  |  |  |  |  |  |
| 11.0 |  | 2.99 | 3.707 | 3.768 | 2.64 |  |  |  |  |  |  |  |
| 12.0 |  | 2.67 | 5.818 | 4.97 | 5.009 |  |  |  |  |  |  |  |
| 13.0 |  | 5.0 | 3.428 | 5.657 | 4.885 |  |  |  |  |  |  |  |
| 14.0 |  | 5.0 | 5.484 | 3.059 | 2.805 |  |  |  |  |  |  |  |
| 15.0 |  | 3.32 | 3.365 | 4.08 | 4.733 |  |  |  |  |  |  |  |
| 16.0 |  |  | 1.493 | 5.585 | 4.452 |  |  |  |  |  |  |  |
| 17.0 |  |  | 4.233 | 4.245 | 2.749 |  |  |  |  |  |  |  |
| 18.0 |  |  | 3.166 | 3.959 | 3.635 |  |  |  |  |  |  |  |
| 19.0 |  |  | 4.987 | 3.84 | 4.371 |  |  |  |  |  |  |  |
| 20.0 |  |  | 6.796 | 6.341 | 4.906 |  |  |  |  |  |  |  |
| 21.0 |  |  |  | 4.254 | 3.985 |  |  |  |  |  |  |  |
| 22.0 |  |  |  | 3.668 | 3.849 |  |  |  |  |  |  |  |
| 23.0 |  |  |  | 4.623 | 3.521 |  |  |  |  |  |  |  |
| 24.0 |  |  |  | 6.505 | 4.982 |  |  |  |  |  |  |  |

## Tutorial

### Part 5: Scenario

- **Worksheet:** 30 Year ANOVA Test

![ANOVA.](assets/microbes_5_anova_image1.png)

After comparing the two recent years, you return to the older student theses. You now have
Shannon Index data spanning **30 years**, from **1994 to 2024**. With your advisor, you decide
to use **ANOVA (Analysis of Variance)** to compare five population means at once.

Extend the comparison to **1994, 2004, 2009, 2014, and 2024**. A one-way ANOVA tests H0: all five
population mean Shannon indices are equal; H1: at least one mean differs. The null model produces a
**right-tailed F test**. It tests differences among means, not whether variance changed or a decline
continued for 30 years.

The Shannon Index combines **richness** (the number of taxa detected) and **evenness**
(their relative abundances). It is calculated as **H = -sum(p_i ln(p_i))**, where p_i
is the proportion assigned to taxon i and ln is the natural logarithm. Higher values indicate
greater diversity at the chosen taxonomic
resolution; the index has no universal upper bound independent of community size and log base.
In the teaching scenario, soil microbial diversity at Busse Woods is estimated using SSU rRNA
sequencing. Urbanization motivates the questions, but these tests compare diversity summaries;
they cannot identify an environmental cause.

Choose the hypothesis and significance level **before inspecting results**. Use alpha = 0.05
throughout. This ANOVA has one right-tailed p-value; do not reinterpret it as a lower-tail or
two-tail variance comparison. A p-value is a probability of a result at least as extreme in the
specified
tail or tails, under the null model and its assumptions. It is not the probability that the null
hypothesis is true. Failure to reject means insufficient evidence for the alternative.

The classical model assumes independent observations, approximately normal residuals,
and a common population variance. Inspect distributions, outliers, and sampling design before
applying it. Matched sites need a model that respects dependence.

The historical part of this teaching scenario comes from older student thesis datasets collected
before modern sequencing was available. For **1994, 2004, and 2009**, the hypothetical projects
used culture-based methods: soil organisms were grown on selected media, colonies were counted and
described by visible features such as color, shape, and growth pattern, and isolates were examined
with staining methods such as Gram staining. The later **2014 and 2024** datasets represent SSU
rRNA sequencing. These methods observe different portions of microbial communities: cultivation
misses organisms that do not grow under the selected conditions, colony appearance does not uniquely
identify species, staining provides broad phenotypic categories, and a CFU is not necessarily one
cell. The historical narrative is a hypothetical teaching scenario, not verified provenance for
the supplied values. Method changes are confounded with year, so even an ANOVA difference would not
show that time or urbanization caused a biological change.

The ANOVA workbook's **2014 observations differ from Part 3/4**: analyze its supplied data as
a separate exercise; do not replace them with the two-year data.

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


#### Step 2: Organize Your Sheet into an ANOVA Table Layout

Construct the ANOVA table in **H1:M4**, leaving the raw data in **A:F** untouched. Column A contains
sample IDs; **B:F** contain years 1994, 2004, 2009, 2014, and 2024. Column G separates raw data and
results. The original dot in G1 is only a separator.

- **Label H1:** Source of Variation
- **Label I1:** Degrees of Freedom (DF)
- **Label J1:** Sum of Squares (SS)
- **Label K1:** Mean Square (MS)
- **Label L1:** F-Statistic
- **Label M1:** P-Value (Right-Tailed)
- **Label H2:** Between Groups
- **Label H3:** Within Groups
- **Label H4:** Total

#### Step 3: Calculate the Group Statistics

Build a second table in **H6:M9**. Calculate each year's sample **mean**, **variance**, and
**size**. `VAR.S` estimates sample variance using n - 1. Blank observations remain blank. The five
sample sizes should be **10, 15, 20, 24, 24**, a total of **93** observations.

- **Label H6:** Sample Name
- **Label I6:** 1994 Sample
- **Label J6:** 2004 Sample
- **Label K6:** 2009 Sample
- **Label L6:** 2014 Sample
- **Label M6:** 2024 Sample
- **Label H7:** Sample Means
- **Label H8:** Sample Variances
- **Label H9:** Sample Sizes
- **Enter I7:** `=AVERAGE(B2:B101)`
- **Enter J7:** `=AVERAGE(C2:C101)`
- **Enter K7:** `=AVERAGE(D2:D101)`
- **Enter L7:** `=AVERAGE(E2:E101)`
- **Enter M7:** `=AVERAGE(F2:F101)`
- **Enter I8:** `=VAR.S(B2:B101)`
- **Enter J8:** `=VAR.S(C2:C101)`
- **Enter K8:** `=VAR.S(D2:D101)`
- **Enter L8:** `=VAR.S(E2:E101)`
- **Enter M8:** `=VAR.S(F2:F101)`
- **Enter I9:** `=COUNT(B2:B101)`
- **Enter J9:** `=COUNT(C2:C101)`
- **Enter K9:** `=COUNT(D2:D101)`
- **Enter L9:** `=COUNT(E2:E101)`
- **Enter M9:** `=COUNT(F2:F101)`

#### Step 4: Calculate the Grand Mean

The **grand mean** is the average of all 93 observations, so each observation has equal weight.
Because group sizes differ, do not take the unweighted average of the five group means.
`AVERAGE(B2:F101)` ignores blanks and supplies the correctly weighted grand mean.

- **Label H11:** Grand Mean
- **Enter I11:** `=AVERAGE(B2:F101)`

#### Step 5: Calculate the Degrees of Freedom (DF)

Let **k = 5** groups and **N = 93** total observations. Between-group df is k - 1 = **4**;
within-group df is N - k = **88**; total df is N - 1 = **92**. Check that between + within = total.

- **Enter I2:** `=COUNT(I7:M7) - 1`
- **Enter I3:** `=COUNT(B2:F101) - COUNT(I7:M7)`
- **Enter I4:** `=COUNT(B2:F101) - 1`

#### Step 6: Calculate the Regression Sum of Squares (SSR)

The **between-group sum of squares**, also called regression sum of squares (SSR) here, sums n times
(group mean - grand mean) squared across years. `SUMPRODUCT` multiplies each squared deviation by
its matching group size, then adds the products. Use the group table, preserving the year order.

- **Enter J2:** `=SUMPRODUCT((I7:M7 - I11)^2, I9:M9)`

#### Step 7: Calculate the Error Sum of Squares (SSE)

The **within-group sum of squares**, or error sum of squares (SSE), sums (n - 1) times sample
variance across years. This equals the sum of squared deviations of observations from their own
group means. It describes variation remaining within years, not a proven random or biological cause.

- **Enter J3:** `=SUMPRODUCT((I9:M9 - 1), I8:M8)`

#### Step 8: Calculate the Total Sum of Squares (SST)

The **total sum of squares (SST)** equals SSR + SSE. It also equals the sum of squared deviations of
all observations from the grand mean. The two components partition total variation into between-year
and within-year contributions.

- **Enter J4:** `=J2 + J3`

#### Step 9: Calculate the Mean Square (MS)

Divide each sum of squares by its corresponding df to obtain a **mean square**. Between-group MS and
within-group MS are the two components of the ANOVA F-statistic. Total MS is not needed for this
test.

- **Enter K2:** `=J2/I2`
- **Enter K3:** `=J3/I3`

#### Step 10: Calculate the F-Statistic

The ANOVA **F-statistic** is between-group MS / within-group MS. Under equal population means, both
estimate the common variance. A large ratio is evidence against equality of means; it does not
identify which means differ.

- **Enter L2:** `=K2/K3`

#### Step 11: Calculate the P-Value

The ANOVA p-value uses the **right tail** only: large F values oppose the equality-of-means null.
`F.DIST.RT` takes F from **L2**, numerator df from **I2**, and denominator df from **I3**. Unlike
Part 4, this is not a two-tail test of two variances.

- **Enter M2:** `=F.DIST.RT(L2, I2, I3)`

#### Step 12: Decision Using an IF Statement

Use `IF` to compare the right-tail p-value in **M2** with alpha **0.05**. Reject if p <= alpha;
otherwise fail to reject. Choose alpha before evaluating the result.

- **Label H13:** Significance Level (alpha)
- **Label H14:** Decision
- **Enter I13:** 0.05
- **Enter I14:** `=IF(M2 <= I13, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

#### Step 13: Interpret the Results

The original data give **F about 0.87893**, df **4, 88**, and **right-tail p about 0.47999**. Fail
to reject at 0.05: evidence is insufficient to conclude that the five population mean Shannon
indices differ. This does not demonstrate stable or identical means. A significant result would
support at least one differing mean, requiring planned comparisons or appropriately adjusted
post-hoc tests to locate differences. Neither outcome establishes a monotonic time trend or an
environmental cause.

- **Label H16:** Interpretation

- **Explain:** Write your interpretation in `I16`. Include the p-value, tail and alternative, alpha, and the evidence-based conclusion. If p > alpha, state that evidence is insufficient; do not claim equality or absence of an effect.

#### Practice: Explore sensitivity

Save a separate practice copy after recording the original result. Treat modified observations
as hypothetical examples, not newly collected evidence.

- **Change:** Modify a few values in columns B:F (the five year columns). Compare the mean, SD or variance, statistic, p-value, and decision before and after. Explain which quantities changed and why.
- **Add:** Enter hypothetical numeric observations in blank cells within rows 2:101 of the raw-data columns. Check the updated counts; leave unobserved entries blank. Compare adding values near a group mean with adding extreme values.
- **Compare:** Discuss how sample size, effect size, variability, and assumptions influence the result. More observations can reduce standard errors under the model, but do not guarantee a smaller p-value or repair biased or dependent observations.

#### Key Takeaways

- **ANOVA** compares multiple population means at once by comparing variation between groups
  with variation within groups.
- The **right-tail p-value** tests whether all five population means are equal; a rejection
  supports at least one difference and requires follow-up comparisons to locate it.
- **Sample size:** It affects precision, but larger samples do not repair dependence, biased sampling,
  or differences in measurement methods.
- **Comparing years:** This does not by itself establish a time trend or an environmental cause.
