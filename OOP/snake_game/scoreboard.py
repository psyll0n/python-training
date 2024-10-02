from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")

# Create a Scoreboard class that inherits from the Turtle class in the `turtle` module.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=-0, y=250)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=("Verdana", 18, "bold"))






