def deviation(x_arr, y_arr, f):
	if f is None:
		print('---')
		return None
	eps = 0
	print('\t№\t|\tx\t\t|\ty\t\t|\tphi\t\t|\teps')
	for i in range(len(x_arr)):
		eps += (f(x_arr[i]) - y_arr[i]) ** 2
		print(f'\t{i + 1}\t|\t{x_arr[i]:.3f}\t|\t{y_arr[i]:.3f}\t|\t{f(x_arr[i]):.3f}\t|\t{abs(f(x_arr[i]) - y_arr[i]):.3f}')
	return (eps / len(x_arr)) ** 0.5
