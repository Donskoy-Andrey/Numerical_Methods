import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def read_file(path: str = "data.txt") -> tuple:
    xs, ys = [], []
    info = None
    with open(path, 'r') as file:
        for line in file.readlines():
            try:
                x, y = line.strip().split()
                xs.append(float(x))
                ys.append(float(y))
            except Exception as err:
                info = f"Invalid Data Error: {repr(err)}"
                return None, None, None, None, info

    try:
        k = int(sys.argv[1])
    except Exception as err:
        info = f"Params Error: {repr(err)}"
        k = None

    assert len(xs) == len(ys)
    return xs, ys, len(xs), k, info


def draw(xs: list, ys: list, x_points: list, y_points: list) -> None:
    plt.figure(figsize=(10, 10))
    sns.lineplot(x=xs, y=ys, alpha=0.3, c='black', legend=True)
    sns.lineplot(x=x_points, y=y_points, alpha=0.5, c='orange', legend=True)
    plt.legend(title='Data Label', loc='upper left', labels=['standard line', None, 'polynom line'])
    sns.scatterplot(x=xs, y=ys, c='r', s=80, legend=False)
    plt.grid(True)
    try:
        plt.savefig(sys.argv[3])
    except IndexError:
        plt.savefig('data/images/image.png')


def algorithm(xs: list, ys: list, k: int):
    x = np.array(xs)[:, None]
    y = np.array(ys)[:, None]

    x_matrix = np.array(np.power(x, 0))
    for i in range(1, k + 1):
        x_matrix = np.hstack((x_matrix, np.power(x, i)))

    b = np.linalg.inv(x_matrix.T @ x_matrix) @ x_matrix.T @ y

    x_points = np.linspace(min(x), max(x), 50)[:, 0]
    y_points = []
    for i in x_points:
        current_x = np.array([i ** power for power in range(k + 1)])
        y_points.append(np.dot(current_x, b).item())
    draw(xs, ys, x_points, y_points)


def main():
    try:
        data_path = sys.argv[2]
    except IndexError:
        data_path = r"data/data.txt"
    xs, ys, n, k, info = read_file(data_path)
    if info is not None:
        print(info)
        return

    if not (n >= k+1):
        '''
        Для построения регрессии полиномом k-й степени необходимо, 
        по крайней мере, (k+1) точек данных.
        '''
        raise Exception("Not Enough Data.")

    algorithm(xs, ys, k)


if __name__ == "__main__":
    main()
