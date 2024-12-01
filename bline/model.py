import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
t = [1, 0, 2, 1, 1, 0]  # Коэффициенты t0, t1, t2, t3, t4, t5
a = 0.5  # Критерий принятия решения

# Модельная функция
def model_function(x1, x2):
    return t[0] + t[1] * x1 + t[2] * x2 + t[3] * x1 * x2 + t[4] * x1**2 + t[5] * x2**2

# Создаем сетку значений
x1 = np.linspace(-15, 15, 500)
x2 = np.linspace(-15, 15, 500)
x1, x2 = np.meshgrid(x1, x2)

# Вычисляем значения модели и границу
decision_boundary = model_function(x1, x2) - a

# Построение графика
plt.figure(figsize=(8, 6))

# Граница классов
#Красная линия: это кривая, где 𝑦 = 0.5. Она разделяет классы.
plt.contour(x1, x2, decision_boundary, levels=[0], colors='black', linewidths=2)

# Области классов

#область 0
#Голубая область: класс 0 (𝑦 < 0.5).
plt.contourf(x1, x2, decision_boundary, levels=[-np.inf, 0], colors=['lightblue'], alpha=0.6)

#область 1
#Зеленая область: класс 1 (𝑦 >= 0.5).
plt.contourf(x1, x2, decision_boundary, levels=[0, np.inf], colors=['lightgreen'], alpha=0.6)

# Оформление графика
plt.title("Decision Boundary and Class Regions")
plt.xlabel("x1")
plt.ylabel("x2")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  # Горизонтальная ось
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)  # Вертикальная ось
plt.grid()
plt.show()
