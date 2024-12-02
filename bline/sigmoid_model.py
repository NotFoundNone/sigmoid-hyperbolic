import numpy as np
import matplotlib.pyplot as plt

# Параметры модели t = (t0, t1, t2, t3, t4, t5)
t = np.array([1, 0, 2, 1, 1, 0])

# Функция модели f(x1, x2)
def f(x1, x2):
    return t[0] + t[1] * x1 + t[2] * x2 + t[3] * x1 * x2 + t[4] * x1**2 + t[5] * x2**2

# Сигмоида
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Сетка для построения графика
x1_vals = np.linspace(-20, 20, 400)
x2_vals = np.linspace(-20, 20, 400)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = f(X1, X2)

# Сигмоид на сетке
S = sigmoid(Z)

# Построение графика
plt.figure(figsize=(8, 6))

# Контуры для границы раздела
plt.contour(X1, X2, S, levels=[0.5], colors='red', linewidths=2)

# Области для классов
plt.contourf(X1, X2, S, levels=[0, 0.5], colors='lightblue', alpha=0.5)  # Класс 0
plt.contourf(X1, X2, S, levels=[0.5, 1], colors='lightcoral', alpha=0.5)  # Класс 1

# Оформление
plt.title('Разделяющая кривая для двух классов')
plt.xlabel('x1')
plt.ylabel('x2')
plt.colorbar(label='Вероятность принадлежности классу 1')

# Показываем график
plt.show()
