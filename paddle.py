from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.createpaddle(position)


    def createpaddle(self,position):
        self.goto(position)

    def _up(self):
        self.goto(self.xcor(),self.ycor() + 20)

    def _down(self):
        self.goto(self.xcor(), self.ycor() - 20)