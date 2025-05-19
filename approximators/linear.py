def approximate(f, x_arr):
	sx, sxx, sy, sxy, n = 0, 0, 0, 0, 0
	print(f'|\t№\t|\tx\t\t|\ty\t\t|')
	for x in x_arr:
		y = f(x)
		n += 1
		sx += x
		sxx += x**2
		sxy += x * y
		sy += y
		print(f'|\t{n}\t|\t{x:.3f}\t|\t{y:.3f}\t|')
	a = (sxy * n - sx * sy) / (sxx * n - sx**2)
	b = (sxx * sy - sx * sxy) / (sxx * n - sx ** 2)
	return a, b