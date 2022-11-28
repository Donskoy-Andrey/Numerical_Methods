import math

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return 9*x+3*y

y0 = 0


def adams(a, b, n):
    h = abs(a-b)/n
    x = [h * i for i in range(0, n+1)]
    res = [y0, 9/2*(h**2) + 27/6*(h**3), 18*(h**2) + 4*27/3*(h**3), 81/2*(h**2)+27*27/6*(h**3)]
    for i in range(3, n):
        f1 = f(x[i], res[i])
        deltaf1 = f1 - f(x[i-1], res[i-1])
        deltaf2 = f1 - 2 * f(x[i-1], res[i-1]) + f(x[i-2], res[i-2])
        deltaf3 = f1 - 3 * f(x[i-1], res[i-1]) + 3*f(x[i-2], res[i-2]) - f(x[i-3], res[i-3])
        res.append(res[i] + h*(f1 +1/2*deltaf1 +5/12*deltaf2 +3/8*deltaf3))
        # y_next = res[i] + h*(f1 +1/2*deltaf1 +5/12*deltaf2 +3/8*deltaf3)
        # res.append(res[i] + h*(f(x[i+1], y_next) + +1/2*deltaf1 +1/12*deltaf2 - 1/24*deltaf3))
    return [x, res]


# x, res = adams(0, 1, 1000)

N = [2**i for i in range(4, 10)]
print(N)
results = []
for i in range(0, len(N)-1):
    #ans = [1*(-1 + math.exp(3*arg) - 3*arg) for arg in ]
    results.append(abs(max(adams(0, 1, N[i])[1]) - max(adams(0, 1, N[i+1])[1])))
print('test: ', [results[i] / results[i+1] for i in range(len(results[::-2]))])
print(results)
plt.plot([N[i] for i in range(0, len(N)-1)], results, color='b')
# plt.plot([N[i] for i in range(0, len(N)-1)], [250/(N[i]**3) for i in range(0, len(N)-1)], linestyle='dashed', color='g')
# plt.plot(x, res, color='b')
# plt.plot(x, [1*(-1 + math.exp(3*arg) - 3*arg) for arg in x], color='g')
#plt.axis([-5,255, -1e-10, 1e-10])
plt.grid()
# plt.show()
