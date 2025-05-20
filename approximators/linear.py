def approximate(x_arr, y_arr):
	sx, sxx, sy, sxy, n = 0, 0, 0, 0, 0
	print(f'|\t№\t|\tx\t\t|\ty\t\t|')
	for i in range(0, len(x_arr)):
		n += 1
		sx += x_arr[i]
		sxx += x_arr[i] ** 2
		sxy += x_arr[i] * y_arr[i]
		sy += y_arr[i]
		print(f'|\t{n}\t|\t{x_arr[i]:.3f}\t|\t{y_arr[i]:.3f}\t|')
	if sxx * n - sx ** 2:
		a = (sxy * n - sx * sy) / (sxx * n - sx ** 2)
		b = (sxx * sy - sx * sxy) / (sxx * n - sx ** 2)
		return a, b
	else:
		print('Cannot use this method')
		return None, None


def correlation(f, x_arr):
	s_upper = 0
	sx_lower, sy_lower = 0, 0
	mid_x, mid_y = sum(x_arr) / len(x_arr), sum([f(x) for x in x_arr]) / len(x_arr)
	for i in range(len(x_arr)):
		x = x_arr[i]
		s_upper += (x - mid_x) * (f(x) - mid_y)
		sx_lower += (x - mid_x) ** 2
		sy_lower += (f(x) - mid_y) ** 2
	return s_upper / (sx_lower * sy_lower) ** 0.5
