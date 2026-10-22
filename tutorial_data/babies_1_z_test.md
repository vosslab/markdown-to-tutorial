# Joe's hospital: national z-test

**"Joe's Hospital of Fried Foods" vs. National Average**

**Z-Test Tutorial for BIOL 318/418**

![][image1]

A **Z-test** is a statistical test used when you want to know if the average of your sample is
meaningfully different from a known population mean. It works by comparing the sample mean to the
population mean, while taking into account the population's standard deviation and the size of the
sample. The result is a Z test statistic, which tells you how many standard errors away your sample
mean is from the population mean. If this distance is big enough (based on probability cutoffs
called p-values), you can reject the idea that your sample is "just like" the population. A z-test
requires a genuinely known population standard deviation and a normally distributed sample mean.
With a small independent sample, this needs an approximately normal birth-weight population; a large
sample can justify an approximation. There is no automatic cutoff at 30.

## Workbook

### Sheet: Datas for Part 1 and 2

| Infant<br>Number | Birth Weight<br>(pounds) |
| --- | --- |
| 1 | 9.56 |
| 2 | 7.88 |
| 3 | 7.22 |
| 4 | 8.02 |
| 5 | 7.43 |
| 6 | 9.91 |
| 7 | 6.84 |
| 8 | 9.95 |
| 9 | 9.53 |
| 10 | 8.25 |
| 11 | 6.14 |
| 12 | 6.43 |
| 13 | 9.27 |
| 14 | 6.46 |
| 15 | 5.83 |
| 16 | 5.62 |
| 17 | 7.01 |
| 18 | 6.29 |
| 19 | 9.36 |
| 20 | 7.35 |
| 21 | 9.54 |
| 22 | 6.61 |
| 23 | 9.72 |
| 24 | 7.17 |

### Sheet: Part 1 National Z-Test

| Infant<br>Number | Birth Weight<br>(pounds) |
| --- | --- |
| 1 | 9.56 |
| 2 | 7.88 |
| 3 | 7.22 |
| 4 | 8.02 |
| 5 | 7.43 |
| 6 | 9.91 |
| 7 | 6.84 |
| 8 | 9.95 |
| 9 | 9.53 |
| 10 | 8.25 |
| 11 | 6.14 |
| 12 | 6.43 |
| 13 | 9.27 |
| 14 | 6.46 |
| 15 | 5.83 |
| 16 | 5.62 |
| 17 | 7.01 |
| 18 | 6.29 |
| 19 | 9.36 |
| 20 | 7.35 |
| 21 | 9.54 |
| 22 | 6.61 |
| 23 | 9.72 |
| 24 | 7.17 |

#### At: D1

| Statistical Names | Statistical Values |
| --- | --- |

## Tutorial

### Part 1: National z-test

- **Worksheet:** Part 1 National Z-Test

"*Joe's Hospital of Fried Foods*" claims that their babies are larger than the national average. For
this fictional teaching scenario, assume a national average newborn weight of 7.5 lbs and a known
population standard deviation of 1.5 lbs. In this tutorial, you'll use Google Sheets to conduct a
z-test using the sample data provided.

For the right-tailed claim, H0: the hospital population mean is at most 7.5 lbs; H1: it is greater
than 7.5 lbs. The test is calculated at the null boundary of 7.5 lbs.

For the two-tailed comparison, H0: the hospital population mean equals 7.5 lbs; H1: it differs from
7.5 lbs. Choose the alternative before examining results. A hospital comparison does not establish
that fried foods cause a change in birth weight.

#### Step 1: Set Up Your Google Sheet

- **Open:** Upload the generated student XLSX to Google Drive and open it in Google Sheets.
- **Choose:** File > Make a copy
- **Rename:** Add your name and, if useful, the date to the spreadsheet name.
- **Locate:** The workbook contains `Datas for Part 1 and 2` and `Part 1 National Z-Test`.
  The original combined instructor template also had a Part 2 tab; that tutorial now has its own
  workbook.
- **Copy exercise:** The working sheet already contains the same 24 observations. To practice the
  original copy operation or reset your practice edits, copy the data table from the data sheet
  and paste it at the same location on the working sheet. This overwrites that data region only.
- **Historical template:** [Original instructor Google
  Sheet](https://docs.google.com/spreadsheets/d/1A3hMTmSyL8Z-8v2K7Zit27SYXdgzQ7fHGqxqR7kCAPU/edit).
  This link has no verified tab mapping; use the generated workbook for this tutorial.

There are 24 supplied weights in rows 2-25. The formulas deliberately include
blank rows through row 40 so you can extend the data in the practice task.

#### Step 2: Set Up the Known Population Values

**Population parameter**: A population parameter describes the entire group of interest, meaning
every individual in the group you want to study, such as all babies born in the United States.

- **Instruction:** Working in the tab **"Part 1 National Z-Test"**
- **Columns D and E:** Set aside this column for statistical calculations.
- **Inspect:** The workbook supplies "Statistical Names" in `D1` and "Statistical Values" in `E1`.
- **Label D2:** Population Mean
- **Enter E2:** `7.5`
   - **Instruction:** ^ this is our representative mean baby weight of the population
- **Label D3:** Population St.Dev
- **Enter E3:** `1.5`
   - **Instruction:** ^ this is our representative baby weight standard deviation of the population
After these entries, the calculation area should contain:

| Cell | Contents |
| --- | --- |
| D1 | Statistical Names (supplied) |
| E1 | Statistical Values (supplied) |
| D2 | Population Mean (your label) |
| E2 | 7.5 (your entry) |
| D3 | Population St.Dev (your label) |
| E3 | 1.5 (your entry) |

#### Step 3: Calculate the Sample Values

**Sample statistic**: A sample statistic describes a smaller subset drawn from that population, such
as a group of babies born at one hospital which is a subset of all babies born in the United States.

- **Label D5:** Sample Size
- **Enter E5:** `=COUNT(B2:B40)`
  - **Method:** Use the `COUNT` function to dynamically count the number of weights:
   - **Instruction:** This formula counts the weights from cells B2 to B40, allowing for flexibility
     if you add more data. It will automatically ignore empty cells.
- **Label D6:** Sample Mean
- **Enter E6:** `=AVERAGE(B2:B40)`
  - **Method:** Use the `AVERAGE` function to calculate the sample mean:
   - **Instruction:** This formula calculates the mean of weights from cells B2 to B40, allowing for
     flexibility if you add more data. It will automatically ignore empty cells.
- **Label D7:** Sample St.Dev
- **Enter E7:** `=STDEV.S(B2:B40)`
  - **Method:** Use the `STDEV.S` function to calculate the sample standard deviation:
   - **Instruction:** This formula calculates the standard deviation of weights from cells B2 to
     B40, allowing for flexibility if you add more data. It will automatically ignore empty cells.
   - **Instruction:** We will not be using the sample standard deviation for this statistical test

#### Step 4: Calculate the Z Test Statistic

- **Label D9:** Z Test Statistic
- **Enter E9:** `=(E6 - E2) / (E3 / SQRT(E5))`
   - **Instruction:** Formula: (sample mean - population mean) / \[ population standard deviation /
     sqrt(sample size) \]
   - **Instruction:** This formula uses the sample mean (E6), population mean (E2), population
     standard deviation (E3), and sample size (E5). The use of `SQRT(E5)` adjusts for varying sample
     sizes.

   **Note:** In a Z-test, the calculated value is called the Z test statistic, not a simple z-score.
   A z-score measures how far one data point is from the mean, while the Z test statistic measures
   how far the sample mean is from the population mean. Both use the same standardized scale, which
   is why they look alike but apply to different situations.

#### Step 5: Determine the Type of Test (One-Tailed or Two-Tailed) and Calculate the P-Value

When running a hypothesis test, you need to decide whether you care about differences in one
direction or both. A one-tailed test looks only for an effect in a single direction (for example,
asking if a group is larger than another), while a two-tailed test checks for any difference in
either direction (larger or smaller). This choice depends entirely on how you frame your research
question.

##### Substep 5.1: Understand the Research Question

- **Plan:** Joe's claim is that his hospital's mean is greater than the national average, so the
  assigned test is right-tailed. Record that alternative before calculating or comparing either
  p-value. The two-tailed result is included for comparison, not as a second chance to find a
  significant result.
- **One-Tailed Test:** Use this if testing whether babies at the hospital are **larger** than the
  national average.
- **Two-Tailed Test:** Use this if testing for **any difference** (either larger or smaller) in baby
  weights.

##### Substep 5.2: Calculate the P-Value Based on the Chosen Test

- **Two-Tailed Test:**
   - **Label D11:** P-Value (Two-Tailed)
   - **Enter E11:** `=2 * (1 - NORM.DIST(ABS(E9), 0, 1, TRUE))`
- **One-Tailed Test:**
   - **Label D12:** P-Value (One-Tailed, Right Tail)
   - **Enter E12:** `=1 - NORM.DIST(E9, 0, 1, TRUE)`

`NORM.DIST(z, 0, 1, TRUE)` gives the standard normal cumulative probability: **0** sets the mean,
**1** sets the standard deviation, and **TRUE** selects cumulative probability. For your Z statistic,
it tells you
the probability of seeing a value less than or equal to that number under the bell-shaped curve of
the standard normal distribution (mean \= 0, standard deviation \= 1). This is what allows us to
turn a test statistic into a p-value.

Both p-values and decisions are calculated so you can compare the two approaches. Use only the
right-tailed test chosen from Joe's claim when reporting the result; do not choose between the tests
based on which p-value is smaller.

![][image9]

#### Step 6: Make a Decision Using an IF Statement

- **Label D14:** Significance Level (&alpha;)
- **Enter E14:** `0.05`
- **Label D16:** Two-Tail Decision
- **Enter E16:** `=IF(E11 <= E14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  - **Method:** Use the **IF** statement to automatically determine whether to reject the null
    hypothesis:
- **Label D17:** One-Tail Decision
- **Enter E17:** `=IF(E12 <= E14, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  - **Method:** Use the **IF** statement to automatically determine whether to reject the null
    hypothesis:
- **Instruction:** Explanation:
- **Instruction:** The **IF** statement checks if the p-value (from either E11 or E12) is **less
  than or equal to** the significance level (in **E14**).
- **Instruction:** If the condition is true (p-value &le; 0.05), it returns "Reject the Null
  Hypothesis."
- **Instruction:** If the condition is false (p-value \> 0.05), it returns "Fail to Reject the Null
  Hypothesis."

#### Step 7: Interpret the Results

- **Label D19:** Interpretation
- **Instruction:** In cell `E19`, write your own brief interpretation of your findings based on your
  chosen test:
   - **Two-Tailed Test Example:** "With a p-value of \[calculated value\], we \[reject/fail to
     reject\] the null hypothesis, indicating that the average weight at 'Joe's Hospital of Fried
     Foods' \[is/is not\] significantly **different** from the national average"
   - **One-Tailed Test Example:** "With a p-value of \[calculated value\], we \[reject/fail to
     reject\] the null hypothesis, indicating that the average weight at 'Joe's Hospital of Fried
     Foods' \[is/is not\] significantly **greater than** the national average"

#### Practice Task:

- **Instruction:** Add more baby weights to Column B (up to row B40) to see how the sample size
  impacts the **Z test statistic** and **p-value**.
- **Instruction:** Modify some of the existing baby weight values to higher or lower numbers and
  observe how the **sample mean**, **Z test statistic**, and **p-value** in Column E adjust
  automatically.
- **Instruction:** Discuss how changing the dataset size or individual baby weights affects the
  hypothesis test results and your interpretation.

#### Key Takeaways:

- **Flexibility:** By using a flexible range (B2:B40), this setup allows you to vary the number of
  babies and observe how it influences statistical outcomes.
- **Z Test Statistics:** Standardizing using Z test statistics helps compare the sample mean to a
  known population mean, even when sample sizes change.
- **Dynamic Calculations:** Google Sheets automatically recalculates the Z test statistic and
  p-value as you add or modify data, showing real-time effects on hypothesis testing.

#### Looking ahead: Joe faces a challenge

Joe was ecstatic after conducting his Z-test, certain that his hospital's babies were the heaviest
in town. He was ready to claim the Baby Butter Ball Award and throw a butter-and-bacon-themed
celebration.

But just as Joe began planning his victory speech, the award committee sent him a stern letter:

"Joe, we've reviewed your analysis. While you compared your babies' weights to the national average
using a Z-test, you assumed the population standard deviation was known. That's risky, given the
variation in hospital practices and diets. There is also a small-sample assumption to check. You
used fewer than 30 babies, so we must check approximate normality rather than rely on a large-sample
argument. A small sample alone does not invalidate a z-test; here the unknown population standard
deviation calls for a t-test that adjusts for estimation uncertainty. Until you redo the analysis
properly, you're disqualified from the Baby Butter Ball Award."

![][image10]

Joe's heart sank. As the news spread, protesters gathered outside the hospital. Some were angry with
Joe, holding signs that read "You Should Know Better" and "Joe is a Fraud." Others blamed the Butter
Ball Committee, with signs like "We Were Cheated" and "The T-Test Was Created by Only a Student\!"

Joe stood in disbelief, watching the chaos unfold. His hopes for the Baby Butter Ball Award were
slipping away.

##### Statistical references

The [NIST guide to tests of a process
mean](https://www.itl.nist.gov/div898/handbook/prc/section2/prc.htm)
distinguishes the known-standard-deviation z-test from the estimated-standard-deviation t-test.

[image1]: assets/babies_1_image1.png

[image9]: assets/babies_1_image9.png

[image10]: assets/babies_1_image10.png
