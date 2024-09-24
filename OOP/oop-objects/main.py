#! python3

# Import the Turtle graphics library
# https://docs.python.org/3/library/turtle.html
import turtle
import module_A
from pygments.styles.dracula import green
from reportlab.lib.colors import darkgreen

print(module_A.variable_module_A)

# Construct an object from the Turtle module and Turtle class
timmy_the_turtle = turtle.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color(green)
print(timmy_the_turtle)

my_screen = turtle.Screen()

# Print the attribute `canvheight` of the `my_screen` object.
print(my_screen.canvheight)

# Call the forward() method of the `timmy_the_turtle` object and give it the command to move forward 100 pixels
timmy_the_turtle.forward(100)


# Calling the .exitonclick() object method of the `my_screen` object
my_screen.exitonclick()
