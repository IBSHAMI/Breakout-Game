from turtle import Turtle


class GameStatus(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.game_status = "off"

    def game_off(self):
        self.clear()
        self.goto(0, -70)
        self.write(f"Welcome to the game \n"
                   f"press Enter to start", align="center", font=("Courier", 40, "normal"))

    def game_on(self):
        self.game_status = "on"
        self.reset()

    def game_lost(self):
        self.game_status = "lost"
        self.clear()
        self.goto(0, -70)
        self.write(f"you   lost\n Gameover", align="center", font=("Courier", 30, "normal"))
