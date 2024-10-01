import turtle
from turtle import Turtle, Screen


t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


screen.listen()
# Using a function as input of the `screen.onkey()` function
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()