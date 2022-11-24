import random
from os.path import exists

N = 10


def main():
    path = "data/data.txt"
    if not exists(path):
        raise Exception(f'File {path} not found. Correct path.')
    coordinates = []

    with open(path, 'w') as file:
        amount = N
        for i in range(amount):
            while True:
                x = random.randint(0, N)  # [0; N]
                y = random.randint(0, N)  # [0; N]
                if x not in coordinates:
                    coordinates.append(x)
                    break
            string = f'{x} {y}\n'
            file.write(string)


if __name__ == "__main__":
    main()