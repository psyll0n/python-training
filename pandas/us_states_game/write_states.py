from turtle import Turtle


class WriteState(Turtle):

    FONT = ("Ariel", 8, "bold")

    def __init__(self):
        super().__init__()
        self._setup_turtle()

    def _setup_turtle(self):
        """Configure the turtle's appearance and position."""
        self.hideturtle()
        self.color("black")
        self.penup()

    def map_update(self, answer_state, xcor, ycor):
        """Update the turtle position and write the state name on the map."""
        self.goto(x=xcor, y=ycor)  # Move the turtle to the x, y coordinates
        self.write(f"{answer_state}", font=self.FONT)  # Write the state name
