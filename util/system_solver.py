import numpy as np


def solve_linear_system(A, B):
	A = np.array(A)
	B = np.array(B)
	try:
		solution = np.linalg.solve(A, B)
		return solution
	except np.linalg.LinAlgError:
		return None, None, None