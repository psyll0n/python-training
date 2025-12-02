"""Dice Roller Simulation.

A dice rolling simulator that allows users to roll multiple dice with customizable
number of sides. The program tracks the total sum and identifies critical rolls.

Features:
- Configurable number of dice and dice sides
- Critical fail detection (rolling a 1)
- Critical success detection (rolling max value)
- Sum calculation of all rolls
"""

import random


def main():
    """
    Main function to run the dice roller simulation.
    
    Prompts the user for the number of dice to roll and the number of sides
    on each die, then simulates the rolls and displays results.
    """
    # Initialize variables for dice configuration and tracking
    dice_rolls = int(input("How many dice would you like to roll? "))
    dice_size = int(input("How many sides are the dice? "))
    dice_sum = 0  # Track the total sum of all dice rolls

    # Roll each die and accumulate the results
    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)  # Generate random number for this die
        dice_sum += roll  # Add this roll to the running total

        if roll == 1:
            print(f"You rolled a {roll}! Critical fail!")
        elif roll == 6:
            print(f"You rolled a {roll}! Critical Success!")
        else:
            print(f"You rolled a {roll}...")
    print(f"You have rolled a total of: {dice_sum}")


if __name__ == "__main__":
    main()

"""
Here are some potential Next Steps:

Add more inputs (like player or team name).
Store each player's roll totals in separate arrays.
Choose a dice-based game that you can fully simulate using python.
"""
