from datetime import datetime
from datetime import timedelta
import os
from time import sleep


__doc__ = """

Write a clock app to display the time of your local timezone

Next steps:

    - can you write make it work without using timedelta ?

    - are we really sure the parse function is always gonna work ?

    - change numbers in NUMBERS

"""


def parse(raw):
    """
    Strips external empty spaces out
    """
    out = raw
    if isinstance(raw, str):
        out = [out]

    out = [[line.lstrip() for line in n.split("\n")] for n in out]
    max_len = [max([len(line.rstrip()) for line in n]) for n in out]
    out = [[" " * (m - len(line)) + line[:m] for line in n] for n, m in zip(out, max_len)]
    out = ["\n".join(lines) for lines in out]

    if isinstance(raw, str):
        out = out[0]

    return out


def convert_to_bigger_numbers(number):
    out = []
    for digit in str(number):
        if number < 10:
            out += [NUMBERS[0]]
        out += [NUMBERS[int(digit)]]
    return out


SEPARATOR = """

        ██

        ██

"""

NUMBERS = [
    """
         ████████
         ██    ██
         ██    ██
         ██    ██
         ████████
    """,

    """
         ██
         ██
         ██
         ██
         ██
    """,

    """
        ██████
            ██
        ██████
        ██    
        ██████
    """,

    """
        ██████
            ██
         █████
            ██
        ██████
    """,

    """
        ██   ██
        ██   ██
        ███████
             ██
             ██
    """,

    """
        ███████
        ██     
        ███████
             ██
        ███████
    """,

    """
        ███████
        ██     
        ███████
        ██   ██
        ███████
    """,

    """
        ███████
             ██
             ██
             ██
             ██
    """,

    """
        ███████
        ██   ██
        ███████
        ██   ██
        ███████
    """,

    """
        ███████
        ██   ██
        ███████
             ██
        ███████
    """
]

NUMBERS = parse(NUMBERS)
SEPARATOR = parse(SEPARATOR)

d = datetime.today()

while True:

    os.system("clear") # windows: cls
    time = []

    time += convert_to_bigger_numbers(d.hour)
    time.append(SEPARATOR)

    time += convert_to_bigger_numbers(d.minute)
    time.append(SEPARATOR)

    time += convert_to_bigger_numbers(d.second)

    screen_height = int(os.get_terminal_size().lines)
    screen_width = int(os.get_terminal_size().columns)

    number_height = len(NUMBERS[0].split("\n"))
    number_width = max([len(n.split("\n")[0]) for n in NUMBERS])
    distance_btw_numbers = number_width // 2

    display = "\n" * ((screen_height - number_height) // 2)

    for line in range(number_height):

        display += " " * ((screen_width - (number_width + distance_btw_numbers) * 6) // 2)

        for t in time:
            display += t.split("\n")[line]
            display += " " * distance_btw_numbers

        display += "\n"

    print(display)

    sleep(1)

    d += timedelta(seconds=1)
