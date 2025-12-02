"""Random Number Guessing Game with API Integration.

A number guessing game that attempts to fetch a random number from an external API.
If the API call fails, it falls back to using Python's built-in random module.

Features:
- API-based random number generation with fallback
- Guess tracking and history
- Hint system (higher/lower feedback)
- Error handling for invalid inputs
"""

from random import randrange
import requests

# Initialize game variables
guess = None
guesses = []  # Track all guesses made by the player
minimum = 1
maximum = 20

# Attempt to fetch a random number from the API
try:
    response = requests.get(
        "http://www.randomnumberapi.com/api/v1.0/random",
        params=(("min", minimum), ("max", maximum)),
    )
    # Check if API call was successful (HTTP 200 status)
    if response.status_code == 200:
        random = response.json()[0]  # Extract random number from JSON response
    else:
        # API returned error status, use local random generation
        random = randrange(minimum, maximum)
except:
    # API call failed (network error, timeout, etc.), use fallback
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
