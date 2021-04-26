from turtle import Screen
from player_paddle import Paddle
from ball import Ball
from bricks import Bricks
from score_borad import Scoreboard
import time

game_screen = Screen()
Width, Height = 800, 650
game_screen.setup(Width, Height)
game_screen.bgcolor("black")
game_screen.title("Arcade Game")
game_screen.tracer(0)

# X_Walls and Y_walls limits for ball collisions plus error term for better collisions
error = 20
X_Wall = Width / 2 - error
Y_wall = Height / 2 - error

# number of paddle segments
number_of_seg_paddle = 4

# number of brick segments
number_of_seg_brick = 4

paddle = Paddle(number_of_seg_paddle)
bricks = Bricks()
ball = Ball()
score = Scoreboard()

game_screen.listen()
game_screen.onkeypress(paddle.going_left, "Left")
game_screen.onkeypress(paddle.going_right, "Right")
ball_brick_distance_list = []
game_is_on = True

while game_is_on:
    collosion_with_brick = False
    time.sleep(0.009)
    game_screen.update()
    ball.ball_moving()
    print(ball.bounced)
    if ball.xcor() >= X_Wall or ball.xcor() <= -X_Wall:
        ball.ball_x_wall_collosion()

    if ball.ycor() >= Y_wall:
        ball.ball_y_wall_collosion()
    for i in range(4):
        if ball.distance(paddle.paddle_segments[i]) < 30:
            ball.ball_paddle_collosion()

    for brick in bricks.bricks_list:
        if brick.distance(ball) <= 50:
            ball.ball_brick_middle_collosion()
            brick.reset()
            brick_index = bricks.bricks_list.index(brick)
            color = bricks.bricks_color[brick_index]
            bricks.bricks_list.remove(brick)
            bricks.bricks_color.remove(bricks.bricks_color[brick_index])
            if color == "yellow":
                score.score_points(1)
            elif color == "green":
                score.score_points(3)
            elif color == "Orange":
                score.score_points(5)
            else:
                score.score_points(7)
            break
    print(ball.heading())

game_screen.update()
game_screen.exitonclick()
