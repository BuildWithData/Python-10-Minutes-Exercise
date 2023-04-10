import os
import random


__doc__ = """

Write a program to challange the user to guess a series of words

Next steps:

    - load WORDS from a file
    - add score to WORDS based on their difficulty
    - use ASCII to improve what is displayed

"""

WORDS = {
    "HOME": "The place where you live...",
    "MARS": "Where Elon wants humanity to go...",
    "PARIS": "what's the capital of France ?"
}

score = 0

for expected, msg in WORDS.items():

    expected = expected.upper()
    indexes = list(range(len(expected)))
    show = []

    answer = None
    to_display = None

    header = f"Score: {score}\n"

    while to_display != expected and answer != expected:

        if answer is not None:
            i = random.choice(indexes)
            show.append(i)
            indexes = [el for el in indexes if el != i]

        to_display = "".join(["_" if i not in show else c for i, c in enumerate(expected)])
        os.system("clear")

        print(header)
        print(msg)
        print("\n", " " * 5, to_display)

        if len(indexes) > 0:
            answer = input("\nType your answer here: ").upper()

    score += len(indexes)

    if answer == expected:
        print(f"\nThat's right !!!! You got {score} points !!!")
    else:
        print("\nBad luck, you missed this !!!")

    input("\nPress ENTER to move to next word...")

print("\nThe game is over")
print("Final score:", score)
