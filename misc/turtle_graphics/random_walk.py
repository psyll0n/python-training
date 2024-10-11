import turtle
import random


t = turtle.Turtle()
turtle.colormode(255)  # Sets the color mode to RGB
t.shape("turtle")

directions = [0, 90, 180, 270]

for _ in range(300):  # set it 300 times to draw
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    t.color(r, g, b)
    t.forward(30)
    t.setheading(random.choice(directions))  # Randomly choose a direction.
    t.speed("fast")
    if t.filling():
        t.pensize(20)
    else:
        t.pensize(15)


screen = turtle.Screen()
screen.exitonclick()
