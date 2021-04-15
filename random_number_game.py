# Import a random number generator module and also a module allowing API calls to be made from the script.
from random import randrange
import requests


# Define guess, minimum, maximum variables and create an empty list called guesses.
guess = None
guesses = []
minimum = 1
maximum = 20

# Make an API call and get a random integer between the values specified in the variables minimum and maximum.
try:
    response = requests.get("http://www.randomnumberapi.com/api/v1.0/random", params = (('min', minimum),('max', maximum)))
    # If the call is successful get the value of the random integer from the generated JSON.
    random = response.json()[0]
except:
    # This means that something went wrong and the API call produced a status code different than 200.
    random = randrange(minimum, maximum)

try:
    while guess != random:
        try:
            guess = int(input(f"Specify a number between {minimum} and {maximum}: "))
            guesses.append(guess)
        except:
            print("You have not entered a number.")
        if guess < random:
            print("Your number is below the correct number.")
        elif guess > random: 
            print("Your number is above the correct number.")
        elif guess == random:
            print("Good job. You have guessed the correct number!")
            print(f"Your previous guesses: {guesses}")
       
except:
    print("Please, specify a number between 1 and 20.")


