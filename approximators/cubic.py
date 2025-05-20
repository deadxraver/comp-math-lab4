import numpy as np
import util.system_solver


def approximate(x_arr, y_arr) -> (float, float, float, float):
	sx, sy, sxx, sxy, sx3, sxxy, sx4, sx5, sx6, sx3y = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	n = 0
	print(f'|\t№\t|\tx\t\t|\ty\t\t|')
	for i in range(len(x_arr)):
		n += 1
		x = x_arr[i]
		y = y_arr[i]
		sx += x
		sy += y
		sxx += x ** 2
		sxy += x * y
		sx3 += x ** 3
		sxxy += y * x ** 2
		sx4 += x ** 4
		sx5 += x ** 5
		sx6 += x ** 6
		sx3y += y * x ** 3
		print(f'|\t{n}\t|\t{x:.3f}\t|\t{y:.3f}\t|')
	A = np.array([
		[n, sx, sxx, sx3],
		[sx, sxx, sx3, sx4],
		[sxx, sx3, sx4, sx5],
		[sx3, sx4, sx5, sx6]
	])
	B = np.array([sy, sxy, sxxy, sx3y])
	a0, a1, a2, a3 = util.system_solver.solve_linear_system(A, B)
	return float(a0), float(a1), float(a2), float(a3)
