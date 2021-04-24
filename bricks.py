from turtle import Turtle

# Bricks layers color
colors = ["yellow", "green", "Orange", "red"]

# first brick location
X = -362
Y = 60

# bricks Heading
HEADING = 0  # 0 DEGREE

# bricks number in each layer
NUMBER_OF_BRICKS = 20

# spacing between each layer
LAYER_SPACING = 30

# spacing between bricks in the same layer
BRICKS_SPACING = 80


class Bricks():

    def __init__(self):
        global X, Y
        self.X = X
        self.Y = Y
        self.layer_index = 0
        self.bricks = []
        for color in colors:
            self.X = X
            for i in range(NUMBER_OF_BRICKS):
                self.bricks.append(Turtle())
                self.bricks[-1].shape("square")
                self.bricks[-1].color(color)
                self.bricks[-1].penup()
                self.bricks[-1].shapesize(stretch_wid=None, stretch_len=3.6, outline=None)
                self.bricks[-1].setheading(HEADING)
                self.bricks[-1].goto(self.X, self.Y)
                if i == 9:
                    self.X = X
                    self.Y += LAYER_SPACING
                else:
                    self.X += BRICKS_SPACING
            self.Y += LAYER_SPACING
