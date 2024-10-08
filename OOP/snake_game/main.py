import time
from turtle import Screen, textinput
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def restart_game():
    """Prompt the user to play again and return their response."""
    return textinput("Play again?", "Y / N").lower()

def is_game_over(snake, score, lives):
    """
    Handle game over logic: Decrease lives, reset game objects, or end the game
    when all lives are lost.

    Returns:
        bool: True if the game should continue, False if it's over.
    """
    if lives == 0:
        score.game_over()
        return False
    else:
        lives -= 1
        score.reset()
        snake.reset()
        score.update_scoreboard()
        return True

def main():
    # Initialize game state
    game_is_on = True
    lives = 2

    # Set up the game screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    # Initialize game objects
    snake = Snake()
    food = Food()
    score = Scoreboard()

    # Set up event listeners for user input (arrow keys)
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Main game loop
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # Detect collision with wall
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
            game_is_on = is_game_over(snake, score, lives)
            lives -= 1

        # Detect collision with snake's own body (tail)
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = is_game_over(snake, score, lives)
                lives -= 1
                break

    # After the game ends, ask if the player wants to restart
    if restart_game() == "y":
        screen.clear()
        main()
    else:
        screen.exitonclick()

if __name__ == "__main__":
    main()