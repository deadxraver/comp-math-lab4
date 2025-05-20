def deviation(x_arr, y_arr, f):
	if f is None:
		print('---')
		return None
	eps = 0
	print('\t№\t|\tx\t\t|\ty\t\t|\tphi\t\t|\teps')
	for i in range(len(x_arr)):
		eps += (f(x_arr[i]) - y_arr[i]) ** 2
		print(
			f'\t{i + 1}\t|\t{x_arr[i]:.3f}\t|\t{y_arr[i]:.3f}\t|\t{f(x_arr[i]):.3f}\t|\t{abs(f(x_arr[i]) - y_arr[i]):.3f}')
	return (eps / len(x_arr)) ** 0.5


def determination_coeff(x_arr, y_arr, f):
	if f is None:
		print('---')
		return None
	phi_mid = sum(f(x) for x in x_arr) / len(x_arr)
	return 1 - sum([(y_arr[i] - f(x_arr[i]))**2 for i in range(len(x_arr))]) / sum(
		[(y_arr[i] - phi_mid)**2 for i in range(len(x_arr))]) ** 2
