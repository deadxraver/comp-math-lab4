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
