## **Microbial Diversity ANOVA Tutorial** **for BIOL 318/418**

![][image1]

## Part 5 Scenario

After successfully rejecting the **null hypothesis** using the **F-test**, you confirmed that microbial diversity in Busse Woods not only decreased between 2014 and 2024 but also became more **uniform**. However, this raised new questions: Has this pattern of declining diversity and reduced variability been happening for even longer? To investigate, you now have microbial diversity data spanning **30 years**, from **1994 to 2024**.

To analyze how microbial diversity has shifted over time, you decide to use **ANOVA** (Analysis of Variance). This statistical test will allow you to compare microbial diversity across **five different time points**: **1994**, **2004**, **2009**, **2014**, and **2024**. By comparing these years, you can determine if the trends seen in recent years are part of a longer-term decline or if there were periods of **stability**.

#### Why Use ANOVA Now?

**ANOVA** is ideal for comparing more than two groups, making it the perfect tool for analyzing microbial diversity across multiple years. This test will help determine whether the **diversity values** have changed significantly over time by comparing the **variance** within each year to the **variance** between the years. By doing so, you can assess whether the observed **decline** and **homogenization** of microbial communities is a recent phenomenon or part of a larger, long-term trend.

### Step 1: Copy the Data

#### Step-by-Step Tutorial:

1. **Access the data source:**  
   * Go to the following link:

[https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit](https://docs.google.com/spreadsheets/d/1cAlU997q8IazW6wJhBwYRrrO2l6ls0yCAo3Rx9BlUY0/edit) 

* In the **Part 5: ANOVA data** tab, click on the **down triangle** next to the tab name.  
  ![][image2]  
  * Select **Copy to**.  
  * Choose “**Existing spreadsheet”**.  
  * A window will pop up asking for the link to your target spreadsheet.  
2. **Link your spreadsheet:**  
   * Go back to your tutorial document and copy your spreadsheet link from the table above.  
   * Paste the link into the pop-up window and hit **Enter**.  
   * Click on your spreadsheet from the pop-up list and hit **Insert**.  
3. **Find the copied data:**  
   * Go to your own spreadsheet.  
   * Find the tab labeled **"Copy of Part 5: ANOVA Data"**. This contains the dataset you need for the analysis.  
   * Rename the new tab to **"Part 5: 30 Year ANOVA Test, Fixed"**.

### Step 2: Organize Your Sheet into an ANOVA Table Layout

In this step, we will set up a traditional ANOVA table with **source of variation**, **sum of squares (SS)**, **degrees of freedom (DF)**, **mean square (MS)**, **F-statistic**, and **P-value**.

#### **ANOVA Table Setup:**

1. **Column A-F**: Your raw data for each year (1994, 2004, 2009, 2014, and 2024).  
2. **Column G**: we will leave this blank to separate the data from the calculations  
3. **Column H**: This column will be used to label the **sources of variation** in the ANOVA.  
4. **Columns I-M**: These columns will contain the calculated values for sums of squares, degrees of freedom, mean squares, F-statistic, and p-value.

#### Step-by-Step Tutorial:

1. In **Column H**, create the row headers for the **ANOVA table**:  
   * **H1**: Type **"Source of Variation"**.  
   * **H2**: Type **"Between Groups"**.  
   * **H3**: Type **"Within Groups"**.  
   * **H4**: Type **"Total"**.  
2. In **Column I**, add the following column headers:  
   * **I1**: Type **"Degrees of Freedom (DF)"**.  
   * **J1**: Type **"Sum of Squares (SS)"**.  
   * **K1**: Type **"Mean Square (MS)"**.  
   * **L1**: Type **"F-Statistic"**.  
   * **M1**: Type **"P-Value"**.  
3. The final table should look something like this

| Source of Variation | Degrees of Freedom (DF) | Sum of Squares (SS) | Mean Square (MS) | F-Statistic | P-Value |
| :---: | ----- | ----- | ----- | ----- | ----- |
| **Between Groups** |  |  |  |  |  |
| **Within Groups** |  |  |  |  |  |
| **Total** |  |  |  |  |  |

### Step 3: Calculate the Group Statistics

The first step in an ANOVA test is to calculate the basic statistics for each group (in this case, each year). You need to calculate the **mean**, **variance**, and **sample size** for each group. These statistics will help us understand how each group differs individually before comparing them across time.

#### Step-by-Step Tutorial:

We will set up another table to organize the **group statistics** for each year.

1. **Setup Another Table:**  
   * In **cell H6**, type **Sample Name**.  
   * In **cell I6**, type **1994 Sample**.  
   * In **cell J6**, type **2004 Sample**.  
   * In **cell K6**, type **2009 Sample**.  
   * In **cell L6**, type **2014 Sample**.  
   * In **cell M6**, type **2024 Sample**.  
2. **For Sample Means:**  
   * In **cell H7**, type **Sample Means**.  
   * In **cell I7**, use the formula `=AVERAGE(B:B)` to calculate the **sample mean** for 1994\.  
   * In **cell J7**, use the formula `=AVERAGE(C:C)` to calculate the **sample mean** for 2004\.  
   * In **cell K7**, use the formula `=AVERAGE(D:D)` to calculate the **sample mean** for 2009\.  
   * In **cell L7**, use the formula `=AVERAGE(E:E)` to calculate the **sample mean** for 2014\.  
   * In **cell M7**, use the formula `=AVERAGE(F:F)` to calculate the **sample mean** for 2024\.  
3. **For Sample Variances:**  
   * In **cell H8**, type **Sample Variances**.  
   * In **cell I8**, use the formula `=VAR.S(B:B)` to calculate the **sample variance** for 1994\.  
   * In **cell J8**, use the formula `=VAR.S(C:C)` to calculate the **sample variance** for 2004\.  
   * In **cell K8**, use the formula `=VAR.S(D:D)` to calculate the **sample variance** for 2009\.  
   * In **cell L8**, use the formula `=VAR.S(E:E)` to calculate the **sample variance** for 2014\.  
   * In **cell M8**, use the formula `=VAR.S(F:F)` to calculate the **sample variance** for 2024\.  
4. **For Sample Sizes:**  
   * In **cell H9**, type **Sample Sizes**.  
   * In **cell I9**, use the formula `=COUNT(B:B)` to calculate the **sample size** for 1994\.  
   * In **cell J9**, use the formula `=COUNT(C:C)` to calculate the **sample size** for 2004\.  
   * In **cell K9**, use the formula `=COUNT(D:D)` to calculate the **sample size** for 2009\.  
   * In **cell L9**, use the formula `=COUNT(E:E)` to calculate the **sample size** for 2014\.  
   * In **cell M9**, use the formula `=COUNT(F:F)` to calculate the **sample size** for 2024\.

#### Explanation:

This step focuses on calculating the **group statistics**: the **means**, **variances**, and **sample sizes** for each year’s data. These values will be crucial for the ANOVA test because they allow us to assess how each group behaves individually. The **means** show us the average microbial diversity in each year, while the **variances** tell us how much the data is spread out within each year. Finally, the **sample sizes** help evaluate the reliability of these statistics for each year.

These statistics will feed into the next step, where we calculate the **sums of squares** and start filling out the ANOVA table.

### Step 4: Calculate the Grand Mean

In this step, you will calculate the **grand mean**, which is the overall average of all data points across the different groups. The grand mean helps you compare individual group means to the overall dataset. It serves as a reference point for future steps, such as calculating the total variability and assessing how much each group deviates from the overall dataset. You will calculate the grand mean using the **AVERAGE** function to capture the mean of all values in the dataset.

#### Step-by-Step Tutorial:

* In **cell H11**, type **Grand Mean**.  
* In **cell I11**, use the formula `=AVERAGE(B:F)` to calculate the **overall mean** of all the Shannon Index values.

### Step 5: Calculate the Degrees of Freedom (DF)

In this step, you will calculate the **Degrees of Freedom (DF)** for both the **between groups** (DF treatment) and **within groups** (DF error) components, as well as the **total DF**. The DF reflects the number of independent data points contributing to each variance estimate. In ANOVA, the DF for each component helps us understand the amount of information available for estimating the variability between and within groups.

#### Step-by-Step Tutorial:

* In **cell `I2`**, use the formula `=COUNT(I7:M7) - 1` to calculate the **DF Between** (DF treatment). This calculates the degrees of freedom for the variation between groups, which is the number of groups minus one.  
* In **cell `I3`**, use the formula `=COUNT(B2:F101) - COUNT(I7:M7)` to calculate the **DF Within** (DF error). This calculates the degrees of freedom for the variation within groups by subtracting the number of groups from the total number of observations.  
* In **cell `I4`**, use the formula `=COUNT(B2:F101) - 1` to calculate the **DF Total**. This is the degrees of freedom for the total variability, representing the total number of observations minus one.

#### Explanation:

The **Degrees of Freedom (DF)** reflect the number of independent values that contribute to the variance estimates in the ANOVA table. Here is how the different components of the DF are calculated:

* **DF Between (DF treatment)**: This is the degrees of freedom associated with the variability between groups (for example, between different years). It is calculated as the number of groups (**k**) minus one. The formula `=COUNT(I7:M7) - 1` counts the number of groups and subtracts one.  
* **DF Within (DF error)**: This is the degrees of freedom associated with the variability within groups. It is calculated as the total number of observations (**n**) minus the number of groups (**k**). The formula `=COUNT(B2:F101) - COUNT(I7:M7)` calculates the total number of observations and subtracts the number of groups to give the DF within.  
* **DF Total**: This is the total degrees of freedom, representing the total variability in the dataset. It is calculated as the total number of observations (**n**) minus one. The formula `=COUNT(B2:F101) - 1` calculates this directly.

The relationship between these degrees of freedom is: `DF Total = DF Between + DF Within`

### Step 6: Calculate the Regression Sum of Squares (SSR)

In this step, you will calculate the **Regression Sum of Squares (SSR)**. This represents how much of the total variance is explained by the differences between the group means. The SSR helps quantify the portion of the total variation that can be attributed to the differences between the groups, such as the different years in your dataset.

#### Step-by-Step Tutorial:

* Go back up to our original table.  
* In **cell `J2`**, type the formula `=SUMPRODUCT((I7:M7 - I11)^2, I9:M9)` to calculate the **SS Between**.

#### Explanation:

The **SSR** quantifies the variation between the group means and how much of the total variance can be explained by the differences between those means. By comparing the mean values of each group to the **grand mean** (the overall average), the **SSR** isolates the variance due to differences between the groups. This is calculated by summing the squared deviations of each group mean from the grand mean, weighted by the sample size of each group.

The **SUMPRODUCT** function multiplies corresponding elements from two arrays and sums the products. In this case, `(I7:M7 - I10)^2` calculates the squared differences between each group mean (from cells `I7:M7`) and the grand mean (in `I11`). The second array, `I9:M9`, contains the sample sizes for each group. **SUMPRODUCT** multiplies these squared differences by the respective sample sizes and sums them to yield the **SSR**, which tells us how much of the total variance is explained by the differences between the group means.

### Step 7: Calculate the Error Sum of Squares (SSE)

In this step, you will calculate the **Error Sum of Squares (SSE)**. This measures the variation within each group that cannot be explained by differences between the group means. It captures how much of the total variability is due to random differences within the groups.

#### Step-by-Step Tutorial:

1. In **cell `J3`**, use the formula `=SUMPRODUCT((I9:M9 - 1), I8:M8)` to calculate the SSE. This formula calculates the squared deviations of each observation from its respective group mean.

#### Explanation:

The **SSE** quantifies the variability within the groups that is not explained by the differences between the group means. By calculating the squared deviations of each observation from the group mean, this step identifies the portion of variance due to random fluctuations within each group. Summing these squared deviations provides the **SSE**, which is essential for understanding how much of the total variation is due to within-group differences.

### Step 8: Calculate the Total Sum of Squares (SST)

In this step, you will calculate the **Total Sum of Squares (SST)**, which measures the overall variability in the dataset. The SST accounts for both the variability between the group means (SSR) and the variability within each group (SSE). It compares each data point to the **grand mean** to capture the total variance in the dataset.

#### Step-by-Step Tutorial:

2. In **cell `J4`**, use the formula `=J2 + J3` to calculate the SST.

#### Explanation:

The **Total Sum of Squares (SST)** measures the overall variance in the dataset by comparing each individual data point to the grand mean. It captures all the variability present in the data. The **SST** is broken down into two components:

1. **SSR**: The portion of the total variance explained by the differences between the group means.  
2. **SSE**: The portion of the total variance that is due to random variability within the groups, not explained by the group means.

The relationship between these terms is: `SST = SSR + SSE`

By calculating the **SST**, you quantify the total variability in your dataset, which you will later partition into the components explained by group differences (SSR) and the remaining unexplained variation (SSE).

### Step 9: Calculate the Mean Square (MS)

The **mean square (MS)** is calculated by dividing the **sum of squares (SS)** by the **degrees of freedom (DF)**. This represents the average variability for each source of variance (between groups and within groups).

#### Step-by-Step Tutorial:

* In cell **`K2`**, type `=J2/I2` to calculate the **MS Between**.  
* In cell **`K3`**, type `=J3/I3` to calculate the **MS Within**.

#### Explanation:

The **mean squares (MS)** are the average variability per **degree of freedom** for each source of variance. The **MS Between** tells us how much variability is due to the differences between years, while the **MS Within** captures the average variability within each year. These values are crucial for calculating the **F-statistic** in the next step.

### Step 10: Calculate the F-Statistic

Now that you have calculated the **F-statistic**, the next step is to determine whether the observed differences in microbial diversity between years are statistically significant. This is done by calculating the **p-value**, which tells you the probability that the observed differences in the group means are due to random variation rather than a true effect. In an ANOVA, the p-value is calculated based on the **F-statistic** and the **degrees of freedom** for both the between groups and within groups components.

#### Step-by-Step Tutorial:

* In cell **`L2`**, type `=K2/K3` to calculate the **F-statistic**.

#### Explanation:

The **F-statistic** is the ratio of the **between groups variance** to the **within groups variance**. A larger F-statistic suggests that more of the variance is due to differences between years, and the greater the chance that the differences between the means are statistically significant. We will use the F-statistic in the next step to determine statistical significance.

### Step 11: Calculate the P-Value

Now that the F-statistic has been calculated, we can determine whether the differences in microbial diversity between the years are statistically significant by calculating the **P-value**. The P-value will tell us the probability that the observed differences are due to chance. A smaller P-value (typically less than 0.05) indicates that the differences between the groups are statistically significant.

#### Step-by-Step Tutorial:

* In **cell `M2`**, use the formula `=F.DIST.RT(L2, I2, I3)` to calculate the P-value.

### **Explanation:**

The **F.DIST.RT** function calculates the right-tailed probability of the F-distribution. This function takes the following inputs:

* The **F-statistic** (calculated in cell **L2**),  
* **Degrees of freedom** between the groups (**I2**),  
* **Degrees of freedom** within the groups (**I3**).

The result of this function gives us the **P-value**, which shows whether the differences in microbial diversity across the years (1994, 2004, 2009, 2014, and 2024\) are statistically significant. If the P-value is less than 0.05, you can conclude that the differences between the groups are significant, meaning that the year-to-year changes in microbial diversity are not likely due to random chance.

### Step 12: Decision Using an IF Statement

In hypothesis testing, the decision to **reject** or **fail to reject** the **null hypothesis** is based on the **p-value** and the significance level (**α**) set before the test. In most cases, **α** is 0.05. If the **p-value** is less than or equal to 0.05, the result is considered **statistically significant**, meaning that the variation in microbial diversity between the years is unlikely due to chance alone. To simplify this decision-making process in **Google Sheets**, we will use the **IF** statement to evaluate whether the **p-value** is less than or equal to the significance level (0.05).

#### Step-by-Step Tutorial:

1. In cell **H13**, type **Significance Level (α)**.  
2. In cell **I13**, enter **0.05**.  
3. In cell **H14**, type **Decision**.  
4. In cell **I14**, use the formula `=IF(M2 <= I13, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")` to decide whether to reject the null hypothesis based on the **ANOVA** p-value.  
5. 

#### Explanation

The **IF** statement evaluates whether the **p-value** (in **M3**) is less than or equal to **0.05** (the significance level). If the **p-value** is smaller than or equal to 0.05, you will **reject the null hypothesis**, indicating that the variation in microbial diversity across the years is statistically significant. If the **p-value** is greater than 0.05, you will **fail to reject the null hypothesis**, meaning the observed differences in diversity across the years could have occurred by chance.

This process simplifies the interpretation of your **ANOVA** results, ensuring that you can quickly assess whether there is a statistically significant difference in microbial diversity over the years.

### Step 13: Interpret the Results

Now that you have calculated the **ANOVA** results, the next step is to **interpret** the findings. This involves assessing whether microbial diversity in Busse Woods has changed significantly over the decades (1994 to 2024). By comparing the **p-value** to **0.05**, you can determine if the differences in microbial diversity over time are due to environmental pressures like **urbanization** or **climate change**, or if they occurred by random chance.

#### Step-by-Step Tutorial:

* In **cell H16**, type **Interpretation.**  
* **In cell I16**, write a brief interpretation of your findings based on the **ANOVA** results. Example:  
  * "With a **p-value** of \[calculated value\], we \[reject/fail to reject\] the null hypothesis, indicating that microbial diversity \[has/has not\] changed significantly over time."

#### Explanation:

The interpretation hinges on comparing the **p-value** to the **significance level** (α \= 0.05). If the **p-value** is less than or equal to 0.05, the **null hypothesis** is **rejected**, which suggests that there are **statistically significant differences** in microbial diversity between the different years. This would imply that environmental changes over time have had a measurable impact on biodiversity.

If the **p-value** is greater than 0.05, you would **fail to reject the null hypothesis**, suggesting that the microbial diversity has not changed significantly over time. This provides valuable insight into whether **environmental pressures** are influencing both the **mean** and **variability** of microbial communities across time.

### Practice Task:

* Modify some of the Shannon Index values for the **1994**, **2004**, **2009**, **2014**, and **2024** data columns. Observe how the **sample means**, **F-statistic**, and **p-value** change.  
* Add more sample numbers (increase the sample size) and note the impact on the **ANOVA** results.  
* Discuss how sample size influences the **ANOVA** test and compare this to earlier F-test results.

### Key Takeaways:

1. **ANOVA** allows for the comparison of **multiple groups** at once, making it useful for assessing whether microbial diversity has changed over multiple decades.  
2. The **p-value** helps determine whether the differences in **microbial diversity** across years are **statistically significant**.  
3. A larger sample size provides more reliable results in both **ANOVA** and other statistical tests, reducing uncertainty.  
4. **ANOVA** is a powerful tool for identifying **trends over time** in biodiversity, revealing the impact of **environmental factors** on ecosystems.

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>