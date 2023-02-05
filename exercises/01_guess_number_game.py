from random import randint

__doc__ = """

Write a program that:

    - pick a number between 0 and 100
    - ask the user to guess it
    - cheer the user when guess is right
    - hint if next guess should be higher/lower than pvs one

Next steps:

    - count number of attempts
    - limit user to guess X attempts
    - count how many attempts are left after each guess

"""

number = randint(0, 100)
print("I have picked a number between 0 and 100")
guess = None

while number != guess:

    guess = int(input("\nWanna guess it ? "))

    if guess > number:
        print("Number is lower than", guess)
    elif guess < number:
        print("Number is higher than", guess)
    else:
        print("You got it right !!!")
