# Microbial diversity ANOVA

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The ecological story is a hypothesis for practice; the supplied artifacts do not establish a real field-study provenance or a causal effect of urbanization.

## Workbook

### Sheet: 30 Year ANOVA Test

| `"Sample\nID"` | `"1994\nShannon\nIndices"` | `"2004\nShannon\nIndices "` | `"2009\nShannon\nIndices "` | `"2014\nShannon\nIndices "` | `"2024\nShannon\nIndices "` | "." | "Source of Variation" | "Degrees of Freedom (DF)" | "Sum of Squares (SS)" | "Mean Square (MS)" | "F-Statistic" | "P-Value" |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.0 | 3.66 | 4.96 | 5.43 | 1.754 | 2.413 |  | "Between Groups" |  |  |  |  |  |
| 2.0 | 3.98 | 5.12 | 5.43 | 3.173 | 3.853 |  | "Within Groups" |  |  |  |  |  |
| 3.0 | 5.0 | 3.78 | 3.82 | 2.226 | 2.645 |  | "Total" |  |  |  |  |  |
| 4.0 | 5.0 | 3.73 | 4.026 | 5.345 | 4.871 |  |  |  |  |  |  |  |
| 5.0 | 3.56 | 5.0 | 6.099 | 2.598 | 2.357 |  | "Sample Name" | "1994 Sample" | "2004 Sample" | "2009 Sample" | "2014 Sample" | "2024 Sample" |
| 6.0 | 5.0 | 5.54 | 6.461 | 5.588 | 4.281 |  | "Sample Means" |  |  |  |  |  |
| 7.0 | 5.0 | 4.91 | 2.551 | 4.504 | 3.433 |  | "Sample Variances" |  |  |  |  |  |
| 8.0 | 6.21 | 4.26 | 2.713 | 1.927 | 2.876 |  | "Sample Sizes" |  |  |  |  |  |
| 9.0 | 3.22 | 3.85 | 3.786 | 4.552 | 4.415 |  |  |  |  |  |  |  |
| 10.0 | 3.62 | 5.0 | 3.104 | 2.623 | 3.46 |  | "Grand Mean" |  |  |  |  |  |
| 11.0 |  | 2.99 | 3.707 | 3.768 | 2.64 |  |  |  |  |  |  |  |
| 12.0 |  | 2.67 | 5.818 | 4.97 | 5.009 |  | "Significance Level (\u03b1)" |  |  |  |  |  |
| 13.0 |  | 5.0 | 3.428 | 5.657 | 4.885 |  | "Decision" |  |  |  |  |  |
| 14.0 |  | 5.0 | 5.484 | 3.059 | 2.805 |  |  |  |  |  |  |  |
| 15.0 |  | 3.32 | 3.365 | 4.08 | 4.733 |  | "Interpretation" |  |  |  |  |  |
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

![][image1]

### Part 5: Scenario

- **Worksheet:** 30 Year ANOVA Test

After successfully rejecting the **null hypothesis** using the **F-test**, you confirmed that microbial diversity in Busse Woods not only decreased between 2014 and 2024 but also became more **uniform**. However, this raised new questions: Has this pattern of declining diversity and reduced variability been happening for even longer? To investigate, you now have microbial diversity data spanning **30 years**, from **1994 to 2024**.

To analyze how microbial diversity has shifted over time, you decide to use **ANOVA** (Analysis of Variance). This statistical test will allow you to compare microbial diversity across **five different time points**: **1994**, **2004**, **2009**, **2014**, and **2024**. Comparing these years extends the investigation, while separating a general difference in means from a specific directional trend or period of stability.

Why Use ANOVA Now?

**ANOVA** is ideal for comparing more than two groups, making it the perfect tool for analyzing microbial diversity across multiple years. This test will help determine whether the **diversity values** have changed significantly over time by comparing the **variance** within each year to the **variance** between the years. The omnibus test asks whether at least one mean differs. It does not directly test temporal trend or homogenization of community composition.


The main directional hypothesis is chosen **before inspecting results**. Computing additional tails here is a teaching comparison; do not select whichever p-value is smallest. A p-value is a probability under the null model, not the probability that the null is true or that urbanization caused a change. Failure to reject does not prove equality or absence of ecological effects. Samples must represent the target population and be sufficiently independent; inspect distributions and outliers. Larger sample size alone cannot repair biased sampling.

The one-way ANOVA null is equality of all **five population means**; the alternative is that at least one differs. Its p-value is always the **right tail** of F. This classical model assumes independent observations, approximately normal residuals, and a common population variance. The year sample sizes are **10, 15, 20, 24, and 24**, respectively. Matching sites or measurements would require a dependence-aware model. Different culture and sequencing methods in the story can confound a year comparison; colony appearance or Gram stain alone cannot accurately identify every microbial species. The provided ANOVA 2014 values are different from the two-year comparison 2014 values: retain each original dataset and do not silently substitute.

#### Step 1: Copy the Data

- **Open:** Open the generated XLSX workbook in Google Sheets and select the worksheet named above. The complete source data is already included; do not paste another copy over it.

The original course data remains available in the [shared source workbook](https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit). For manual copying, use the tab menu, choose Copy to > Existing spreadsheet, paste your target spreadsheet link, select it, and insert. Rename the copied tab to match the worksheet named above. Personal copies can receive different URLs.

![][image2]

The raw observations retain their original addresses. Rows 2 through 25 contain the 24 current samples; the calculation ranges deliberately extend through row 101 for practice additions. In ANOVA, earlier years have fewer observations and blank cells are not zeroes.


#### Step 2: Organize Your Sheet into an ANOVA Table Layout


In this step, we will set up a traditional ANOVA table with **source of variation**, **sum of squares (SS)**, **degrees of freedom (DF)**, **mean square (MS)**, **F-statistic**, and **P-value**.

**ANOVA Table Setup:**

- **Guide:** **Column A-F**: Your raw data for each year (1994, 2004, 2009, 2014, and 2024).
- **Guide:** **Column G**: this separates the data from the calculations; the source template retains a dot in `G1`
- **Guide:** **Column H**: This column will be used to label the **sources of variation** in the ANOVA.
- **Guide:** **Columns I-M**: These columns will contain the calculated values for sums of squares, degrees of freedom, mean squares, F-statistic, and p-value.


- **Guide:** In **Column H**, create the row headers for the **ANOVA table**:
- **Guide:** In **Column I**, add the following column headers:
- **Guide:** The final table should look something like this

| Source of Variation | Degrees of Freedom (DF) | Sum of Squares (SS) | Mean Square (MS) | F-Statistic | P-Value |
| :---: | ----- | ----- | ----- | ----- | ----- |
| **Between Groups** |  |  |  |  |  |
| **Within Groups** |  |  |  |  |  |
| **Total** |  |  |  |  |  |


#### Step 3: Calculate the Group Statistics

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


The first step in an ANOVA test is to calculate the basic statistics for each group (in this case, each year). You need to calculate the **mean**, **variance**, and **sample size** for each group. These statistics will help us understand how each group differs individually before comparing them across time.


We will set up another table to organize the **group statistics** for each year.

- **Guide:** **Setup Another Table:**
- **Guide:** **For Sample Means:**
- **Guide:** **For Sample Variances:**
- **Guide:** **For Sample Sizes:**

Explanation:

This step focuses on calculating the **group statistics**: the **means**, **variances**, and **sample sizes** for each year&#8217;s data. These values will be crucial for the ANOVA test because they allow us to assess how each group behaves individually. The **means** show us the average microbial diversity in each year, while the **variances** tell us how much the data is spread out within each year. Finally, the **sample sizes** help evaluate the reliability of these statistics for each year.

These statistics will feed into the next step, where we calculate the **sums of squares** and start filling out the ANOVA table.


#### Step 4: Calculate the Grand Mean

- **Enter I11:** `=AVERAGE(B2:F101)`


In this step, you will calculate the **grand mean**, which is the overall average of all data points across the different groups. The grand mean helps you compare individual group means to the overall dataset. It serves as a reference point for future steps, such as calculating the total variability and assessing how much each group deviates from the overall dataset. You will calculate the grand mean using the **AVERAGE** function to capture the mean of all values in the dataset.


#### Step 5: Calculate the Degrees of Freedom (DF)

- **Enter I2:** `=COUNT(I7:M7) - 1`
- **Enter I3:** `=COUNT(B2:F101) - COUNT(I7:M7)`
- **Enter I4:** `=COUNT(B2:F101) - 1`


In this step, you will calculate the **Degrees of Freedom (DF)** for both the **between groups** (DF treatment) and **within groups** (DF error) components, as well as the **total DF**. The DF reflects the number of independent data points contributing to each variance estimate. In ANOVA, the DF for each component helps us understand the amount of information available for estimating the variability between and within groups.


Explanation:

The **Degrees of Freedom (DF)** reflect the number of independent values that contribute to the variance estimates in the ANOVA table. Here is how the different components of the DF are calculated:

- **Guide:** **DF Between (DF treatment)**: This is the degrees of freedom associated with the variability between groups (for example, between different years). It is calculated as the number of groups (**k**) minus one. The formula `=COUNT(I7:M7) - 1` counts the number of groups and subtracts one.
- **Guide:** **DF Within (DF error)**: This is the degrees of freedom associated with the variability within groups. It is calculated as the total number of observations (**n**) minus the number of groups (**k**). The formula `=COUNT(B2:F101) - COUNT(I7:M7)` calculates the total number of observations and subtracts the number of groups to give the DF within.
- **Guide:** **DF Total**: This is the total degrees of freedom, representing the total variability in the dataset. It is calculated as the total number of observations (**n**) minus one. The formula `=COUNT(B2:F101) - 1` calculates this directly.

The relationship between these degrees of freedom is: `DF Total = DF Between + DF Within`


#### Step 6: Calculate the Regression Sum of Squares (SSR)

- **Enter J2:** `=SUMPRODUCT((I7:M7 - I11)^2, I9:M9)`


In this step, you will calculate the **Regression Sum of Squares (SSR)**. This represents how much of the total variance is explained by the differences between the group means. The SSR helps quantify the portion of the total variation that can be attributed to the differences between the groups, such as the different years in your dataset.


- **Guide:** Go back up to our original table.

Explanation:

The **SSR** quantifies the variation between the group means and how much of the total variance can be explained by the differences between those means. By comparing the mean values of each group to the **grand mean** (the overall average), the **SSR** isolates the variance due to differences between the groups. This is calculated by summing the squared deviations of each group mean from the grand mean, weighted by the sample size of each group.

The **SUMPRODUCT** function multiplies corresponding elements from two arrays and sums the products. In this case, `(I7:M7 - I11)^2` calculates the squared differences between each group mean (from cells `I7:M7`) and the grand mean (in `I11`). The second array, `I9:M9`, contains the sample sizes for each group. **SUMPRODUCT** multiplies these squared differences by the respective sample sizes and sums them to yield the **SSR**, which tells us how much of the total variance is explained by the differences between the group means.


#### Step 7: Calculate the Error Sum of Squares (SSE)

- **Enter J3:** `=SUMPRODUCT((I9:M9 - 1), I8:M8)`


In this step, you will calculate the **Error Sum of Squares (SSE)**. This measures the variation within each group that cannot be explained by differences between the group means. It captures how much of the total variability is due to random differences within the groups.


Explanation:

The **SSE** quantifies the variability within the groups that is not explained by the differences between the group means. By calculating the squared deviations of each observation from the group mean, this step identifies the portion of variance due to random fluctuations within each group. Summing these squared deviations provides the **SSE**, which is essential for understanding how much of the total variation is due to within-group differences.


#### Step 8: Calculate the Total Sum of Squares (SST)

- **Enter J4:** `=J2 + J3`


In this step, you will calculate the **Total Sum of Squares (SST)**, which measures the overall variability in the dataset. The SST accounts for both the variability between the group means (SSR) and the variability within each group (SSE). It compares each data point to the **grand mean** to capture the total variance in the dataset.


Explanation:

The **Total Sum of Squares (SST)** measures the overall variance in the dataset by comparing each individual data point to the grand mean. It captures all the variability present in the data. The **SST** is broken down into two components:

- **Guide:** **SSR**: The portion of the total variance explained by the differences between the group means.
- **Guide:** **SSE**: The portion of the total variance that is due to random variability within the groups, not explained by the group means.

The relationship between these terms is: `SST = SSR + SSE`

By calculating the **SST**, you quantify the total variability in your dataset, which you will later partition into the components explained by group differences (SSR) and the remaining unexplained variation (SSE).


#### Step 9: Calculate the Mean Square (MS)

- **Enter K2:** `=J2/I2`
- **Enter K3:** `=J3/I3`


The **mean square (MS)** is calculated by dividing the **sum of squares (SS)** by the **degrees of freedom (DF)**. This represents the average variability for each source of variance (between groups and within groups).


Explanation:

The **mean squares (MS)** are the average variability per **degree of freedom** for each source of variance. The **MS Between** tells us how much variability is due to the differences between years, while the **MS Within** captures the average variability within each year. These values are crucial for calculating the **F-statistic** in the next step.


#### Step 10: Calculate the F-Statistic

- **Enter L2:** `=K2/K3`


Now that you have calculated the **F-statistic**, the next step is to determine whether the observed differences in microbial diversity between years are statistically significant. Under the null hypothesis and test assumptions, the p-value is the probability of a statistic at least as extreme as the observed statistic in the selected tail or tails. In an ANOVA, the p-value is calculated based on the **F-statistic** and the **degrees of freedom** for both the between groups and within groups components.


Explanation:

The **F-statistic** is the ratio of the **between groups variance** to the **within groups variance**. A larger F-statistic suggests that more of the variance is due to differences between years, and the greater the chance that the differences between the means are statistically significant. We will use the F-statistic in the next step to determine statistical significance.


#### Step 11: Calculate the P-Value

- **Enter M2:** `=F.DIST.RT(L2, I2, I3)`


Now that the F-statistic has been calculated, we can determine whether the differences in microbial diversity between the years are statistically significant by calculating the **P-value**. Under the null hypothesis and test assumptions, the p-value is the probability of a statistic at least as extreme as the observed statistic in the selected tail or tails. A smaller P-value (typically less than 0.05) indicates that the differences between the groups are statistically significant.


**Explanation:**

The **F.DIST.RT** function calculates the right-tailed probability of the F-distribution. This function takes the following inputs:

- **Guide:** The **F-statistic** (calculated in cell **L2**),
- **Guide:** **Degrees of freedom** between the groups (**I2**),
- **Guide:** **Degrees of freedom** within the groups (**I3**).

The result of this function gives us the **P-value**, which shows whether the differences in microbial diversity across the years (1994, 2004, 2009, 2014, and 2024\) are statistically significant. If the P-value is less than 0.05, you can conclude that the differences between the groups are significant, meaning that the year-to-year changes in microbial diversity are not likely due to random chance.


#### Step 12: Decision Using an IF Statement

- **Enter I13:** 0.05
- **Enter I14:** `=IF(M2 <= I13, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`


In hypothesis testing, the decision to **reject** or **fail to reject** the **null hypothesis** is based on the **p-value** and the significance level (**&#945;**) set before the test. In most cases, **&#945;** is 0.05. If the **p-value** is less than or equal to 0.05, the result is considered **statistically significant**, meaning that the variation in microbial diversity between the years is unlikely due to chance alone. To simplify this decision-making process in **Google Sheets**, we will use the **IF** statement to evaluate whether the **p-value** is less than or equal to the significance level (0.05).


Explanation

The **IF** statement evaluates whether the **p-value** (in **M2**) is less than or equal to **0.05** (the significance level). If the **p-value** is smaller than or equal to 0.05, you will **reject the null hypothesis**, indicating that the variation in microbial diversity across the years is statistically significant. If the **p-value** is greater than 0.05, you will **fail to reject the null hypothesis**, meaning the observed differences in diversity across the years could have occurred by chance.

This process simplifies the interpretation of your **ANOVA** results, ensuring that you can quickly assess whether there is a statistically significant difference in microbial diversity over the years.


#### Step 13: Interpret the Results

Interpret the ANOVA by comparing the **right-tailed p-value** in `M2` with 0.05. A significant result supports the conclusion that at least one population mean differs; a nonsignificant result provides insufficient evidence of a difference. ANOVA alone identifies neither the differing years, a monotonic time trend, a variance change, nor a cause such as urbanization or climate change.


- **Guide:** "With a **p-value** of \[calculated value\], we \[reject/fail to reject\] the null hypothesis, indicating that microbial diversity \[has/has not\] changed significantly over time."

Explanation:

For a significant ANOVA, conclude that the data support at least one difference among population mean Shannon indices. For a nonsignificant result, state that evidence is insufficient to distinguish the means. Neither outcome establishes which environmental mechanism produced the observations; planned comparisons or appropriately adjusted post-hoc tests are needed to locate differences.

Practice Task:

- **Guide:** Modify some of the Shannon Index values for the **1994**, **2004**, **2009**, **2014**, and **2024** data columns. Observe how the **sample means**, **F-statistic**, and **p-value** change.
- **Guide:** Add more sample numbers (increase the sample size) and note the impact on the **ANOVA** results.
- **Guide:** Discuss how sample size influences the **ANOVA** test and compare this to earlier F-test results.

Key Takeaways:

- **Guide:** **ANOVA** allows for the comparison of **multiple groups** at once, making it useful for assessing whether microbial diversity has changed over multiple decades.
- **Guide:** The **p-value** helps determine whether the differences in **microbial diversity** across years are **statistically significant**.
- **Guide:** A larger sample size provides more reliable results in both **ANOVA** and other statistical tests, reducing uncertainty.
- **Guide:** **ANOVA** tests equality of population means. It does not by itself establish a time trend, identify a cause, or compare variances.


- **Explain:** Write your own interpretation in `I16`. Include the calculated p-value, selected tail and alternative direction, significance level, and evidence-based conclusion. Do not type the example placeholders literally.

[image1]: assets/microbes_5_anova_image1.png
[image2]: assets/microbes_5_anova_image2.png
