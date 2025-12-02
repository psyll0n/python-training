"""Turtle Graphics - Progressive Shape Drawing.

Draws a series of regular polygons with increasing number of sides (3 to 9).
Each shape is drawn in a random RGB color using the turtle graphics module.

Features:
- Starts with triangle (3 sides) and ends with nonagon (9 sides)
- Random RGB colors for each shape
- Fixed side length (100 units)
- Automatic angle calculation based on number of sides

Shapes Drawn:
- Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon
"""

import turtle
import random

# Initialize turtle
t = turtle.Turtle()
turtle.colormode(255)  # Sets the color mode to RGB (0-255)
t.shape("turtle")
t.color("DarkOliveGreen")

sides = 3  # Start with a triangle


def draw_shape():
    """
    Draw a regular polygon with the current number of sides.
    
    Uses global 'sides' variable to determine polygon complexity.
    Each polygon is drawn in a random RGB color.
    """
    global sides
    # Generate random RGB color
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    
    # Draw the polygon
    for i in range(sides):
        t.forward(100)
        t.right(360 / sides)  # Calculate interior angle
        t.pencolor(r, g, b)
    
    sides += 1  # Increment for next shape


# Draw shapes from triangle (3 sides) to nonagon (9 sides)
while sides < 10:
    draw_shape()

# Keep window open until clicked
screen = turtle.Screen()
screen.exitonclick()
