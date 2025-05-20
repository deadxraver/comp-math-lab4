import numpy as np

def solve_linear_system(A, B):
	A = np.array(A)
	B = np.array(B)
	try:
		solution = np.linalg.solve(A, B)
		return solution
	except np.linalg.LinAlgError:
		return None, None, None

def approximate(x_arr, y_arr):
	sx, sxx, sx3, sx4, sy, sxy, n, sxxy = 0, 0, 0, 0, 0, 0, 0, 0
	print(f'|\t№\t|\tx\t\t|\ty\t\t|')
	for i in range(len(x_arr)):
		x = x_arr[i]
		y = y_arr[i]
		n += 1
		sx += x
		sxx += x ** 2
		sxy += x * y
		sy += y
		sx3 += x ** 3
		sx4 += x ** 4
		sxxy += y * x ** 2
		print(f'|\t{n}\t|\t{x:.3f}\t|\t{y:.3f}\t|')

	A = np.array([
		[n, sx, sxx],
		[sx, sxx, sx3],
		[sxx, sx3, sx4]
	])

	B = np.array([sy, sxy, sxxy])

	try:
		a0, a1, a2 = solve_linear_system(A, B)
		return float(a0), float(a1), float(a2)
	except np.linalg.LinAlgError:
		return None
