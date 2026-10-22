## **Microbial Diversity** **Benchmark T-Test Tutorial** **for BIOL 318/418**

## ![][image1]

## Part 2 Scenario:

Now, you face a more realistic challenge. Without knowing the true **population standard deviation** for microbial diversity, you must rely on the **sample standard deviation** from your collected data. This is where the **T-test** comes in. The T-test is specifically designed to handle smaller **sample sizes** and the uncertainty that comes from estimating the population standard deviation.

Feeling the pressure but determined to reach a solid conclusion about the health of Busse Woods, you open your spreadsheet again. This time, you will:

* Calculate the **sample mean** and **sample standard deviation** from your microbial diversity data.  
* Perform a **one-sample T-test** to determine if the microbial diversity in Busse Woods is significantly lower than the benchmark value of 4.0, indicating possible biodiversity loss due to urbanization

#### Why Use a T-Test Now?

In short, two reasons:

* **Unknown Population Standard Deviation**  
* **Small Sample Size**

In environmental data, like microbial diversity in a forest preserve, the **population standard deviation** is often unknown. Instead, you must estimate it using your **sample’s standard deviation**. This uncertainty makes the **T-test** the best fit. The **sample size** in your study is small (fewer than 30 samples), and the **T-test** accounts for extra variability from smaller datasets, providing a more accurate result under these conditions.

### Step 1: Set Up Your Google Sheet for the T-Test

1. Open your spreadsheet  
2. Create a new sheet and name it **"Part 2: Microbial T-Test"**.  
3. Again, copy the data from the **"Parts 1 and 2: Busse Woods 2024"** tab into your new sheet.

[https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit](https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit) 

4. The data in Column B represents the **Shannon Index** for microbial samples from Busse Woods.

### Step 2: Set Up the Known Population Values

1. Column C will be used for **Statistical Names**.  
2. Column D will contain the calculated values.  
3. In cell **C1**, type **"Statistical Names"**.  
4. In cell **D1**, type **"Values"**.  
5. In cell **C2**, type **"Population Mean,"** and in cell **D2**, enter **4.0** (the known average microbial diversity for similar ecosystems).

### Step 3: Calculate the Sample Statistics

1. In cell **C4**, type **"Sample Mean."**  
2. In cell **D4**, use the **AVERAGE** function to calculate the sample mean for your microbial diversity values:  
   * Enter: `=AVERAGE(B2:B101)`  
3. In cell **C5**, type **"Sample Standard Deviation."**  
4. In cell **D5**, use the **STDEV** function to calculate the sample standard deviation:  
   * Enter: `=STDEV(B2:B101)`  
5. In cell **C6**, type **"Sample Size,"** and in cell **D6**, use the **COUNT** function to count the number of samples:  
   * Enter: `=COUNT(B2:B101)`

### Step 4: Calculate the T-Statistic

1. In cell **C8**, type **"T-Statistic."**  
2. In cell **D8**, use this formula to calculate the t-statistic:  
   * Enter: `=(D4 - D2) / (D5 / SQRT(D6))`  
   * This formula uses the sample mean (D4), the assumed population mean (D2), the sample standard deviation (D5), and the sample size (D6).

#### Explanation: T-Statistic

The **T-statistic** measures how far the **sample mean** is from the **population mean**, relative to the variability in the sample. It accounts for both the **sample standard deviation** and the **sample size**, providing a standardized way to compare the sample to the population. By dividing the difference between the **sample mean** and the **population mean** by the standard error (which is the **sample standard deviation** divided by the square root of the **sample size**), the **T-statistic** allows us to determine how extreme the observed sample is compared to what we would expect if the **null hypothesis** were true.

### Step 5: Calculate the Degrees of Freedom

1. In cell **C9**, type **"Degrees of Freedom."**  
2. In cell **D9**, calculate the degrees of freedom using:  
   * Enter: `=D6 - 1`  
   * Here, `D6` is the sample size, so subtracting 1 gives us the degrees of freedom.

#### Explanation: Why Do We Use Degrees of Freedom?

In statistics, **degrees of freedom** represent the number of independent values in a dataset that can vary when estimating a statistical parameter. In the context of a **T-test**, degrees of freedom adjust for the uncertainty introduced when estimating the **population standard deviation** using the **sample standard deviation**.

When calculating the **sample standard deviation**, one of the values—typically the mean—is fixed based on the rest of the data. This is why we subtract **1** from the **sample size** to get the **degrees of freedom**. Smaller degrees of freedom result in a more conservative test, meaning we need stronger evidence to reject the **null hypothesis**. Larger sample sizes, and therefore more degrees of freedom, lead to a **T-distribution** that more closely resembles a **normal (Z) distribution**.

### Step 6: Determine the Type of Test (One-Tailed or Two-Tailed)

For the **T-test** on **microbial diversity** data from **Busse Woods**, you need to decide whether you are testing for any **significant difference** or a specific **directional difference** from the benchmark (**Shannon Index** of 4.0).

* **Two-Tailed Test:** Use this when you are checking if the **microbial diversity** is either **higher or lower** than the benchmark. This is for testing any significant deviation from the benchmark, regardless of direction.  
* **One-Tailed Test:** Use this when you have a specific hypothesis about the direction of the difference, such as testing if **microbial diversity** is **lower** than the benchmark. A **one-tailed test** focuses on deviations in a single direction.

In this case, since you suspect that the diversity has **decreased** due to **urbanization**, you would likely choose a **one-tailed test (lower)** to check if the **microbial diversity** is significantly **lower** than the benchmark.

### Step 7: Calculate the P-Values

In this step, we will calculate p-values, which help us understand how likely it is that the difference between the sample data and the benchmark is due to random chance.

You will calculate the **p-values** using different approaches: **T.DIST.2T** for the two-tailed test, **T.DIST** for flexible cumulative probability, and **T.TEST** for a direct statistical test. Each method provides a different way of assessing the statistical significance of your data. By comparing the results from each function, you will gain a clearer understanding of how the **T-test** works in Google Sheets.

### 7.1. Two-Tailed Test:

For the **two-tailed test**, you are testing whether the microbial diversity in **Busse Woods** is either **higher** or **lower** than the benchmark. Here are the function inputs you will use:

**T.DIST.2T(x, degrees\_freedom):** x is the absolute value of the **T-statistic** (calculated in **D8**), and **degrees\_freedom** is provided in **D9**. This function handles both tails of the distribution and calculates the p-value automatically.

**T.DIST(x, degrees\_freedom, cumulative):** x is the absolute value of the **T-statistic**, **degrees\_freedom** is in **D9**, and **cumulative** is set to **FALSE**. You will need to subtract from **1** and multiply by **2** to cover both sides of the distribution.

#### Step-by-Step Tutorial:

* In cell **C10**, type **"P-Value (Two-Tailed)"**.  
* In cell **D10**, enter the formula:  
  `=T.DIST.2T(ABS(D8), D9)`  
* In cell **E10**, enter the formula:  
  `=2 * (1 - T.DIST(ABS(D8), D9, TRUE))`

#### Explanation for Two-Tailed Test:

In a **two-tailed test**, you are checking whether the **microbial diversity** in Busse Woods is **significantly higher or lower** than the **benchmark**. The formula starts by calculating the **absolute value** of the **T-statistic** using **ABS(D8)**. This captures the **magnitude of the difference** between the **sample mean** and the **benchmark**.

The **T.DIST.2T** function handles **both tails** of the **distribution**. This means the result automatically accounts for deviations in **both directions**.

The second formula, **T.DIST**, requires you to handle **both sides manually**. First, calculate the **cumulative probability** for **one tail** using **T.DIST**. Then, subtract it from 1 to capture the **upper tail**. Finally, multiply by 2 to account for both **upper and lower tails**.

### 7.2. One-Tailed Test (for lower values):

For the **one-tailed test**, you are interested in testing whether the microbial diversity in **Busse Woods** is **lower** than the benchmark. This test will help you determine if environmental factors, such as urbanization, have reduced biodiversity. Here are the function inputs:

**T.DIST(x, degrees\_freedom, cumulative):** x is the **T-statistic** (calculated in **D8**), degrees\_freedom is in **D9**, and **cumulative** is set to **TRUE**. This function calculates the cumulative probability for values less than or equal to the **T-statistic**.

#### Step-by-Step Tutorial:

* In cell **C11**, type **"P-Value (One-Tailed, Lower)"**.  
* In cell **D11**, enter the formula:  
  `=T.DIST(D8, D9, TRUE)`  
* Leave cell **E11** blank

#### Explanation for One-Tailed Test (Lower):

In a **one-tailed test**, you are only interested in whether the microbial diversity is **lower** than the benchmark. The **T.DIST** function calculates the **cumulative probability** for values **less than or equal to** the **T-statistic**, meaning you are testing for values in the **lower tail** of the distribution. The **T.DIST.RT** function is typically used for **right-tailed tests**, but in this case, it is useful for testing **lower values**. **T.TEST** simplifies the process by allowing a one-tailed test with tails set to **1**.

### 7.3. One-Tailed Test (for higher values):

Although you are testing whether the microbial diversity is **lower** than the benchmark, it is also useful to calculate the **p-value** for the **opposite direction** to understand how much diversity might exceed expectations. Here are the function inputs for the **one-tailed test** for higher values:

**T.DIST.RT(x, degrees\_freedom):** x is the **T-statistic**, and **degrees\_freedom** is in **D9**. This function calculates the p-value for values **greater than** the **T-statistic**, testing for an increase in diversity.

**T.DIST(x, degrees\_freedom, cumulative):** x is the **T-statistic** (calculated in **D8**), degrees\_freedom is in **D9**, and **cumulative** is set to **TRUE**. This function calculates the cumulative probability for values less than or equal to the **T-statistic**. In order to get values above, we subtract this result from one.

#### Step-by-Step Tutorial:

* In cell **C12**, type **"P-Value (One-Tailed, Higher)"**.  
* In cell **D12**, enter the formula:  
  `=T.DIST.RT(D8, D9)`  
* In cell **E12**, enter the formula:  
  `=1 - T.DIST(D8, D9, TRUE)`

#### Explanation for One-Tailed Test (Higher):

This test examines whether the microbial diversity in **Busse Woods** is **higher** than the benchmark, testing for potential **increases** in biodiversity. The **T.DIST.RT** function calculates the probability of obtaining a **T-statistic** greater than or equal to the calculated value, which is ideal for testing whether the diversity exceeds the benchmark. This approach provides insight into the **upper tail** of the distribution and how microbial diversity might vary in the **opposite direction** of your primary hypothesis.

### Step 8: Decision Using an IF Statement

In hypothesis testing, the decision to **reject** or **fail to reject** the null hypothesis depends on comparing the p-value to a predetermined significance level (α). Typically, α is set at 0.05, meaning if the p-value is less than or equal to 0.05, we consider the result **statistically significant** and reject the null hypothesis. To streamline this decision process in Google Sheets, we will use the **IF statement**, which evaluates a condition and returns one value if the condition is true and another if false. In this case, we will check whether the p-value is less than or equal to α.

#### Step-by-Step Tutorial:

* In **cell C14**, type "**Significance Level (α)**." In **cell D14**, enter **0.05**.  
* In **cell C15**, type "**Two-Tail Decision**."  
* In **cell D15**, use the **IF statement** to determine whether to reject the null hypothesis using the two-tailed test p-value:  
  **Formula:** `=IF(D10 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`  
* In **cell C16**, type "**One-Tail Decision (Lower).**"  
* In **cell D16**, use the **IF statement** to determine whether to reject the null hypothesis using the one-tailed (lower) test p-value:  
  **Formula:** `=IF(D11 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`  
* In **cell C17**, type "**One-Tail Decision (Higher).**"  
* In **cell D17**, use the **IF statement** to determine whether to reject the null hypothesis using the one-tailed (higher) test p-value:  
  **Formula:** `=IF(D12 <= D14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

#### Explanation

The **IF statement** is a basic yet powerful programming concept that allows the program to evaluate a condition and make decisions. Here, we use it to compare the **p-value** to the **significance level (α)** and automate the decision-making process in hypothesis testing.

In statistical analysis, if the **p-value** is less than or equal to the **significance level (0.05)**, the result is considered **statistically significant**, meaning there is sufficient evidence to reject the null hypothesis. For instance, if the two-tailed test's p-value is ≤ 0.05, we reject the null hypothesis, indicating that microbial diversity in **Busse Woods** is **significantly different** from the benchmark. Conversely, if the p-value exceeds 0.05, we **fail to reject** the null hypothesis, implying the microbial diversity is **similar to the benchmark** and no significant deviation is found.

This process helps determine whether the data supports the conclusion that **urbanization** and **environmental factors** have affected microbial diversity at Busse Woods.

### Step 9: Interpret the Results

At this point, you should have conducted both the **two-tailed** and **one-tailed tests** (lower and higher) to compare the microbial diversity in **Busse Woods** against the benchmark value (Shannon Index \= 4.0). You should have determined that the focus is on the **One-Tailed Test (Lower)** to assess whether microbial diversity in **Busse Woods** is **significantly lower** than the benchmark. The goal is to determine if the diversity has declined due to **urbanization** or other **environmental pressures**. You are specifically testing if the microbial diversity in **Busse Woods** has decreased compared to the expected average for similar ecosystems.

#### Step-by-Step Tutorial:

1. In **cell C19**, type **Interpretation**.  
2. In **cell D19**, write a brief interpretation of your findings based on the one-tailed (lower) test. Example: "With a p-value of \[calculated value\], we \[reject/fail to reject\] the null hypothesis, indicating that microbial diversity in **Busse Woods** \[is/is not\] significantly lower than the benchmark."

#### Explanation:

In hypothesis testing, the interpretation depends on comparing the **p-value** to the **significance level** (α \= 0.05). If the **p-value** is **less than or equal to 0.05**, the result is considered **statistically significant**, meaning the null hypothesis is **rejected**. Rejecting the null hypothesis in this case suggests that microbial diversity in **Busse Woods** is **significantly lower** than the benchmark value of **4.0** (representing the average diversity for similar ecosystems). This implies that factors such as **urbanization**, **pollution**, or **climate change** may have contributed to a **decline in biodiversity** in the area.

If the **p-value is greater than 0.05**, you **fail to reject** the null hypothesis. This means there is **insufficient evidence** to conclude that microbial diversity is lower than the benchmark. In this scenario, microbial diversity in **Busse Woods** is either **equal to** or within the expected range for ecosystems similar to the benchmark, suggesting that biodiversity may not have been significantly affected by external factors.

Completing this interpretation allows you to clearly state whether microbial diversity in **Busse Woods** has been impacted by environmental changes, based on the results of your hypothesis test. This helps you draw meaningful conclusions about the **health of the ecosystem** and whether the data supports the hypothesis that biodiversity in **Busse Woods** has declined.

### Practice Task:

* Change some of the **Shannon Index** values for microbial diversity in **Column B** (Busse Woods data). Observe how the **sample standard deviation**, **t-statistic**, and **p-value** adjust automatically.  
* Add more sample locations (e.g., increasing the sample size beyond 30\) and note how the **p-value** changes. Discuss when the **one-sample T-test** results start to resemble those of a **z-test**.  
* Discuss how the flexibility in **sample size** affects the results of the **one-sample T-test** and compare this to your earlier **z-test** results. Specifically, observe how a larger sample size reduces uncertainty, impacting the p-value and overall hypothesis test results.

### Key Takeaways:

1. Use the **one-sample T-test** when comparing a dataset (e.g., **Shannon Index** values for microbial diversity in **Busse Woods**) to a known benchmark when the **population standard deviation is unknown** and/or the sample size is small.  
2. The **t-distribution** accounts for additional uncertainty introduced by using the **sample standard deviation** instead of the population standard deviation.  
3. As the **sample size increases**, the **one-sample T-test** results begin to resemble those of the **z-test**. This occurs because the **t-distribution** approximates the **normal distribution** as the sample size becomes larger, making the T-test and Z-test results more similar.  
4. The **one-sample T-test** is particularly useful for assessing whether microbial diversity in **Busse Woods** has significantly declined in comparison to the benchmark, especially when the sample size is limited.

## Part 3 Setup: Microbial Diversity at Busse Woods

After conducting the **T-test** on microbial diversity at **Busse Woods**, your confidence in the significant difference from the benchmark began to waver. The results of the **T-test** did not confirm the earlier findings from the **Z-test**, and you now question whether the diversity at **Busse Woods** is truly different from the benchmark.

This project is important to you. For months, your team has monitored the effects of **urbanization** and **climate change** on biodiversity in urban forest preserves. **Busse Woods**, once considered a pristine environment, has shown signs of stress in recent years. Your goal was to provide hard data showing whether these changes were affecting **microbial ecosystems**, a key indicator of environmental health. While the **Z-test** initially suggested a significant shift, the new results call that conclusion into doubt.

Just as you were preparing to discard your report and start over, your advisor suggested a new approach. You both remembered that your team has access to a rich dataset from **2014**, a time when concerns about rising temperatures and pollution were increasing. Instead of only comparing the current data to a benchmark, your advisor proposed analyzing changes over time. This could provide a clearer picture of how **Busse Woods** has evolved in response to **environmental pressures**.

By comparing your current data from **2024** with diversity data collected in **2014**, you can determine whether there has been a significant decrease in microbial diversity over the last decade. This **longitudinal analysis** will allow you to draw meaningful conclusions about how these factors have impacted **Busse Woods' microbial communities**.

### Moving to the Two Sample T-Test

In the next part of this tutorial, we will learn how to conduct a **Two Sample T-test**, which allows for a direct comparison between **two different datasets**. By comparing microbial diversity from **Busse Woods in 2014** with your current data from **2024**, you will gain insights into how the ecosystem has changed over the past decade. This analysis could reveal whether **urbanization** and **climate change** are contributing to the loss of biodiversity in the area. The findings from this comparison may provide stronger evidence to support conservation efforts and inform future environmental policies.

***…Ask the instructor for the next tutorial link.***

[image1]: <data:image/png;base64,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>