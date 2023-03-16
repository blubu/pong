from turtle import Screen
from classes import Paddle, Ball, Scoreboard
import time

# setting screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# setting variables
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score = Scoreboard()

# listen for events
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.xcor() > 350 and ball.distance(r_paddle) < 50 or ball.xcor() < -350 and ball.distance(l_paddle) < 50:
        ball.deflect()

    if ball.xcor() > 370:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
