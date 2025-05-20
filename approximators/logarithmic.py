import math

import approximators.linear


def approximate(x_arr, y_arr):
	new_x = []
	new_y = []
	for i in range(len(x_arr)):
			try:
				new_x.append(math.log(x_arr[i]))
				new_y.append(y_arr[i])
			except ValueError:
				continue
	if new_x:
		a, b = approximators.linear.approximate(new_x, new_y)
		if a is None:
			return None
		return a, b
	return None