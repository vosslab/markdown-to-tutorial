# Joe's hospital versus Green Veggies

**"Joe's Hospital of Fried Foods" vs.** **"Green Veggies Health Center"**

**Two Sample T-Test Tutorial for BIOL 318/418**

## Workbook

### Sheet: Fried Foods vs Green Veggies

| Infant<br>Number | Joe's Fried Foods<br>Birth Weight (pounds) | Green Veggies<br>Birth Weight (pounds) |
| --- | --- | --- |
| 1 | 9.56 | 9.16 |
| 2 | 8.88 | 7.86 |
| 3 | 7.22 | 7.38 |
| 4 | 8.02 | 6.41 |
| 5 | 9.43 | 8.64 |
| 6 | 9.91 | 8.04 |
| 7 | 6.84 | 7.15 |
| 8 | 9.95 | 7.75 |
| 9 | 9.53 | 5.96 |
| 10 | 8.25 | 7.61 |
| 11 | 6.14 | 7.18 |
| 12 | 6.43 | 8.01 |
| 13 | 9.27 | 7.77 |
| 14 | 6.46 | 7.43 |
| 15 | 5.83 | 7.45 |
| 16 | 5.62 | 7.77 |
| 17 | 7.01 | 9.08 |
| 18 | 9.29 | 6.87 |
| 19 | 9.36 | 7.06 |
| 20 | 7.35 | 8.01 |
| 21 | 9.54 | 8.68 |
| 22 | 6.61 | 7.25 |
| 23 | 9.72 | 7.36 |
| 24 | 7.17 | 7.88 |

## Tutorial

### Part 3: Compare two hospitals

- **Worksheet:** Fried Foods vs Green Veggies

#### Previous Scenario: One-Sample T-Test with National Average

In the previous situation, you used a **one-sample t-test** to compare the average baby weights at
**"Joe's Hospital of Fried Foods"** to the national average of **7.5 lbs**. Since the **population
standard deviation** was unknown, you used the **sample standard deviation** from Joe's Hospital to
perform the test.

#### New Scenario: Comparing Two Hospitals (Two-Sample T-Test)

Now, things are getting competitive. Joe, hoping to reinstate his eligibility for the **Baby Butter
Ball Award**, faces a direct challenge from **Alex**, CEO of **"Green Veggies Health Center."**
Alex's superfood-rich prenatal care has her convinced that her hospital's babies are just as hefty,
if not heavier, than Joe's fried-food babies.

#### Step 0: Why Use a T-Test Now?

- **Unknown Population Standard Deviation**: Like before, we do not know the population standard
  deviation for either hospital, so we will use each hospital's **sample standard deviation**.
- **Comparison of Two Independent Groups**: A **two-sample t-test** is the correct tool to compare
  the average baby weights at **Joe's Hospital** and **Green Veggies Health Center**, which are
  independent groups.
- **Small Sample Size:** There are 24 observations per hospital. A **t-test** accounts for estimated
  variability; check independence, approximate normality and influential outliers, especially for
  small samples. Here we use Welch's version without assuming equal population variances. Matching
  infant numbers are identifiers, not evidence of paired observations.

#### Step 1: Set Up Your Google Sheet

- **Open:** Upload the generated student XLSX to Google Drive and open it in Google Sheets.
- **Choose:** File > Make a copy
- **Rename:** Add your name and, if useful, the date.
- **Historical template:** [Original instructor Google
  Sheet](https://docs.google.com/spreadsheets/d/13gzEAw_zGJyWcNErpK2m_N8bBzrRKbyZpBHAbtytVsI/edit).
  This link has no verified tab mapping. The generated workbook contains the complete original
  data in `A1:C25`, with 24 babies in each group. Ranges through row 101 intentionally leave
  room for practice additions; blank cells do not increase the sample sizes.

#### Before calculating summaries: choose the test

Before calculating or comparing the group means, standard deviations, or sample sizes, use the
research question to choose and record your alternative in your notes. Use a two-tailed test when
the question asks whether the means differ in either direction. Use a right-tailed test only for a
clear, justified prediction that Joe's mean is greater. For any difference, record H0: the hospital
population means are equal; H1: they differ. For Joe-greater, record H0: Joe's mean is less than or
equal to Green Veggies' mean; H1: Joe's mean is greater. Keep this choice for the final
interpretation, regardless of which result the summaries or p-values suggest.

#### Step 2: Set Up the Statistical Calculations

- **Label F1:** Statistical Names
- **Label G1:** Fried Food Values
- **Label H1:** Green Veggie Values

#### Step 3: Calculate the Sample Means

- **Label F2:** Sample Mean
- **Enter G2:** `=AVERAGE(B2:B101)`
- **Enter H2:** `=AVERAGE(C2:C101)`

#### Step 4: Calculate the Sample Standard Deviations

- **Label F3:** Sample Standard Deviation
- **Enter G3:** `=STDEV.S(B2:B101)`
- **Enter H3:** `=STDEV.S(C2:C101)`

#### Step 5: Calculate the Sample Sizes

- **Label F4:** Sample Size
- **Enter G4:** `=COUNT(B2:B101)`
- **Enter H4:** `=COUNT(C2:C101)`

#### Step 6: Perform the Two-Sample T-Test in Google Sheets

##### Substep: Calculate the p-value

- **Syntax:** The function has the form `=T.TEST(range1, range2, tails, type)`.
  `B2:B101` is Joe's birth-weight range; `C2:C101` is Green Veggies' range.
  Tails is 2 for two-tailed and 1 for one-tailed. Type 3 specifies the unequal-variance
  two-sample test (Welch); type 2 would assume equal population variances.
- **Alternative: Two-tailed difference**
  - **Label F5:** P-Value (Two-Tailed Difference)
  - **Enter G5:** `=T.TEST(B2:B101, C2:C101, 2, 3)`
  - **Explanation:** The first 2 requests both tails; the final 3 selects Welch's test.
    The alternative is that the hospital population means differ in either direction.
- **Alternative: One-tailed, Joe's mean greater**
  - **Label F5:** P-Value (Right-Tailed: Joe's Mean Greater)
  - **Enter G5:** `=IF(G2>=H2,T.TEST(B2:B101,C2:C101,1,3),1-T.TEST(B2:B101,C2:C101,1,3))`
  - **Explanation:** Google Sheets' one-tailed `T.TEST` uses the magnitude of the statistic.
    It does not select a directional alternative from the order of the ranges. The `IF` checks
    the mean difference so this formula returns the right-tailed p-value for Joe greater than
    Green Veggies, including a p-value above 0.5 when the observed difference points the other way.

Use the alternative you recorded before calculating the group summaries. The supplied group means
and standard deviations are calculated from their own columns, not copied from the
national-comparison tutorial.

##### Important notes

- **Two-Tailed Test:** Is more conservative since it tests for any difference in either direction.
  It splits the significance level (e.g., 0.05) between both tails of the distribution, requiring
  stronger evidence to reject the null hypothesis.
- **One-Tailed Test:** Is more powerful if you have a specific hypothesis about the direction of the
  difference (e.g., Joe's babies are heavier). However, it does **not** account for the possibility
  of a difference in the opposite direction, so it should only be used if you have a clear,
  justified expectation.

##### Substep: Plan the decision

- **Preview:** Compare the p-value in `G5` from your chosen alternative with a significance
  level of 0.05. The next step enters the significance level and the decision formula once.

#### Step 7: Make a Decision Using the P-Value

- **Label F6:** Significance Level (&alpha;)
- **Enter G6:** `0.05`
- **Label F7:** Decision
- **Enter G7:** `=IF(G5 <= G6, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`

#### Step 8: Interpret the Results

- **Label F8:** Interpretation
- **Instruction:** In cell `G8`, write a brief interpretation of the test results based on the
  p-value and your decision.

##### Example interpretation:

- **Instruction:** "With a p-value of \[calculated value\], we \[reject/fail to reject\] the null
  hypothesis, for the two-tailed test, indicating that the average weight of newborns at 'Joe's
  Hospital of Fried Foods' \[is/is not\] significantly different from that of 'Green Vegetables
  Health Center.'"

For the right-tailed alternative, state whether the data provide sufficient evidence that Joe's
population mean is greater. Failing to reject does not establish equal means. These observational
data do not establish a causal effect of either hospital's diet.

##### Statistical references

The [Google Sheets T.TEST documentation](https://support.google.com/docs/answer/6055837?hl=en)
explains the tails and type arguments and the absolute-statistic behavior.
