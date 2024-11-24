import numpy as np
import pandas as pd
from sigmoid import sigmoid, sigmoid_derivative
from hyperbolic import tanh_derivative
from plots import plot_sigmoid, plot_hyperbolic

# Заданные точки
x_values = np.array([0, 3, -3, 8, -8, 15, -15])

# Вычисление значений функций
sigmoid_values = np.round(sigmoid(x_values), 15)
sigmoid_derivative_values = np.round(sigmoid_derivative(x_values), 15)
tanh_derivative_values = np.round(tanh_derivative(x_values), 15)

# Создание таблицы
results = pd.DataFrame({
    "x": x_values,
    "Sigmoid(x)": sigmoid_values,
    "Sigmoid'(x)": sigmoid_derivative_values,
    "Tanh'(x)": tanh_derivative_values
})

# Отображение таблицы
print(results)

# Построение графиков
plot_sigmoid((-15, 15))
plot_hyperbolic((-15, 15))
