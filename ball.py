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
