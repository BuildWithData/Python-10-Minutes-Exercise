import os
import random


__doc__ = """

Write a program to play rock paper scissors

Next Steps:

    - refactor the program to make the player always lose

    - when playing multiple matches, display a recap board
    to keep track of how many games the player has won/lost
    in total

    - implement rock paper scissors lizard spock, as Sheldon explains:

        scissors cuts paper
        paper covers rock
        rock crushes lizard
        lizard poisons Spock
        Spock smashes scissors
        scissors decapitates lizard
        lizard eats paper
        paper disproves Spock
        Spock vaporizes rock
        and as it always has
        rock crushes scissors

    sources:

        https://the-big-bang-theory.com/rock-paper-scissors-lizard-spock/
        https://www.youtube.com/watch?v=x5Q6-wMx-K8

"""

IMAGE = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,

    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,

    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

COMPUTER_LOSE = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

player = None
game_is_on = True

while game_is_on:

    os.system("clear") # windows: cls

    while IMAGE.get(player) is None:
        player = input("Choose between Rock, Paper, Scissors: ").lower()

    computer = random.choice(list(IMAGE.keys()))

    print(IMAGE[player])
    print("Computer:", computer)
    print(IMAGE[computer])

    if player == computer:
        print("It's a tie")
    else:
        if COMPUTER_LOSE[player] == computer:
            print("You won !!!")
        else:
            print("You lost...")

    game_is_on = input("You wanna play again ? ").lower() == "yes"
    player = None
