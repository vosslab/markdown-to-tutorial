# Microbial diversity two-sample F-test

For BIOL 318/418. This teaching scenario uses the complete original workbook observations. The ecological story is a hypothesis for practice; the supplied artifacts do not establish a real field-study provenance or a causal effect of urbanization.

## Workbook

### Sheet: Two Sample F-Test

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

### Part 4: Scenario

- **Worksheet:** Two Sample F-Test

After comparing the microbial diversity in **Busse Woods** between **2014** and **2024** using a **Two Sample T-test**, you successfully confirmed that the overall diversity has **decreased** over the past decade. However, while analyzing the data further, you observe something unexpected: the **2024 Shannon Index values** appear more **similar** to one another compared to those from **2014**. This raises new questions about whether the **variability** in microbial diversity has changed alongside the mean. Could environmental pressures like **urbanization** and **climate change** be not only reducing biodiversity but also making microbial communities more **uniform**?

Excited by this idea, you present your findings to your advisor, who praises your observation and suggests conducting an **F-test** to compare the **variances** between the two years. By comparing the **spread** of diversity values in **2014** and **2024**, the **F-test** will help determine whether environmental pressures are contributing to the **homogenization** of microbial communities in **Busse Woods**. This could reveal important insights into how **ecological resilience** is changing and whether some of the forest's unique **microenvironments** are being lost.

Why Use an F-Test Now?

While the **Two Sample T-test** compared the **means** of microbial diversity between **2014** and **2024**, the **F-test** allows you to assess the **variances**. This test is ideal when you need to determine whether the **spread** of data has changed significantly between two groups or time periods. In this case, it will help you explore whether the microbial communities in **Busse Woods** have become more **uniform**, providing a deeper understanding of how the ecosystem is evolving under **environmental pressures**.


The main directional hypothesis is chosen **before inspecting results**. Computing additional tails here is a teaching comparison; do not select whichever p-value is smallest. A p-value is a probability under the null model, not the probability that the null is true or that urbanization caused a change. Failure to reject does not prove equality or absence of ecological effects. Samples must represent the target population and be sufficiently independent; inspect distributions and outliers. Larger sample size alone cannot repair biased sampling.

The source lists the **same 24 named locations in both years**. This exercise demonstrates an **independent-samples** method only under an explicit working assumption of independence across years; the file alone cannot establish it. If these are repeated measurements at matched sites, a paired t-test (for means) or another method respecting dependence is needed. Do not treat matching row labels as evidence of independence.

The classical F-test assumes **independent normal populations** and is sensitive to nonnormality. A lower variance of Shannon indices is not proof that taxonomic community composition has become homogeneous. The ratio is **2024 variance / 2014 variance**, with numerator DF in `E14` and denominator DF in `E13`. Use the direct CDF tails after unequal-size practice changes.

#### Step 1: Copy the Data

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
- **Guide:** Sample means are not needed for the F-test, so you can skip this step.
- **Guide:** **Sample Standard Deviations**:
- **Guide:** **Sample Sizes**:


#### Step 4: Calculate the F-Statistic

- **Replace D11:** F-Statistic
- **Enter E11:** `=E6^2 / E5^2`


Now, we will calculate the **F-statistic** to compare the **variances** of the two datasets.


Explanation: F-Statistic

The **F-statistic** is used to compare the **variances** of two samples. It is the ratio of the variances of the two datasets (2014 and 2024). If the **F-statistic** is close to **1**, it indicates that the **variances** of the two datasets are similar. However, an F-statistic far from **1** in either direction may provide evidence that the variances differ, with one sample having more **spread** in the diversity values than the other.

It is important to note that **sample means are not relevant** for the **F-test**. The test focuses entirely on the **spread** of the data (**variance**), regardless of where the data is centered (**mean**). This means that even if the two groups have the same or different means, the **F-test** only cares about how **spread out** the values are in each group.

This calculation will help determine whether the **spread** (**variability**) in microbial diversity across sampling locations has changed over time. This could indicate a shift toward more **uniformity** or **homogenization** in the **2024 data**, suggesting that environmental pressures may have made the microbial communities in **Busse Woods** more **consistent** in their diversity, possibly reducing their **ecological resilience**.


#### Step 5: Calculate the Degrees of Freedom

- **Replace D13:** Degrees of Freedom for 2014
- **Enter E13:** `=E8 - 1`
- **Replace D14:** Degrees of Freedom for 2024
- **Enter E14:** `=E9 - 1`


In an **F-test**, degrees of freedom are used differently than in a **T-test**. In this case, the degrees of freedom correspond to the **sample sizes** of each group, minus one for each. The **F-test** compares the **variances** of two samples, and the degrees of freedom help us interpret how reliable these variance estimates are.


Explanation

In the **F-test**, the **degrees of freedom (DF)** represent the number of independent data points used to calculate the variance in each sample. For each sample, the **DF** is calculated as **sample size \- 1**. This reflects the fact that one degree of freedom is used up in estimating the mean, so only the remaining data points are "free to vary."

These degrees of freedom are used to interpret the **F-statistic**, which compares the **variances** of the two samples. Larger degrees of freedom make the test more reliable because they indicate a more accurate estimate of the population variance.

In **biological studies**, where **sample sizes** are often small, the **F-distribution** becomes wider, meaning that it takes a larger difference in variances to conclude that they are statistically different. As degrees of freedom increase (i.e., as the sample size increases), the null F-distribution concentrates near **1**; this improves precision in comparing variances.


#### Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)


In an **F-test**, you are testing whether the **variances** between two datasets (in this case, the Shannon Index values for 2014 and 2024\) are significantly different. You need to decide whether you are testing for any significant difference in variance (a **two-tailed test**) or a specific hypothesis about which year has greater variance (a **one-tailed test**).

- **Guide:** **Two-Tailed Test**: This test is used to check whether the **variance** of microbial diversity in 2024 is **significantly different** (either higher or lower) from that in 2014\. If you are unsure about the direction of change but suspect there is a difference in the variability of the data, the two-tailed test is appropriate.
- **Guide:** **One-Tailed Test**: This test is used when you have a specific hypothesis about the direction of the variance difference. For example:
- **Guide:** **Lower One-Tailed Test**: This checks if the **variance** in 2024 is **lower** than in 2014, suggesting that microbial diversity in 2024 may be more **homogeneous** than in 2014\.
- **Guide:** **Higher One-Tailed Test**: This checks if the **variance** in 2024 is **higher** than in 2014, which could indicate that the microbial diversity in 2024 has **greater variability**.

For an **F-test**, you are no longer testing the **mean** or **direction of change** in microbial diversity but rather whether the **spread of values (variance)** has changed significantly. In this case, because you suspect that environmental factors have **reduced variability** in microbial diversity in 2024, a **lower one-tailed F-test** would be appropriate.


#### Step 7: Calculate the P-Values


Now that you are working with two samples (2014 and 2024 Shannon Index values), you will calculate the **F-statistic** and the **p-values** to compare the **variances** of microbial diversity between these two datasets. The **F-statistic** is the ratio of the variances between the two groups, and the **p-value** will help you determine if the observed variance difference is statistically significant.

You will perform both **two-tailed** and **one-tailed** tests (lower and higher) to check if the **variance** of microbial diversity has either increased or decreased from 2014 to 2024\. You will also use both **manual calculations** and the **F.TEST** function to automate the process.

Explanation of F.DIST Inputs:

The function **`F.DIST`** evaluates the F distribution. With **TRUE**, it returns the cumulative probability to the left of the observed F-statistic under the null hypothesis and test assumptions. This is the lower-tail p-value; higher- and two-tailed tests require the tail calculations below. Here are the inputs:

- **Guide:** **F.DIST(x, degrees\_freedom1, degrees\_freedom2, cumulative)**
- **Guide:** **x**: This is the **F-statistic**, calculated as the ratio of the variances of the two groups.
- **Guide:** **degrees\_freedom1**: This is the **degrees of freedom** for the numerator dataset (2024 for the ratio in `E11`), calculated as the sample size minus one.
- **Guide:** **degrees\_freedom2**: This is the **degrees of freedom** for the denominator dataset (2014 for the ratio in `E11`), calculated as the sample size minus one.
- **Guide:** **cumulative**: This specifies whether you want the **cumulative distribution function** (TRUE) or the **probability density function** (FALSE). You will use TRUE for calculating the cumulative probability.

Explanation of F.TEST Inputs:

The function **`F.TEST`** simplifies the F-test process by directly comparing the variances of two datasets and calculating the p-value. Here are the inputs:

- **Guide:** **F.TEST(array1, array2)**
- **Guide:** **array1**: This is the range of values for the first dataset (for example, the 2014 Shannon Index values in column B).
- **Guide:** **array2**: This is the range of values for the second dataset (for example, the 2024 Shannon Index values in column C).

The **`F.TEST`** function returns the **p-value**, which tells you whether the variance between the two datasets is significantly different. A smaller **p-value** (less than 0.05) suggests that the difference in variance is statistically significant.

##### Substep 7.1: Two-Tailed Test:

- **Enter E16:** `=MIN(1, 2 * MIN(F.DIST(E11, E14, E13, TRUE), F.DIST.RT(E11, E14, E13)))`
- **Enter G16:** `=F.TEST(C2:C101, B2:B101)`

This test checks if the **variance** in microbial diversity has changed in **either direction** between 2014 and 2024\.


- **Guide:** This calculates the **two-tailed p-value** from twice the smaller CDF tail, capped at one.
- **Guide:** This calculates the **two-tailed p-value** directly, comparing the **variances** between the two datasets (2014 in column B and 2024 in column C).

Explanation for Two-Tailed Test:

In this two-tailed **F-test**, you are testing whether the **variance** in microbial diversity has **significantly changed** between 2014 and 2024\. The **F.DIST** function compares the **variances** of the two datasets, and the **F.TEST** function simplifies the process by calculating the p-value automatically. A significant **p-value** suggests that the **spread** (variance) in microbial diversity has either **increased or decreased** between 2014 and 2024\.

##### Substep 7.2: One-Tailed Test (for lower values):

- **Enter E17:** `=F.DIST(E11, E14, E13, TRUE)`
- **Enter G17:** `=IF(F.DIST(E11, E14, E13, TRUE) <= 0.5, F.TEST(C2:C101, B2:B101)/2, 1 - F.TEST(C2:C101, B2:B101)/2)`

This test evaluates whether the **variance** in microbial diversity is **lower** in 2024 than in 2014, suggesting that the diversity is becoming more **homogeneous**.


Explanation for One-Tailed Test (Lower):

In this **one-tailed F-test**, you are testing if the **variance** in microbial diversity has **decreased**, meaning the diversity values are becoming more **uniform** in 2024\. If the **p-value** is significant, it suggests that the **variance** in 2024 is **lower**, indicating possible environmental pressures leading to more uniform microbial communities.
**F.TEST** gives twice the smaller tail probability. To recover the requested lower tail, the formula in `G17` first checks whether the direct CDF in `E17` is at most 0.5. If so, halve `F.TEST`; otherwise subtract that half from one. This handles both observed variance directions and remains valid when practice changes the sample sizes. Use `G18 = 1 - G17` for the higher tail. The degrees of freedom must always follow their numerator and denominator variances.

##### Substep 7.3: One-Tailed Test (for higher values):

- **Enter E18:** `=F.DIST.RT(E11, E14, E13)`
- **Enter F18:** `=F.DIST(E5^2 / E6^2, E13, E14, TRUE)`
- **Enter G18:** `=1 - G17`

This test evaluates whether the **variance** in microbial diversity is **higher** in 2024 than in 2014, suggesting that diversity is becoming more **variable**.


- **Guide:** This formula calculates the p-value for a higher one-tailed test, checking if the variance in **2024** is greater than that of **2014**.
- **Guide:** The **F.DIST.RT** function calculates the right-tailed probability, which tests whether the variance in 2024 is significantly greater than in 2014\.
- **Guide:** This formula performs the same test but with the variances swapped. It evaluates if the variance in **2024** is greater than the variance in **2014** by reversing the order of the ratio.
- **Guide:** This approach helps confirm the results and provides insight into how the variances compare.
- **Guide:** This function simplifies the calculation, directly testing if the variance in **2024** is greater than in **2014** by comparing the two datasets.

Explanation for One-Tailed Test (Higher):

In this **one-tailed F-test**, you are assessing whether the **variance in microbial diversity** has increased between 2014 and 2024\. A higher variance in 2024 suggests that diversity values are becoming more spread out, indicating greater variability in microbial communities.

The formula `F.DIST.RT(E11, E14, E13)` specifically tests if **2024** has more variability than **2014** by calculating the ratio of their variances. If the **p-value** is significant (typically less than 0.05), this means the **variance in 2024 is statistically greater** than in 2014\. This increased spread in diversity values could indicate that **environmental factors**&#8212;such as urbanization or climate changes&#8212;have led to more variability across microbial communities.

The reciprocal-ratio calculation swaps both the ratio and its degrees of freedom. It is a cross-check of the same upper-tail probability, not an additional independent test or proof of an ecological mechanism.


#### Step 8: Decision Using an IF Statement

- **Enter E20:** 0.05
- **Label D22:** Two-Tail Decision
- **Enter E22:** `=IF(E16 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label D23:** One-Tail Decision (Lower)
- **Enter E23:** `=IF(E17 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
- **Label D24:** One-Tail Decision (Higher)
- **Enter E24:** `=IF(E18 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`


In hypothesis testing, the decision to **reject** or **fail to reject** the **null hypothesis** is based on comparing the **p-value** to a predetermined **significance level (&#945;)**, often set at **0.05**. If the p-value is less than or equal to **0.05**, the result is considered **statistically significant**, meaning the variance between the two years (2014 and 2024\) is unlikely to have occurred by chance. To make this process easier, we will use the **IF statement** in Google Sheets, which evaluates a condition and returns one value if true and another if false. In this case, we will check whether the p-value is less than or equal to **&#945; (0.05)**.


- **Guide:** to determine whether to reject the null hypothesis using the two-tailed test p-value.
- **Guide:** to determine whether to reject the null hypothesis using the one-tailed (lower) test p-value.
- **Guide:** to determine whether to reject the null hypothesis using the one-tailed (higher) test p-value.

Explanation

The **IF statement** simplifies decision-making by evaluating whether the **p-value** is **less than or equal to 0.05** (our significance level). If it is, the test result is **statistically significant**, and you **reject the null hypothesis**, meaning the variance between the two years is significantly different. For instance, if the one-tailed (higher) test p-value is less than **0.05**, you would reject the null hypothesis, indicating that the variance in **2024** is significantly higher than in **2014**. Conversely, if the p-value is greater than **0.05**, you would **fail to reject the null hypothesis**, implying that the variance between the two years is not significantly different.

This automated process ensures that you can efficiently assess whether there has been a significant change in microbial diversity variance over time in Busse Woods, allowing for a clearer interpretation of the results and the effects of environmental pressures on biodiversity.


#### Step 9: Interpret the Results

- **Label D26:** Interpretation


You have just conducted the **F-test** to compare the **variance** in microbial diversity between **2014** and **2024**. Your focus is on determining whether the **variability** in the **Shannon Index** has significantly changed. Specifically, you are testing if the **2024 Shannon Index** values are **more uniform** or **more spread out** compared to **2014**.


- **Guide:** *"With a p-value of \[calculated value\], we \[reject/fail to reject\] the null hypothesis, indicating that the variance in microbial diversity in Busse Woods \[is/is not\] significantly different in 2024 compared to 2014."*

Explanation:

The interpretation depends on comparing the **p-value** to the **significance level** (**&#945; \= 0.05**). If the p-value is less than or equal to **0.05**, the result is **statistically significant**, and you **reject** the null hypothesis. This means that the **variance** in **2024** is significantly **higher** or **lower** than in **2014**, depending on whether you used a **one-tailed** or **two-tailed** test.

If the p-value is greater than 0.05, **fail to reject the null hypothesis**. The data provide insufficient evidence for the selected alternative. This does not establish equality, equivalence, unchanged biodiversity, or absence of an environmental effect.

By interpreting the results of the **F-test**, you can assess if environmental pressures are contributing to changes in both the **diversity** and the **variability** of microbial communities over time.

Practice Task:

- **Guide:** Change some of the **Shannon Index** values in **Column B** (2014 data) and **Column C** (2024 data). Observe how the **sample standard deviations**, **F-statistic**, and **p-value** adjust.
- **Guide:** Add more sample locations (e.g., increase sample size beyond 30\) and see how this impacts the **F-statistic** and **p-value**.
- **Guide:** Discuss how **sample size** affects the **F-test** results and compare this to earlier **T-test** results. Focus on how a larger sample size reduces **uncertainty** and impacts the **p-value** and the **F-distribution**.

Key Takeaways:

- **Guide:** Use the **F-test** to compare the **variability** (variance) between two datasets. This is useful for assessing whether environmental factors are leading to more **uniformity** or more **variability** in microbial diversity.
- **Guide:** The **F-distribution** focuses on comparing **variance** rather than **mean** values, giving a clearer picture of changes in **data spread**.
- **Guide:** Larger **sample sizes** improve the reliability of the **F-test**, but the test remains useful for small sample sizes when examining differences in **variability**.
- **Guide:** The **F-test** complements the **T-test** by focusing on the **spread** of data in microbial diversity, which can reveal different patterns in **ecosystem health** over time.

Part 5 Setup: Expanding the Investigation into More Years with ANOVA

After conducting the **F-test** comparing microbial diversity in **2014** and **2024**, you successfully **rejected the null hypothesis**. The earlier t-test addresses mean diversity; the F-test separately addresses variance. Interpret each using its own result and selected hypothesis. This raises important questions: Has this trend been ongoing for years? Has the decline in diversity and **reduction in variability** been happening gradually?

As you think about this, an idea strikes. You recall older data in the lab that has not been analyzed for years. Early in your time here, you heard about old student theses where previous graduate students collected microbial diversity data before modern sequencing methods became available. These projects were massive, each representing an entire thesis, where students relied on traditional culture-based techniques to estimate diversity.

Without DNA sequencing, these students used **plate counts** and **staining techniques** to identify and quantify microbial species. They grew colonies on **selective media** and counted **colony-forming units (CFUs)** as a measure of microbial abundance. Colony **colors, shapes, and growth patterns** helped describe cultivable isolates, but distinct species can share appearances and one species can vary in appearance. Staining methods like **Gram staining** helped differentiate species, providing broad phenotypic categories rather than definitive species identification. Culture-based methods count only organisms that grow under the chosen conditions; CFUs are not necessarily individual cells or complete species counts.

These methods, while labor-intensive, provided valuable **estimates of microbial diversity**. Manual colony counting required days of careful incubation and observation. Despite the limitations of these methods, the meticulous documentation provided solid data that can now offer insights into **microbial ecosystems** before high-throughput technologies.

Inspired by this, you explore three theses from **1994**, **2004**, and **2009**, each containing **Shannon Index values** based on these traditional microbial techniques. Combining this older data with the **2014** and **2024** data gives you a **30-year timeline** of microbial diversity at **Busse Woods**. Now, you are ready to conduct an **ANOVA (Analysis of Variance)** to test whether the population means differ among years.

With all the data in hand, you can now analyze how microbial diversity has shifted over the decades. **ANOVA** will allow you to compare multiple time points at once, helping you assess whether the changes in diversity across the years are significant.

Moving to ANOVA

**ANOVA** allows for the comparison of **multiple groups** simultaneously, unlike a **T-test**, which compares only two. Here, you will analyze microbial diversity across five time points: **1994**, **2004**, **2009**, **2014**, and **2024**. The goal is to determine whether **microbial diversity** has shifted significantly over the past 30 years. **ANOVA** works by comparing the **variance within each year** (how much diversity fluctuated within that year) against the **variance between years** (the overall change in diversity across time).

This analysis asks whether the five population mean Shannon indices differ. Describing a decline, stability, or taxonomic homogenization needs additional comparisons and biological evidence; the omnibus mean test alone cannot establish these patterns.

***&#8230;Ask the instructor for the next tutorial link.***

[https://docs.google.com/document/d/1xkWsWENaOLRHUk6MO50anhL4DEbjmK8\_xBmj22k3tts/edit](https://docs.google.com/document/d/1xkWsWENaOLRHUk6MO50anhL4DEbjmK8_xBmj22k3tts/edit)

- **Explain:** Write your own interpretation in `E26`. Include the calculated p-value, selected tail and alternative direction, significance level, and evidence-based conclusion. Do not type the example placeholders literally.

[image1]: assets/microbes_4_f_test_image1.png
