import random

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

ascii_art = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
player_choice = int(
    input('Choose 0 for "rock", 1 for "paper" or 2 "scissors. Enter your choice: ')
)

print("Computer choice: ")
print(ascii_art[computer_choice])

try:
    print("Player choice: ")
    print(ascii_art[player_choice])
    if player_choice == 0 and computer_choice == 2:
        print("You win this turn!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose this turn!")
    elif computer_choice > player_choice:
        print("You lose this turn!")
    elif player_choice > computer_choice:
        print("You win this turn!")
    else:
        computer_choice == player_choice
        print("This turn is a draw!")
except IndexError:
    if player_choice >= 3 or player_choice < 0:
        print("You typed an invalid number! You lose!")
