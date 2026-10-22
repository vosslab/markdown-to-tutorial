# Microbial diversity benchmark t-test

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The ecological story is a hypothesis for practice; the supplied artifacts do not establish a real field-study provenance or a causal effect of urbanization.

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

![][image1]

### Part 2: Scenario

- **Worksheet:** Microbial T-Test

Now, you face a more realistic challenge. Without knowing the true **population standard deviation** for microbial diversity, you must rely on the **sample standard deviation** from your collected data. This is where the **T-test** comes in. The T-test is specifically designed to handle smaller **sample sizes** and the uncertainty that comes from estimating the population standard deviation.

Feeling the pressure but determined to reach a solid conclusion about the health of Busse Woods, you open your spreadsheet again. This time, you will:

- **Guide:** Calculate the **sample mean** and **sample standard deviation** from your microbial diversity data.
- **Guide:** Perform a **one-sample T-test** to determine if the microbial diversity in Busse Woods is significantly lower than the benchmark value of 4.0, indicating possible biodiversity loss due to urbanization

Why Use a T-Test Now?

In short, two reasons:

- **Unknown Population Standard Deviation**
- **Small Sample Size**

In environmental data, like microbial diversity in a forest preserve, the **population standard deviation** is often unknown. Instead, you must estimate it using your **sample&#8217;s standard deviation**. This uncertainty makes the **T-test** the best fit. The **sample size** in your study is small (fewer than 30 samples), and the **T-test** accounts for extra variability from smaller datasets, providing a more accurate result under these conditions.


The main directional hypothesis is chosen **before inspecting results**. Computing additional tails here is a teaching comparison; do not select whichever p-value is smallest. A p-value is a probability under the null model, not the probability that the null is true or that urbanization caused a change. Failure to reject does not prove equality or absence of ecological effects. Samples must represent the target population and be sufficiently independent; inspect distributions and outliers. Larger sample size alone cannot repair biased sampling.

The benchmark 4.0 is stipulated for the exercise. The t-test estimates the unknown population SD with the sample SD and uses n - 1 degrees of freedom; it also applies to larger samples. The current dataset has **24 observations**. For small samples, the normal-population model and absence of severe outliers matter.

#### Step 1: Set Up Your Google Sheet for the T-Test

- **Open:** Open the generated XLSX workbook in Google Sheets and select the worksheet named above. The complete source data is already included; do not paste another copy over it.

The original course data remains available in the [shared source workbook](https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit). For manual copying, use the tab menu, choose Copy to > Existing spreadsheet, paste your target spreadsheet link, select it, and insert. Rename the copied tab to match the worksheet named above. Personal copies can receive different URLs.

The raw observations retain their original addresses. Rows 2 through 25 contain the 24 current samples; the calculation ranges deliberately extend through row 101 for practice additions. In ANOVA, earlier years have fewer observations and blank cells are not zeroes.


#### Step 2: Set Up the Known Population Values

- **Label C2:** Population Mean
- **Enter D2:** 4.0


- **Guide:** Column C will be used for **Statistical Names**.
- **Guide:** Column D will contain the calculated values.


#### Step 3: Calculate the Sample Statistics

- **Label C4:** Sample Mean
- **Enter D4:** `=AVERAGE(B2:B101)`
- **Label C5:** Sample Standard Deviation
- **Enter D5:** `=STDEV(B2:B101)`
- **Label C6:** Sample Size
- **Enter D6:** `=COUNT(B2:B101)`


#### Step 4: Calculate the T-Statistic

- **Label C8:** T-Statistic
- **Enter D8:** `=(D4 - D2) / (D5 / SQRT(D6))`


- **Guide:** This formula uses the sample mean (D4), the assumed population mean (D2), the sample standard deviation (D5), and the sample size (D6).

Explanation: T-Statistic

The **T-statistic** measures how far the **sample mean** is from the **population mean**, relative to the variability in the sample. It accounts for both the **sample standard deviation** and the **sample size**, providing a standardized way to compare the sample to the population. By dividing the difference between the **sample mean** and the **population mean** by the standard error (which is the **sample standard deviation** divided by the square root of the **sample size**), the **T-statistic** allows us to determine how extreme the observed sample is compared to what we would expect if the **null hypothesis** were true.


#### Step 5: Calculate the Degrees of Freedom

- **Label C9:** Degrees of Freedom
- **Enter D9:** `=D6 - 1`


- **Guide:** Here, `D6` is the sample size, so subtracting 1 gives us the degrees of freedom.

Explanation: Why Do We Use Degrees of Freedom?

In statistics, **degrees of freedom** represent the number of independent values in a dataset that can vary when estimating a statistical parameter. In the context of a **T-test**, degrees of freedom adjust for the uncertainty introduced when estimating the **population standard deviation** using the **sample standard deviation**.

When calculating the **sample standard deviation**, one of the values&#8212;typically the mean&#8212;is fixed based on the rest of the data. This is why we subtract **1** from the **sample size** to get the **degrees of freedom**. Smaller degrees of freedom result in a more conservative test, meaning we need stronger evidence to reject the **null hypothesis**. Larger sample sizes, and therefore more degrees of freedom, lead to a **T-distribution** that more closely resembles a **normal (Z) distribution**.


#### Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)


For the **T-test** on **microbial diversity** data from **Busse Woods**, you need to decide whether you are testing for any **significant difference** or a specific **directional difference** from the benchmark (**Shannon Index** of 4.0).

- **Guide:** **Two-Tailed Test:** Use this when you are checking if the **microbial diversity** is either **higher or lower** than the benchmark. This is for testing any significant deviation from the benchmark, regardless of direction.
- **Guide:** **One-Tailed Test:** Use this when you have a specific hypothesis about the direction of the difference, such as testing if **microbial diversity** is **lower** than the benchmark. A **one-tailed test** focuses on deviations in a single direction.

In this case, since you suspect that the diversity has **decreased** due to **urbanization**, you would likely choose a **one-tailed test (lower)** to check if the **microbial diversity** is significantly **lower** than the benchmark.


#### Step 7: Calculate the P-Values


 Under the null hypothesis and test assumptions, the p-value is the probability of a statistic at least as extreme as the observed statistic in the selected tail or tails.

You will calculate the **p-values** using different approaches: **T.DIST.2T** for the two-tailed test, **T.DIST** for flexible cumulative probability, with no direct two-sample **T.TEST** call in this one-sample analysis. Each method provides a different way of assessing the statistical significance of your data. By comparing the results from each function, you will gain a clearer understanding of how the **T-test** works in Google Sheets.

##### Substep 7.1: Two-Tailed Test:

- **Label C10:** P-Value (Two-Tailed)
- **Enter D10:** `=T.DIST.2T(ABS(D8), D9)`
- **Enter E10:** `=2 * (1 - T.DIST(ABS(D8), D9, TRUE))`

For the **two-tailed test**, you are testing whether the microbial diversity in **Busse Woods** is either **higher** or **lower** than the benchmark. Here are the function inputs you will use:

**T.DIST.2T(x, degrees\_freedom):** x is the absolute value of the **T-statistic** (calculated in **D8**), and **degrees\_freedom** is provided in **D9**. This function handles both tails of the distribution and calculates the p-value automatically.

**T.DIST(x, degrees\_freedom, cumulative):** x is the absolute value of the **T-statistic**, **degrees\_freedom** is in **D9**, and **cumulative** is set to **TRUE**. You will need to subtract from **1** and multiply by **2** to cover both sides of the distribution.


Explanation for Two-Tailed Test:


The **T.DIST.2T** function handles **both tails** of the **distribution**. This means the result automatically accounts for deviations in **both directions**.

The second formula, **T.DIST**, requires you to handle **both sides manually**. First, calculate the **cumulative probability** for **one tail** using **T.DIST**. Then, subtract it from 1 to capture the **upper tail**. Finally, multiply by 2 to account for both **upper and lower tails**.

##### Substep 7.2: One-Tailed Test (for lower values):

- **Label C11:** P-Value (One-Tailed, Lower)
- **Enter D11:** `=T.DIST(D8, D9, TRUE)`

For the **one-tailed test**, you are interested in testing whether the microbial diversity in **Busse Woods** is **lower** than the benchmark. This test will help you determine if environmental factors, such as urbanization, have reduced biodiversity. Here are the function inputs:

**T.DIST(x, degrees\_freedom, cumulative):** x is the **T-statistic** (calculated in **D8**), degrees\_freedom is in **D9**, and **cumulative** is set to **TRUE**. This function calculates the cumulative probability for values less than or equal to the **T-statistic**.


- **Guide:** Leave cell **E11** blank

Explanation for One-Tailed Test (Lower):

In a **one-tailed test**, you are only interested in whether the microbial diversity is **lower** than the benchmark. The **T.DIST** function calculates the **cumulative probability** for values **less than or equal to** the **T-statistic**, meaning you are testing for values in the **lower tail** of the distribution. Use the signed statistic with `T.DIST(D8, D9, TRUE)` for the lower tail. A two-sample `T.TEST` call is not a one-sample benchmark test.

##### Substep 7.3: One-Tailed Test (for higher values):

- **Label C12:** P-Value (One-Tailed, Higher)
- **Enter D12:** `=1 - T.DIST(D8, D9, TRUE)`
- **Enter E12:** `=T.DIST(-D8, D9, TRUE)`

Although you are testing whether the microbial diversity is **lower** than the benchmark, it is also useful to calculate the **p-value** for the **opposite direction** to understand how much diversity might exceed expectations. Here are the function inputs for the **one-tailed test** for higher values:

**Upper tail:** Use `1 - T.DIST(D8, D9, TRUE)` or the symmetry formula `T.DIST(-D8, D9, TRUE)`. Both work for negative as well as positive t-statistics; do not pass a negative value to a right-tail function that requires a nonnegative input.

**T.DIST(x, degrees\_freedom, cumulative):** x is the **T-statistic** (calculated in **D8**), degrees\_freedom is in **D9**, and **cumulative** is set to **TRUE**. This function calculates the cumulative probability for values less than or equal to the **T-statistic**. In order to get values above, we subtract this result from one.


Explanation for One-Tailed Test (Higher):

This test examines whether the microbial diversity in **Busse Woods** is **higher** than the benchmark, testing for potential **increases** in biodiversity. The complement of the signed cumulative probability calculates the probability of obtaining a **T-statistic** greater than or equal to the calculated value, which is ideal for testing whether the diversity exceeds the benchmark. This approach provides insight into the **upper tail** of the distribution and how microbial diversity might vary in the **opposite direction** of your primary hypothesis.


#### Step 8: Decision Using an IF Statement

- **Label C14:** Significance Level (alpha)
- **Enter D14:** 0.05
- **Label C15:** Two-Tail Decision
- **Enter D15:** `=IF(D10 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label C16:** One-Tail Decision (Lower)
- **Enter D16:** `=IF(D11 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label C17:** One-Tail Decision (Higher)
- **Enter D17:** `=IF(D12 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`


In hypothesis testing, the decision to **reject** or **fail to reject** the null hypothesis depends on comparing the p-value to a predetermined significance level (&#945;). Typically, &#945; is set at 0.05, meaning if the p-value is less than or equal to 0.05, we consider the result **statistically significant** and reject the null hypothesis. To streamline this decision process in Google Sheets, we will use the **IF statement**, which evaluates a condition and returns one value if the condition is true and another if false. In this case, we will check whether the p-value is less than or equal to &#945;.


  **Formula:** `=IF(D10 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  **Formula:** `=IF(D11 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  **Formula:** `=IF(D12 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

Explanation

The **IF statement** is a basic yet powerful programming concept that allows the program to evaluate a condition and make decisions. Here, we use it to compare the **p-value** to the **significance level (&#945;)** and automate the decision-making process in hypothesis testing.

If the p-value is greater than 0.05, **fail to reject the null hypothesis**. The data provide insufficient evidence for the selected alternative. This does not establish equality, equivalence, unchanged biodiversity, or absence of an environmental effect.

This process helps determine whether the data supports the conclusion that **urbanization** and **environmental factors** have affected microbial diversity at Busse Woods.


#### Step 9: Interpret the Results

- **Label C19:** Interpretation


At this point, you should have conducted both the **two-tailed** and **one-tailed tests** (lower and higher) to compare the microbial diversity in **Busse Woods** against the benchmark value (Shannon Index \= 4.0). You should have determined that the focus is on the **One-Tailed Test (Lower)** to assess whether microbial diversity in **Busse Woods** is **significantly lower** than the benchmark. The goal is to determine if the diversity has declined due to **urbanization** or other **environmental pressures**. You are specifically testing if the microbial diversity in **Busse Woods** has decreased compared to the expected average for similar ecosystems.


Explanation:

In hypothesis testing, the interpretation depends on comparing the **p-value** to the **significance level** (&#945; \= 0.05). If the **p-value** is **less than or equal to 0.05**, the result is considered **statistically significant**, meaning the null hypothesis is **rejected**. Rejecting the null hypothesis in this case suggests that microbial diversity in **Busse Woods** is **significantly lower** than the benchmark value of **4.0** (representing the average diversity for similar ecosystems). This implies that factors such as **urbanization**, **pollution**, or **climate change** may have contributed to a **decline in biodiversity** in the area.

If the p-value is greater than 0.05, **fail to reject the null hypothesis**. The data provide insufficient evidence for the selected alternative. This does not establish equality, equivalence, unchanged biodiversity, or absence of an environmental effect.

Completing this interpretation allows you to clearly state whether microbial diversity in **Busse Woods** has been impacted by environmental changes, based on the results of your hypothesis test. This helps you draw meaningful conclusions about the **health of the ecosystem** and whether the data supports the hypothesis that biodiversity in **Busse Woods** has declined.

Practice Task:

- **Guide:** Change some of the **Shannon Index** values for microbial diversity in **Column B** (Busse Woods data). Observe how the **sample standard deviation**, **t-statistic**, and **p-value** adjust automatically.
- **Guide:** Add more sample locations (e.g., increasing the sample size beyond 30\) and note how the **p-value** changes. Discuss when the **one-sample T-test** results start to resemble those of a **z-test**.
- **Guide:** Discuss how the flexibility in **sample size** affects the results of the **one-sample T-test** and compare this to your earlier **z-test** results. Specifically, observe how a larger sample size reduces uncertainty, impacting the p-value and overall hypothesis test results.

Key Takeaways:

- **Guide:** Use the **one-sample T-test** when comparing a dataset (e.g., **Shannon Index** values for microbial diversity in **Busse Woods**) to a known benchmark when the **population standard deviation is unknown** and/or the sample size is small.
- **Guide:** The **t-distribution** accounts for additional uncertainty introduced by using the **sample standard deviation** instead of the population standard deviation.
- **Guide:** As the **sample size increases**, the **one-sample T-test** results begin to resemble those of the **z-test**. This occurs because the **t-distribution** approximates the **normal distribution** as the sample size becomes larger, making the T-test and Z-test results more similar.
- **Guide:** The **one-sample T-test** is particularly useful for assessing whether microbial diversity in **Busse Woods** has significantly declined in comparison to the benchmark, especially when the sample size is limited.

Part 3 Setup: Microbial Diversity at Busse Woods

After conducting the **T-test** on microbial diversity at **Busse Woods**, your confidence in the significant difference from the benchmark began to waver. The results of the **T-test** did not confirm the earlier findings from the **Z-test**, and you now question whether the diversity at **Busse Woods** is truly different from the benchmark.

This project is important to you. For months, your team has monitored the effects of **urbanization** and **climate change** on biodiversity in urban forest preserves. **Busse Woods**, once considered a pristine environment, has shown signs of stress in recent years. Your goal was to provide hard data showing whether these changes were affecting **microbial ecosystems**, a key indicator of environmental health. While the **Z-test** initially suggested a significant shift, the new results call that conclusion into doubt.

Just as you were preparing to discard your report and start over, your advisor suggested a new approach. You both remembered that your team has access to a rich dataset from **2014**, a time when concerns about rising temperatures and pollution were increasing. Instead of only comparing the current data to a benchmark, your advisor proposed analyzing changes over time. This could provide a clearer picture of how **Busse Woods** has evolved in response to **environmental pressures**.

By comparing your current data from **2024** with diversity data collected in **2014**, you can determine whether there has been a significant decrease in microbial diversity over the last decade. This **longitudinal analysis** will allow you to draw meaningful conclusions about how these factors have impacted **Busse Woods' microbial communities**.

Moving to the Two Sample T-Test

In the next part of this tutorial, we will learn how to conduct a **Two Sample T-test**, which allows for a direct comparison between **two different datasets**. By comparing microbial diversity from **Busse Woods in 2014** with your current data from **2024**, you will gain insights into how the ecosystem has changed over the past decade. This analysis could reveal whether **urbanization** and **climate change** are contributing to the loss of biodiversity in the area. The findings from this comparison may provide stronger evidence to support conservation efforts and inform future environmental policies.

***&#8230;Ask the instructor for the next tutorial link.***

- **Explain:** Write your own interpretation in `D19`. Include the calculated p-value, selected tail and alternative direction, significance level, and evidence-based conclusion. Do not type the example placeholders literally.

[image1]: assets/microbes_2_t_test_image1.png
