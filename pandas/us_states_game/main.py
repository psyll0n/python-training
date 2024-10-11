import turtle
import pandas as pd
import time
from write_states import WriteState


# Set up the game screen size and its properties
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data
data = pd.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_states = []
_map = WriteState()
user_score = 0

# Timer setup
total_time = 5 * 60  # 5 minutes in seconds

# Use a loop to allow the user to keep guessing
start_time = time.time()  # Get the start time
while len(guessed_states) < 50:
    # Calculate remaining time
    elapsed_time = time.time() - start_time
    remaining_time = int(total_time - elapsed_time)
    if remaining_time <= 0:
        break  # End the game when time runs out

    # Convert remaining time to minutes and seconds
    mins, secs = divmod(remaining_time, 60)
    timer_format = f"{mins:02d}:{secs:02d}"

    # Prompt the user with the current score and remaining time
    answer_state = screen.textinput(
        title=f"Time Left: {timer_format} | Guess the State...",
        prompt=f"Current Score: {user_score}/50. What's another state's name?",
    ).title()

    if answer_state == "Exit":
        break

    # Check whether the user's guess is among the 50 states and if it's not guessed already
    if answer_state not in guessed_states and answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        xcor = state_data.x.item()  # Get the x coordinate of the state
        ycor = state_data.y.item()  # Get the y coordinate of the state

        # Update the US map with the name of the state
        _map.map_update(answer_state, xcor, ycor)

        user_score += 1

# Handle the end of the game: Show states left to guess by using list comprehension.
states_left = [state for state in all_states if state not in guessed_states]

# Show unguessed states on the screen
for state in states_left:
    state_data = data[data.state == state]
    xcor = state_data.x.item()  # Get the x coordinate of the state
    ycor = state_data.y.item()  # Get the y coordinate of the state
    _map.map_update(state, xcor, ycor)

# Save states that were not guessed to a CSV file
states_to_learn = {"states_left": states_left}

states = pd.DataFrame(states_to_learn)
states.to_csv("states_to_learn.csv")


screen.exitonclick()
