"""Protect direction and polynomial coefficient inference in independent oracles."""

import math

import numpy
import pytest

import tutorial_oracles


#============================================
def test_signed_tails_preserve_research_direction() -> None:
	"""A negative statistic must give a large right tail, including for student t."""
	for degrees in (None, 12):
		negative = tutorial_oracles.tails(-2., degrees)
		positive = tutorial_oracles.tails(2., degrees)
		assert negative[2] > .95
		assert negative == pytest.approx((positive[0], positive[2], positive[1]))
		assert negative[0] == pytest.approx(2 * negative[1])


#============================================
def test_quadratic_coefficient_order_and_standard_error() -> None:
	"""Prevent reversing LINEST predictor coefficients or using the wrong covariance."""
	x = numpy.array([-2., -1., 0., 1., 2.])
	# The residual is orthogonal to the intercept, x and x squared.
	y = numpy.array([9.1, 1.6, 1.6, 5.6, 17.1])
	result = tutorial_oracles.regression(x, y, 2)
	assert result["beta"] == pytest.approx([1., 2., 3.])
	assert result["df"] == 2
	assert result["se"][2] == pytest.approx(math.sqrt(.025))
