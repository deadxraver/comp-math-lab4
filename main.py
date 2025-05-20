import math
import warnings

import util.mid_quad_deviation

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
linear_f = lambda x: linear_coef[0] * x + linear_coef[1]
print(f'Коэффициент корреляции: {approximators.linear.correlation(linear_f, x_arr)}')
###################################
print('Квадратичная аппроксимация:')
quadratic_coef = approximators.quadratic.approximate(x_arr, y_arr)
print(quadratic_coef)
quadratic_f = lambda x: quadratic_coef[0] + quadratic_coef[1] * x + quadratic_coef[2] * x ** 2
###################################
print('Экспоненциальная аппроксимация:')
exponential_coef = approximators.exponential.approximate(x_arr, y_arr)
exponential_f = None
if exponential_coef is not None:
	print(exponential_coef)
	exponential_f = lambda x: exponential_coef[0] * math.exp(exponential_coef[1] * x)
else:
	print('Нельзя применить экспоненциальную аппроксимацию')
###################################
print('Логарифмическая аппроксимация:')
logarithmic_coef = approximators.logarithmic.approximate(x_arr, y_arr)
logarithmic_f = None
if logarithmic_coef is not None:
	print(logarithmic_coef)
	logarithmic_f = lambda x: logarithmic_coef[0] * np.log(x) + logarithmic_coef[1]
else:
	print('Нельзя применить логарифмическую аппроксимацию')
###################################
print('Степенная аппроксимация:')
power_coef = approximators.power.approximate(x_arr, y_arr)
power_f = None
if power_coef is not None:
	print(power_coef)
	power_f = lambda x: power_coef[0] * np.pow(x, power_coef[1])
else:
	print('Нельзя применить степенную аппроксимацию')
###################################
print('Кубическая аппроксимация:')
cubic_coef = approximators.cubic.approximate(x_arr, y_arr)
cubic_f = None
if cubic_coef is not None:
	print(cubic_coef)
	cubic_f = lambda x: cubic_coef[0] + cubic_coef[1] * x + cubic_coef[2] * x ** 2 + cubic_coef[3] * x ** 3
else:
	print('Нельзя применить кубическую аппроксимацию')
###################################
print('\nОтклонения')
print('Линейная:')
linear_d = util.mid_quad_deviation.deviation(x_arr, y_arr, linear_f)
print(f'Среднеквадратическое отклонение: {linear_d}')
print('Квадратичная:')
quadratic_d = util.mid_quad_deviation.deviation(x_arr, y_arr, quadratic_f)
print(f'Среднеквадратическое отклонение: {quadratic_d}')
print('Экспоненциальная:')
exponential_d = util.mid_quad_deviation.deviation(x_arr, y_arr, exponential_f)
print(f'Среднеквадратическое отклонение: {exponential_d}')
print('Логарифмическая:')
logarithmic_d = util.mid_quad_deviation.deviation(x_arr, y_arr, logarithmic_f)
print(f'Среднеквадратическое отклонение: {logarithmic_d}')
print('Степенная:')
power_d = util.mid_quad_deviation.deviation(x_arr, y_arr, power_f)
print(f'Среднеквадратическое отклонение: {power_d}')
print('Кубическая:')
cubic_d = util.mid_quad_deviation.deviation(x_arr, y_arr, cubic_f)
print(f'Среднеквадратическое отклонение: {cubic_d}')
min_d = min(linear_d or float('inf'), quadratic_d or float('inf'), exponential_d or float('inf'),
			logarithmic_d or float('inf'), power_d or float('inf'), cubic_d or float('inf'))
graph.add_function(linear_f, [x_arr[0] - 1, x_arr[-1] + 1], label='Линейная', is_best=min_d == linear_d)
graph.add_function(quadratic_f, [x_arr[0] - 1, x_arr[-1] + 1], label='Квадратичная', is_best=min_d == quadratic_d)
graph.add_function(exponential_f, [x_arr[0] - 1, x_arr[-1] + 1], label='Экспоненциальная',
				   is_best=min_d == exponential_d)
graph.add_function(logarithmic_f, [x_arr[0] - 1, x_arr[-1] + 1], label='Логарифмическая',
				   is_best=min_d == logarithmic_d)
graph.add_function(power_f, [x_arr[0] - 1, x_arr[-1] + 1], label='Степенная', is_best=min_d == power_d)
graph.add_function(cubic_f, [x_arr[0] - 1, x_arr[-1] + 1], label='Кубическая', is_best=min_d == cubic_d)
print(f'Наиболее близкая аппроксимация - {graph.best_approx}, среднеквадратическое отклонение для нее равно {min_d}')
graph.show()
