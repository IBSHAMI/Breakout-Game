from turtle import Turtle

# Bricks layers color
colors = ["yellow", "green", "Orange", "red"]

# first brick location
X = -380
Y = 60

# bricks Heading
HEADING = 0  # 0 DEGREE

# bricks number in each layer
NUMBER_OF_BRICKS = 16

# spacing between each layer
LAYER_SPACING = 30

# spacing between bricks in the same layer
BRICKS_SPACING = 18


class Bricks():

    def __init__(self, brick_segments_number):
        global X, Y
        self.X_segments_spacing = 20
        self.X = X
        self.Y = Y
        self.segments_num = brick_segments_number
        self.layer_index = 0
        self.bricks = []
        self.brick_segments = []
        for color in colors:
            self.X = X # start again from beginning of the row and fill
            for i in range(NUMBER_OF_BRICKS):
                for u in range(self.segments_num):
                    self.brick_segments.append(Turtle())
                    self.brick_segments[-1].shape("square")
                    self.brick_segments[-1].color(color)
                    self.brick_segments[-1].penup()
                    self.brick_segments[-1].setheading(HEADING)
                    self.brick_segments[-1].goto(self.X, self.Y)
                    self.X += self.X_segments_spacing # spacing between each
                self.bricks.append(self.brick_segments[-1])
                if i == 7:
                    self.X = X
                    self.Y += LAYER_SPACING
                else:
                    self.X += BRICKS_SPACING
            self.Y += LAYER_SPACING

