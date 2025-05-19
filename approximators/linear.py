def approximate(f, x_start, x_finish, h):
	x = x_start
	if x_start > x_finish or h < 0:
		return None
	sx, sxx, sy, sxy, n = 0, 0, 0, 0, 0
	print(f'|\t№\t|\tx\t\t|\ty\t\t|')
	while x < x_finish:
		y = f(x)
		n += 1
		sx += x
		sxx += x**2
		sxy += x * y
		sy += y
		print(f'|\t{n}\t|\t{x:.3f}\t|\t{y:.3f}\t|')
		x += h
	a = (sxy * n - sx * sy) / (sxx * n - sx**2)
	b = (sxx * sy - sx * sxy) / (sxx * n - sx ** 2)
	return a, b