from drawing import draw, draw_deviation
import logging
import numpy as np

logging.getLogger().setLevel(logging.INFO)


def dYdX(x, y):
    """ y' = y + x^2 """
    return y + x**2


def delta(x: float, yValues: list, h: float, delta_num: int) -> float:
    fCurrent = dYdX(x, yValues[-1])
    fMinus1 = dYdX(x - 1 * h, yValues[-2])
    fMinus2 = dYdX(x - 2 * h, yValues[-3])
    fMinus3 = dYdX(x - 3 * h, yValues[-4])

    return [fCurrent - fMinus1,
            fCurrent - 2 * fMinus1 + fMinus2,
            fCurrent - 3 * fMinus1 + 3 * fMinus2 - fMinus3][delta_num-1]


def euler(start: float, h: float, initial_params: float, end: float) -> list:
    count = int((end - start) / h) + 1
    steps = np.linspace(start, end, count)
    euler_y = [initial_params]
    for step in steps[1:]:
        euler_y.append(euler_y[-1] + h * dYdX(step - h, euler_y[-1]))
    return euler_y


def adam(start: float, h: float, initial_params: float, end: float) -> tuple:
    def ySolver(l: int, h: float) -> float:
        return 1 + l * h + ((l * h) ** 2) / 2 + 3 * ((l * h) ** 3) / 6

    count = int((end - start) / h) + 1
    steps = np.linspace(start, end, count)
    all_y = []

    yValues = [initial_params,
               ySolver(1, h),
               ySolver(2, h),
               ySolver(3, h)]

    all_y.extend(yValues)

    for step in steps[3:-1]:
        fCurrent = dYdX(step, yValues[-1])
        yPredicted = yValues[-1] + h * (
                fCurrent
                + 1 * delta(step, yValues, h, delta_num=1) / 2
                + 5 * delta(step, yValues, h, delta_num=2) / 12
                + 3 * delta(step, yValues, h, delta_num=3) / 8)

        yValues.append(yPredicted)
        fNext_predicted = dYdX(step + h, yValues[-1])

        yBiased = yValues[-2] + h * (
                fNext_predicted
                - delta(step + h, yValues, h, delta_num=1) / 2
                - delta(step + h, yValues, h, delta_num=2) / 12
                - delta(step + h, yValues, h, delta_num=3) / 24)

        yValues = yValues[:-1] + [yBiased]
        all_y.append(yValues[-1])
    euler_y = euler(start, h, initial_params, end)
    return steps, all_y, euler_y


def main(start=0, end=10, initial_params=1):
    hs = [1/2**i for i in range(8, 0, -1)]

    x_points, y_points = [], []
    measures = []
    measures_euler = []
    y_points_euler = []

    for i, h in enumerate(hs):
        logging.info(f'\tProcessing with h = {h}')
        all_x, all_y, eiler_y = adam(start, h, initial_params, end)

        draw(all_x, all_y, h, eiler_y)
        measures.append(all_y)
        measures_euler.append(eiler_y)

        if i > 0:
            x_points.append(int((end - start) / hs[i - 1]) + 1)
            y_points.append(
                np.max(
                    abs(np.array(measures[i]) - np.array(measures[i - 1])[::int(hs[i] / hs[i-1])])
                )
            )
            y_points_euler.append(
                np.max(
                    abs(np.array(measures_euler[i]) - np.array(measures_euler[i - 1])[::int(hs[i] / hs[i-1])])
                )
            )

    changing_adam = []
    changing_euler = []
    for i in range(len(y_points) - 1, 0, -1):
        changing_adam.append(y_points[i] / y_points[i - 1])
        changing_euler.append(y_points_euler[i] / y_points_euler[i - 1])

    logging.info(f'\tAdam changing = {changing_adam}')
    logging.info(f'\tEuler changing = {changing_euler}')
    draw_deviation(x_points, y_points, y_points_euler)


main()
