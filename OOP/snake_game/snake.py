from turtle import Turtle


# Setting up constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create the snake's body at the start of the game
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    # Reset the snake's position if end-game condition occurs.
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # Add a new segment to the snake as it eats more food
    def extend(self):
        # Access the segments list and get the position of the last segment of the snake's body.
        # Add it as a new segment in the same position as the last segment.
        self.add_segment(self.segments[-1].position())

    # Define a move() method for the objects of the Snake class.
    def move(self):
        # Snake movement logic
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Create four methods for control the snake's movement. Up, Down, Left and Right.
    def up(self):
        # Forbid movement in the opposite direction of UP
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Forbid movement in the opposite direction of DOWN
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Forbid movement in the opposite direction of LEFT
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Forbid movement in the opposite direction of RIGHT
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)