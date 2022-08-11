from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)


l_paddle = Paddle((-370,0))
r_paddle = Paddle((370,0))
ball = Ball()

screen.listen()
screen.onkeypress(key='w',fun=l_paddle._up)
screen.onkeypress(key='s',fun=l_paddle._down)
screen.onkeypress(key='Up',fun=r_paddle._up)
screen.onkeypress(key='Down',fun=r_paddle._down)


l_score = Score((-180,200))
r_score = Score((180,200))


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    sleep(ball.move_speed)
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if ball.xcor() > 420:
        l_score.score_count()
        ball.reset_position()
        sleep(1)
        ball.bounce_x()
    elif ball.xcor() < -420:
        r_score.score_count()
        ball.reset_position()
        sleep(1)
        ball.bounce_x()
    if ball.distance(l_paddle) < 60 and ball.xcor() <= -355 or ball.distance(r_paddle) < 60 and ball.xcor() >= 355:
        ball.bounce_x()
    if l_score.value >= 10 or r_score.value >= 10:
        game_is_on = False


screen.exitonclick()