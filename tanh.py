import numpy as np
import matplotlib.pyplot as plt
from hyperbolic import sinh, cosh, tanh

# Диапазон x
x = np.linspace(-5, 5, 500)

# Вычисление tanh(x)
y_tanh = tanh(x)

# Построение графика tanh(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y_tanh, label=r"$\tanh(x)$", color='blue', linewidth=2)

# Оформление графика
plt.title("График гиперболического тангенса", fontsize=16)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.xlabel("x", fontsize=14)
plt.ylabel(r"$\tanh(x)$", fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()
