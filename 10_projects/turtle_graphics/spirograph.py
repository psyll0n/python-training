"""Turtle Graphics - Spirograph Pattern.

Creates a beautiful spirograph pattern by drawing overlapping circles
with incrementally rotated headings. Each circle is drawn in a random RGB color.

Features:
- Circular spirograph pattern
- Customizable gap size between circle starting points
- Random RGB colors for each circle
- Fast drawing speed
- Radius of 100 units per circle

The pattern is created by drawing circles and rotating the turtle's heading
slightly after each circle, creating an overlapping circular pattern.
"""

import turtle
import random

# Initialize turtle
t = turtle.Turtle()
turtle.colormode(255)  # Sets the color mode to RGB (0-255)
t.shape("turtle")


def draw_spirograph(size_of_gap):
    """
    Draw a spirograph pattern with overlapping circles.
    
    Args:
        size_of_gap (int): The angle (in degrees) to rotate between each circle.
                          Smaller gaps create denser patterns.
    
    The function draws circles in a complete rotation (360 degrees),
    with each circle starting at a position rotated by size_of_gap degrees.
    """
    # Calculate number of circles needed for complete rotation
    for _ in range(int(360 / size_of_gap)):
        r = 100  # Circle radius
        t.speed("fast")
        t.circle(r)
        
        # Generate random RGB color for next circle
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        t.color(r, g, b)
        
        # Rotate heading for next circle position
        t.setheading(t.heading() + size_of_gap)


# Create spirograph with 5-degree gaps (72 circles total)
draw_spirograph(5)

# Keep window open until clicked
screen = turtle.Screen()
screen.exitonclick()
