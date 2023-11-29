import numpy as np
from matplotlib import pyplot as plt

c = np.arange(-10, 1.001, 0.25)
x = 3.67
y = np.power((2 * x - c), 0.6) + 0.567

print("Максимальное значение ", np.max(y))
print("Минимальное значение ", np.min(y))
print("Среднее значение ", np.mean(y))
print(" Отсортированные (по возрастанию) ", np.sort(y))
print("Количество элементов ", len(y))

plt.figure(figsize=(10, 10))
plt.plot(c, y, label='c', marker='o')
plt.xlabel('c')
plt.ylabel('l')
plt.grid(True)
plt.plot(c, np.full_like(c, np.mean(y)), "--", label='Среднее значение', marker='x')
plt.legend()
plt.show()
