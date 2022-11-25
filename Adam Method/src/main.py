from drawing import draw
import logging

logging.getLogger().setLevel(logging.INFO)


def dYdX(x, y):
    """ y' = y + x^2 """
    return y + x**2


def delta(x, yValues, h, delta_num):
    fCurrent = dYdX(x, yValues[-1])
    fMinus1 = dYdX(x - 1 * h, yValues[-2])
    fMinus2 = dYdX(x - 2 * h, yValues[-3])
    fMinus3 = dYdX(x - 3 * h, yValues[-4])

    return [fCurrent - fMinus1,
            fCurrent - 2 * fMinus1 + fMinus2,
            fCurrent - 3 * fMinus1 + 3 * fMinus2 - fMinus3][delta_num-1]


def method(start: float, h: float, initial_params: float, end: float) -> tuple:
    def ySolver(l: int, h: float) -> float:
        return 1 + l * h + ((l * h) ** 2) / 2 + 4 * ((l * h) ** 3) / 6

    steps = int((end - start) / h)
    x = start

    all_x, all_y = [], []

    yValues = [initial_params,
               ySolver(1, h),
               ySolver(2, h),
               ySolver(3, h)]

    all_x.extend([x, x+h, x+2*h])
    all_y.extend(yValues[:-1])

    x += 3 * h

    for step in range(3, steps + 1):
        fCurrent = dYdX(x, yValues[-1])
        yPredicted = yValues[-1] + h * (
                fCurrent
                + 1 * delta(x, yValues, h, delta_num=1) / 2
                + 5 * delta(x, yValues, h, delta_num=2) / 12
                + 3 * delta(x, yValues, h, delta_num=3) / 8)

        yValues.append(yPredicted)
        fNext_predicted = dYdX(x + h, yValues[-1])

        yBiased = yValues[-2] + h * (
                fNext_predicted
                - delta(x + h, yValues, h, delta_num=1) / 2
                - delta(x + h, yValues, h, delta_num=2) / 12
                - delta(x + h, yValues, h, delta_num=3) / 24)
        yValues.append(yBiased)

        x += h
        all_x.append(x)
        all_y.append(yValues[-1])
    return all_x, all_y


def main(start=0, end=10, initial_params=0):
    hs = [1, 0.5, 0.2, 0.01]

    for h in hs:
        logging.info(f'\tProcessing with h = {h}')
        all_x, all_y = method(start, h, initial_params, end)
        draw(all_x, all_y, h)


main()
