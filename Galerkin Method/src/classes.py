import logging


class Phi:
    def __init__(self, left: float, right: float, h: float):
        logging.info('\t\tCreated class Phi')
        self.left = left
        self.right = right
        self.h = h
        self.size = int((self.right - self.left) / self.h)

    def func(self, num: int, x: float, v: list) -> float:
        x_left, x_centered, x_right = v[num - 1], v[num], v[num + 1]
        if (x <= x_left) or (x >= x_right):
            return 0
        if x_left < x <= x_centered:
            return (x - x_left) / self.h
        if x_centered < x < x_right:
            return (x_right - x) / self.h

    def derivative_1(self, num: int, x: float, v: list) -> float:
        x_left, x_centered, x_right = v[num - 1], v[num], v[num + 1]
        if (x <= x_left) or (x >= x_right):
            return 0
        if x_left < x <= x_centered:
            return 1 / self.h
        if x_centered < x < x_right:
            return -1 / self.h

    def derivative_2(self, num: int, x: float, v: list) -> float:
        return 0

    def integrate(self, f) -> float:
        n = 4000
        h = (self.right - self.left) / n
        xi = self.left
        result = 0
        result = result + f(xi) / 2 * h
        for i in range(1, n - 1):
            xi = xi + h
            result = result + f(xi) * h
        xi = self.right
        result = result + f(xi) / 2 * h
        return result


class Params:
    def __init__(self, phi: Phi):
        logging.info('\t\tCreated class Params')
        self.phi = phi

    def a_params(self, i, j, x_v):
        f = lambda x: (
                -1 * self.phi.derivative_1(i, x, x_v) * self.phi.derivative_1(j, x, x_v) +
                -3 * self.phi.derivative_1(i, x, x_v) * self.phi.func(j, x, x_v) +
                -1 * self.phi.func(i, x, x_v) * self.phi.func(j, x, x_v)
        )
        return self.phi.integrate(f)

    def b_params(self, i, x_v):
        f = lambda x: (4 * x + 6) * self.phi.func(i, x, x_v)
        return self.phi.integrate(f)
