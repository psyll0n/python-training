import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


game_is_on = True

# Set screen size, title and background color
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the snake object by using the Snake() class.
snake = Snake()
food = Food()
score = Scoreboard()

# Create an Event-Listener that listens for keystrokes.
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Call the move() method of the Snake() class.
    snake.move()

    # Detect collision with food, i.e. the snake eats a piece of food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_scoreboard()
        score.increase_score()

    # Detect wall collisions
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()


    # Detect collision with the snake's tail.
    # Loop through the segments in the `segments` list.
    for segment in snake.segments[1:]:
        # Check what is the distance of the `snake's head from the rest of the segments in it body.
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
        # If the snake's head collides with any segment of it's body, trigger the `Game Over` sequence.

screen.exitonclick()
