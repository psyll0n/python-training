"""Rock, Paper, Scissors Game.

A simple implementation of the classic Rock, Paper, Scissors game.
The player competes against the computer in a single round.

Game Rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choice results in a draw
"""

import random

# ASCII art representations of each choice
rock = """     
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\\
"""

paper = """
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        
"""

scissors = """   
                     
         (O)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
"""

# Store all choices in a list for easy access by index
ascii_art = [rock, paper, scissors]

# Computer randomly selects rock (0), paper (1), or scissors (2)
computer_choice = random.randint(0, 2)

# Get player's choice
player_choice = int(
    input('Choose 0 for "rock", 1 for "paper" or 2 "scissors. Enter your choice: ')
)

# Display computer's choice
print("Computer choice: ")
print(ascii_art[computer_choice])

try:
    # Display player's choice
    print("Player choice: ")
    print(ascii_art[player_choice])
    
    # Determine winner based on game rules
    if player_choice == 0 and computer_choice == 2:  # Rock beats Scissors
        print("You win this turn!")
    elif computer_choice == 0 and player_choice == 2:  # Rock beats Scissors
        print("You lose this turn!")
    elif computer_choice > player_choice:  # Higher index wins (Paper > Rock, Scissors > Paper)
        print("You lose this turn!")
    elif player_choice > computer_choice:  # Higher index wins
        print("You win this turn!")
    else:  # Same choice
        print("This turn is a draw!")
except IndexError:
    # Handle invalid player input (out of range 0-2)
    if player_choice >= 3 or player_choice < 0:
        print("You typed an invalid number! You lose!")
