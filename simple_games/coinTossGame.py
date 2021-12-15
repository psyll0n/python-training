#! python3
# coinTossGame.py - Coin toss guessing game.
# Script for testing / exercise of the python's built-in logging / debugging functionality.

import random
import logging


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("Start of program")

guess = ""


while guess not in ("heads", "tails"):
    logging.debug("Start of guess")
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
    logging.debug("User input accepted")
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads

    # We need to convert heads/tails to 0/1, or visa versa.
    if toss == 0:
        toss = "tails"
    elif toss == 1:
        toss = "heads"
    logging.debug("Does " + str(toss) + " equal " + str(guess) + "?")

    if toss == guess:
        print("You got it!")
    else:
        print("Nope! Guess again!")
        guess = input()
        if toss == guess:
            print("You got it!")
        else:
            print("Nope! You are really bad at this game.")
