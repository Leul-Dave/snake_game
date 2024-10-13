from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        with open('data') as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 20)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data', mode='w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
