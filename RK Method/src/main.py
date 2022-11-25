import pandas as pd
import numpy as np
import sys
import logging
from drawing import draw, draw_deviation

logging.getLogger().setLevel(logging.INFO)


def parsing_params() -> tuple:
    try:
        path = sys.argv[1]
    except IndexError as err:
        logging.error("\tYou forgot to enter a path. Program uses default path.\n")
        path = '../data/data.csv'

    try:
        data = pd.read_csv(path, header=None)
    except FileNotFoundError as err:
        logging.error("\tFile doesn't exist. Program uses default path.\n")
        path = '../data/data.csv'
        data = pd.read_csv(path, header=None)

    c_params = data.iloc[:-1, 0].values
    a_params = data.iloc[:-1, 1:]
    b_params = data.iloc[-1, 1:].values
    return a_params, b_params, c_params


def dUdX(x: float, u: tuple) -> np.array:
    """
    dUdX = f value = [U2, -U1 * cos(x)]
    """
    return np.array([u[1], -u[0] * np.cos(x)])
    # return np.array([u[1], -x * u[1] + np.exp(-x*x)])


def method(x0: float, h: float, initial_params: tuple, end: float,
           a_params: pd.DataFrame, b_params: list, c_params: list) -> np.array:
    start = x0

    count = int((end - x0) / h)
    u_values = []
    u = initial_params
    for i in range(count):
        k1 = dUdX(x0 + c_params[0] * h,
                  u)
        coef_k2 = a_params.iloc[1, 0] * k1
        k2 = dUdX(x0 + c_params[1] * h,
                  u + h * coef_k2)
        coef_k3 = a_params.iloc[2, 0] * k1 + a_params.iloc[2, 1] * k2
        k3 = dUdX(x0 + c_params[2] * h,
                  u + h * coef_k3)
        k = [k1, k2, k3]
        coefficient = np.array([0.0, 0.0])
        for num in range(3):
            coefficient += b_params[num] * k[num]
        u = u + h * coefficient
        x0 += h
        u_values.append(u)

    u_values = np.vstack(u_values)
    draw(u_values, start, end, h)
    return u_values


def main(start=0, end=10, initial_params=(1, 0)):
    a_params, b_params, c_params = parsing_params()

    all_y, x_points, y_points = [], [], []
    hs = [1/160, 1/80, 1/40, 1/20, 1/10, 1/5]

    for i, h in enumerate(hs):
        logging.info(f"\tStart method with h = {h}.")
        u_values = method(start, h, initial_params, end,
                          a_params, b_params, c_params)
        all_y.append(u_values[:, 1])
        if i > 0:
            x_points.append(int((end - start) / h))
            y_points.append(
                np.max(
                    abs(all_y[i] - all_y[i - 1][1::int(hs[i] / hs[i-1])])
                )
            )
    draw_deviation(x_points, y_points)

    mean_changing = 0
    for i in range(0, len(y_points)-1):
        mean_changing += y_points[i+1] / y_points[i]
    mean_changing /= len(y_points) - 1
    logging.info(f'\tMean changing = {mean_changing}')


main()
