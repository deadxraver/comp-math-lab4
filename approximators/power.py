import math

import approximators.linear


def approximate(x_arr, y_arr):
	new_x = []
	new_y = []
	for i in range(len(x_arr)):
		try:
			x = math.log(x_arr[i])
			y = math.log(y_arr[i])
			new_x.append(x)
			new_y.append(y)
		except ValueError:
			continue
	if x_arr:
		a, b = approximators.linear.approximate(new_x, new_y)
		if a is None:
			return None
		return math.exp(a), b
	return None
