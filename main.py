import approximators.linear
import approximators.quadratic

f = lambda x: 17 * x / (x ** 4 + 16)

h = 0.4
x_start = -4
x_finish = 0
x = x_start
x_arr = []
while x <= x_finish:
	x_arr.append(x)
	x += h
print('Линейная аппроксимация:')
linear_coef = approximators.linear.approximate(f, x_arr)
print(linear_coef)
print('Квадратичная аппроксимация:')
quadratic_coef = approximators.quadratic.approximate(f, x_arr)
print(quadratic_coef)
