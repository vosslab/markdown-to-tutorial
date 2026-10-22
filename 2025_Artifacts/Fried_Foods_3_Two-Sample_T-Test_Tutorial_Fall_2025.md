## **"Joe's Hospital of Fried Foods" vs.** **“Green Veggies Health Center”**

## **Two Sample T-Test Tutorial for BIOL 318/418**

## Part 3: Two-Sample T-Test Scenario

### Previous Scenario: One-Sample T-Test with National Average

In the previous situation, you used a **one-sample t-test** to compare the average baby weights at **"Joe's Hospital of Fried Foods"** to the national average of **7.5 lbs**. Since the **population standard deviation** was unknown, you used the **sample standard deviation** from Joe's Hospital to perform the test.

### New Scenario: Comparing Two Hospitals (Two-Sample T-Test)

Now, things are getting competitive. Joe, feeling confident after reinstating his eligibility for the **Baby Butter Ball Award**, faces a direct challenge from **Alex**, CEO of **“Green Veggies Health Center.”** Alex’s superfood-rich prenatal care has her convinced that her hospital’s babies are just as hefty, if not heavier, than Joe’s fried-food babies.

### Step 0: Why Use a T-Test Now?

1. **Unknown Population Standard Deviation**: Like before, we do not know the population standard deviation for either hospital, so we will use each hospital's **sample standard deviation**.  
2. **Comparison of Two Independent Groups**: A **two-sample t-test** is the correct tool to compare the average baby weights at **Joe's Hospital** and **Green Veggies Health Center**, which are independent groups.  
3. **Small Sample Size**: If each hospital has fewer than 30 babies, a **t-test** will adjust for the variability typically found in small samples.

### Step 1: Set Up Your Google Sheet

1. Open the template spreadsheet created by the instructor

[https://docs.google.com/spreadsheets/d/13gzEAw\_zGJyWcNErpK2m\_N8bBzrRKbyZpBHAbtytVsI/edit](https://docs.google.com/spreadsheets/d/13gzEAw_zGJyWcNErpK2m_N8bBzrRKbyZpBHAbtytVsI/edit) 

2. Make a personal copy of the Google Sheet by going under **File** and “**Make a Copy**”  
3. Change the name of the Spreadsheet by adding your name and perhaps add the date

### Step 2: Set Up the Statistical Calculations

1. **Column F:** Type **"Statistical Names."**  
2. **Column G:** Type **"Fried Food Values."**  
3. **Column H:** Type **"Green Veggie Values."**

### Step 3: Calculate the Sample Means

1. In cell **F2**, type **"Sample Mean."**  
2. In cell **G2**, calculate the mean for Joe's Hospital using:  
   * `=AVERAGE(B2:B101)`  
3. In cell **H2**, calculate the mean for Green Veggies using:  
   * `=AVERAGE(C2:C101)`

### Step 4: Calculate the Sample Standard Deviations

1. In cell **F3**, type **"Sample Standard Deviation."**  
2. In cell **G3**, calculate the sample standard deviation for Joe's Hospital using:  
   * `=STDEV.S(B2:B101)`  
3. In cell **H3**, calculate the sample standard deviation for Green Veggies using:  
   * `=STDEV.S(C2:C101)`

### Step 5: Calculate the Sample Sizes

1. In cell **F4**, type **"Sample Size."**  
2. In cell **G4**, calculate the sample size for Joe's Hospital using:  
   * `=COUNT(B2:B101)`  
3. In cell **H4**, calculate the sample size for Green Veggies using:  
   * `=COUNT(C2:C101)`

### Step 6: Perform the Two-Sample T-Test in Google Sheets

#### 6.1: Determine the Type of Test

When comparing two groups, like **"Joe's Hospital of Fried Foods"** and **"Green Vegetables Health Center,"** you need to decide on the direction of your hypothesis:

* **Two-Tailed Test:** This is used when you want to test if there is **any significant difference** in the average weights between the two hospitals, regardless of direction. This means you’re checking if the weights at one hospital are **either higher or lower** than the other.  
  * **Example Hypothesis:**  
    * **Null Hypothesis (H0​)**: The average weights at Joe's Hospital are equal to those at Green Veggies.  
    * **Alternative Hypothesis (H1​)**: The average weights at Joe's Hospital are **different** from those at Green Veggies (either higher or lower).  
  * Use a **two-tailed test** if you **do not have a specific expectation** about which hospital’s average weight is higher.  
* **One-Tailed Test:** This is used when you have a **specific direction** in mind. For example, if you specifically want to test if the babies at **Joe's Hospital** are **heavier** than those at **Green Veggies**, you would use a **one-tailed test**.  
  * **Example Hypothesis:**  
    * **Null Hypothesis (H0​)**: The average weights at Joe's Hospital are **less than or equal to** those at Green Veggies.  
    * **Alternative Hypothesis (H1​)**: The average weights at Joe's Hospital are **greater** than those at Green Veggies.  
  * Use a **one-tailed test** if you have a **specific hypothesis** about which hospital has heavier babies.

#### 6.2: Calculate the P-Value Based on the Chosen Test

1. **In cell F5**, type **"P-Value (Two-Sample T-Test)."**  
2. **In cell G5**, use the `T.TEST` function to perform the two-sample t-test. The syntax of the `T.TEST` function is:  
   * `=T.TEST(range1, range2, tails, type)`  
   * Here’s how you’ll set up the formula:  
     * **Range1 (Joe's Hospital):** B2:B100  
     * **Range2 (Green Veggies):** C2:C100  
     * **Tails:** This specifies if the test is **one-tailed** or **two-tailed**.  
       * Enter **1** for a **one-tailed test**.  
       * Enter **2** for a **two-tailed test**.  
     * **Type:** This specifies the type of t-test. Use **2** to indicate that you are performing a **two-sample t-test with unequal variances** (Welch's t-test).  
3. **Two-Tailed Test:** If you want to check for any significant difference, enter:  
   * `=T.TEST(B2:B101, C2:C101, 2, 2)`  
   * Explanation:  
     * **B2:B101** and **C2:C101** are the ranges for the weights of Joe's Hospital and Green Veggies, respectively.  
     * The **first "2"** indicates a **two-tailed test**.  
     * The **second "2"** indicates you are using the **two-sample t-test with unequal variances** (Welch's t-test).  
4. **One-Tailed Test:** If you want to check if babies at Joe's Hospital are **specifically heavier**, enter:  
   * `=T.TEST(B2:B101, C2:C101, 1, 2)`  
   * Explanation:  
     * The **first "1"** specifies that this is a **one-tailed test**, testing if one group (Joe's Hospital) is **greater** than the other (Green Veggies).

#### Important Notes:

* **Two-Tailed Test:** Is more conservative since it tests for any difference in either direction. It splits the significance level (e.g., 0.05) between both tails of the distribution, requiring stronger evidence to reject the null hypothesis.  
* **One-Tailed Test:** Is more powerful if you have a specific hypothesis about the direction of the difference (e.g., Joe’s babies are heavier). However, it does **not** account for the possibility of a difference in the opposite direction, so it should only be used if you have a clear, justified expectation.

#### Step 6.3: Input the Decision

1. In **cell F6**, type **"Significance Level (α)."** In **cell G6**, enter **"0.05."**  
2. In **cell F7**, type **"Decision."**  
3. In **cell G7**, use an **IF** statement to interpret the p-value:  
   * For the **two-tailed test**: `=IF(G5 <= G6, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`  
   * Adjust **G5** to the appropriate cell if you used a **one-tailed test**.

### Step 7: Make a Decision Using the P-Value

1. In cell **F6**, type **"Significance Level (α)."** In cell **G6**, enter **"0.05."**  
2. In cell **F7**, type **"Decision."**  
3. In cell **G7**, use an **IF** statement to compare the p-value to the significance level:  
   * Enter: `=IF(G5 <= G6, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

### Step 8: Interpret the Results

1. In cell **F8**, type **"Interpretation."**  
2. In cell **G8**, write a brief interpretation of the test results based on the p-value and your decision.

#### Example Interpretation:

* "With a p-value of \[calculated value\], we \[reject/fail to reject\] the null hypothesis, indicating that the average weight of newborns at 'Joe's Hospital of Fried Foods' \[is/is not\] significantly different from that of 'Green Vegetables Health Center.'"