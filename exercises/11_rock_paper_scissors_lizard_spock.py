import os
import random


def get_images_next_to_each_other(left: str, right: str, l_label: str, r_label: str) -> str:

    SCREEN_WIDTH = os.get_terminal_size().columns

    out = []

    l_image = IMAGE[left].split("\n")
    r_image = IMAGE[right].split("\n")

    n_left = [len(l) for l in l_image]
    n_right = [len(l) for l in r_image]

    for n in range(max(len(n_left), len(n_right))):

        try:
            l = l_image[n]
        except IndexError:
            l = ""

        l += " " * (SCREEN_WIDTH // 2 - len(l))

        try:
            l += r_image[n]
        except IndexError:
            l += ""

        l = "".join(l)

        out.append(l)

    out.append(" ")

    footer = l_label + ": " + left
    footer += " " * (SCREEN_WIDTH // 2 - len(footer))
    footer += r_label + ": " + right
    out.append(footer)

    out.append(" ")

    out = "\n".join(out)

    return out


__doc__ = """

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
    """,

    "lizard": """
               _.--._       /|
             .'()..()`.    / /
            ( `-.__.-' )  ( (
             \        /    \ \ 
              \      /      ) )
            .' -.__.- `.-.-'_.'
          .'  /-____-\  `.-'
          \  /-.____.-\  /-.
           \ \`-.__.-'/ /\|\|
          .'  `.    .'  `.
          |/\/\|    |/\/\|
    """,

    "spock": """
               __---###---__
            _-""###########""-_
          .'###################'.
         /#######################
        |###____###########____###|
       |#| --.._           _..-- |#|
  .'\ |##|  '-._'-._   _.-'_.-'  |##| /'.
  |  \|#|    .--'-_'   '_-'--.    |#|/  |
   \  |#|   '._o.'       '.o_.'   |#|  /
    \                                 /
      |                             |
       |         ._     _.         |
        \      /   '___'   \      /
         \    |             |    /
          |   | ___________ |   |
           | |   _________   | |
            | |             | |
            '. |           | .'        .
              \             /  ..    .| |
              |'.         .'| .\ \  | | |
      _______/ '.'-_____-'.'  \ \ \ | | |
    .'_______/    '-----'      \ \ \| | |
   /                            \   '    |
  |      |                 .'-_  |       |
 |      |                   '. ''         |
 |      |                     '-._       |
|      |                          '-.__.'
|______|___________________________|_____\_
    """
}

COMPUTER_LOSE = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "spock": ["rock", "scissors"],
    "lizard": ["paper", "spock"],
}

player = None
game_is_on = True

while game_is_on:

    os.system("clear") # windows: cls

    while IMAGE.get(player) is None:
        player = input("Choose between Rock, Paper, Scissors, Lizard, Spock: ").lower()

    computer = random.choice(list(IMAGE.keys()))

    image = get_images_next_to_each_other(player, computer, "You", "Computer")

    print(image)

    if player == computer:
        print("It's a tie")
    else:
        if computer in COMPUTER_LOSE[player]:
            print("You won !!!")
        else:
            print("You lost...")

    game_is_on = input("You wanna play again ? ").lower() == "yes"
    player = None
