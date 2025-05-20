import math
import sys
import warnings

import util.deviation

warnings.filterwarnings("ignore")
import numpy as np

import approximators.linear
import approximators.quadratic
import approximators.exponential
import approximators.logarithmic
import approximators.power
import approximators.cubic
import util.input_handler
import graph

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', '-f')

args = parser.parse_args()

if args.filename is not None:
	util.input_handler.setfile(args.filename)

n = None
try:
	n = int(util.input_handler.read("Введите количество элементов(от 9 до 12): "))
	if n < 9 or n > 12:
		raise ValueError
except ValueError:
	print('Введите число от 9 до 12')
	sys.exit(-1)
x_arr = []
y_arr = []
print(f'Введите {n} элементов в формате `x y`')
for i in range(n):
	try:
		x, y = map(int, util.input_handler.read().split())
		x_arr.append(x)
		y_arr.append(y)
	except:
		print('Неправильный ввод!')
		sys.exit(-1)
print('Спасибо!')
graph.create_plot()
graph.add_points(x_arr, y_arr, label='Исходные точки')
###################################
print('Линейная аппроксимация:')
linear_coef = approximators.linear.approximate(x_arr, y_arr)
print(linear_coef)
linear_f = lambda x: linear_coef[0] * x + linear_coef[1]
print(f'Коэффициент корреляции: {approximators.linear.correlation(linear_f, x_arr)}')
print('Коэффициент детерминации:')
print(util.deviation.determination_coeff(x_arr, y_arr, linear_f))
###################################
print('Квадратичная аппроксимация:')
quadratic_coef = approximators.quadratic.approximate(x_arr, y_arr)
print(quadratic_coef)
quadratic_f = lambda x: quadratic_coef[0] + quadratic_coef[1] * x + quadratic_coef[2] * x ** 2
print('Коэффициент детерминации:')
print(util.deviation.determination_coeff(x_arr, y_arr, quadratic_f))
###################################
print('Экспоненциальная аппроксимация:')
exponential_coef = approximators.exponential.approximate(x_arr, y_arr)
exponential_f = None
if exponential_coef is not None:
	print(exponential_coef)
	exponential_f = lambda x: exponential_coef[0] * math.exp(exponential_coef[1] * x)
	print('Коэффициент детерминации:')
	print(util.deviation.determination_coeff(x_arr, y_arr, exponential_f))
else:
	print('Нельзя применить экспоненциальную аппроксимацию')
###################################
print('Логарифмическая аппроксимация:')
logarithmic_coef = approximators.logarithmic.approximate(x_arr, y_arr)
logarithmic_f = None
if logarithmic_coef is not None:
	print(logarithmic_coef)
	logarithmic_f = lambda x: logarithmic_coef[0] * np.log(x) + logarithmic_coef[1]
	print('Коэффициент детерминации:')
	print(util.deviation.determination_coeff(x_arr, y_arr, logarithmic_f))
else:
	print('Нельзя применить логарифмическую аппроксимацию')
###################################
print('Степенная аппроксимация:')
power_coef = approximators.power.approximate(x_arr, y_arr)
power_f = None
if power_coef is not None:
	print(power_coef)
	power_f = lambda x: power_coef[0] * np.pow(x, power_coef[1])
	print('Коэффициент детерминации:')
	print(util.deviation.determination_coeff(x_arr, y_arr, power_f))
else:
	print('Нельзя применить степенную аппроксимацию')
###################################
print('Кубическая аппроксимация:')
cubic_coef = approximators.cubic.approximate(x_arr, y_arr)
cubic_f = None
if cubic_coef is not None:
	print(cubic_coef)
	cubic_f = lambda x: cubic_coef[0] + cubic_coef[1] * x + cubic_coef[2] * x ** 2 + cubic_coef[3] * x ** 3
	print('Коэффициент детерминации:')
	print(util.deviation.determination_coeff(x_arr, y_arr, cubic_f))
else:
	print('Нельзя применить кубическую аппроксимацию')
###################################
print('\nОтклонения')
print('Линейная:')
linear_d = util.deviation.deviation(x_arr, y_arr, linear_f)
print(f'Среднеквадратическое отклонение: {linear_d}')
print('Квадратичная:')
quadratic_d = util.deviation.deviation(x_arr, y_arr, quadratic_f)
print(f'Среднеквадратическое отклонение: {quadratic_d}')
print('Экспоненциальная:')
exponential_d = util.deviation.deviation(x_arr, y_arr, exponential_f)
print(f'Среднеквадратическое отклонение: {exponential_d}')
print('Логарифмическая:')
logarithmic_d = util.deviation.deviation(x_arr, y_arr, logarithmic_f)
print(f'Среднеквадратическое отклонение: {logarithmic_d}')
print('Степенная:')
power_d = util.deviation.deviation(x_arr, y_arr, power_f)
print(f'Среднеквадратическое отклонение: {power_d}')
print('Кубическая:')
cubic_d = util.deviation.deviation(x_arr, y_arr, cubic_f)
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
