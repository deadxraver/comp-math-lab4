import approximators.linear
import approximators.quadratic
import graph

f = lambda x: 17 * x / (x ** 4 + 16)

h = 0.4
x_start = -4
x_finish = 0
x = x_start
x_arr = []
while x <= x_finish:
	x_arr.append(x)
	x += h
graph.create_plot()
graph.add_points(f, x_arr)
print('Линейная аппроксимация:')
linear_coef = approximators.linear.approximate(f, x_arr)
print(linear_coef)
graph.add_function(lambda x: linear_coef[0] * x + linear_coef[1], [x_arr[0] - 1, x_arr[-1] + 1], label='Линейная')
print('Квадратичная аппроксимация:')
quadratic_coef = approximators.quadratic.approximate(f, x_arr)
print(quadratic_coef)
graph.add_function(lambda x: quadratic_coef[0] + quadratic_coef[1] * x + quadratic_coef[2] * x**2, [x_arr[0] - 1, x_arr[-1] + 1], label='Квадратичная')

graph.show()
