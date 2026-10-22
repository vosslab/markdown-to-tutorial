# Dr. Caffeine's All-Nighter Academy: quadratic regression

Dr. Caffeine is staring at the straight-line fit like he just failed his own exam. The observations
rise and then fall: students with moderate sleep tend to score higher than students near either
end of this dataset. A straight line cannot capture that academic roller coaster. Time for a
new plan, another coffee, and possibly a nap!

This is tutorial 3 of 3. Complete
**Dr. Caffeine's All-Nighter Academy: linear regression** first, or bring equivalent
knowledge of scatterplots, slope, intercept, R-squared, and two-tailed regression tests.
This workbook includes all 25 original pairs and recreates the linear comparison, so it does not
require a completed previous workbook. Data provenance:
[original class template](https://docs.google.com/spreadsheets/d/1mhOQhC_1hqnbvYItPT3y-V-_9l9q3pN7MtZDcOevaA0/edit?gid=0#gid=0).

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

### Part: Let the model curve

- **Worksheet:** Sleep and scores

#### Step: Revisit the linear fit

- **Open:** Upload the generated XLSX workbook to Google Drive and open it in Google Sheets.
- **Choose:** File > Make a copy
- **Rename:** Include your name and the date. Work in Sleep and scores.
- **Select:** `A1:B26`
- **Choose:** Insert > Chart
- **Choose:** Chart editor > Setup > Chart type > Scatter chart
- **Check:** Use hours of sleep on x and exam score (%) on y; add these axis labels and an
  informative chart title.
- **Choose:** Chart editor > Customize > Series
- **Set:** Add a Linear trendline, use the equation as its label, and display R-squared.
  Turn on the legend under Customize > Legend if R-squared is hidden.
- **Label L1:** Linear comparison
- **Label L2:** Slope
- **Enter M2:** `=SLOPE(B2:B26,A2:A26)`
- **Label L3:** Intercept
- **Enter M3:** `=INTERCEPT(B2:B26,A2:A26)`
- **Label L4:** Linear R-squared
- **Enter M4:** `=RSQ(B2:B26,A2:A26)`
- **Compare:** If you completed the previous tutorial, these values should agree with its
  results. Does the line follow both the rising and falling portions of the scatterplot?

A straight line can show a positive overall slope while missing curvature. Do not assume the
linear R-squared must be near zero. Compare the calculated value with the actual shape.

![Why consider a curve?](assets/caffeine_10.png)

Research question: Does adding a squared sleep-hours term better describe this relationship?
For a **two-tailed** test of the quadratic term, H<sub>0</sub>: &beta;2 = 0 versus
H<sub>1</sub>: &beta;2 &ne; 0, with the linear term retained. This asks about curvature in either
direction, not whether sleep causes scores to change.

![Question about the quadratic model](assets/caffeine_11.png)

#### Step: Square the predictor

Squaring lets the model curve. Six hours squared is 36 hours squared; the student did not
sleep for 36 hours! Keep exam scores out of the predictor table.

- **Label C1:** Sleep hours squared
- **Enter C2:** `=A2^2`
- **Fill C2:C26:** Down
- **Do:** Select `C2:C26`, including the formula you entered in the first row, then press
  Ctrl+D (Windows) or Command+D (Mac). You can also drag the blue fill handle from `C2` to `C26`.
  Relative references
  change with the row: the last formula should be `=A26^2`.
- **Check:** `C2` should be 9 and `C26` should be 72.25.
- **Label E1:** Sleep hours predictor
- **Label F1:** Squared sleep predictor
- **Enter E2:** `=A2`
- **Enter F2:** `=C2`
- **Fill E2:F26:** Down
- **Do:** Select `E2:F26` and use the same Fill down shortcut, or select `E2:F2` and drag its
  fill handle down to row 26. Each column copies its own first formula; both predictors must stay
  aligned with the same student in column B.
- **Check:** `E26` should contain `=A26` and show 8.5; `F26` should contain `=C26` and show 72.25.

#### Step: Understand the equation

![Quadratic regression illustration](assets/caffeine_12.png)

Quadratic regression fits a polynomial that curves with respect to x:
y-hat = b0 + b1 x + b2 x<sup>2</sup>.
Here y-hat is predicted score, b0 is the intercept, b1 x is the linear term, b2 x<sup>2</sup>
is the quadratic term, and x is hours of sleep. It remains a linear regression in its coefficients;
the squared predictor allows a curved relationship in sleep hours.

- **Explain:** What would happen to the equation if b2 were zero?
- **Predict:** Would a negative or positive b2 make an upside-down U? Record your prediction.

#### Step: Fit the quadratic model

LINEST uses exam score as response and both adjacent predictor columns `E2:F26` as inputs.
The coefficient order is reversed: first squared sleep, then sleep, then intercept.
INDEX extracts scalar results without occupying a spill range.

- **Label H1:** Quadratic statistic
- **Label I1:** Value
- **Label H2:** Quadratic coefficient b2
- **Enter I2:** `=INDEX(LINEST(B2:B26,E2:F26,TRUE,TRUE),1,1)`
- **Label H3:** Linear coefficient b1
- **Enter I3:** `=INDEX(LINEST(B2:B26,E2:F26,TRUE,TRUE),1,2)`
- **Label H4:** Intercept b0
- **Enter I4:** `=INDEX(LINEST(B2:B26,E2:F26,TRUE,TRUE),1,3)`
- **Label H5:** Quadratic R-squared
- **Enter I5:** `=INDEX(LINEST(B2:B26,E2:F26,TRUE,TRUE),3,1)`
- **Label H6:** Standard error of b2
- **Enter I6:** `=INDEX(LINEST(B2:B26,E2:F26,TRUE,TRUE),2,1)`
- **Label H7:** Residual degrees of freedom
- **Enter I7:** `=INDEX(LINEST(B2:B26,E2:F26,TRUE,TRUE),4,2)`
- **Check:** Degrees of freedom should be 25 - 3 = 22. Write your fitted equation using `I2:I4`.
- **Interpret:** A negative `I2` bends the model downward. Unlike the straight-line slope,
  `I3` alone is not the score change for every extra hour: that change also depends on sleep
  through the squared term. Does the fitted sign of `I2` agree with your prediction?
- **Label H8:** Predicted score at 7 hours
- **Enter I8:** `=I4+I3*7+I2*7^2`
- **Explain:** Compare this model prediction with the linear prediction `=M3+M2*7` in your notes.
  Neither is a guarantee for an individual student.

#### Step: Test the curvature

The two-tailed test asks whether the population quadratic coefficient differs from zero in either
direction while the linear term stays in the model. Use &alpha; = 0.05. Inference assumes a suitable
quadratic mean model with independent normal errors of constant variance; a p-value alone cannot
check those assumptions.

- **Label H10:** t-statistic for quadratic term
- **Enter I10:** `=I2/I6`
- **Label H11:** Two-tailed p-value (quadratic term differs from zero)
- **Enter I11:** `=T.DIST.2T(ABS(I10),I7)`
- **Record:** Two-tailed p-value for a nonzero quadratic term in either direction = _____.
- **Decide:** If p < 0.05, reject H<sub>0</sub>; otherwise fail to reject it. State your conclusion
  about evidence of a quadratic term, conditional on the model assumptions.

The nominal p-value assumes this quadratic model and test were chosen before examining this
pattern. Because the curve is motivated by the rise and fall already seen in these same data,
treat the p-value as exploratory: selecting a model after seeing the pattern can make the usual
p-value too optimistic. Confirm the curvature with new, independent data and a model specified
before examining those data.

#### Step: Compare the models

![Linear and quadratic fits to the same 25 observations](assets/caffeine_sleep_score_model_comparison.png)

Both panels use the 25 observations in your workbook. Check your chart and R-squared values
against these fitted models.

Did the extra curve help, or did we merely complicate the equation? Linear regression describes
a straight line; quadratic regression allows curvature. A larger R-squared accounts for a larger
fraction of variation **in this dataset**. Adding a predictor cannot lower ordinary training
R-squared, so that increase alone does not prove the more complex model is preferable.

- **Compare:** Record linear R-squared from `M4` and quadratic R-squared from `I5`.
- **Open chart:** Double-click your scatterplot.
- **Choose:** Chart editor > Customize > Series > Trendline
- **Set:** For the chart trendline setting, change Linear to Polynomial and set Degree to 2.
  Display the equation and R-squared; this chart setting is separate from spreadsheet cells.
- **Compare:** Does the polynomial curve follow the rise and fall of the observations more
  faithfully? Check the chart against your fitted coefficients, allowing for display rounding.
- **Reflect:** Combine the visual pattern, R-squared values, and quadratic-term test. What evidence
  supports curvature? Why is a high R-squared alone insufficient to validate a model?
- **Explain:** What would you examine next, such as residual patterns or performance on new data,
  before relying on predictions beyond this exercise?

#### Step: Give Dr. Caffeine a verdict

Congratulations! You survived two regression models. Your reward is a better understanding of
statistics and maybe a snack, with no more coffee.

![Final academy celebration](assets/caffeine_14.png)

- **Conclude:** Answer the research question in a short paragraph: describe the observed pattern,
  compare the models, and distinguish evidence of association from a causal conclusion.
- **Reflect:** Could studying, stress, or caffeine contribute to this pattern? What kind of study
  would help investigate causal effects?
- **Apply:** A student asks you to predict a score after 16 hours of sleep. Explain why neither
  the larger R-squared nor the significant quadratic term justifies that extrapolation.
- **Submit:** Include the labeled scatterplot with the quadratic trendline, both fitted equations
  and R-squared values, your seven-hour prediction, and your two-tailed curvature-test decision.
  Add your verdict and one reason to check the model on new data.

A relationship does not automatically mean causation. The observed sleep range is 3 to 11.5 hours;
these data do not establish that increasing or reducing any student's sleep will change their score,
or define a universally optimal amount of sleep. Class dismissed: drink some water, close those
50 browser tabs, and get some sleep!
