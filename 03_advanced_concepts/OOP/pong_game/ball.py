from turtle import Turtle


class Ball(Turtle):
    """Sets up the ball object class"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_speed = 0.05

        # Ball movement variables
        self.x_move = 12  # Horizontal speed
        self.y_move = 12  # Vertical speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Method for ball bouncing effect
    def bounce_x(self):
        # Reverse the vertical direction (y-axis) when bouncing
        self.x_move *= -1
        self.ball_speed *= 0.9

    # Method for ball bouncing effect
    def bounce_y(self):
        # Reverse the vertical direction (y-axis) when bouncing
        self.y_move *= -1

    # Reset the ball position after paddle misses the ball
    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.05
        self.bounce_x()
