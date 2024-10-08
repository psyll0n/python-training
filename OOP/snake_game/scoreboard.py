from turtle import Turtle
import os


class Scoreboard(Turtle):
    """
    A class to manage and display the game's score and high score.
    Inherits from the Turtle class in the turtle module.
    """

    ALIGNMENT = "center"
    FONT = ("Courier", 14, "bold")
    HIGH_SCORE_FILE = "high_score.txt"

    def __init__(self):
        """Initialize the Scoreboard object."""
        super().__init__()
        self.score = 0
        self.high_score = self._load_high_score()
        self._setup_turtle()
        self.update_scoreboard()

    def _setup_turtle(self):
        """Configure the turtle's appearance and position."""
        self.hideturtle()
        self.color("green")
        self.penup()
        self.goto(x=0, y=250)

    def _load_high_score(self):
        """
        Load the high score from a file.

        Returns:
            int: The high score loaded from the file, or 0 if the file doesn't exist.
        """
        try:
            with open(self.HIGH_SCORE_FILE, mode="r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def increase_score(self):
        """Increase the current score by 1 and update the scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the current display and write the updated score and high score."""
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=self.ALIGNMENT,
            font=self.FONT
        )

    def reset(self):
        """
        Reset the game score and update the high score if necessary.
        The new high score is saved to a file.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.score = 0
        self.update_scoreboard()

    def _save_high_score(self):
        """Save the current high score to a file."""
        with open(self.HIGH_SCORE_FILE, mode="w") as file:
            file.write(str(self.high_score))


    def game_over(self):
        """Display 'GAME OVER' message in the center of the screen."""
        self.clear()
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=self.ALIGNMENT, font=self.FONT)
