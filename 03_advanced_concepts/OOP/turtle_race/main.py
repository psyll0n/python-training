from turtle import Turtle, Screen
import random

# Set up the screen for the turtle race
screen = Screen()
screen.setup(width=500, height=400)

# Variables controlling the state of the race and setup details
race_is_on = False
number_of_turtles = 6  # Maximum of 6 turtles, matching the length of `y_positions`
colors = ["blue", "green", "red", "orange", "purple", "black"]
y_positions = [100, 60, 20, -20, -60, -100]
all_turtles = []


def set_color():
    """
    Randomly selects a color from the available `colors` list for a turtle.
    Removes the selected color from the list to avoid duplicates.

    Returns:
        str: The randomly selected color for a turtle.
    """
    if colors:
        turtle_color = random.choice(colors)
        colors.remove(turtle_color)  # Ensures each turtle has a unique color
        return turtle_color


# Create turtle objects and position them on the screen
for turtle_index in range(number_of_turtles):
    t = Turtle(shape="turtle")
    t.color(set_color())
    t.penup()
    t.goto(x=-230, y=y_positions[turtle_index])  # Starting position for each turtle
    all_turtles.append(t)

# Get user's bet for the race
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

# Start the race if a bet was made
if user_bet:
    race_is_on = True

# Main loop controlling the turtle race
while race_is_on:
    for t in all_turtles:
        # Check if any turtle has reached the finish line
        if t.xcor() > 230:  # Finish line is at x=230
            race_is_on = False
            print("Game Over!")
            winner = t.color()[
                0
            ]  # Get the color of the winning turtle without the pen color.
            if winner == user_bet:
                print(f"The winner is {winner}! You win!")
            else:
                print(f"The winner is {winner}! You lost!")

        # Move each turtle a random distance forward
        random_distance = random.randint(0, 10)
        t.forward(random_distance)

# Close the screen when the user clicks
screen.exitonclick()
