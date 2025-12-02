#! python3
"""Higher or Lower - Instagram Followers Game.

A game where players guess which celebrity has more Instagram followers.
The game continues until the player makes an incorrect guess, tracking their score.

Features:
- Celebrity Instagram follower data
- Score tracking
- Randomized celebrity selection
- ASCII art logos
- Continuous gameplay until wrong answer

Game Flow:
1. Display two celebrities
2. Player guesses who has more followers
3. Correct guess: score increases, continue
4. Wrong guess: game over, display final score
"""

import random
import instagram_data
import ascii_art

# Print game logo
print(ascii_art.game_logo)

# Initialize score and game over state
current_score = 0
game_over = False


def compare(instagram_followers_A, instagram_followers_B, user_input):
    """
    Compares the Instagram follower counts of two celebrities and updates the score.

    Args:
        instagram_followers_A (int): Follower count of celebrity A.
        instagram_followers_B (int): Follower count of celebrity B.
        user_input (str): The user's choice, either "A" or "B".

    Returns:
        bool: True if the user is correct, False otherwise.
    """
    if user_input == "A" and instagram_followers_A > instagram_followers_B:
        return True
    elif user_input == "B" and instagram_followers_B > instagram_followers_A:
        return True
    return False

# Main game loop
celebrity_A = random.choice(instagram_data.data)  # Initial selection for A

while not game_over:
    # Select a new random celebrity for B (ensure it's different from A)
    celebrity_B = random.choice(instagram_data.data)
    while celebrity_A == celebrity_B:
        celebrity_B = random.choice(instagram_data.data)

    # Extract data for celebrity A
    celebrity_name_A = celebrity_A["name"]
    description_celebrity_A = celebrity_A["description"]
    instagram_followers_A = celebrity_A["follower_count"]
    country_celebrity_A = celebrity_A["country"]

    # Extract data for celebrity B
    celebrity_name_B = celebrity_B["name"]
    description_celebrity_B = celebrity_B["description"]
    instagram_followers_B = celebrity_B["follower_count"]
    country_celebrity_B = celebrity_B["country"]

    # Display celebrity A details
    print(
        f"Compare A: {celebrity_name_A}, {description_celebrity_A}, from {country_celebrity_A}"
    )

    # Print the Vs. ASCII art
    print(ascii_art.vs_logo)

    # Display celebrity B details
    print(
        f"Against B: {celebrity_name_B}, {description_celebrity_B}, from {country_celebrity_B}"
    )

    # Get user's guess
    user_input = (
        input("Who has more Instagram followers? Type 'A' or 'B': ").strip().upper()
    )
    print("\n" * 100)  # Clear screen

    # Check if the user's choice is correct
    if compare(instagram_followers_A, instagram_followers_B, user_input):
        print(ascii_art.game_logo)
        current_score += 1
        print(f"You are right! Current score: {current_score}")

        # Update celebrity_A to be the one with more followers (for continuity)
        if user_input == "B":
            celebrity_A = celebrity_B  # B becomes the new A for next round

    else:
        game_over = True
        # Display game over message
        print(ascii_art.game_logo)
        print(f"Sorry, that's wrong! Game OVER!")
        print(
            f"{celebrity_name_A} has {instagram_followers_A} Million followers"
        )
        print(
            f"{celebrity_name_B} has {instagram_followers_B} Million followers"
        )
        print(f"Final score: {current_score}")
        print(f"Final score: {current_score}")
