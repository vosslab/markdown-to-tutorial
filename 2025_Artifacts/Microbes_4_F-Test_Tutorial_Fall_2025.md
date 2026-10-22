## **Microbial Diversity Two Sample F-Test Tutorial** **for BIOL 318/418**

![][image1]

## Part 4 Scenario

After comparing the microbial diversity in **Busse Woods** between **2014** and **2024** using a **Two Sample T-test**, you successfully confirmed that the overall diversity has **decreased** over the past decade. However, while analyzing the data further, you observe something unexpected: the **2024 Shannon Index values** appear more **similar** to one another compared to those from **2014**. This raises new questions about whether the **variability** in microbial diversity has changed alongside the mean. Could environmental pressures like **urbanization** and **climate change** be not only reducing biodiversity but also making microbial communities more **uniform**?

Excited by this idea, you present your findings to your advisor, who praises your observation and suggests conducting an **F-test** to compare the **variances** between the two years. By comparing the **spread** of diversity values in **2014** and **2024**, the **F-test** will help determine whether environmental pressures are contributing to the **homogenization** of microbial communities in **Busse Woods**. This could reveal important insights into how **ecological resilience** is changing and whether some of the forest's unique **microenvironments** are being lost.

#### Why Use an F-Test Now?

While the **Two Sample T-test** compared the **means** of microbial diversity between **2014** and **2024**, the **F-test** allows you to assess the **variances**. This test is ideal when you need to determine whether the **spread** of data has changed significantly between two groups or time periods. In this case, it will help you explore whether the microbial communities in **Busse Woods** have become more **uniform**, providing a deeper understanding of how the ecosystem is evolving under **environmental pressures**.

### Step 1: Copy the Data

1. Open your spreadsheet.
2. Create a new sheet and name it **"Part 4: Two Sample F-Test"**.
3. Copy the data from the "**Part 3 and 4: Busse Woods 2014 and 2024**" tab into the new sheet.

[https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit](https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit)

### Step 2: Organize Your Sheet

1. The data will look like this:
   * **Column A**: Sample Location ID
   * **Column B**: **2014 Shannon Index** (microbial diversity from the 2014 dataset)
   * **Column C**: **2024 Shannon Index** (current microbial diversity data)
   * **Column D**: Statistical Names
   * **Columns E through G**: Calculated Values
2. Here's how to set it up:
   * In cell **D1**, type "**Statistical Names**".
   * In cell **E1**, type "**Values**".
   * In cell **F1**, type "**Alternate Values 1**".
   * In cell **G1**, type "**Alternate Values 2**".

### Step 3: Calculate the Sample Statistics

Now, let us calculate the statistics needed for both datasets.

1. **Sample Means**:
   * Sample means are not needed for the F-test, so you can skip this step.
2. **Sample Standard Deviations**:
   * In cell D5, type **2014 Sample Standard Deviation**.
   * In **E5**, use the formula `=STDEV(B2:B101)` to calculate the sample standard deviation for **2014**.
   * In cell D6, type **2024 Sample Standard Deviation**.
   * In **E6**, use the formula `=STDEV(C2:C101)` to calculate the sample standard deviation for **2024**.
3. **Sample Sizes**:
   * In cell D8, type **2014 Sample Size**.
   * In **E8**, use the formula `=COUNT(B2:B101)` to count the number of samples for **2014**.
   * In cell D9, type **2024 Sample Size**.
   * In **E9**, use the formula `=COUNT(C2:C101)` to count the number of samples for **2024**.

### Step 4: Calculate the F-Statistic

Now, we will calculate the **F-statistic** to compare the **variances** of the two datasets.

* In **cell D11**, type **F-Statistic**.
* In **E11**, calculate the **F-statistic** using this formula:
  `=E6^2 / E5^2`

#### Explanation: F-Statistic

The **F-statistic** is used to compare the **variances** of two samples. It is the ratio of the variances of the two datasets (2014 and 2024). If the **F-statistic** is close to **1**, it indicates that the **variances** of the two datasets are similar. However, a larger **F-statistic** (significantly greater than **1**) suggests that the **variances** are different, with one sample having more **spread** in the diversity values than the other.

It is important to note that **sample means are not relevant** for the **F-test**. The test focuses entirely on the **spread** of the data (**variance**), regardless of where the data is centered (**mean**). This means that even if the two groups have the same or different means, the **F-test** only cares about how **spread out** the values are in each group.

This calculation will help determine whether the **spread** (**variability**) in microbial diversity across sampling locations has changed over time. This could indicate a shift toward more **uniformity** or **homogenization** in the **2024 data**, suggesting that environmental pressures may have made the microbial communities in **Busse Woods** more **consistent** in their diversity, possibly reducing their **ecological resilience**.

### Step 5: Calculate the Degrees of Freedom

In an **F-test**, degrees of freedom are used differently than in a **T-test**. In this case, the degrees of freedom correspond to the **sample sizes** of each group, minus one for each. The **F-test** compares the **variances** of two samples, and the degrees of freedom help us interpret how reliable these variance estimates are.

**Step-by-Step Tutorial**:

* In **cell D13**, type **Degrees of Freedom for 2014**.
* In **E13**, type `=E8 - 1` to calculate the degrees of freedom for the **2014 dataset**.
* In **cell D14**, type **Degrees of Freedom for 2024**.
* In **E14**, type `=E9 - 1` to calculate the degrees of freedom for the **2024 dataset**.

#### Explanation

In the **F-test**, the **degrees of freedom (DF)** represent the number of independent data points used to calculate the variance in each sample. For each sample, the **DF** is calculated as **sample size \- 1**. This reflects the fact that one degree of freedom is used up in estimating the mean, so only the remaining data points are "free to vary."

These degrees of freedom are used to interpret the **F-statistic**, which compares the **variances** of the two samples. Larger degrees of freedom make the test more reliable because they indicate a more accurate estimate of the population variance.

In **biological studies**, where **sample sizes** are often small, the **F-distribution** becomes wider, meaning that it takes a larger difference in variances to conclude that they are statistically different. As degrees of freedom increase (i.e., as the sample size increases), the **F-distribution** approaches the shape of a **normal distribution**, leading to more precise results.

### Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)

In an **F-test**, you are testing whether the **variances** between two datasets (in this case, the Shannon Index values for 2014 and 2024\) are significantly different. You need to decide whether you are testing for any significant difference in variance (a **two-tailed test**) or a specific hypothesis about which year has greater variance (a **one-tailed test**).

* **Two-Tailed Test**: This test is used to check whether the **variance** of microbial diversity in 2024 is **significantly different** (either higher or lower) from that in 2014\. If you are unsure about the direction of change but suspect there is a difference in the variability of the data, the two-tailed test is appropriate.
* **One-Tailed Test**: This test is used when you have a specific hypothesis about the direction of the variance difference. For example:
  * **Lower One-Tailed Test**: This checks if the **variance** in 2024 is **lower** than in 2014, suggesting that microbial diversity in 2024 may be more **homogeneous** than in 2014\.
  * **Higher One-Tailed Test**: This checks if the **variance** in 2024 is **higher** than in 2014, which could indicate that the microbial diversity in 2024 has **greater variability**.

For an **F-test**, you are no longer testing the **mean** or **direction of change** in microbial diversity but rather whether the **spread of values (variance)** has changed significantly. In this case, because you suspect that environmental factors have **reduced variability** in microbial diversity in 2024, a **lower one-tailed F-test** would be appropriate.

### Step 7: Calculate the P-Values

Now that you are working with two samples (2014 and 2024 Shannon Index values), you will calculate the **F-statistic** and the **p-values** to compare the **variances** of microbial diversity between these two datasets. The **F-statistic** is the ratio of the variances between the two groups, and the **p-value** will help you determine if the observed variance difference is statistically significant.

You will perform both **two-tailed** and **one-tailed** tests (lower and higher) to check if the **variance** of microbial diversity has either increased or decreased from 2014 to 2024\. You will also use both **manual calculations** and the **F.TEST** function to automate the process.

#### Explanation of F.DIST Inputs:

The function **`F.DIST`** is used to calculate the cumulative distribution function (CDF) of the F-distribution, which tells us the probability that the observed F-statistic is due to random chance. Here are the inputs:

* **F.DIST(x, degrees\_freedom1, degrees\_freedom2, cumulative)**
  * **x**: This is the **F-statistic**, calculated as the ratio of the variances of the two groups.
  * **degrees\_freedom1**: This is the **degrees of freedom** for the first dataset (for example, the 2014 dataset), calculated as the sample size minus one.
  * **degrees\_freedom2**: This is the **degrees of freedom** for the second dataset (for example, the 2024 dataset), calculated as the sample size minus one.
  * **cumulative**: This specifies whether you want the **cumulative distribution function** (TRUE) or the **probability density function** (FALSE). You will use TRUE for calculating the cumulative probability.

#### Explanation of F.TEST Inputs:

The function **`F.TEST`** simplifies the F-test process by directly comparing the variances of two datasets and calculating the p-value. Here are the inputs:

* **F.TEST(array1, array2)**
  * **array1**: This is the range of values for the first dataset (for example, the 2014 Shannon Index values in column B).
  * **array2**: This is the range of values for the second dataset (for example, the 2024 Shannon Index values in column C).

The **`F.TEST`** function returns the **p-value**, which tells you whether the variance between the two datasets is significantly different. A smaller **p-value** (less than 0.05) suggests that the difference in variance is statistically significant.

### 7.1. Two-Tailed Test:

This test checks if the **variance** in microbial diversity has changed in **either direction** between 2014 and 2024\.

#### Step-by-Step Tutorial:

* In **cell D16**, type **P-Value (Two-Tailed)**.
* In **E16**, calculate the **F-statistic** using the following formula:
  * `=2 * F.DIST(ABS(E11), E13, E14, TRUE)`
  * This calculates the **F-statistic** based on the **variance** ratio of the two samples and their degrees of freedom.
* In **G16**, calculate the **p-value**:
  * `=F.TEST(C2:C101, B2:B101)` 0.044
  * This calculates the **two-tailed p-value** directly, comparing the **variances** between the two datasets (2014 in column B and 2024 in column C).

#### Explanation for Two-Tailed Test:

In this two-tailed **F-test**, you are testing whether the **variance** in microbial diversity has **significantly changed** between 2014 and 2024\. The **F.DIST** function compares the **variances** of the two datasets, and the **F.TEST** function simplifies the process by calculating the p-value automatically. A significant **p-value** suggests that the **spread** (variance) in microbial diversity has either **increased or decreased** between 2014 and 2024\.

### 7.2. One-Tailed Test (for lower values):

This test evaluates whether the **variance** in microbial diversity is **lower** in 2024 than in 2014, suggesting that the diversity is becoming more **homogeneous**.

#### Step-by-Step Tutorial:

* In **cell D17**, type **P-Value (One-Tailed, Lower)**.
* In **E17**, use the following formula: `=F.DIST(E11, E13, E14, TRUE)` This calculates the **F-statistic** for a **lower one-tailed test**, testing if the **variance** in 2024 is smaller than in 2014\.
* In **G17**, calculate the **one-tailed p-value** using: `=F.TEST(C2:C101, B2:B101)/2` This provides a quicker calculation, testing if the **variance** in 2024 is significantly lower.

#### Explanation for One-Tailed Test (Lower):

In this **one-tailed F-test**, you are testing if the **variance** in microbial diversity has **decreased**, meaning the diversity values are becoming more **uniform** in 2024\. If the **p-value** is significant, it suggests that the **variance** in 2024 is **lower**, indicating possible environmental pressures leading to more uniform microbial communities.
Since the **F.TEST** gives a **two-tailed p-value**, dividing by 2 adjusts it for a **one-tailed test**. For the **one-tailed lower test**, this means you are checking whether the variance in 2024 is significantly **lower** than in 2014\. The p-value needs to reflect this **one-directional** hypothesis.

### 7.3. One-Tailed Test (for higher values):

This test evaluates whether the **variance** in microbial diversity is **higher** in 2024 than in 2014, suggesting that diversity is becoming more **variable**.

#### Step-by-Step Tutorial:

1. **In cell D18,** type **P-Value (One-Tailed, Higher)**.
2. **In E18,** use the following formula: `=F.DIST.RT(E11, E13, E14)`.
   * This formula calculates the F-statistic for a higher one-tailed test, checking if the variance in **2024** is greater than that of **2014**.
   * The **F.DIST.RT** function calculates the right-tailed probability, which tests whether the variance in 2024 is significantly greater than in 2014\.
3. **In F18,** use the following formula: `=F.DIST(E5^2 / E6^2, E13, E14, TRUE)`.
   * This formula performs the same test but with the variances swapped. It evaluates if the variance in **2024** is greater than the variance in **2014** by reversing the order of the ratio.
   * This approach helps confirm the results and provides insight into how the variances compare.
4. **In G18,** calculate the one-tailed p-value using: `=1 - F.TEST(C2:C101, B2:B101)/2`.
   * This function simplifies the calculation, directly testing if the variance in **2024** is greater than in **2014** by comparing the two datasets.

#### Explanation for One-Tailed Test (Higher):

In this **one-tailed F-test**, you are assessing whether the **variance in microbial diversity** has increased between 2014 and 2024\. A higher variance in 2024 suggests that diversity values are becoming more spread out, indicating greater variability in microbial communities.

The formula **F.DIST.RT(E6^2 / E5^2)** specifically tests if **2024** has more variability than **2014** by calculating the ratio of their variances. If the **p-value** is significant (typically less than 0.05), this means the **variance in 2024 is statistically greater** than in 2014\. This increased spread in diversity values could indicate that **environmental factors**-such as urbanization or climate changes-have led to more variability across microbial communities.

By testing both directions (with swapped ratios), you can confirm which year has higher variability, providing a robust analysis of how microbial diversity has evolved.

### Step 8: Decision Using an IF Statement

In hypothesis testing, the decision to **reject** or **fail to reject** the **null hypothesis** is based on comparing the **p-value** to a predetermined **significance level (&alpha;)**, often set at **0.05**. If the p-value is less than or equal to **0.05**, the result is considered **statistically significant**, meaning the variance between the two years (2014 and 2024\) is unlikely to have occurred by chance. To make this process easier, we will use the **IF statement** in Google Sheets, which evaluates a condition and returns one value if true and another if false. In this case, we will check whether the p-value is less than or equal to **&alpha; (0.05)**.

#### Step-by-Step Tutorial:

* **In cell D20,** type **Significance Level (&alpha;)**.
* **In cell E20,** enter **0.05**.
* **In cell D22,** type **Two-Tail Decision**.
* **In cell E22,** use the formula
  * `=IF(E16 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  * to determine whether to reject the null hypothesis using the two-tailed test p-value.
* **In cell D23,** type **One-Tail Decision (Lower)**.
* **In cell E23,** use the formula
  * `=IF(E17 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  * to determine whether to reject the null hypothesis using the one-tailed (lower) test p-value.
* **In cell D24,** type **One-Tail Decision (Higher)**.
* **In cell E24,** use the formula
  * `=IF(E18 <= E20, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  * to determine whether to reject the null hypothesis using the one-tailed (higher) test p-value.

#### Explanation

The **IF statement** simplifies decision-making by evaluating whether the **p-value** is **less than or equal to 0.05** (our significance level). If it is, the test result is **statistically significant**, and you **reject the null hypothesis**, meaning the variance between the two years is significantly different. For instance, if the one-tailed (higher) test p-value is less than **0.05**, you would reject the null hypothesis, indicating that the variance in **2024** is significantly higher than in **2014**. Conversely, if the p-value is greater than **0.05**, you would **fail to reject the null hypothesis**, implying that the variance between the two years is not significantly different.

This automated process ensures that you can efficiently assess whether there has been a significant change in microbial diversity variance over time in Busse Woods, allowing for a clearer interpretation of the results and the effects of environmental pressures on biodiversity.

### Step 9: Interpret the Results

You have just conducted the **F-test** to compare the **variance** in microbial diversity between **2014** and **2024**. Your focus is on determining whether the **variability** in the **Shannon Index** has significantly changed. Specifically, you are testing if the **2024 Shannon Index** values are **more uniform** or **more spread out** compared to **2014**.

#### Step-by-Step Tutorial:

* In **cell D26**, type **Interpretation.**
* **In cell E26**, write a brief interpretation of your findings based on the **F-test** results. Example:
* *"With a p-value of \[calculated value\], we \[reject/fail to reject\] the null hypothesis, indicating that the variance in microbial diversity in Busse Woods \[is/is not\] significantly different in 2024 compared to 2014."*

#### Explanation:

The interpretation depends on comparing the **p-value** to the **significance level** (**&alpha; \= 0.05**). If the p-value is less than or equal to **0.05**, the result is **statistically significant**, and you **reject** the null hypothesis. This means that the **variance** in **2024** is significantly **higher** or **lower** than in **2014**, depending on whether you used a **one-tailed** or **two-tailed** test.

If the **p-value** is greater than **0.05**, you **fail to reject** the null hypothesis. This suggests that there is no significant difference in the **variances**, meaning the microbial diversity in **2024** is either **similarly variable** or **more uniform** than in **2014**. This provides insight into whether environmental factors like **urbanization** or **climate change** are affecting the **spread** of microbial diversity, not just the **mean**.

By interpreting the results of the **F-test**, you can assess if environmental pressures are contributing to changes in both the **diversity** and the **variability** of microbial communities over time.

### Practice Task:

* Change some of the **Shannon Index** values in **Column B** (2014 data) and **Column C** (2024 data). Observe how the **sample standard deviations**, **F-statistic**, and **p-value** adjust.
* Add more sample locations (e.g., increase sample size beyond 30\) and see how this impacts the **F-statistic** and **p-value**.
* Discuss how **sample size** affects the **F-test** results and compare this to earlier **T-test** results. Focus on how a larger sample size reduces **uncertainty** and impacts the **p-value** and the **F-distribution**.

### Key Takeaways:

1. Use the **F-test** to compare the **variability** (variance) between two datasets. This is useful for assessing whether environmental factors are leading to more **uniformity** or more **variability** in microbial diversity.
2. The **F-distribution** focuses on comparing **variance** rather than **mean** values, giving a clearer picture of changes in **data spread**.
3. Larger **sample sizes** improve the reliability of the **F-test**, but the test remains useful for small sample sizes when examining differences in **variability**.
4. The **F-test** complements the **T-test** by focusing on the **spread** of data in microbial diversity, which can reveal different patterns in **ecosystem health** over time.

## Part 5 Setup: Expanding the Investigation into More Years with ANOVA

After conducting the **F-test** comparing microbial diversity in **2014** and **2024**, you successfully **rejected the null hypothesis**. The analysis confirmed a **decrease in diversity** and revealed that **2024** showed significantly **less variance** than **2014**. This raises important questions: Has this trend been ongoing for years? Has the decline in diversity and **reduction in variability** been happening gradually?

As you think about this, an idea strikes. You recall older data in the lab that has not been analyzed for years. Early in your time here, you heard about old student theses where previous graduate students collected microbial diversity data before modern sequencing methods became available. These projects were massive, each representing an entire thesis, where students relied on traditional culture-based techniques to estimate diversity.

Without DNA sequencing, these students used **plate counts** and **staining techniques** to identify and quantify microbial species. They grew colonies on **selective media** and counted **colony-forming units (CFUs)** as a measure of microbial abundance. Each species formed colonies with distinct **colors, shapes, or growth patterns**. Staining methods like **Gram staining** helped differentiate species, allowing for accurate identification and counts within the microbial community.

These methods, while labor-intensive, provided valuable **estimates of microbial diversity**. Manual colony counting required days of careful incubation and observation. Despite the limitations of these methods, the meticulous documentation provided solid data that can now offer insights into **microbial ecosystems** before high-throughput technologies.

Inspired by this, you explore three theses from **1994**, **2004**, and **2009**, each containing **Shannon Index values** based on these traditional microbial techniques. Combining this older data with the **2014** and **2024** data gives you a **30-year timeline** of microbial diversity at **Busse Woods**. Now, you are ready to conduct an **ANOVA (Analysis of Variance)** to determine if the trends in microbial diversity over time are **statistically significant**.

With all the data in hand, you can now analyze how microbial diversity has shifted over the decades. **ANOVA** will allow you to compare multiple time points at once, helping you assess whether the changes in diversity across the years are significant.

### Moving to ANOVA

**ANOVA** allows for the comparison of **multiple groups** simultaneously, unlike a **T-test**, which compares only two. Here, you will analyze microbial diversity across five time points: **1994**, **2004**, **2009**, **2014**, and **2024**. The goal is to determine whether **microbial diversity** has shifted significantly over the past 30 years. **ANOVA** works by comparing the **variance within each year** (how much diversity fluctuated within that year) against the **variance between years** (the overall change in diversity across time).

This analysis will reveal whether diversity declines started earlier or if periods of stability in microbial communities existed. It will also help determine if the **homogenization** observed in **2024** is a recent occurrence or part of a longer-term trend.

***...Ask the instructor for the next tutorial link.***

[https://docs.google.com/document/d/1xkWsWENaOLRHUk6MO50anhL4DEbjmK8\_xBmj22k3tts/edit](https://docs.google.com/document/d/1xkWsWENaOLRHUk6MO50anhL4DEbjmK8_xBmj22k3tts/edit)

[image1]: <data:image/png;base64,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>
