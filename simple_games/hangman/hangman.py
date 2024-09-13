import random
from hangman_words import word_list
from hangman_ascii_art import HANGMAN_LOGO, HANGMAN_STAGES

# Welcome message and logo
print(f"Welcome to...\n{HANGMAN_LOGO}")

# Initialize the game variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_"] * word_length
correct_guesses = []
wrong_guesses = []
lives = 6
game_over = False

# Uncomment this line if you want to reveal the word for testing purposes.
# print(f"Chosen word: {chosen_word}")

# Main game loop
while not game_over:
    # Show current word progress
    print("\n" + " ".join(display))
    
    # Get user input and validate it
    guess = input("\nMake a guess (a single letter): ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue

    # If the guess has already been made, notify the player
    if guess in correct_guesses or guess in wrong_guesses:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue
    
    # Process correct guess
    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")
        correct_guesses.append(guess)

        # Reveal the correct letters in the display
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
        
        # Check if the player has guessed all letters
        if "_" not in display:
            game_over = True
            print("\n********* Congratulations! You've guessed the word! *********")
            print(f"The word was: {chosen_word}")
            break
    
    # Process incorrect guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        wrong_guesses.append(guess)
        lives -= 1
        print(HANGMAN_STAGES[-1])
        HANGMAN_STAGES.pop(-1)

        # Check if the player is out of lives
        if lives == 0:
            game_over = True
            print("\n********* Game Over! You've run out of lives! *********")
            print(f"The word was: {chosen_word}")
            break

# Final game status
print(f"\nCorrect guesses: {correct_guesses}")
print(f"Incorrect guesses: {wrong_guesses}")
