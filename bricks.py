from turtle import Turtle

# Bricks layers color
colors = ["yellow", "green", "Orange", "red"]

# first brick location
X = -360
Y = 60

# bricks Heading
HEADING = 0  # 0 DEGREE

# bricks number in each layer
NUMBER_OF_BRICKS = 22

# spacing between each layer
LAYER_SPACING = 30

# spacing between bricks in the same layer
BRICKS_SPACING = 71


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        global X, Y
        self.X = X
        self.Y = Y
        self.layer_index = 0
        self.bricks_list = []
        self.bricks_color = []
        for color in colors:
            self.X = X  # start again from beginning of the row and fill
            for i in range(NUMBER_OF_BRICKS):
                self.bricks_list.append(Turtle())
                self.bricks_list[-1].shape("square")
                self.bricks_list[-1].color(color)
                self.bricks_list[-1].penup()
                self.bricks_list[-1].shapesize(stretch_wid=None, stretch_len=3.2, outline=None)
                self.bricks_list[-1].setheading(HEADING)
                self.bricks_color.append(color)
                self.bricks_list[-1].goto(self.X, self.Y)
                if i == 10:
                    self.X = X
                    self.Y += LAYER_SPACING
                else:
                    self.X += BRICKS_SPACING
            self.Y += LAYER_SPACING

