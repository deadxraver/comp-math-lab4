import math
import warnings

warnings.filterwarnings("ignore")
import numpy as np

import approximators.linear
import approximators.quadratic
import approximators.exponential
import approximators.logarithmic
import approximators.power
import approximators.cubic
import graph

f = lambda x: 17 * x / (x ** 4 + 16)

h = 0.4
x_start = 0
x_finish = 4
x = x_start
x_arr = []
y_arr = []
while x <= x_finish:
	x_arr.append(x)
	y_arr.append(f(x))
	x += h
graph.create_plot()
graph.add_points(f, x_arr)
###################################
print('Линейная аппроксимация:')
linear_coef = approximators.linear.approximate(x_arr, y_arr)
print(linear_coef)
graph.add_function(lambda x: linear_coef[0] * x + linear_coef[1], [x_arr[0] - 1, x_arr[-1] + 1], label='Линейная')
###################################
print('Квадратичная аппроксимация:')
quadratic_coef = approximators.quadratic.approximate(x_arr, y_arr)
print(quadratic_coef)
graph.add_function(lambda x: quadratic_coef[0] + quadratic_coef[1] * x + quadratic_coef[2] * x ** 2,
				   [x_arr[0] - 1, x_arr[-1] + 1], label='Квадратичная')
###################################
print('Экспоненциальная аппроксимация:')
exponential_coef = approximators.exponential.approximate(x_arr, y_arr)
if exponential_coef is not None:
	print(exponential_coef)
	graph.add_function(lambda x: exponential_coef[0] * math.exp(exponential_coef[1] * x), [x_arr[0] - 1, x_arr[-1] + 1],
					   label='Экспоненциальная')
else:
	print('Нельзя применить экспоненциальную аппроксимацию')
###################################
print('Логарифмическая аппроксимация:')
logarithmic_coef = approximators.logarithmic.approximate(x_arr, y_arr)
if logarithmic_coef is not None:
	print(logarithmic_coef)
	graph.add_function(lambda x: logarithmic_coef[0] * np.log(x) + logarithmic_coef[1], [x_arr[0] - 1, x_arr[-1] + 1],
					   label='Логарифмическая')
else:
	print('Нельзя применить логарифмическую аппроксимацию')
###################################
print('Степенная аппроксимация:')
power_coef = approximators.power.approximate(x_arr, y_arr)
if power_coef is not None:
	print(power_coef)
	graph.add_function(lambda x: power_coef[0] * np.pow(x, power_coef[1]), [x_arr[0] - 1, x_arr[-1] + 1],
					   label='Степенная')
else:
	print('Нельзя применить степенную аппроксимацию')
###################################
print('Кубическая аппроксимация:')
cubic_coef = approximators.cubic.approximate(x_arr, y_arr)
if cubic_coef is not None:
	print(cubic_coef)
	graph.add_function(lambda x: cubic_coef[0] + cubic_coef[1] * x + cubic_coef[2] * x ** 2 + cubic_coef[3] * x ** 3,
					   [x_arr[0] - 1, x_arr[-1] + 1],
					   label='Кубическая')
else:
	print('Нельзя применить кубическую аппроксимацию')
###################################
graph.show()
