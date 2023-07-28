from turtle import Turtle
ALIGNMENT ='center'
FONT = ('Arial', 24, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore') as h_score:
            self.highscore = int(h_score.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore', mode='w') as h_score:
                h_score.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()

    """def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAMEOVER!!\nyour final score: {self.score}", align=ALIGNMENT, font=FONT)"""




