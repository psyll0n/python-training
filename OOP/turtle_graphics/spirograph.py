import turtle
import random


t = turtle.Turtle()
turtle.colormode(255) # Sets the color mode to RGB
t.shape("turtle")


for _ in range(100):
    r = 100
    t.speed("fastest")
    t.circle(r)
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    t.color(r, g, b)
    current_heading = t.heading()
    t.setheading(current_heading + 5)


screen = turtle.Screen()
screen.exitonclick()
