import math

import approximators.linear

def approximate(f, x_arr):
	a, b = approximators.linear.approximate(lambda x: math.log(f(x)), x_arr)
	if a is None:
		return None
	a = math.exp(a)
	return a, b