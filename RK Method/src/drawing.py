import matplotlib.pyplot as plt
import numpy as np
import logging


def draw(u_values: np.array, start: float, end: float, h: float) -> None:
    count = int((end - start) / h)
    x_values = np.linspace(start, end, count)

    fig, axs = plt.subplots(1, 2, figsize=(20, 10))
    fig.suptitle(f'Solution with h = {h}', c='black', size=40)
    axs[0].plot(x_values, u_values[:, 0], c='black')
    axs[0].legend(['y (x)'], prop={'size': 20})
    axs[1].plot(u_values[:, 0], u_values[:, 1], c='red')
    axs[1].legend(['y\' (y)'], prop={'size': 20})
    plt.savefig(f'data/images/output-{h}.png')
    logging.info(f"\tImage saved.\n")


def draw_deviation(x_points: list, y_points: list) -> None:
    fig, axs = plt.subplots(1, 2, figsize=(20, 10))
    for i in range(2):
        axs[i].set_ylabel('Error value', size=30)
        axs[i].set_xlabel('Amount of steps', size=30)

    axs[0].plot(x_points, y_points, c='black')
    axs[0].set_title('Standard graph', size=35)
    axs[1].plot(np.log(x_points), np.log(y_points), c='red')
    axs[1].set_title('Log graph', size=35)
    plt.savefig('data/images/deviation.png')
    logging.info(f"\tDeviation image saved.")