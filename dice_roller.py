# Import the random module. 

import random 

# Define a function called main. Promp for user input spcifying the number of dice and dice rolls.

def main():

# Define variables dice_rolls, dice_size and dice_sum.

  dice_rolls = int(input("How many dice would you like to roll? "))
  dice_size = int(input("How many sides are the dice? "))
  dice_sum = 0

# Define a for-loop in which the random module is used to generate random numbers and store those in the roll local variable.
# The dice_sum local variable stores the output / sum of all the randomly generated numbers. 
  
  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    dice_sum += roll  # this can also be written as: dice_sum = dice_sum + roll / x += y /

    if roll == 1:
      print(f"You rolled a {roll}! Critical fail!")
    elif roll == 6:
      print(f"You rolled a {roll}! Critical Success!")
    else:
      print(f"You rolled a {roll}...")
  print(f"You have rolled a total of: {dice_sum}")
if __name__== "__main__":
  main()        

"""
Here are some potential Next Steps:

Add more inputs (like player or team name).
Store each player's roll totals in separate arrays.
Choose a dice-based game that you can fully simulate using python.
"""
