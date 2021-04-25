from turtle import Screen, mainloop, Turtle
from player_paddle import Paddle
from ball import Ball
from bricks import Bricks
import time


game_screen = Screen()
Width, Height = 800, 650
game_screen.setup(Width, Height)
game_screen.bgcolor("black")
game_screen.title("Arcade Game")
game_screen.tracer(0)

# X_Walls and Y_walls limits for ball collisions plus error term for better collisions
error = 20
X_Wall = Width/2 - error
Y_wall = Height/2 - error





paddle = Paddle()
bricks = Bricks()
ball = Ball()


game_screen.listen()
game_screen.onkeypress(paddle.going_left, "Left")
game_screen.onkeypress(paddle.going_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.027)
    game_screen.update()
    ball.ball_moving()

    if ball.xcor() >= X_Wall or ball.xcor() <= -X_Wall:
        ball.ball_x_wall_collosion()

    if ball.ycor() >= Y_wall:
        ball.ball_y_wall_collosion()


game_screen.update()
game_screen.exitonclick()
