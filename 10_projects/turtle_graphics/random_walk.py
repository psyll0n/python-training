"""Turtle Graphics - Random Walk Animation.

Creates a random walk pattern using turtle graphics with random colors and directions.
The turtle moves forward in one of four cardinal directions (0°, 90°, 180°, 270°)
with each step in a new random RGB color.

Features:
- 300 step random walk
- Random RGB colors for each step
- Cardinal direction movement (N, E, S, W)
- Variable pen size
- Fast drawing speed
"""

import turtle
import random

# Initialize turtle
t = turtle.Turtle()
turtle.colormode(255)  # Sets the color mode to RGB (0-255)
t.shape("turtle")

# Four cardinal directions (degrees)
directions = [0, 90, 180, 270]

# Execute 300 random walk steps
for _ in range(300):
    # Generate random RGB color for this step
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    t.color(r, g, b)
    
    # Move forward 30 units
    t.forward(30)
    
    # Randomly choose next direction
    t.setheading(random.choice(directions))
    
    # Set fast drawing speed
    t.speed("fast")
    
    # Vary pen size
    if t.filling():
        t.pensize(20)
    else:
        t.pensize(15)

# Keep window open until clicked
screen = turtle.Screen()
screen.exitonclick()
