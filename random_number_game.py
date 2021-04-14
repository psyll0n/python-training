from random import randrange
import requests


# Define guess, minimum, maximum variables and create an empty list called guesses.
guess = None
guesses = []
minimum = 1
maximum = 20

try:
    response = requests.get("http://www.randomnumberapi.com/api/v1.0/random", params = (('min', minimum),('max', maximum)))
    random = response.json()[0]
    # This means that something went wrong and the API call failed.
except:
    random = randrange(1, 20)

try:
    while guess != random:
        guess = int(input(f"Specify a number between {minimum} and {maximum}: "))
        guesses.append(guess)
        if guess < random:
            print("Your number is below the correct number.")
        elif guess > random: 
            print("Your number is above the correct number.")
        elif guess == random:
            print("Good job. You have guessed the correct number!")
            print(f"Your previous guesses: {guesses}")
        else:
            print("You have not specified a number.")
 
except:
    print("Please, specify a number between 1 and 20.")


