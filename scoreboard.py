from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.create()

    def create(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(-180, 0)
        self.write(f"Game Over : Level {self.level}", align="left", font=FONT)
        self.goto(0, -40)
        self.color("red")
        self.write("A new game will start in 3 seconds", font=("Courier", 20, "normal"), align="center")

    def update_level(self):
        self.level += 1
