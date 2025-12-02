import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def setup_screen():
    """Sets up the main game screen."""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Turtle Crossing Game")
    screen.tracer(0)
    return screen


def main():
    """Main game logic function"""
    game_is_on = True
    screen = setup_screen()
    car_manager = CarManager()
    player = Player()
    score = Scoreboard()
    screen.listen()
    screen.onkey(player.move, "Up")

    while game_is_on:
        car_manager.generate_car()
        car_manager.drive()

        # Detect collisions with the player.
        for car in car_manager.all_cars:
            if car.distance(player) < 10:
                game_is_on = False
                score.game_over()

        # Detect a successful crossing of the road and increase the player score.
        # Reset the player position.
        if player.ycor() >= 280:
            score.increase_level()
            player.reset_position()
            car_manager.level_up()
        time.sleep(0.1)
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
