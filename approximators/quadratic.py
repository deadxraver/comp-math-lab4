def approximate(f, x_arr):
	sx, sxx, sx3, sx4, sy, sxy, n, sxxy = 0, 0, 0, 0, 0, 0, 0, 0
	print(f'|\t№\t|\tx\t\t|\ty\t\t|')
	for x in x_arr:
		y = f(x)
		n += 1
		sx += x
		sxx += x ** 2
		sxy += x * y
		sy += y
		sx3 += x ** 3
		sx4 += x ** 4
		sxxy += x ** 2 * y
		print(f'|\t{n}\t|\t{x:.3f}\t|\t{y:.3f}\t|')
	d = n * sx * sx4 + 2 * sx * sx3 * sxx - sxx ** 3 - n * sx3 ** 2 - sx4 * sx ** 2
	if d == 0:
		return None
	a0 = (sy * sxx * sx3 + sx * sx3 * sxxy + sxy * sx3 * sxx - sxxy * sxx ** 2 - sy * sx3 ** 2 - sxy * sx * sx4) / d
	a1 = (n * sxy * sx4 + sx * sxx * sxxy + sxx * sy * sx3 - sxx ** 2 * sxy - sxxy * sx3 * n - sx * sy * sx4) / d
	a2 = (n * sxx * sxxy + sx * sx3 * sy + sx * sxx * sxy - sxx ** 2 * sy - n * sx3 * sxy - sx ** 2 * sxxy) / d
	return a0, a1, a2
