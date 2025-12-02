#! python3

import random
import os
import ascii_art


def clear_screen():
    """
    Clears the terminal screen using the appropriate command for the user's operating system.
    """
    # Check if the system is Windows, then use 'cls'. Otherwise, use 'clear'.
    if os.name == "nt":  # 'nt' stands for Windows
        os.system("cls")
    else:
        # Corrected from 'sleep 10' to 'clear' for Unix-based systems
        os.system("clear")


def deal_cards():
    """
    Returns a random card from the standard deck.
    Cards 2-10 have their face value, while Jack, Queen, and King count as 10.
    Ace can be 11 or 1.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Ace is 11, face cards are 10
    return random.choice(cards)


def calculate_score(cards):
    """
    Calculates the total score from a list of cards.
    Adjusts the value of Ace (11) to 1 if the total score exceeds 21.

    Args:
    cards (list): List of cards in hand.

    Returns:
    int: The score for the hand. 0 represents a Blackjack (21 from two cards).
    """
    if sum(cards) == 21 and len(cards) == 2:  # Blackjack condition
        return 0
    if 11 in cards and sum(cards) > 21:  # Convert Ace from 11 to 1 if score > 21
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(user_score, computer_score):
    """
    Compares the scores of the user and the computer and determines the winner.

    Args:
    user_score (int): The user's total score.
    computer_score (int): The computer's total score.

    Returns:
    str: The result of the game (win, lose, draw).
    """
    if user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0:
        return "You win with a Blackjack! 😎"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack 😱!"
    elif user_score > 21:
        return "You went over. You lose! 😤"
    elif computer_score > 21:
        return "The opponent went over! You win! 😁"
    elif user_score > computer_score:
        return "You win! 😁"
    else:
        return "You lose! 😤"


def play_a_game():
    """
    Main function to play a game of Blackjack between the user and the computer.
    Handles card dealing, score calculation, and game logic.
    """
    # Initialize hands and scores
    user_cards = []
    computer_cards = []
    game_over = False

    # Deal initial two cards to both user and computer
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_over:
        # Calculate scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Display current state
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for game over conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask if the user wants to draw another card
            draw_another_card = input(
                "Would you like to draw a new card? Type 'y' to draw or 'n' to pass: \n"
            )
            if draw_another_card == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True

    # Computer's turn to draw cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    # Display final hands and results
    print(compare_scores(user_score, computer_score))
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {
          computer_cards}, final score: {computer_score}"
    )


# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_screen()
    print(ascii_art.logo)
    print("Blackjack Game")
    play_a_game()
