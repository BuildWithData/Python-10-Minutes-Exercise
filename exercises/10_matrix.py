import math
import os
import random
import time


__doc__ = """

Write a program to display the matrix rain

Next steps:

    - change probability function

    - increase number of frames per second

"""


DARK_GREEN = "\033[00;32m"
LIGHT_GREEN = "\033[01;32m"
BLACK = "\033[00;30m"

n_columns = os.get_terminal_size().columns // 2 # japanese characters are 2 column wide
n_rows = os.get_terminal_size().lines

CHARACTERS = [chr(12446 + i) for i in range(96)]

count = [0 for _ in range(n_columns)]
colors = []

while True:

    rows = [[random.choice(CHARACTERS) for _ in range(n_columns)] for _ in range(n_rows)]

    new_colors = []

    for i in range(n_columns):

        a = 0.1
        probability = round(math.exp(- 1 / abs(a * count[i])) * 100 if count[i] != 0 else 0)

        if count[i] <= 0:
            bag = [LIGHT_GREEN if n < probability else BLACK for n in range(100)]
        else:
            bag = [BLACK if n < probability else DARK_GREEN for n in range(100)]

        color = random.choice(bag)

        if color == LIGHT_GREEN:
            count[i] = 1
        elif color == DARK_GREEN:
            count[i] += 1
        else:
            if count[i] < 0:
                count[i] -= 1
            else:
                count[i] = -1

        new_colors.append(color)

    colors.append(new_colors)

    if len(colors) > n_rows:
        colors = colors[1:]

    os.system("clear") # windows: cls

    for r, r_c in zip(rows, reversed(colors)):
        for c, c_c in zip(r, r_c):
            print(c_c, c, end="", sep="", flush=True)
    time.sleep(0.2)
