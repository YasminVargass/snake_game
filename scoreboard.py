from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 18, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score} ", False, align=ALIGN, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over.", False, align=ALIGN, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()