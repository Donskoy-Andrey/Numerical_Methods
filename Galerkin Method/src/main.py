import numpy as np
import numpy.linalg as la
import logging
from classes import Phi, Params
from drawing import draw, draw_deviation


logging.getLogger().setLevel(logging.INFO)


def solve(interval: tuple, h: float, name: str = None):
    left, right = interval
    phi = Phi(left, right, h)
    params = Params(phi)
    size = phi.size

    x_v = np.linspace(left, right, size + 1)

    a_params = np.zeros((size - 1, size - 1))
    b_params = np.zeros((size - 1))

    for i in range(1, size - 1):
        for j in range(i - 1, i + 2):
            a_params[i - 1, j - 1] = params.a_params(i, j, x_v)

    a_params[size - 2, size - 2] = params.a_params(size - 1, size - 1, x_v)
    a_params[size - 2, size - 3] = params.a_params(size - 1, size - 2, x_v)

    for i in range(1, size):
        b_params[i - 1] = params.b_params(i, x_v)

    c_matrix = np.linalg.solve(a_params.T, b_params)

    y_v = []
    for x in x_v:
        y = 3 * x
        for i in range(0, len(c_matrix)):
            y = y + c_matrix[i] * phi.func(i, x, x_v)
        y_v.append(y)

    if name is not None:
        draw(left, right, x_v, y_v, name)
    return np.array(y_v)


def main(interval: tuple = (0, 1)):

    steps = [2**i for i in range(2, 8)]
    hs = [1/step for step in steps]

    res = []
    solves = []
    for h_index in range(len(hs)):
        logging.info(f"\tStart method with steps = {steps[h_index]}.")
        solves.append(solve(interval, hs[h_index], f'{steps[h_index]}'))

    for i in range(len(solves) - 1):
        res.append(
            max(
                abs(solves[i] - solves[i+1][::2])
            )
        )
    draw_deviation(steps[:-1], res)


main()



