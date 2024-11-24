import numpy as np

def sigmoid(x):
    """
    Вычисление сигмоиды.
    Формула: y(x) = 1 / (1 + exp(-x))
    """
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """
    Вычисление производной сигмоиды.
    Формула: y'(x) = y(x) * (1 - y(x))
    где y(x) = sigmoid(x)
    """
    s = sigmoid(x)
    return s * (1 - s)
