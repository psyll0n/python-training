from turtle import Turtle


class Paddle(Turtle):
    """Sets up the paddle player object class"""
    def __init__(self, position):
        super().__init__()
        self.position = self.position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    # Define methods for the up and down movement of the player paddles.
    def go_up(self):
        """Move the paddle up, but stop if it reaches the top boundary."""
        if self.ycor() < 250:  # Upper limit, considering paddle height
            new_y = self.ycor() + 50
            self.goto(self.xcor(), new_y)


    def go_down(self):
        """Move the paddle down, but stop if it reaches the bottom boundary."""
        if self.ycor() > -240:  # Lower limit, considering paddle height
            new_y = self.ycor() - 50
            self.goto(self.xcor(), new_y)


