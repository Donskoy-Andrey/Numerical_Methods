import matplotlib.pyplot as plt
import numpy as np
import logging


def draw(all_x, all_y, h, euler_y):
    def real_function(x):
        return -x**2 - 2 * x + 3 * np.exp(x) - 2

    x_real = np.linspace(min(all_x), max(all_x), 1000)
    y_real = [
        real_function(x) for x in x_real
    ]
    plt.figure(figsize=(5, 5))
    plt.title(f'Solution with h = {h}', size=20)
    plt.plot(all_x, all_y, c='black')
    plt.plot(x_real, y_real, c='red')
    plt.plot(all_x, euler_y, c='blue')
    plt.legend(['Adam', 'Real', 'Euler'], prop={'size': 10})
    plt.savefig(f'data/images/output-{h}.png')
    logging.info('\tImage saved.\n')


def draw_deviation(x_points: list, y_points: list, y_points_euler: list) -> None:
    fig, axs = plt.subplots(1, 2, figsize=(20, 10))
    for i in range(2):
        axs[i].set_ylabel('Error value', size=30)
        axs[i].set_xlabel('Amount of steps', size=30)

    axs[0].plot(x_points, y_points, c='black')
    axs[0].scatter(x_points, y_points, c='black')

    axs[0].plot(x_points, y_points_euler, c='blue')
    axs[0].scatter(x_points, y_points_euler, c='blue')

    axs[0].set_title('Standard graph', size=35)
    axs[0].legend(['Adam', '', 'Euler', ''])

    axs[1].plot(x_points, np.log(y_points), c='red')
    axs[1].scatter(x_points, np.log(y_points), c='red')

    axs[1].plot(x_points, np.log(y_points_euler), c='blue')
    axs[1].scatter(x_points, np.log(y_points_euler), c='blue')

    axs[1].set_title('Log graph', size=35)

    axs[1].legend(['Adam', '', 'Euler', ''])
    plt.savefig('data/images/deviation.png')
    logging.info(f"\tDeviation image saved.")