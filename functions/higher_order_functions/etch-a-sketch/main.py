from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_clockwise():
    t.right(10)

def move_counter_clockwise():
    t.left(10)

def clear_screen():
    t.screen.reset()

# An "Event-Listener". Method in the Turtle module that `listens` for keyboard events.
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
