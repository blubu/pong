from turtle import Turtle


# paddle class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 290:
            self.goto(self.xcor(), self.ycor()+15)

    def move_down(self):
        if self.ycor() > -290:
            self.goto(self.xcor(), self.ycor()-15)


# ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self):
        self.y_move *= -1

    def deflect(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1


# score class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lp = 0
        self.rp = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lp, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.rp, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.lp += 1
        self.update_score()

    def r_point(self):
        self.rp += 1
        self.update_score()
