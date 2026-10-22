# Dr. Caffeine's All-Nighter Academy: linear regression

Welcome to All-Nighter Academy! Dr. Caffeine notices that some students stay up late studying
while others prioritize sleep. Is sleep related to final exam performance, or is he just running
on too much caffeine? Grab your coffee: each student will become a dot on a scatterplot.

This is tutorial 2 of 3. Familiarity with spreadsheet entry and descriptive statistics from
**Dr. Caffeine's All-Nighter Academy: descriptive statistics** is helpful.
This workbook supplies the same complete 25 original observations, so you do not need a completed
previous workbook. Data provenance:
[original class template](https://docs.google.com/spreadsheets/d/1mhOQhC_1hqnbvYItPT3y-V-_9l9q3pN7MtZDcOevaA0/edit?gid=0#gid=0).

![Dr. Caffeine introduces the scenario](assets/caffeine_02.png)

Linear regression models a relationship between quantitative variables by fitting a straight line.
It describes the direction and strength of a linear association. We will fit, interpret, and test
that line, then ask whether it misses a curved pattern.

![Sleep and exam performance scenario](assets/caffeine_03.png)

## Workbook

### Sheet: Sleep and scores

| Hours of Sleep | Exam score (%) |
| --- | --- |
| 3 | 55 |
| 3.5 | 57 |
| 4 | 58 |
| 4 | 65 |
| 4.5 | 70 |
| 11 | 72 |
| 5 | 73 |
| 11.5 | 74 |
| 7 | 77 |
| 6 | 79 |
| 5.5 | 80 |
| 7.5 | 82 |
| 10 | 83 |
| 7 | 84 |
| 10.5 | 85 |
| 6.5 | 88 |
| 8 | 88 |
| 6.5 | 90 |
| 9.5 | 90 |
| 7.5 | 91 |
| 8 | 93 |
| 7 | 94 |
| 8.5 | 96 |
| 9 | 97 |
| 8.5 | 100 |

## Tutorial

### Part: Investigate a straight line

- **Worksheet:** Sleep and scores

#### Step: Prepare the investigation

Research question: Does the number of hours a student sleeps predict their final exam score?

- **Open:** Upload the generated XLSX workbook to Google Drive and open it in Google Sheets.
- **Choose:** File > Make a copy
- **Rename:** Include your name and the date. Use the Sleep and scores tab throughout.
- **Inspect:** The complete paired dataset is already in `A1:B26`; no copying from another
  workbook is needed. Each row is one student. Keep the sleep/score pairs together and record
  narrative responses in your notes.
- **Practice:** Enter each formula in its named cell, including the opening `=`, then press Enter.
  Select the cell again to inspect the formula bar. Leave the original data in columns A and B.

![Workspace setup illustration](assets/caffeine_05.png)

#### Step: Identify the variables

Before performing calculations, distinguish the predictor from the response.

- **Identify:** X, the predictor, is hours of sleep in `A2:A26`.
- **Identify:** Y, the response, is exam score (%) in `B2:B26`.
- **Explain:** Why is sleep the predictor for this research question?

An association does not show causation. Study habits, stress, and caffeine intake could also
be related to scores. These observations alone cannot isolate a causal effect of sleep.

#### Step: Make a scatterplot

A scatterplot shows direction, form, and strength before we calculate a regression equation.

![Hours of sleep and exam scores for all 25 students](assets/caffeine_sleep_score_scatter.png)

These are the 25 observations supplied in your workbook. Check your chart against these points.

##### Substep: Create the chart

- **Select:** `A1:B26`
- **Choose:** Insert > Chart
- **Choose:** Chart editor > Setup > Chart type > Scatter chart
- **Check:** Hours of sleep are on the x-axis; exam scores are on the y-axis.
- **Choose:** Chart editor > Customize > Chart and axis titles
- **Title:** Hours of Sleep vs. Final Exam Scores.
- **Name axes:** Horizontal axis: Hours of Sleep. Vertical axis: Final Exam Score (%).

##### Substep: Pause and predict

- **Observe:** A positive linear pattern rises from left to right; a negative pattern falls.
- **Observe:** A weak linear relationship has substantial scatter around its overall direction.
  No apparent linear relationship can still conceal a curve.
- **Predict:** Record the direction, strength, and shape before calculating. Do the points rise,
  fall, or bend? Do not force every pattern into a positive/negative classification.

![Dr. Caffeine discusses the scatterplot](assets/caffeine_07.png)

#### Step: Calculate the regression line

Simple linear regression finds the least-squares straight line through the observations.
The equation is predicted exam score = intercept + slope &times; hours of sleep,
or y-hat = b0 + b1 x. Here y-hat is a predicted score, b0 is the intercept, b1 is the slope,
and x is hours of sleep.

![Linear regression illustration](assets/caffeine_08.png)

- **Label D1:** Regression measure
- **Label E1:** Calculated result
- **Label D2:** Slope
- **Enter E2:** `=SLOPE(B2:B26,A2:A26)`
- **Label D6:** Intercept
- **Enter E6:** `=INTERCEPT(B2:B26,A2:A26)`
- **Label D10:** R-squared
- **Enter E10:** `=RSQ(B2:B26,A2:A26)`

The slope is the predicted change in score, in percentage points, per additional hour of sleep.
The intercept predicts a score at zero hours. R-squared (R<sup>2</sup>) is the fraction of score
variation accounted for by this fitted model.

- **Open chart:** Double-click your scatterplot.
- **Choose:** Chart editor > Customize > Series
- **Set:** Turn on Trendline and choose Linear. Under Label, choose Use equation; show R-squared.
- **Check:** If R-squared is hidden, turn on the legend under Customize > Legend.
- **Compare:** The chart and your cells should use the same data and agree up to rounding.

#### Step: Interpret and predict

Consider the hypothetical equation predicted score = 45 + 5 &times; hours of sleep.
The intercept is 45%; the slope is 5 percentage points per hour. These are examples, not the
coefficients of Dr. Caffeine's dataset. A prediction at zero hours may not be meaningful because
zero is outside the observed sleep range (3 to 11.5 hours).

- **Interpret:** Use your slope in `E2`: for one additional hour of sleep, predicted score changes
  by approximately _____ percentage points, on average. Is the slope positive or negative?
- **Compare:** Does this agree with your scatterplot prediction?
- **Interpret:** Use your intercept in `E6`: predicted score at zero hours is _____%.
  Why is extrapolation to zero hours questionable?
- **Label D14:** Predicted score at 7 hours
- **Enter E14:** `=E6+E2*7`
- **Explain:** Substitute x = 7 into y-hat = b0 + b1 x. This is a model prediction, not a
  guarantee for an individual student's score.

#### Step: Evaluate fit and evidence

If R-squared were 0.60, the fitted linear model would account for 60% of the observed variation
in scores. R-squared alone does not show that a straight line captures the pattern well.

- **Reflect:** What is your R-squared in `E10`, and what does it say about the fitted line?

Test the population slope with a **two-tailed** alternative:
H<sub>0</sub>: &beta;1 = 0 (no linear association), versus
H<sub>1</sub>: &beta;1 &ne; 0 (association in either direction).
Use significance level &alpha; = 0.05. Classical slope inference assumes an appropriate linear
mean model with independent, normally distributed errors of constant variance; inspect the
scatterplot before treating this test as a complete account of the relationship.

##### Substep: Extract regression statistics

LINEST returns regression statistics. We use INDEX to extract one value at a time, keeping
neighboring cells free rather than spilling an array. For one predictor the LINEST array's first
row contains slope/intercept, second row their standard errors, and fourth row F/degrees of freedom.

- **Label G1:** Regression statistics
- **Label G2:** Slope
- **Enter H2:** `=INDEX(LINEST(B2:B26,A2:A26,TRUE,TRUE),1,1)`
- **Label G3:** Standard error of slope
- **Enter H3:** `=INDEX(LINEST(B2:B26,A2:A26,TRUE,TRUE),2,1)`
- **Label G5:** Residual degrees of freedom
- **Enter H5:** `=INDEX(LINEST(B2:B26,A2:A26,TRUE,TRUE),4,2)`
- **Compare:** `H2` should agree with `E2`; `H5` should equal 25 - 2 = 23.

##### Substep: Calculate the test statistic

The t statistic measures how many estimated standard errors the slope is from zero:
t = slope / standard error of slope.

- **Label J2:** t-statistic
- **Enter K2:** `=H2/H3`
- **Label J6:** Residual degrees of freedom
- **Enter K6:** `=H5`

##### Substep: Calculate the two-tailed p-value

The two-tailed p-value tests a slope different from zero in either direction. A directional
one-tailed test would require a specific alternative chosen before examining the data;
that is not our question here.

- **Label J10:** Two-tailed p-value (slope differs from zero)
- **Enter K10:** `=T.DIST.2T(ABS(K2),K6)`
- **Record:** Two-tailed p-value for a nonzero slope in either direction = _____.

##### Substep: Make a decision

- **Compare:** Compare `K10` with 0.05. If p < 0.05, reject H<sub>0</sub>; there is statistically
  significant evidence against a zero slope under the regression assumptions.
- **Decide:** If p &ge; 0.05, fail to reject H<sub>0</sub>; evidence of a nonzero linear slope
  is insufficient. This does not establish that there is no relationship of any kind.
- **Reflect:** Report your p-value, decision, and evidence about a linear association.

A p-value does not measure the strength of a relationship or the probability the null hypothesis
is true. A significant slope also does not rescue a model that misses a curve. Statistics:
humbling us one coffee at a time.

#### Step: Interpret the whole pattern

- **Check:** Your slope should be about 3.18 percentage points per hour and R-squared about
  0.347. If not, check that all three regression functions use scores first and sleep second,
  with rows 2 through 26 in both ranges.
- **Reflect:** Does the straight line capture the scatterplot's overall pattern? Explain using
  the plot, the R-squared, and the scope of the slope test.
- **Explain:** Why would an upside-down U be poorly summarized by one constant slope?
- **Apply:** A classmate says, "The slope is significant, so every extra hour of sleep improves
  every student's score by the slope amount." Identify the prediction, model-shape, and causal
  claims that go beyond what these observations establish.
- **Submit:** Include your labeled scatterplot and trendline, regression calculations, seven-hour
  prediction, two-tailed slope-test decision, and a short answer to Dr. Caffeine's research
  question. Explain whether you would keep investigating a curved model.

Dr. Caffeine needs more than a line that looks official. Continue with **Dr. Caffeine's All-Nighter
Academy: quadratic regression** to fit a curve and compare models. That workbook repeats all the
data and supplies its own linear comparison calculations.
