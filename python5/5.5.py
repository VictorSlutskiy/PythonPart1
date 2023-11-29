import numpy as np
from matplotlib import pyplot as plt

x, y = np.meshgrid(np.linspace(0, 10, 20), np.linspace(0, 10, 20))
z1 = np.power(x, 0.25) + np.power(y, 0.25)
z2 = np.power(x, 2) - np.power(y, 2)
z3 = 2 * x + 3 * y
z4 = np.power(x, 2) + np.power(y, 2)
z5 = 2 + 2 * x + 2 * y - np.power(x, 2) - np.power(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z1, label='z1')
ax.plot_surface(x, y, z2, label='z2')
ax.plot_surface(x, y, z3, label='z3')
ax.plot_surface(x, y, z4, label='z4')
ax.plot_surface(x, y, z5, label='z5')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.legend()
plt.show()