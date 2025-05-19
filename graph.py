import numpy as np
import matplotlib.pyplot as plt


def create_plot(figsize=(10, 6)):
	plt.figure(figsize=figsize)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True, alpha=0.3)


def add_function(func, interval, label=None, color=None, linestyle='--'):
	a, b = interval
	x = np.linspace(a, b, 500)
	y = np.vectorize(func)(x)

	plt.plot(x, y,
			 label=label,
			 color=color,
			 linestyle=linestyle,
			 zorder=1)


def add_points(func, points, label=None, color='red', marker_size=100):
	x_points = np.array(points)
	y_points = np.vectorize(func)(x_points)

	plt.scatter(x_points, y_points,
				color=color,
				s=marker_size,
				zorder=2,
				label=label,
				edgecolors='black')


def show():
	plt.title('Графики функций')
	plt.legend()
	plt.show()