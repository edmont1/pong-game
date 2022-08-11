from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score_position(position)
        self.value = 0
        self.writescore()

    def writescore(self):
        self.write(font=('Courier', 60, 'normal'), align='center', arg=f'{self.value}')

    def score_position(self,position):
        self.goto(position)

    def score_count(self):
        self.value += 1
        self.clear()
        self.writescore()
