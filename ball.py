from turtle import Turtle
import random

# Screen dimensions
Width, Height = 800, 650

# Initial positions
Y_INITIAL = (-Height / 2) + 80
X_INITIAL = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.new_x, self.new_y = None, None
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(X_INITIAL, Y_INITIAL)
        self.x_move = 5
        self.y_move = 5
        self.bounced = False

    def ball_moving(self):
        self.new_x, self.new_y = self.xcor() + self.x_move, self.ycor() + self.y_move
        self.goto(self.new_x, self.new_y)

    def ball_x_wall_collosion(self):
        self.x_move *= -1
        self.bounced = False

    def ball_y_wall_collosion(self):
        self.y_move *= -1
        self.bounced = False

    # def ball_paddle_edges_collosion(self, ball_x_pos, paddle_Seg_x_pos, seg_num):
    #     if seg_num == 0:
    #         if ball_x_pos >= paddle_Seg_x_pos:
    #             self.y_move *= -1
    #             self.x_move *= -1
    #             print("here")
    #         else:
    #             self.y_move *= -1
    #     else:
    #         if ball_x_pos <= paddle_Seg_x_pos:
    #             self.y_move *= -1
    #             self.x_move *= -1
    #             print("here")
    #         else:
    #             self.y_move *= -1

    def ball_paddle_collosion(self):
        if not self.bounced:
            self.y_move *= -1
            self.setheading(random.randint(0, 5))
            self.bounced = True
        else:
            pass

    def ball_brick_edges_collosion(self):
        self.y_move *= -1
        self.x_move *= -1
        self.bounced = False

    def ball_brick_middle_collosion(self):
        self.y_move *= -1
        self.bounced = False
