from drawing import draw, draw_deviation
import logging
import numpy as np

logging.getLogger().setLevel(logging.INFO)
eps = 0.0000001


def dYdX(x, y):
    """ y' = y + x^2 """
    return y + x**2


def method(start: float, h: float, initial_params: float, end: float) -> tuple:
    def ySolver(l: int, h: float) -> float:
        return 1 + l * h + ((l * h) ** 2) / 2 + 3.2*2 * ((l * h) ** 3) / 6

    count = int((end - start) / h) + 1
    steps = np.linspace(start, end, count)

    all_y = []

    yValues = [initial_params,
               ySolver(1, h),
               ySolver(2, h),
               ySolver(3, h)]

    all_y.extend(yValues[:-1])

    for step in steps[3:]:
        yPredicted = yValues[-1] + h / 24 * (
                55 * dYdX(step, yValues[-1])
                - 59 * dYdX(step - 1 * h, yValues[-2])
                + 37 * dYdX(step - 2 * h, yValues[-3])
                - 9 * dYdX(step - 3 * h, yValues[-4])
        )

        yValues.append(yPredicted)
        yBiased = 0

        while abs(yPredicted - yBiased) > eps:
            yPredicted = yBiased
            yBiased = yValues[-2] + h / 24 * (
                    9 * dYdX(step + 1 * h, yValues[-1])
                    + 19 * dYdX(step + 0 * h, yValues[-2])
                    - 5 * dYdX(step - 1 * h, yValues[-3])
                    + 1 * dYdX(step - 2 * h, yValues[-4])
            )

        yValues = yValues[:-1] + [yBiased]
        all_y.append(yValues[-1])
    return steps, all_y


def main(start=0, end=10, initial_params=1):
    hs = [1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2]

    x_points, y_points = [], []
    measures = []

    for i, h in enumerate(hs):
        logging.info(f'\tProcessing with h = {h}')
        all_x, all_y = method(start, h, initial_params, end)
        draw(all_x, all_y, h)
        measures.append(all_y)

        if i > 0:
            x_points.append(int((end - start) / hs[i - 1]) + 1)
            y_points.append(
                np.max(
                    abs(np.array(measures[i]) - np.array(measures[i - 1])[::int(hs[i] / hs[i-1])])
                )
            )

    mean_changing = 0
    for i in range(0, len(y_points) - 1):
        mean_changing += y_points[i + 1] / y_points[i]
    mean_changing /= len(y_points) - 1
    logging.info(f'\tMean changing = {mean_changing}')
    draw_deviation(x_points, y_points)


main()
