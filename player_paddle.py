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
X_WALL_RIGHT = X_WALL - 80
X_WALL_LEFT = -X_WALL + 75
# those values turen to provide sufficient wall barrier so the paddle can reach exactly the edge on the screen

# Paddle Velocity
VELOCITY = 20


class Paddle():
    def __init__(self, paddle_segments_num):
        self.number_of_seg = paddle_segments_num
        self.paddle_segments = []
        self.X_INITIAL = 0
        for i in range(self.number_of_seg):
            self.paddle_segments.append(Turtle())
            self.paddle_segments[i].shape("square")
            self.paddle_segments[i].color("#DCDCDC")
            self.paddle_segments[i].penup()
            self.paddle_segments[i].setheading(HEADING)
            self.paddle_segments[i].goto(self.X_INITIAL, Y_INITIAL)
            self.X_INITIAL += 20

    def going_left(self):
        if self.paddle_segments[-1].xcor() > X_WALL_LEFT:
            for i in range(self.number_of_seg - 1, -1, -1):
                self.paddle_segments[i].backward(VELOCITY)

    def going_right(self):
        if self.paddle_segments[0].xcor() < X_WALL_RIGHT:
            for i in range(0, self.number_of_seg, 1):
                self.paddle_segments[i].forward(VELOCITY)
