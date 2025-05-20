import math

import approximators.linear

def approximate(x_arr, y_arr):
	new_y_arr = []
	new_x_arr = []
	for i in range(len(x_arr)):
		try:
			new_y_arr.append(math.log(y_arr[i]))
			new_x_arr.append(x_arr[i])
		except ValueError:
			continue
	if new_x_arr:
		a, b = approximators.linear.approximate(new_x_arr, new_y_arr)
		if a is None:
			return None
		a = math.exp(a)
		return a, b
	return None