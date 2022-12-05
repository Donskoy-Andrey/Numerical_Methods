import numpy as np
import matplotlib.pyplot as plt
import logging


def real_solution(x):
    return (
            -1 * np.exp(3 / 2 + np.sqrt(13)) * (x - 6) + np.exp(3 / 2) * (x - 6) +
            2 * np.exp(1 / 2 * (np.sqrt(13) - (np.sqrt(13) - 3) * x)) -
            6 * np.exp(-1 / 2 * (np.sqrt(13) - 3) * x + np.sqrt(13) + 3/2) +
            6 * np.exp(1 / 2 * ((3 + np.sqrt(13)) * x + 3)) -
            2 * np.exp(1 / 2 * ((3 + np.sqrt(13)) * x + np.sqrt(13)))
            ) / (np.exp(3 / 2) * (np.exp(np.sqrt(13)) - 1))


def draw(left: float, right: float, x_v: np.array, y_v: list, name: str) -> None:
    plt.figure()
    plt.title(f'Solution', c='black', size=20)
    xs = np.linspace(left, right, 1000)
    ys = [real_solution(x) for x in xs]
    plt.plot(xs, ys, c='r')
    plt.plot(x_v, y_v, c='black')
    plt.legend(['real', 'method'])
    plt.savefig(f'data/images/output-{name}.png')
    logging.info('\t\tSaved image')


def draw_deviation(steps: list, res: list) -> None:
    plt.figure()
    plt.title(f'Deviation', c='black', size=20)
    plt.plot(steps[::-1], res[::-1])
    plt.ylabel('Error value', size=15)
    plt.xlabel('Amount of steps', size=15)
    plt.grid()
    plt.savefig('data/images/deviation.png')