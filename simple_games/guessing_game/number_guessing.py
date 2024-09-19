#! python3
import random
import ascii_art

# Print the ASCII art logo
print(ascii_art.logo)

# Initialize the game settings: guesses list, max guesses, range of numbers.
guesses = []  # List to store user's guesses
max_guesses = -1  # Will be set based on difficulty level
minimum = 1  # Minimum value for the secret number
maximum = 100  # Maximum value for the secret number
# Randomly generate the secret number
secret_number = random.randint(minimum, maximum)
game_over = False  # Flag to track if the game is over


def guess_the_number(guess):
    """
    Handles the logic for processing the user's guess and provides feedback.

    Args:
    guess (int): The user's current guess.

    Returns:
    None
    """
    global max_guesses
    global game_over

    if guess < secret_number:
        print("Your number is below the correct number. Guess again...")
        guesses.append(guess)
        print(f"Your guesses so far: {guesses}")
    elif guess > secret_number:
        print("Your number is above the correct number. Guess again...")
        guesses.append(guess)
        print(f"Your guesses so far: {guesses}")
    else:
        game_over = True
        print("Good job. You have guessed the correct number!")
        guesses.append(guess)
        print(f"Your guesses: {guesses}")


# Introduction to the game
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100...")

# Ask the player to select a difficulty level
difficulty = input("Choose difficulty. Type 'easy' or 'hard' to begin: ")

# Set the maximum number of guesses based on the chosen difficulty
if difficulty == "easy":
    max_guesses = 10
    print("You have 10 attempts remaining to guess the number.")
elif difficulty == "hard":
    max_guesses = 5
    print("You have 5 attempts remaining to guess the number.")
else:
    print("Invalid difficulty selected. Defaulting to 'hard'.")
    max_guesses = 5

# Main game loop: Continue until the user either guesses the number or runs out of guesses
while not game_over:
    print(f"Number of guesses remaining: {max_guesses}")

    # If the player has used all guesses, the game is over
    if max_guesses == 0:
        game_over = True
        print("Game Over! You have failed to guess the number.")
        print(f"The correct number was: {secret_number}")
    else:
        # Ask the player for their guess and process it
        try:
            guess = int(input("Make a guess: "))
            guess_the_number(guess)
            max_guesses -= 1
        except ValueError:
            print("Invalid input. Please enter a number.")
