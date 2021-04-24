from turtle import Screen, mainloop, Turtle
from player_paddle import Paddle
import time

game_screen = Screen()
Width, Height = 800, 650
game_screen.setup(Width, Height)
game_screen.bgcolor("black")
game_screen.title("Arcade Game")
game_screen.tracer(0)

paddle = Paddle()

game_screen.exitonclick()
