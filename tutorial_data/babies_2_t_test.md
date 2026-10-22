# Joe's hospital: one-sample t-test

**"Joe's Hospital of Fried Foods" vs. National Average**

**T-Test Tutorial for BIOL 318/418**

![][image1]

A **T-test** is a statistical test used when you want to know if the average of your sample is
meaningfully different from a known value, but you cannot assume the population standard deviation
is known. Instead, it uses the sample's own standard deviation and adjusts for smaller sample sizes
through the t-distribution. The result is a t test statistic, which tells you how far the sample
mean is from the hypothesized population mean in units of estimated standard error. Because it
accounts for added uncertainty, the t-test is appropriate when population variability is estimated
from the sample. Small samples also require attention to independence, approximate normality, and
outliers.

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

### Sheet: Part 2 National T-Test

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

#### At: E3

| not used |
| --- |

## Tutorial

### Part 2: National one-sample t-test

- **Worksheet:** Part 2 National T-Test

There are 24 supplied weights in rows 2-25. The formulas deliberately allow additions through
row 101, ignoring blank cells. Use independent observations from an approximately normal population
for this small-sample model; neither a t-test nor a z-test fixes biased sampling.

#### The New Challenge: Prove It with a One-Sample T-Test

The awards committee has pointed out that Joe's approach wasn't entirely sound. They raised two key
issues:

- **Instruction:** Assumed Population Standard Deviation - Joe can no longer assume the national
  standard deviation applies, given the variation in practices across hospitals.
- **Instruction:** Small Sample Size - Joe has only 24 observations. Both tests need a suitable
  model for the sample mean; for a small sample, check approximate normality and influential
  outliers. Sample size alone does not invalidate a z-test.

#### The New Scenario: Enter the T-Test

Joe now faces a more realistic challenge. Without knowing the population standard deviation, Joe
must rely on his sample's standard deviation to redo the analysis. This is where the T-test comes
into play. The T-test is designed to account for the smaller sample size and the added uncertainty
from estimating the population standard deviation.

Feeling the pressure but determined to stay in the running for the Baby Butter Ball Award, Joe opens
his spreadsheet once again. This time, he must:

- **Instruction:** Calculate the sample mean and the sample standard deviation from his hospital's
  baby weight data.
- **Instruction:** Perform a one-sample T-test to determine if his babies' weights are significantly
  larger than the national average of 7.5 lbs.

For the one-tailed right-tail claim, H0: the hospital mean is at most 7.5 lbs and H1: it is
greater than 7.5 lbs. For the two-tailed comparison, H0: it equals 7.5 lbs and H1: it differs.
Choose the alternative before examining results. The national value is a fictional teaching
benchmark, not a verified current public-health estimate.

Joe's stated claim makes the right-tailed test the assigned test. Record that choice before
calculating either p-value. The two-tailed result is included for comparison, not as a second chance
to find a significant result.

#### Step 1: Why Use a T-Test Now?

- **Unknown Population Standard Deviation:** In real-world situations, we often **do not have** the
  population standard deviation. Therefore, we estimate it using the **sample standard deviation**.
- **Small Sample Size:** With an unknown population standard deviation, the t-test accounts for
  uncertainty in the estimated standard error. For a small sample, check approximate normality and
  outliers; t is not a cure for non-normal or dependent data.

#### Step 2: Set Up Your Google Sheet for the T-Test

- **Open:** Open the generated student XLSX in Google Sheets. It is a standalone workbook for this
  tutorial and already contains the data for Part 2.
- **Choose:** File > Make a copy
- **Rename:** Add your name and, if useful, the date.
- **Copy exercise:** Copy the table from `Datas for Part 1 and 2` to the same location on
  `Part 2 National T-Test` to practice the original workflow or reset practice edits.
  The working sheet already contains all 24 original observations.
- **Check:** Columns D and E are set aside for statistical calculations. `D1` contains
  "Statistical Names" and `E1` contains "Statistical Values".

- **Label D2:** Population Mean
- **Enter E2:** `7.5`
   - **Instruction:** ^ this is our representative mean baby weight of the population
- **Label D3:** Population St.Dev
- **Inspect:** `E3` is already seeded as "not used" because this test estimates variability from
  the sample instead of using a known population standard deviation.

After these entries, the calculation area should contain:

| Cell | Contents |
| --- | --- |
| D1 | Statistical Names (supplied) |
| E1 | Statistical Values (supplied) |
| D2 | Population Mean (your label) |
| E2 | 7.5 (your entry) |
| D3 | Population St.Dev (your label) |
| E3 | not used (supplied) |

#### Step 3: Calculate the Sample Size

- **Label D5:** Sample Size
- **Enter E5:** `=COUNT(B2:B101)`
  - **Method:** Use the `COUNT` function to dynamically count the number of weights:

#### Step 4: Calculate the Sample Mean

- **Label D6:** Sample Mean
- **Enter E6:** `=AVERAGE(B2:B101)`
  - **Method:** Use the `AVERAGE` function to calculate the sample mean:

#### Step 5: Calculate the Sample Standard Deviation

- **Label D7:** Sample St.Dev
- **Enter E7:** `=STDEV.S(B2:B101)`
  - **Method:** Use the `STDEV.S` function to calculate the sample standard deviation:

#### Step 6: Calculate the T-Statistic

- **Label D9:** T-Statistic
- **Enter E9:** `=(E6 - E2) / (E7 / SQRT(E5))`
  - **Method:** Use this formula to calculate the t-statistic:
   - **Instruction:** This formula uses the sample mean (E6), the assumed population mean (E2 at 7.5
     lbs), the sample standard deviation (E7), and the sample size (E5).

#### Step 7: Calculate the Degrees of Freedom

- **Label D10:** Degrees of Freedom
- **Enter E10:** `=E5 - 1`
   - **Instruction:** Here, `E5` is the sample size, so subtracting 1 gives us the degrees of
     freedom.

##### Explanation: Why Do We Use Degrees of Freedom?

- **What Are Degrees of Freedom?** In statistics, **degrees of freedom** represent the number of
  independent values in a dataset that can vary when estimating a statistical parameter. In the
  context of a t-test, degrees of freedom are used to account for the fact that we are estimating
  the population standard deviation using the **sample standard deviation**.
- **Why Subtract 1?** When calculating the **sample standard deviation**, one of the values (usually
  the mean) is fixed based on the rest of the data. This is why we lose one degree of freedom, which
  adjusts for the uncertainty introduced when estimating the standard deviation from a limited
  sample.
- **Impact on the T-Distribution:** The t-distribution changes shape depending on the degrees of
  freedom. For smaller sample sizes (fewer degrees of freedom), the t-distribution has **heavier
  tails**, reflecting greater variability and uncertainty. As the sample size grows (increasing
  degrees of freedom), the t-distribution becomes more similar to the **normal (z) distribution**.
- **Why It Matters:** In the t-test, degrees of freedom help adjust the **critical values** and
  **p-values** to reflect the sample size's impact. Smaller degrees of freedom make the test more
  conservative, meaning we need stronger evidence to reject the null hypothesis.

#### Step 8: Calculate the P-Value for the T-Test

##### Substep 8.1: Understand the Research Question

- **One-Tailed Test:** Use this if you want to test whether the babies at "Joe's Hospital of Fried
  Foods" are **larger** than the national average. This type of test only looks for a difference in
  **one direction** (greater than).
- **Two-Tailed Test:** Use this if you want to check for **any significant difference** (either
  larger or smaller) in baby weights compared to the national average. This type of test considers
  differences in **both directions**.

##### Substep 8.2: Calculate the P-Value Based on the Chosen Test

- **Determine the Type of Test:** Decide if you are conducting a **two-tailed test** or a
  **one-tailed test** based on the research question:
   - **Two-Tailed Test:** Tests for any difference (either larger or smaller) in baby weights.
   - **One-Tailed Test:** Tests if the baby weights are **specifically larger** than the national
     average.
- **Calculate the P-Value:**
   - **Two-Tailed Test:**
     - **Label D12:** P-Value (Two-Tailed)
     - **Enter E12:** `=T.DIST.2T(ABS(E9), E10)`
       - **Method:** Use the `T.DIST.2T` function:
        - **Instruction:** This formula calculates the p-value for a **two-tailed test** using the
          **absolute value** of the t-statistic (in cell E9) and the **degrees of freedom** (in cell
          E10).
        - **Explanation:** The `T.DIST.2T` function checks for differences in both directions
          (greater or smaller) between the sample mean and the population mean.
   - **One-Tailed Test:**
     - **Label D13:** P-Value (One-Tailed, Right Tail)
     - **Enter E13:** `=1 - T.DIST(E9, E10, TRUE)`
       - **Method:** Use one minus the cumulative `T.DIST` function:
        - **Instruction:** This formula calculates the p-value for a **one-tailed test** using the
          t-statistic (in `E9`) and the **degrees of freedom** (in `E10`).
        - **Explanation:** One minus the cumulative `T.DIST` function calculates the probability of
          observing a value as extreme or more extreme in **one direction** (greater than the
          population mean).

##### Substep 8.3: Important Notes:

- **Instruction:** For a positive t-statistic and a right-tailed alternative, the **two-tailed
  p-value** is double the right-tailed p-value. With a negative statistic, the right-tailed p-value
  exceeds 0.5; do not blindly halve a two-tailed value.
- **Instruction:** Make sure to use the correct function based on whether you are conducting a
  **one-tailed** or **two-tailed** test. This choice directly impacts the interpretation of your
  hypothesis test.

Both p-values and decisions are calculated so you can compare the two approaches. Report only the
result for the test you chose from the research question before calculating either p-value; do not
choose between the tests based on which p-value is smaller.

#### Step 9: Decision Using an IF Statement

- **Label D15:** Significance Level (&alpha;)
- **Enter E15:** `0.05`
- **Label D17:** Two-Tail Decision
- **Enter E17:** `=IF(E12 <= E15, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  - **Method:** Use the **IF** statement to automatically determine whether to reject the null
    hypothesis:
- **Label D18:** One-Tail Decision
- **Enter E18:** `=IF(E13 <= E15, "Reject the Null Hypothesis", "Fail to Reject the Null Hypothesis")`
  - **Method:** Use the **IF** statement to automatically determine whether to reject the null
    hypothesis:

#### Step 10: Interpret the Results

- **Label D20:** Interpretation
- **Instruction:** In cell `E20`, write a brief interpretation of your findings based on the p-value
  and test type.

#### Practice Task:

- **Instruction:** Change some baby weights in Column B and observe how the sample standard
  deviation, t-statistic, and p-value adjust automatically.
- **Instruction:** Add more baby weights (e.g., increasing the sample size beyond 30\) and note how
  the p-value changes. Discuss when the t-test results start to resemble the z-test.
- **Instruction:** Discuss how the flexibility in sample size affects the results of the t-test and
  compare this to their earlier z-test results.

#### Key Takeaways:

- **Instruction:** Use the **t-test** when the **population standard deviation is unknown** and is
  estimated from the sample. A small sample alone does not decide between z and t; independence and
  approximate normality remain important.
- **Instruction:** The **t-distribution** accounts for the additional uncertainty introduced by
  using the sample standard deviation.
- **Instruction:** When the sample size is large, the t-test and z-test produce similar results,
  showing that the t-distribution approximates the normal distribution as the sample size increases.

#### Joe's hoped-for redemption

After carefully following the steps, Joe anxiously awaits the results. He hopes the t-test will show
that his babies are significantly larger than the national average and that the committee will
reinstate his eligibility for the Baby Butter Ball Award. With the supplied data and a significance
level of 0.05, however, the right-tailed p-value is about 0.154. He must fail to reject the null
hypothesis. His preferred ending is not supported by these observations.

As Joe accepts the news, he feels humility. "I've learned a valuable lesson," he admits, holding
back his excitement. "From now on, I'll make sure I'm using the right statistical tools."

But Joe can't resist a small smile. He still hopes to win the award, but recognizes that these data
neither prove heavier babies nor show that fried food makes babies thrive. An award story cannot
replace the statistical evidence.

##### Statistical references

The [NIST guide to tests of a process
mean](https://www.itl.nist.gov/div898/handbook/prc/section2/prc.htm)
distinguishes the known-standard-deviation z-test from the estimated-standard-deviation t-test.

[image1]: assets/babies_2_image1.png
