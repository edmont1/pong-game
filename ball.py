from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.setpos(0,0)
        self.y = 5
        self.x = 5
        self.move_speed = 0.05

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.05
