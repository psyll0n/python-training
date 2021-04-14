from random import randrange
import requests

def main():
    print("Guess the number: ")

main()

guess = None
guesses = []
minimum = 1
maximum = 20


response = requests.get("http://www.randomnumberapi.com/api/v1.0/random",params = (('min', minimum),('max', maximum)))
random = response.json()[0]


while guess != random:
    guess = int(input(f"Specify a number between {minimum} and {maximum}: "))
    guesses.append(guess)

    if guess < random:
        print("Your number is below the correct number.")
    elif guess > random: 
        print("Your number is above the correct number.")
    elif guess == random:
        print("You have guessed the correct number!")
        print(f"Your previous guesses: {guesses}")
    else:
        print("You have not specified a number.")


