import numpy as np

def sinh(x):
    """
    Вычисление гиперболического синуса.
    Формула: sinh(x) = (exp(x) - exp(-x)) / 2
    """
    return np.sinh(x)

def cosh(x):
    """
    Вычисление гиперболического косинуса.
    Формула: cosh(x) = (exp(x) + exp(-x)) / 2
    """
    return np.cosh(x)

def tanh(x):
    """
    Вычисление гиперболического тангенса.
    Формула: tanh(x) = sinh(x) / cosh(x)
             tanh(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
    """
    return np.tanh(x)

def tanh_derivative(x):
    """
    Вычисление производной гиперболического тангенса.
    Формула: tanh'(x) = 1 - tanh^2(x)
    """
    return 1 - np.tanh(x)**2
