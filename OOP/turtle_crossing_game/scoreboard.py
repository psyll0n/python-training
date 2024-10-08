from turtle import Turtle

FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(x=-230, y=260)
        self.level = 0
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=("Verdana", 25, "bold"))