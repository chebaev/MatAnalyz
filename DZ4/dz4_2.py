import math

import matplotlib.pyplot as plt
import numpy as np

# 2) Построить график функции:
# а) y = x^2 + 4x + 3;

# x = np.linspace(-40, 40, 10000)
# y = x ** 2 + 4 * x + 3
# ind = y >= 0
# x1 = x[ind]
# y1 = y[ind]
# x2 = x[~ind]
# y2 = y[~ind]
# plt.figure(1)
# plt.title('График функции |y| = x^2 + 4x + 3')
# plt.ylabel('Ось y')
# plt.xlabel('Ось x')
# plt.grid()
# plt.axis([-10, 16, -10, 10])
# plt.scatter(x1, y1, s=1, c='b')
# plt.scatter(x1, -y1, s=1, c='b')
# plt.plot(x2, y2, 'r--')
# plt.plot(x2, -y2, 'r--')
# plt.show()


x = np.linspace(-40, 40, 10000)
y = -2 * math.sin((3*x))
ind = y >= 0
x1 = x[ind]
y1 = y[ind]
x2 = x[~ind]
y2 = y[~ind]
plt.figure(1)
plt.title('График функции |y| = x^2 + 4x + 3')
plt.ylabel('Ось y')
plt.xlabel('Ось x')
plt.grid()
plt.axis([-10, 16, -10, 10])
plt.scatter(x1, y1, s=1, c='b')
plt.scatter(x1, -y1, s=1, c='b')
plt.plot(x2, y2, 'r--')
plt.plot(x2, -y2, 'r--')
plt.show()