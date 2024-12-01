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

    # График sinh(x)
    plt.figure(figsize=(8, 6))
    plt.plot(x, sinh(x), label="sinh(x)", color="blue", linestyle="--")
    plt.title("График гиперболического синуса (sinh)", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("sinh(x)", fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()

    # График cosh(x)
    plt.figure(figsize=(8, 6))
    plt.plot(x, cosh(x), label="cosh(x)", color="green", linestyle="-.")
    plt.title("График гиперболического косинуса (cosh)", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("cosh(x)", fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()

    # График tanh(x)
    plt.figure(figsize=(8, 6))
    plt.plot(x, tanh(x), label="tanh(x)", color="red")
    plt.title("График гиперболического тангенса (tanh)", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("tanh(x)", fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()
