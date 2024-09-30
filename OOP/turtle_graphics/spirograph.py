import turtle
import random


t = turtle.Turtle()
turtle.colormode(255) # Sets the color mode to RGB
t.shape("turtle")


def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        r = 100
        t.speed("fast")
        t.circle(r)
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        t.color(r, g, b)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
