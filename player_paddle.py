from turtle import Turtle

# Screen dimensions
height, width = 1000, 600


class Paddle(Turtle):
    def __len__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=3, outline=None)
        self.setheading(90)
        self.goto(0, 0)
