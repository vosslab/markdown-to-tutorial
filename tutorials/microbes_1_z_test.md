# Microbial diversity Z-test

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The ecological story is a hypothesis for practice; the supplied artifacts do not establish a real field-study provenance or a causal effect of urbanization.

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

![][image1]

### Part 1: Scenario

- **Worksheet:** Microbial Z-Test

Urbanization around **Busse Woods** may have disrupted the ecosystem, leading to a decline in microbial diversity. By comparing the current microbial diversity in **Busse Woods** to the benchmark for similar ecosystems, we can determine if external pressures, such as pollution or habitat fragmentation, are reducing the biodiversity of the soil. You are analyzing microbial diversity in soil samples collected from different locations in **Busse Woods Forest Preserve** using **SSU rRNA sequencing**. Urbanization around **Busse Woods** is raising concerns that human activities and environmental pressures may be negatively affecting soil health and biodiversity.

The **Shannon Index** is a widely used measure of biodiversity that takes into account both the number of species present, known as **species richness**, and how evenly individuals are distributed among those species, known as **evenness**. The index is calculated by summing the proportion of individuals belonging to each species in a community and multiplying this by the natural logarithm of that proportion, then summing the results for all species and taking the negative of the total. A higher **Shannon Index** value indicates greater biodiversity, with values depending on the community, taxonomic resolution, sampling method, and logarithm base; there is no universal 1.5-to-4.5 limit.

The primary goal of this study is to determine whether microbial diversity (measured using the **Shannon Index**) in **Busse Woods** has decreased compared to the benchmark of 4.0, which is stipulated as the average for this teaching scenario. For this teaching exercise, assume a known population standard deviation of 0.6.

In this tutorial, you will use **Google Sheets** to conduct a **Z-test** using the sample data to investigate whether urbanization has significantly reduced the microbial diversity at **Busse Woods**.

- **Null Hypothesis H&#8320;**: Microbial diversity in the forest preserve is consistent with the known average (Shannon Index \= 4.0).
- **Alternative hypothesis:** The population mean Shannon Index is lower than 4.0 (one-tailed, lower). For this directional test, H0 is mean >= 4.0 and H1 is mean < 4.0. The two-tailed comparison below instead uses H0: mean = 4.0 and H1: mean != 4.0.


The main directional hypothesis is chosen **before inspecting results**. Computing additional tails here is a teaching comparison; do not select whichever p-value is smallest. A p-value is a probability under the null model, not the probability that the null is true or that urbanization caused a change. Failure to reject does not prove equality or absence of ecological effects. Samples must represent the target population and be sufficiently independent; inspect distributions and outliers. Larger sample size alone cannot repair biased sampling.

The benchmark 4.0 is stipulated for the exercise. The population SD 0.6 is assumed known for the Z-test; it is not estimated from these samples. The current dataset has **24 observations**. For small samples, the normal-population model and absence of severe outliers matter.

#### Step 1: Find Your Copy of the Spreadsheet

- **Open:** Open the generated XLSX workbook in Google Sheets and select the worksheet named above. The complete source data is already included; do not paste another copy over it.

The original course data remains available in the [shared source workbook](https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit). For manual copying, use the tab menu, choose Copy to > Existing spreadsheet, paste your target spreadsheet link, select it, and insert. Rename the copied tab to match the worksheet named above. Personal copies can receive different URLs.

The raw observations retain their original addresses. Rows 2 through 25 contain the 24 current samples; the calculation ranges deliberately extend through row 101 for practice additions. In ANOVA, earlier years have fewer observations and blank cells are not zeroes.


#### Step 2: Set Up the Known Population Values

- **Label C2:** Population Mean
- **Enter D2:** 4.0
- **Label C3:** Population Standard Deviation
- **Enter D3:** 0.6


- **Guide:** **Column C** will be used for **Statistical Names**.
- **Guide:** **Column D** will contain the **calculated values**.


#### Step 3: Calculate the Sample Mean

- **Label C5:** Sample Mean
- **Enter D5:** `=AVERAGE(B2:B101)`
- **Label C6:** Sample Size
- **Enter D6:** `=COUNT(B2:B101)`


- **Guide:** This formula calculates the mean of Shannon Index values from cells B2 to B101, allowing for flexibility if you add more data. It will automatically ignore empty cells.


#### Step 4: Calculate the Z-Statistic

- **Label C8:** Z-Statistic
- **Enter D8:** `=(D5 - D2) / (D3 / SQRT(D6))`


- **Guide:** This formula uses the sample mean (D5), population mean (D2), population standard deviation (D3), and sample size (D6). The Z-statistic helps you determine how far the sample mean is from the population mean, accounting for sample size.

Explanation:

The Z-statistic standardizes the difference between the **sample mean** and the **population mean** by converting it into units of standard deviation. This allows you to assess whether the observed microbial diversity at Busse Woods is significantly different from the expected diversity.


#### Step 5: Determine the Type of Test (One-Tailed or Two-Tailed)


When performing a Z-test on microbial diversity data from Busse Woods, you need to decide whether you are testing for **any significant difference** or a **specific directional difference** from the known benchmark (Shannon Index of 4.0).

**Two-Tailed Test:**

This is used when you want to test if there is any **significant difference** in the microbial diversity of your forest preserve, regardless of whether it&#8217;s higher or lower than the known benchmark. You&#8217;re checking for **any deviation** from the benchmark value.

- **Guide:** **Example Hypothesis**:

- **Guide:** **Null Hypothesis (H&#8320;)**: The average microbial diversity in the forest preserve is equal to the benchmark (Shannon Index \= 4.0).

- **Guide:** **Alternative Hypothesis (H&#8321;)**: The average microbial diversity in the forest preserve is different from the benchmark (either higher or lower).

Use a **two-tailed test** if you do not have a specific expectation about whether the microbial diversity is **higher or lower** than the benchmark. You&#8217;re testing for any difference.

**One-Tailed Test:**

This is used when you have a **specific direction** in mind. For example, if you believe that the microbial diversity in your forest preserve is **higher** than the benchmark, you would use a **one-tailed test**.

- **Guide:** **Example Hypothesis**:

- **Guide:** **Null Hypothesis (H&#8320;)**: The microbial diversity in the forest preserve is less than or equal to the benchmark (Shannon Index &#8804; 4.0).

- **Guide:** **Alternative Hypothesis (H&#8321;)**: The microbial diversity in the forest preserve is **greater** than the benchmark (Shannon Index \> 4.0).

Use a **one-tailed test** if you have a specific hypothesis about whether the microbial diversity is **higher** (or lower, if reversed) than the benchmark. This allows you to test for a **directional** difference.


#### Step 6: Calculate the P-Values


To help **you** better understand the different types of tests and how p-values are calculated, **we will guide you** through the steps for calculating all possible p-values (one-tailed and two-tailed).

##### Substep 6.1: Two-Tailed Test:

- **Label C10:** P-Value (Two-Tailed)
- **Enter D10:** `=2 * (1 - NORM.S.DIST(ABS(D8)))`

A two-tailed test is used when you want to check for any difference, whether microbial diversity in Busse Woods is higher or lower than the benchmark.


Explanation for Two-Tailed Test:


The function **`NORM.S.DIST(ABS(D8))`** gives the cumulative probability to the left of the absolute observed Z-statistic. Since **we want to test both sides** (higher and lower), we subtract this value from 1 to find the **probability in the upper tail**, and then multiply by 2 to account for both tails. **This final formula ensures you include both extremes** in your analysis.

However, because we are performing a **two-tailed test**, we are interested in deviations in **both directions**&#8212;whether the microbial diversity in Busse Woods is **higher or lower** than the benchmark. To account for this, we first need to find the probability in the **upper tail** of the distribution. The function **`NORM.S.DIST(ABS(D8))`** gives the cumulative probability for the area under the curve to the **left** of the absolute value of the Z-statistic (i.e., the probability that the Z-statistic is less than or equal to this value). To find the probability of observing a Z-statistic **greater than or equal to the absolute value** of D8 (the upper tail), we subtract this cumulative probability from **1**. This gives us the likelihood of observing a value in the **right tail** of the distribution, beyond the calculated Z-statistic.

Take a look at this image of the **normal distribution curve**, which will help visualize this process:
![][image2]
The shaded area to the left of **Z \= &#8211;1** in the image represents **P(Z \< &#8211;1)**, or the cumulative probability to the left of &#8211;1. This area is given by **`NORM.S.DIST(-1)`**. For the image, P(Z < -1) equals P(Z > +1) by symmetry. For a general positive value z, its upper-tail probability is 1 - NORM.S.DIST(z). By the symmetry of the normal distribution, **`1 - NORM.S.DIST(ABS(D8))`** is equivalent to **`NORM.S.DIST(-ABS(D8))`**, since the normal curve is symmetric around zero. Both approaches give the probability of observing a value in the **upper tail**.

Since we are conducting a **two-tailed test**, we need to account for **extreme values in both tails**&#8212;those significantly **higher** and those significantly **lower** than the benchmark. To do this, we multiply the **upper tail probability** by **2**, which ensures that we include both the **left** and **right** tails of the distribution. The final formula, **`2 * (1 - NORM.S.DIST(ABS(D8)))`**, gives the total probability of observing a Z-statistic as extreme or more extreme than the one calculated, regardless of direction.

##### Substep 6.2: One-Tailed Test (for lower values):

- **Label C11:** P-Value (One-Tailed, Lower)
- **Enter D11:** `=NORM.S.DIST(D8)`

A one-tailed test is used when you have a specific directional hypothesis. In this case, we are testing if microbial diversity in Busse Woods is **lower** than the benchmark.


Explanation for One-Tailed Test (Lower):

For a one-tailed test, we are only interested in whether microbial diversity is **lower** than the benchmark. The function **`NORM.S.DIST(D8)`** calculates the cumulative probability of observing a Z-statistic less than or equal to the calculated Z-statistic. This directly gives us the p-value for the **lower tail**, which is the probability, under the null model, of a Z-statistic no larger than the observed one.

##### Substep 6.3: One-Tailed Test (for higher values):

- **Label C12:** P-Value (One-Tailed, Higher)
- **Enter D12:** `=1 - NORM.S.DIST(D8)`

Even though the hypothesis is about **lower** microbial diversity, we can still calculate the p-value for the **opposite direction** (whether microbial diversity is **higher** than the benchmark) to see how such results would be interpreted.


Explanation for One-Tailed Test (Higher):

The function **`NORM.S.DIST(D8)`** gives the probability to the left of the observed
Z-statistic under the null model. Subtracting it from one gives the probability to the right,
which is the p-value for the alternative that microbial diversity is **higher** than the benchmark.

#### Step 7: Make a Decision Using an IF Statement

- **Label C14:** Significance Level (alpha)
- **Enter D14:** 0.05
- **Label C15:** Two-Tail Decision
- **Enter D15:** `=IF(D10 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label C16:** One-Tail Decision (Lower)
- **Enter D16:** `=IF(D11 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label C17:** One-Tail Decision (Higher)
- **Enter D17:** `=IF(D12 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`


In hypothesis testing, the decision to reject or fail to reject the null hypothesis depends on the comparison between the p-value and the significance level (&#945;). The significance level is typically set at 0.05, meaning that if the p-value is less than or equal to 0.05, we consider the result statistically significant and reject the null hypothesis.

To automate this decision-making process in Google Sheets, **we use the IF statement**, a logical function that **evaluates a condition** and returns one value if the condition is true, and another if it is false. In this case, the condition will check **whether the p-value is less than or equal to the significance level**.


Explanation

The **IF statement** is a fundamental programming concept that allows you to make decisions based on conditions. In this case, **we use it to compare** the p-value to the significance level (**&#945;**) and **decide** whether to reject or fail to reject the null hypothesis.

If the p-value is greater than 0.05, **fail to reject the null hypothesis**. The data provide insufficient evidence for the selected alternative. This does not establish equality, equivalence, unchanged biodiversity, or absence of an environmental effect.


By using the IF statement in Google Sheets, you can automate the process of making these decisions based on your p-values, ensuring clarity and accuracy in interpreting the results of your hypothesis tests.


#### Step 8: Interpret the Results

- **Label C19:** Interpretation


At this point, you should have determined that we are only interested in the results of the **one-tailed (lower)** test. You are specifically testing whether the microbial diversity in Busse Woods is **lower than the benchmark**. This could suggest a reduction in biodiversity due to urbanization or other environmental pressures. The goal is to see if the data supports the hypothesis that microbial diversity has declined.

   **One-Tailed Test Example (Lower):**
   "With a p-value of \[calculated value\], we \[reject/fail to reject\] the null hypothesis, indicating that microbial diversity in Busse Woods \[is/is not\] significantly lower than the benchmark."

Explanation:

In hypothesis testing, the interpretation relies on comparing the **p-value** to the significance level (**&#945; \= 0.05**). If the p-value is less than or equal to 0.05, the result is considered **statistically significant**, and the null hypothesis is rejected. Rejecting the null hypothesis means that the data provides enough evidence to conclude that microbial diversity in Busse Woods is **significantly lower** than the benchmark. This could indicate that environmental factors, such as urbanization, have negatively affected the biodiversity in the area.

If the p-value is greater than 0.05, **fail to reject the null hypothesis**. The data provide insufficient evidence for the selected alternative. This does not establish equality, equivalence, unchanged biodiversity, or absence of an environmental effect.

By completing this interpretation, you can clearly state whether microbial diversity in Busse Woods has been affected based on your hypothesis test results. This helps you draw a meaningful conclusion about the health of the ecosystem.

Practice Task:

- **Guide:** **Add more diversity index values** to Column B. Observe how the **Z-statistic** and **p-value** adjust as you increase the sample size. Notice how adding more data points, especially extreme values, can affect the outcome of the hypothesis test. This will help you understand the sensitivity of the test to the number of samples.
- **Guide:** **Modify some existing values** in Column B by increasing or decreasing the Shannon Index values. Watch how the **Z-statistic** and **p-value** change as a result. This will show how changes to individual values can impact the test results. Try adding values that are either much higher or much lower than the current ones to see the extent of the changes.
- **Guide:** **Think about** how both **changing the dataset size** and modifying individual Shannon Index values impacts the hypothesis test results. Think about how a larger sample size leads to more robust conclusions, while extreme individual values might skew the results. This exercise will reinforce the importance of both sample size and data consistency in hypothesis testing.

Key Takeaways:

- **Guide:** **Flexibility:** This setup allows you to vary the number of samples dynamically by entering values in **Column B**. By using a flexible range (B2:B101), you can observe how adding or removing data points influences the outcome of the test. This highlights how sample size plays a critical role in the reliability of statistical results, especially in ecological data where sample numbers can vary widely.
- **Guide:** **Z-Statistics**: Z-statistics provide a standardized way to compare the **sample mean** to a known **population mean**. Even when the sample size changes, using the Z-statistic allows for a clear comparison. Understanding how to standardize values using Z-statistics is essential for comparing your sample to a benchmark, helping you determine whether the microbial diversity in Busse Woods deviates significantly from the expected value.
- **Guide:** **Dynamic Calculations**: One of the advantages of using Google Sheets is that it automatically recalculates the **Z-statistic** and **p-value** when you modify the data. This allows you to perform real-time analysis and instantly see how changes in your data affect the results. Being able to experiment with different values and sample sizes will help you better grasp the relationship between your data and hypothesis testing, showing the effects of data changes without needing to manually recalculate each time.

Part 2 Setup: Microbial Diversity at Busse Woods

After conducting the Z-test on microbial diversity at Busse Woods, you were confident that the diversity was significantly different from the benchmark. You were ready to present your findings and celebrate a successful environmental analysis.

However, just as you began preparing your report, your supervisor sent a critical email:

&#8220;*While you compared Busse Woods' microbial diversity to the benchmark using a Z-test, we noticed a major issue. You assumed that the population standard deviation was known, but for environmental data like this, making that assumption is risky. Ecosystems vary greatly depending on factors like soil type and vegetation cover, and these can differ even within the same location. The key issue is that the population standard deviation is not actually known for this population. You should use a T-test that estimates it from your sample and accounts for the extra uncertainty. A small sample alone does not rule out a Z-test when the population standard deviation is known and the normal-model assumptions hold. To validate your findings, you must redo the analysis using a T-test.*&#8221;

You realize that the Z-test may not have been appropriate because of these assumptions. To ensure the accuracy of your conclusions, you now need to switch to a **T-test** and recalculate your results. This new approach accounts for uncertainty in estimating the population standard deviation from the sample. You must still assess independence and whether the population is approximately normal, especially with a small sample, before drawing an environmental conclusion.

Moving to the T-Test

In the next part of this tutorial, we will learn how to conduct a **T-test** when the population standard deviation is **unknown**, and the sample size is relatively small. The **T-test** accounts for estimating the population standard deviation from the sample; its use is not restricted to small samples. With a small sample, departures from normality and extreme outliers still require care.

***&#8230;Ask the instructor for the next tutorial link.***


- **Explain:** Write your own interpretation in `D19`. Include the calculated p-value, selected tail and alternative direction, significance level, and evidence-based conclusion. Do not type the example placeholders literally.

[image1]: assets/microbes_1_z_test_image1.png
[image2]: assets/microbes_1_z_test_image2.png
