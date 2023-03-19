import math
import os
import random


__doc__ = """

Write a program to roll dices with 6 faces by:

    - asking number of rolls
    - displaying each roll next to each other

Next steps:

    - what happens if when asked how many rolls the user
    types in a character ? make the code more resilient

    - add different types of dice

"""

FACES = {

    1: [
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"
    ],
    2: [
            "┌─────────┐",
            "│    ●    │",
            "│         │",
            "│    ●    │",
            "└─────────┘",
    ],
    3: [
            "┌─────────┐",
            "│ ●       │",
            "│    ●    │",
            "│       ● │",
            "└─────────┘",
    ],
    4: [
            "┌─────────┐",
            "│ ●     ● │",
            "│         │",
            "│ ●     ● │",
            "└─────────┘",
    ],
    5: [
            "┌─────────┐",
            "│ ●     ● │",
            "│    ●    │",
            "│ ●     ● │",
            "└─────────┘",
    ],
    6: [
            "┌─────────┐",
            "│ ●     ● │",
            "│ ●     ● │",
            "│ ●     ● │",
            "└─────────┘",
    ]
}

n_rolls = int(input("How many dices would you like to roll ? "))

rolls = [random.randint(1, 6) for _ in range(n_rolls)]

screen_width = os.get_terminal_size().columns
max_dices_per_row = math.floor(screen_width / (11 + 1))
n_rows = math.ceil(n_rolls / max_dices_per_row)

for row in range(n_rows):
    result = ""
    first = max_dices_per_row * row
    next_first = first + max_dices_per_row

    for line in range(5):
        for roll in rolls[first:next_first]:
            result += FACES[roll][line]
            result += " "

        result += "\n"

    print(result)
