from turtle import Turtle


# Screen dimensions
Width, Height = 800, 650

# Initial positions
Y_INITIAL = (-Height / 2) + 50
X_INITIAL = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(X_INITIAL, Y_INITIAL)
        self.x_move = 5
        self.y_move = 5

    def ball_moving(self):
        new_x, new_y = self.xcor() + self.x_move, self.ycor() + self.y_move
        self.goto(new_x, new_y)


