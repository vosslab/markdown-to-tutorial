# Babies Z-test story correction

The closing story now makes Joe's mistake consistent with the right-tailed test result. The sample
mean is higher, but the p-value is 0.157, so the test fails to reject the null hypothesis.

Before:

> Joe was ecstatic after conducting his Z-test, certain that his hospital's babies were the heaviest
> in town. He was ready to claim the Baby Butter Ball Award and throw a butter-and-bacon-themed
> celebration.

After:

> Joe mistook the higher sample mean for proof that his hospital's babies were heavier, ignoring the
> nonsignificant Z-test. He was ready to claim the Baby Butter Ball Award and throw a
> butter-and-bacon-themed celebration.

The butter-and-bacon humor remains. No data, formulas, or other tutorial wording changed.

Validation: `source source_me.sh && python3 make_tutorial.py lint tutorial_data/babies_1_z_test.md`
passed offline lint. Existing warnings remain for spare rows through 40 and the unsupplied E19
practice input; Google worksheet mapping notes are unchanged. Google import, navigation, and
calculation were not checked by offline lint.
