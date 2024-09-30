import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)  # Sets the color mode to RGB
t.shape("turtle")
t.color("DarkOliveGreen")

sides = 3

def draw_shape():
    global sides
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    for i in range(sides):
        t.forward(100)
        t.right(360 / sides)
        t.pencolor(r, g, b)
    sides += 1


while sides < 10:
    draw_shape()


screen = turtle.Screen()
screen.exitonclick()

