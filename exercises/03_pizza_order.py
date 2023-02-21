
__doc__ = """

Write a program that:

    - display the menu
    - take order from customer
    - display total

Next Steps:

    - format the menu

    -----------------------            -----------------------
             MENU                               MENU
    -----------------------            -----------------------

     margherita 6.5$                     margherita     6.5$
     pepperoni 9.0$                      pepperoni      9.0$
     hawaiian 10.0$            ->        hawaiian      10.0$
     ham & cheese 8.0$                   ham & cheese   8.0$
     cheese 7.0$                         cheese         7.0$

    -----------------------            -----------------------

    - format the receipt

    - add drinks

    - when asking for 'anything else ?' user can exit by typing
    either No or no. Refactor to make it more robust, here are
    some examples of how it should work:

        'nope' -> exit
        'yes' ->  keep asking
        'yufuuu' -> display 'sorry, can you say it again ?'

"""

MENU = {
    "cheese": 7.0,
    "pepperoni": 8.0,
    "hawaiian": 10.0,
    "margherita": 6.0,
    "ham": 8.0
}

msg = "-----------------------\n"
msg += "         MENU\n"
msg += "-----------------------\n\n"

for flavor, price in MENU.items():
    msg += " " + flavor + " " + str(price) + "$\n"

msg += "\n-----------------------\n\n"
msg += "Welcome to Python Pizza !!!"
print(msg)

order = {flavor: 0 for flavor in MENU}
checkout = False

while checkout is False:
    pizza = input("Which pizza would you like ? ")

    if MENU.get(pizza) is not None:
        n = int(input("How many ? "))
        order[pizza] += n
    else:
        print("Sorry we don't have that")

    checkout = input("Anything else ? ").lower() == "no"

msg = "Thanks, here is your total:\n\n"
msg += "-----------------------\n"
msg += "       RECEIPT\n"
msg += "-----------------------\n\n"

total = 0

for flavor, n in order.items():
    if n > 0:
        total_price = MENU[flavor] * n
        total += total_price
        msg += " " + str(n) + " " + flavor + " " + str(total_price) + "$\n"

msg += "\n-----------------------\n"
msg += "TOTAL: " + str(total) + "$"
print(msg)
