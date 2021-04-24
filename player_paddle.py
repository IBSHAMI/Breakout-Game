from turtle import Turtle

# Screen dimensions
Width, Height = 800, 650

# Paddle Heading
HEADING = 0  # 0 DEGREE

# Initial positions
Y_INITIAL = (-Height / 2) + 25
X_INITIAL = 0

# Wall Position
X_WALL = Width / 2
X_WALL_RIGHT = X_WALL - 65
X_WALL_LEFT = -X_WALL + 60
LEFT_WALL_EDGE_ERROR = -350  # When the paddle reach the the left wall it doesnt reach the excatly the edge like
# right wall .This variable will is the error which will take the paddle to the end of the left path
# (touch the left wall)


# Paddle Velocity
VELOCITY = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#DCDCDC")
        self.penup()
        self.shapesize(stretch_wid=None, stretch_len=5, outline=None)
        self.setheading(HEADING)
        self.goto(X_INITIAL, Y_INITIAL)

    def going_left(self):
        if self.xcor() > X_WALL_LEFT:
            self.backward(VELOCITY)
            if self.xcor() == -340:
                self.goto(LEFT_WALL_EDGE_ERROR, Y_INITIAL)

    def going_right(self):
        if self.xcor() < X_WALL_RIGHT:
            self.forward(VELOCITY)
            print(self.xcor())
