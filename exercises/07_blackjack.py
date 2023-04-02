import os
import random


__doc__ = """

Write a program to play a simplified version of blackjack:

    - one single player vs dealer
    - ace counts 1
    - no money

Next steps:

    - add money
    - soft hand: add the option to count aces either as one or as 11
    - add splitting pairs
    - add doubling down

"""


def get_image(card, face_down=False):

    NUMBER2SIGN = {
        11: "J",
        12: "Q",
        13: "K",
        1 : "A"
    }

    number, suit = card["number"], card["suit"]

    if number not in range(2, 11):
        number = NUMBER2SIGN[number]

    if face_down is True:
        number, suit = "#", "#"

    card = []

    card += ["┌─────┐"]

    card += ["│{}    ".format(number)]
    if number == 10:
        card[-1] = card[-1][:-1]
    card[-1] += "│"

    card += ["│  {}  │".format(suit)]

    card += ["│   "]
    if number == 10:
        card[-1] = card[-1][:-1]
    card[-1] += " {}│".format(number)

    card += ["└─────┘"]

    return card


def display_cards(cards):
    row = ""
    for line in range(5):
        for card in cards:
            row += card[line]
            row += " "
        row += "\n"
    print(row)


def get_card():

    HEARTS = chr(9829)
    DIAMONDS = chr(9830)
    SPADES = chr(9824)
    CLUBS = chr(9827)

    return {
        "number": random.randint(1, 13),
        "suit": random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
    }


player_lost = None
dealer_playing = False

player = [get_card() for _ in range(2)]
dealer = [get_card() for _ in range(2)]

while player_lost is None:

    os.system("clear") # windows: cls

    player_score = sum([card["number"] if card["number"] < 11 else 10 for card in player])
    dealer_score = sum([card["number"] if card["number"] < 11 else 10 for card in dealer])

    if player_score > 21:
        player_lost = True

    elif dealer_playing is True and (dealer_score >= 17 or dealer_score >= player_score):
        if dealer_score > 21:
            player_lost = False
        else:
            player_lost = dealer_score >= player_score


    if dealer_playing is False:
        images = [get_image(dealer[0]), get_image(dealer[1], face_down=True)]
    else:
        images = [get_image(card) for card in dealer]
    print("Dealer: ", dealer_score if dealer_playing is True else "???")
    display_cards(images)

    images = [get_image(card) for card in player]
    print("Player: ", player_score)
    display_cards(images)


    if player_lost is None:
        action = None

        while action not in ["H", "S"] and dealer_playing is False:
            action = input("[H]it, [S]tand: ").upper()

        if dealer_playing is True:
            action = "H"
            input("Press ENTER...")

        if action == "H":
            if dealer_playing is True:
                dealer.append(get_card())
            else:
                player.append(get_card())

        if action == "S":
            dealer_playing = True


if player_lost is False:
    print("Congrats you won !!!")
else:
    print("Dealer won...")
