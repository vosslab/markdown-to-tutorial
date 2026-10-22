# Microbial diversity two-sample t-test

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The ecological story is a hypothesis for practice; the supplied artifacts do not establish a real field-study provenance or a causal effect of urbanization.

## Workbook

### Sheet: Two Sample T-Test

| "Sample Location" | `"2014\nShannon\nIndex "` | `"2024\nShannon\nIndex "` | "Statistical Names" | "Values" |
| --- | --- | --- | --- | --- |
| "Andrews Park" | 4.417 | 2.413 |  |  |
| "Beisner Road Entrance" | 5.359 | 3.853 |  |  |
| "Boat Launch Area" | 1.984 | 2.645 |  |  |
| "Busse Lake" | 6.923 | 4.871 | 2014.0 |  |
| "Debra Park" | 1.412 | 2.357 | 2024.0 |  |
| "Elk Pasture" | 4.677 | 4.281 |  |  |
| "Forest Central Grove" | 4.26 | 3.433 | 2014.0 |  |
| "Forest North Grove" | 2.633 | 2.876 | 2024.0 |  |
| "Forest South Grove" | 3.429 | 4.415 |  |  |
| "Forest West Grove" | 2.965 | 3.46 | "F-statistic" |  |
| "Lake Boating Center" | 4.728 | 2.64 |  |  |
| "Large Event Area" | 6.944 | 5.009 | 2014.0 |  |
| "Main Dam" | 5.404 | 4.885 | 2024.0 |  |
| "Main Pool" | 4.612 | 2.805 |  |  |
| "Marshall Park" | 5.028 | 4.733 | "P-Value (Two-Tailed)" |  |
| "Model Airplane Field" | 5.949 | 4.452 | "P-Value (One-Tailed, Lower)" |  |
| "Nature Preserve" | 3.907 | 2.749 | "P-Value (One-Tailed, Higher)" |  |
| "Ned Brown Meadow" | 4.305 | 3.635 |  |  |
| "North Pool" | 4.665 | 4.371 | "Significance Level (\u03b1)" |  |
| "Osborn  Park" | 4.241 | 4.906 |  |  |
| "Salt Creek Trail" | 4.351 | 3.985 |  |  |
| "South Pool" | 3.791 | 3.849 |  |  |
| "Wildlife Refuge" | 4.079 | 3.521 |  |  |
| "Woodland Meadow" | 6.565 | 4.982 |  |  |

## Tutorial

![][image1]

### Part 3: Scenario

- **Worksheet:** Two Sample T-Test

Now that you have reanalyzed the microbial diversity in **Busse Woods** using a **T-test**, you have noticed the results did not support the significant difference that was initially found using the **Z-test**. This has raised new questions about whether **Busse Woods** is evolving under environmental pressures, such as **urbanization** and **climate change**.

However, rather than discarding the results, your advisor suggests a more insightful comparison: analyzing the changes in **microbial diversity** over time. By comparing the data from **2014** with your current data from **2024**, you can determine whether the diversity has decreased over the past decade. The **Two Sample T-test** will help you assess whether urbanization and other environmental factors are contributing to a decline in microbial biodiversity.

Why Use a Two Sample T-Test Now?

Unlike the earlier **T-test**, where you compared the current microbial diversity to a benchmark, the **Two Sample T-test** allows you to directly compare two different datasets&#8212;**2014** and **2024**&#8212;to determine if there has been a significant change over time. This test is ideal when comparing two groups or time periods, especially when working with relatively small sample sizes.


The main directional hypothesis is chosen **before inspecting results**. Computing additional tails here is a teaching comparison; do not select whichever p-value is smallest. A p-value is a probability under the null model, not the probability that the null is true or that urbanization caused a change. Failure to reject does not prove equality or absence of ecological effects. Samples must represent the target population and be sufficiently independent; inspect distributions and outliers. Larger sample size alone cannot repair biased sampling.

The source lists the **same 24 named locations in both years**. This exercise demonstrates an **independent-samples** method only under an explicit working assumption of independence across years; the file alone cannot establish it. If these are repeated measurements at matched sites, a paired t-test (for means) or another method respecting dependence is needed. Do not treat matching row labels as evidence of independence.

The signed t-statistic is **2024 mean minus 2014 mean**: negative values favor the lower alternative. `T.TEST(...,1,3)` returns a small tail associated with the magnitude, so the `IF` formulas use the sign to return the requested lower or higher directional p-value. Check fractional Welch degrees of freedom when comparing spreadsheet engines: some distribution-function implementations truncate them. Preserve the computed noninteger value in `E13` and report any numerical discrepancy rather than assuming perfect equivalence.

#### Step 1: Set Up Your Google Sheet for the Two Sample T-Test

- **Open:** Open the generated XLSX workbook in Google Sheets and select the worksheet named above. The complete source data is already included; do not paste another copy over it.

The original course data remains available in the [shared source workbook](https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit). For manual copying, use the tab menu, choose Copy to > Existing spreadsheet, paste your target spreadsheet link, select it, and insert. Rename the copied tab to match the worksheet named above. Personal copies can receive different URLs.

The raw observations retain their original addresses. Rows 2 through 25 contain the 24 current samples; the calculation ranges deliberately extend through row 101 for practice additions. In ANOVA, earlier years have fewer observations and blank cells are not zeroes.


#### Step 2: Organize Your Sheet

- **Label F1:** Alternate Values 1
- **Label G1:** Alternate Values 2


- **Guide:** The data will look like this:
- **Guide:** **Column A**: Sample Location ID
- **Guide:** **Column B**: **2014 Shannon Index** (microbial diversity from the 2014 dataset)
- **Guide:** **Column C**: **2024 Shannon Index** (current microbial diversity data)
- **Guide:** **Column D**: Statistical Names
- **Guide:** **Columns E through G**: Calculated Values
- **Guide:** Here&#8217;s how to set it up:


#### Step 3: Calculate the Sample Statistics

- **Label D2:** 2014 Sample Mean
- **Enter E2:** `=AVERAGE(B2:B101)`
- **Label D3:** 2024 Sample Mean
- **Enter E3:** `=AVERAGE(C2:C101)`
- **Replace D5:** 2014 Sample Standard Deviation
- **Enter E5:** `=STDEV(B2:B101)`
- **Replace D6:** 2024 Sample Standard Deviation
- **Enter E6:** `=STDEV(C2:C101)`
- **Replace D8:** 2014 Sample Size
- **Enter E8:** `=COUNT(B2:B101)`
- **Replace D9:** 2024 Sample Size
- **Enter E9:** `=COUNT(C2:C101)`


Now, let us calculate the statistics needed for both datasets.

- **Guide:** **Sample Means**:
- **Guide:** **Sample Standard Deviations**:
- **Guide:** **Sample Sizes**:


#### Step 4: Calculate the T-Statistic

- **Replace D11:** T-Statistic
- **Enter E11:** `=(E3 - E2) / SQRT((E5^2/E8) + (E6^2/E9))`


Now, we will calculate the **T-statistic** for both the 2014 and 2024 datasets to better understand how far the sample means are from each other.


Explanation: T-Statistic

The **T-statistic** measures how far the sample means of 2014 and 2024 are from each other, relative to the variability in both samples. This is done by comparing the difference between the two means to the combined standard error, which accounts for both sample variances and sizes. A larger **absolute T-statistic** indicates a greater difference between the means relative to the variability, while a smaller **T-statistic** suggests that the difference could be due to random variation. This allows us to determine whether the observed difference between the two years is statistically significant.


#### Step 5: Calculate the Degrees of Freedom

- **Replace D13:** Degrees of Freedom
- **Enter E13:** `=((E5^2/E8) + (E6^2/E9))^2 / ((E5^4/((E8^2)*(E8-1))) + (E6^4/((E9^2)*(E9-1))))`


In a **Two Sample T-test**, calculating the degrees of freedom is more complex than simply subtracting one from each sample size, as in a one-sample test. Instead, the degrees of freedom are calculated using the **Welch-Satterthwaite equation**, which adjusts for differences in sample sizes and variances between the two groups being compared. This adjustment is especially important in biological and environmental studies, where unequal sample sizes and variances are common.


Explanation: Why Use the Welch-Satterthwaite Equation?

The **Welch-Satterthwaite equation** combines the variances (squared standard deviations) and sample sizes of both groups, adjusting the degrees of freedom based on the ratio of the variances to their respective sample sizes. This approach accounts for differences in variability between the two groups and uses each variance divided by its own sample size to account for unequal standard errors. The adjustment ensures that the T-test is more conservative when there is greater uncertainty, such as when variances differ widely or sample sizes are small. In molecular biology, where variation in experimental data is common, this method provides a more reliable estimate of whether observed changes are statistically significant.

The formula you used in the spreadsheet automatically adjusts for the differences in your sample variances and sizes, giving you a Welch approximate degrees of freedom value. This ensures that your test results account for the natural variability in microbial diversity between 2014 and 2024, providing a clearer interpretation of statistical significance.

Example of Adjustments:

To better understand how the Welch-Satterthwaite equation accommodates different sample sizes and variances, consider the following scenarios:

| Name | Sample 1 Variance | Sample 1 Size | Sample 2 Variance | Sample 2 Size | Welch Degrees of Freedom |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Both variances and sizes equal | 0.5 | 50 | 0.5 | 50 | 98.00 |
| Larger Sample 1 size, same variance | 0.5 | 50 | 0.5 | 25 | 48.11 |
| Much larger Sample 1 size, same variance | 0.5 | 50 | 0.5 | 10 | 12.87 |
| Same sample size, smaller Sample 2 variance | 0.5 | 50 | 0.4 | 50 | 96.80 |
| Same sample size, much smaller Sample 2 variance | 0.5 | 50 | 0.2 | 50 | 82.79 |
| Both variances and sizes unequal | 0.5 | 50 | 0.3 | 25 | 60.19 |

When both variances and sample sizes are equal, the **Welch-Satterthwaite equation** simplifies to the standard T-test formula for degrees of freedom. For two samples of 50, degrees of freedom are calculated as (50&#8722;1) \+ (50&#8722;1) \= 98\. This reflects the independent values in both groups. Each sample size is reduced by one to account for the population mean estimation. In this balanced scenario, no additional adjustment is needed.
![][image2]

As degrees of freedom increase, the **T-distribution** becomes closer to a **normal distribution**. With more degrees of freedom, the test is more precise. Smaller degrees of freedom result in a wider T-distribution with fatter tails. This reflects greater uncertainty. When variances differ or sample sizes are small, the test becomes more conservative. A larger difference is needed to reject the null hypothesis.

In biological studies, this is important since sample sizes are often small. Lower degrees of freedom make it harder to detect significant results. This means the test is less sensitive. As degrees of freedom increase, the test becomes more reliable. This allows for better conclusions about differences between groups.


#### Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)


In the **Two Sample T-test** comparing microbial diversity between 2014 and 2024, you need to decide if you are testing for any significant difference between the two years (a **two-tailed test**) or for a specific directional change (a **one-tailed test**).

- **Guide:** **Two-Tailed Test**: Use this when you want to determine if microbial diversity has significantly changed in **either direction** between 2014 and 2024\. This test considers whether the diversity is **either higher or lower** in 2024 compared to 2014\.
- **Guide:** **One-Tailed Test**: Use this when you have a specific hypothesis about the direction of the change. For example:
- **Guide:** **Lower One-Tailed Test**: This test checks whether microbial diversity in 2024 is **lower** than in 2014, which may be relevant if you suspect urbanization has decreased biodiversity.
- **Guide:** **Higher One-Tailed Test**: This test checks whether microbial diversity in 2024 is **higher** than in 2014, which could help assess whether biodiversity has unexpectedly increased.

In this case, you likely hypothesize that urbanization has **reduced** diversity, so a **lower one-tailed test** would be appropriate. However, both directions can be tested for a complete analysis.


#### Step 7: Calculate the P-Values


Now that you have two sets of data (2014 and 2024 Shannon Index values), the next step is to calculate the **p-values** to assess whether the differences in microbial diversity between these two years are statistically significant. A **p-value**, under the null hypothesis and assumptions, measures the probability of a statistic at least as extreme as observed in the selected tail or tails. If the p-value is below **0.05**, the difference is considered **statistically significant**.

In this step, you will calculate p-values for **two-tailed** and **one-tailed tests** (lower and higher). Each test evaluates whether microbial diversity has changed in either direction or specifically increased or decreased. You will use both **manual calculations** and the **T.TEST** function. The **T.TEST** function simplifies the process now that you are comparing two samples, which was not available for one-sample T-tests in Part 2\.

Explanation of T.DIST Inputs:

The function **`T.DIST`** calculates the **cumulative probability** for a given **t-statistic** and degrees of freedom. It is useful for both one-tailed and two-tailed tests, depending on how you handle the results. Here are the inputs:

- **Guide:** **T.DIST(x, degrees\_freedom, cumulative)**
- **Guide:** **x**: This is the **t-statistic**, which represents how far the sample mean of 2024 is from the sample mean of 2014, relative to the standard error.
- **Guide:** **degrees\_freedom**: This refers to the **degrees of freedom** of the two samples, calculated based on the Welch-Satterthwaite formula or a simpler approach if variances and sample sizes are equal.
- **Guide:** **cumulative**: This specifies whether you want the **cumulative distribution function** (TRUE) or the **probability density function** (FALSE). You will use TRUE for calculating the cumulative probability.

In the case of a **two-tailed test**, you double the smaller tail probability, equivalently the upper tail beyond the absolute t-statistic to account for both tails of the distribution.

Explanation of T.TEST Inputs:

The function **`T.TEST`** simplifies the T-test by comparing the means of two datasets directly and returning the **p-value**. This function is useful for one-tailed or two-tailed tests, depending on the hypothesis. Here are the inputs:

- **Guide:** **T.TEST(array1, array2, tails, type)**
- **Guide:** **array1**: This is the range of values for the first dataset (e.g., the 2014 Shannon Index values in column B).
- **Guide:** **array2**: This is the range of values for the second dataset (e.g., the 2024 Shannon Index values in column C).
- **Guide:** **tails**: This determines whether the test is **one-tailed (1)** or **two-tailed (2)**. For a one-tailed test, use 1; for a two-tailed test, use 2\.
- **Guide:** **type**: This specifies the type of T-test. Use **3** for the independent two-sample unequal-variance (Welch) test used here. Type **2** instead assumes equal variances; type **1** is paired.

The **T.TEST** function returns the **p-value**, which tells you whether the difference in means between the two datasets is statistically significant. A p-value less than 0.05 suggests that the difference is not due to random variation and is likely significant.

##### Substep 7.1: Two-Tailed Test:

- **Enter E16:** `=T.DIST.2T(ABS(E11), E13)`
- **Enter F16:** `=2 * (1 - T.DIST(ABS(E11), E13, TRUE))`
- **Enter G16:** `=T.TEST(C2:C101, B2:B101, 2, 3)`

This section will guide you through performing a **two-tailed test**. A two-tailed test evaluates whether microbial diversity in 2024 is significantly **higher or lower** than in 2014\. This test is used when there is no specific hypothesis about the direction of the difference, meaning the goal is to detect any significant change, whether it is an increase or a decrease.

Both a **manual calculation** and the **T.TEST** function will be used. The manual calculation will help you understand the process by breaking down the **T-statistic** and degrees of freedom. The **T.TEST** function simplifies the task by calculating the p-value directly, allowing for a quicker comparison between the two datasets.


- **Guide:** This calculates the p-value for the two-tailed test using the absolute value of the T-statistic and degrees of freedom.
- **Guide:** This calculates the cumulative probability for one tail and then multiplies it by 2 to account for both tails.
- **Guide:** This directly compares the two datasets (Shannon Index for 2014 in column **B** and 2024 in column **C**) and calculates the two-tailed p-value automatically.

Explanation for Two-Tailed Test:

In a **two-tailed test**, you are checking whether the **microbial diversity** in 2024 is significantly **higher or lower** than in 2014\. The `T.DIST.2T` function automatically calculates the p-value for both tails, accounting for deviations in either direction. The more manual method using `T.DIST` requires calculating the cumulative probability for one tail, subtracting it from 1 to capture the upper tail, and then multiplying by 2 to account for both tails.

Since you are now working with two samples in Part 3, you can use the **T.TEST** function, which simplifies the process significantly. Unlike in Part 2 (where only one sample was available), **T.TEST** directly compares the two datasets (2014 vs. 2024). It calculates the p-value automatically, saving time and reducing errors, while still allowing students to understand the underlying steps involved in manual calculations.

##### Substep 7.2: One-Tailed Test (for lower values):

- **Enter E17:** `=T.DIST(E11, E13, TRUE)`
- **Enter G17:** `=IF(E11 <= 0, T.TEST(C2:C101, B2:B101, 1, 3), 1 - T.TEST(C2:C101, B2:B101, 1, 3))`

This section focuses on performing a **one-tailed test** to determine if microbial diversity in 2024 is **lower** than in 2014\. A one-tailed test is used when there is a specific hypothesis. In this case, the hypothesis is that diversity has decreased due to environmental factors like **urbanization** or **climate change**.

Both the **manual calculation** and **T.TEST** function will be used to assess if there is a significant difference between 2014 and 2024\. The manual calculation will show how the cumulative probability for the **lower tail** of the distribution is derived. The **T.TEST** function provides a quicker way to compute the same result, offering both clarity and efficiency.


- **Guide:** This calculates the cumulative probability for values less than or equal to the T-statistic, focusing on the lower tail.
- **Guide:** This calculates the one-tailed p-value automatically, testing whether microbial diversity has significantly decreased.

##### Substep 7.3: One-Tailed Test (for higher values):

- **Enter E18:** `=1 - T.DIST(E11, E13, TRUE)`
- **Enter F18:** `=T.DIST(-E11, E13, TRUE)`
- **Enter G18:** `=IF(E11 >= 0, T.TEST(C2:C101, B2:B101, 1, 3), 1 - T.TEST(C2:C101, B2:B101, 1, 3))`

This section will test whether microbial diversity has **increased** between 2014 and 2024\. The focus will be on conducting a **one-tailed test** that checks for a significant **increase** in diversity. This test is useful when the hypothesis suggests that external factors, such as improved environmental conditions, have positively impacted microbial diversity over the years.

Both the **manual calculation** and the **T.TEST** function will be used here. The manual method involves calculating the probability of obtaining a T-statistic greater than or equal to the observed value, while the **T.TEST** function offers a faster alternative, calculating the p-value automatically to assess potential increases in diversity.


- **Guide:** This calculates the probability of obtaining a T-statistic greater than or equal to the observed value, focusing on the upper tail.
- **Guide:** This calculates the cumulative probability for the lower tail, which is then subtracted from 1 to get the probability for the upper tail.
- **Guide:** This calculates the one-tailed p-value automatically, testing whether microbial diversity has significantly increased.


#### Step 8: Decision Using an IF Statement

- **Label D21:** Significance Level (alpha)
- **Enter E21:** 0.05
- **Label D22:** Two-Tail Decision
- **Enter E22:** `=IF(E16 <= E21, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label D23:** One-Tail Decision (Lower)
- **Enter E23:** `=IF(E17 <= E21, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label D24:** One-Tail Decision (Higher)
- **Enter E24:** `=IF(E18 <= E21, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`


In hypothesis testing, the decision to **reject** or **fail to reject** the **null hypothesis** depends on comparing the **p-value** to a predetermined **significance level** (&#945;). The significance level is often set at **0.05**, meaning that if the p-value is less than or equal to 0.05, the result is considered **statistically significant**. This would indicate that the difference between the **2014** and **2024 Shannon Index** values is unlikely to have occurred by chance. To simplify this decision process, we will use the **IF statement** in Google Sheets, which evaluates a condition and returns one value if the condition is true and another if it is false. In this case, we will check if the p-value is less than or equal to &#945; (0.05).


- **Guide:** to determine whether to reject the null hypothesis using the two-tailed test p-value.
- **Guide:** to determine whether to reject the null hypothesis using the one-tailed (lower) test p-value.
- **Guide:** to determine whether to reject the null hypothesis using the one-tailed (higher) test p-value.

Explanation

The **IF statement** in Google Sheets evaluates a condition&#8212;in this case, whether the **p-value** is less than or equal to the **significance level** (&#945;). If the p-value is less than or equal to **0.05**, the result is considered **statistically significant**, and you should **reject the null hypothesis**. This means that there is sufficient evidence to conclude that the **2014** and **2024 Shannon Index** values are **significantly different**.

For example, if the **two-tailed test** p-value is less than or equal to **0.05**, it suggests that **microbial diversity** in Busse Woods has changed significantly between 2014 and 2024\. Conversely, if the p-value is higher than **0.05**, you will **fail to reject the null hypothesis**, implying that the diversity has not changed significantly over time.

This automated decision-making process simplifies hypothesis testing, ensuring that you can quickly assess whether **environmental factors** have impacted microbial diversity in Busse Woods.


#### Step 9: Interpret the Results

- **Label D26:** Interpretation


At this point, you should have conducted both the **two-tailed** and **one-tailed tests** (lower and higher) to compare microbial diversity in **2014** and **2024**. You should have determined that the focus is on the **One-Tailed Test (Lower)** to assess whether microbial diversity in **Busse Woods** has significantly **decreased** between **2014** and **2024**. You are specifically testing whether diversity has declined due to **urbanization** or other **environmental pressures**. The goal is to see if the data supports the hypothesis that microbial diversity has declined.


Explanation:

In hypothesis testing, the interpretation depends on comparing the **p-value** to the **significance level** (&#945; \= 0.05). If the p-value is **less than or equal to 0.05**, the result is considered **statistically significant**, meaning the null hypothesis is **rejected**. Rejecting the null hypothesis in this context suggests that microbial diversity in **Busse Woods** is significantly **lower** in **2024** compared to **2014**. This implies that **environmental factors** like **urbanization** or **climate change** may have reduced biodiversity in the area.

If the p-value is greater than 0.05, **fail to reject the null hypothesis**. The data provide insufficient evidence for the selected alternative. This does not establish equality, equivalence, unchanged biodiversity, or absence of an environmental effect.

By completing this interpretation, you can clearly state whether **microbial diversity** in **Busse Woods** has been affected based on your hypothesis test results. This helps you draw a meaningful conclusion about the **health of the ecosystem** and whether the data supports the hypothesis of declining biodiversity.

Practice Task:

- **Guide:** Change some of the **Shannon Index** values for microbial diversity in **Column B** (2014 data) and **Column C** (2024 data). Observe how the **sample standard deviations**, **t-statistic**, and **p-value** adjust automatically.
- **Guide:** Add more sample locations to both columns (e.g., increasing the sample size beyond 30\) and note how the **p-value** changes. Discuss when the **two-sample T-test** results start to resemble those of a **z-test**.
- **Guide:** Discuss how the flexibility in **sample size** affects the results of the **two-sample T-test** and compare this to your earlier **z-test** results. Focus on how a larger sample size reduces uncertainty and impacts the p-value, degrees of freedom, and overall results.

Key Takeaways:

- **Guide:** Use the **two-sample T-test** when comparing two sets of data where the **population standard deviation is unknown** and/or the sample size is small.
- **Guide:** The **t-distribution** accounts for additional uncertainty introduced by using the **sample standard deviations** from both datasets.
- **Guide:** As the **sample size increases**, the **two-sample T-test** results start to resemble those of the **z-test**. This is because the **t-distribution** approximates the **normal distribution** as the sample size becomes larger, leading to more similar results between the two tests.
- **Guide:** The **two-sample T-test** is particularly useful for comparing microbial diversity across different time periods (2014 vs. 2024\) to assess the impact of environmental factors such as **urbanization** or **climate change** on biodiversity.

Part 4 Setup: Investigating the **Variance** in **Microbial Diversity**

After conducting the **two-sample T-test** comparing microbial diversity in **2014** and **2024**, you feel a sense of accomplishment. The analysis confirmed a **significant decrease** in diversity over time. However, when reviewing the data closely, something stands out. The **2024 Shannon Index values** appear more **similar** to each other than those from **2014**. This raises a new question: Has the **variability** in microbial diversity also changed? While the T-test showed that the **mean diversity** has declined, the more **consistent values** in 2024 suggest something else might be happening.

Excited by this new insight, you present the idea to your advisor. Your advisor listens carefully and responds enthusiastically:

"*That is a great observation\! The fact that the **2024 samples** appear more uniform than the **2014** samples could indicate a real shift in how microbial diversity is distributed across **Busse Woods**. What you are suggesting points to a potential **homogenization** of microbial communities, which could be an effect of **urbanization** or other **environmental pressures**. To test this idea, we can run an **F-test**. The F-test will allow us to compare the **variances** between the two samples and see if there has been a significant change in the **spread** of diversity values.*"

You realize that while the T-test compared the **means** from the two years, the **F-test** would compare their **variances**, helping you assess whether microbial diversity in **2024** is more **uniform** than in **2014**.

Moving to the F-Test

In the next part of this tutorial, you will learn how to conduct an **F-test** to compare the **variances** in microbial diversity between **2014** and **2024**. This test will assess whether the **spread** of diversity values has changed, providing insights into whether **environmental pressures** have made microbial communities more **uniform**. This could suggest that **Busse Woods** has not only lost biodiversity but has also become more **homogenized**, possibly reducing its **ecological resilience**. The results from this **F-test** may provide additional evidence to guide future **conservation efforts**.

***&#8230;Ask the instructor for the next tutorial link.***


- **Explain:** Write your own interpretation in `E26`. Include the calculated p-value, selected tail and alternative direction, significance level, and evidence-based conclusion. Do not type the example placeholders literally.

[image1]: assets/microbes_3_two_sample_t_test_image1.png
[image2]: assets/microbes_3_two_sample_t_test_image2.png
