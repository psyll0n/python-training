import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def setup_screen():
    """Sets up the main game screen."""
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong Game")
    screen.tracer(0)
    return screen


def setup_paddles():
    """Creates the left and right paddles and assigns them colors."""
    r_paddle = Paddle((380, 0))  # Right paddle
    r_paddle.color("Blue")
    r_paddle.speed("fastest")
    l_paddle = Paddle((-380, 0))  # Left paddle
    l_paddle.color("Red")
    l_paddle.speed("fastest")
    return r_paddle, l_paddle


def setup_controls(screen, l_paddle, r_paddle):
    """Sets up keyboard controls for the paddles."""
    screen.listen()
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")


def detect_paddle_collision(ball, r_paddle, l_paddle):
    """
    Detects collisions between the ball and the paddles.
    If the ball hits a paddle, it changes the horizontal direction.
    """
    # Right paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x()

    # Left paddle collision
    if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()


def detect_wall_collision(ball):
    """
    Detects collisions between the ball and the top/bottom walls.
    If the ball hits the top or bottom, it changes the vertical direction.
    """
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


def detect_score(ball, score):
    """
    Detects when the ball goes past either player's paddle.
    Updates the score accordingly and resets the ball.
    """
    if ball.xcor() > 390:
        ball.reset_position()
        score.increase_score_p1()

    if ball.xcor() < -390:
        ball.reset_position()
        score.increase_score_p2()


def check_game_over(score):
    """Checks if either player has won the game (reaching 5 points)."""
    if score.score_p1 == 10 or score.score_p2 == 10:
        score.game_over()
        return True
    return False


def main():
    """Main function to run the Pong game."""
    screen = setup_screen()
    r_paddle, l_paddle = setup_paddles()
    ball = Ball()
    score = Scoreboard()

    setup_controls(screen, l_paddle, r_paddle)

    game_is_on = True
    while game_is_on:
        time.sleep(ball.ball_speed)
        screen.update()
        ball.move()

        # Detect paddle collisions
        detect_paddle_collision(ball, r_paddle, l_paddle)

        # Detect wall collisions (top and bottom)
        detect_wall_collision(ball)

        # Detect when ball goes past the paddles and update score
        detect_score(ball, score)

        # Check if the game is over
        game_is_on = not check_game_over(score)

    screen.exitonclick()


if __name__ == "__main__":
    main()
