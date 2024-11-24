import matplotlib.pyplot as plt
import numpy as np
from sigmoid import sigmoid
from hyperbolic import sinh, cosh, tanh


def plot_sigmoid(x_range):
    """
    Построение графика сигмоиды.
    Формула: y(x) = 1 / (1 + exp(-x))
    """
    x = np.linspace(*x_range, 500) # 500 точек между x_range[0] и x_range[1]
    y = sigmoid(x)

    plt.plot(x, y, label="Sigmoid(x)", color="green")
    plt.title("График сигмоиды")
    plt.xlabel("x")
    plt.ylabel("Sigmoid(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_hyperbolic(x_range):
    """
    Построение графиков гиперболических функций.
    Формулы:
        sinh(x) = (exp(x) - exp(-x)) / 2
        cosh(x) = (exp(x) + exp(-x)) / 2
        tanh(x) = sinh(x) / cosh(x)
    """
    x = np.linspace(*x_range, 500)
    y_sinh = sinh(x)
    y_cosh = cosh(x)
    y_tanh = tanh(x)

    plt.plot(x, y_sinh, label="sinh(x)", linestyle="--")
    plt.plot(x, y_cosh, label="cosh(x)", linestyle="-.")
    plt.plot(x, y_tanh, label="tanh(x)")
    plt.title("Гиперболические функции")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
