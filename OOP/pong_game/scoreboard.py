from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "bold")

class Scoreboard(Turtle):
    """Sets up the Scoreboard object class"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("Green")
        self.penup()
        self.goto(x=-0, y=250)
        self.score_p1 = 0
        self.score_p2 = 0
        self.write(f"{self.score_p1} : {self.score_p2}", align="center", font=FONT)
        self.update_scoreboard()


    def increase_score_p1(self):
        self.score_p1 += 1
        self.clear()
        self.update_scoreboard()


    def increase_score_p2(self):
        self.score_p2 += 1
        self.clear()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"{self.score_p1} : {self.score_p2}", align="center", font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=("Verdana", 25, "bold"))

