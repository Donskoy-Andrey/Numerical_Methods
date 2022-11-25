import matplotlib.pyplot as plt
import numpy as np
import logging


def draw(all_x, all_y, h):
    def real_function(x):
        y = -x**2 - 2 * x + 3 * np.exp(x) - 2
        return y

    x_real = np.linspace(min(all_x), max(all_x), 1000)
    y_real = [
        real_function(x) for x in x_real
    ]
    plt.figure(figsize=(10, 10))
    plt.title(f'Solution with h = {h}', size=20)
    plt.plot(all_x, all_y, c='black')
    plt.plot(x_real, y_real, c='red')
    plt.legend(['fake', 'real'], prop={'size': 20})
    plt.savefig(f'data/images/output-{h}.png')
    logging.info('\tImage saved.\n')