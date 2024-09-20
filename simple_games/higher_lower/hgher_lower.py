#! python3

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
    None: Updates global variables for game state and score.
    """
    global game_over
    global current_score

    if user_input == "A" and instagram_followers_A > instagram_followers_B:
        current_score += 1
        print(f"You are right! Current score: {current_score}")
    elif user_input == "B" and instagram_followers_B > instagram_followers_A:
        current_score += 1
        print(f"You are right! Current score: {current_score}")
    else:
        game_over = True
        print(ascii_art.game_logo)
        print(f"Sorry, that's wrong! GAME OVER!")
        print(f"Final score: {current_score}")


# Main game loop
while not game_over:

    # Randomly choose two celebrities from the data
    celebrity_A = random.choice(instagram_data.data)
    celebrity_B = random.choice(instagram_data.data)

    # Ensure both chosen celebrities are not the same
    while celebrity_A == celebrity_B:
        celebrity_B = random.choice(instagram_data.data)

    # Access the relevant fields for A
    celebrity_name_A = celebrity_A["name"]
    description_celebrity_A = celebrity_A["description"]
    instagram_followers_A = celebrity_A["follower_count"]
    country_celebrity_A = celebrity_A["country"]

    # Access the relevant fields for B
    celebrity_name_B = celebrity_B["name"]
    description_celebrity_B = celebrity_B["description"]
    instagram_followers_B = celebrity_B["follower_count"]
    country_celebrity_B = celebrity_B["country"]

    # Print details for celebrity A
    print(f"Compare A: {celebrity_name_A}, {
          description_celebrity_A}, from {country_celebrity_A}")

    # Print the Vs. ASCII art
    print(ascii_art.vs_logo)

    # Print details for celebrity B
    print(f"Against B: {celebrity_name_B}, {
          description_celebrity_B}, from {country_celebrity_B}")

    # Prompt user to choose who has more Instagram followers

    user_input = input(
        "Who has more Instagram followers? Type 'A' or 'B': ").strip().upper()
    print("\n" * 50)

    # Compare the follower counts and check if the user is correct
    compare(instagram_followers_A, instagram_followers_B, user_input)
