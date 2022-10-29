from turtle import Turtle

MOVEMENT_SPEED = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.goto(0, -300)
        self.move_up()

    def move_up(self):
        self.fd(MOVEMENT_SPEED)
        print(f'moving, currently at y:{self.ycor()}')


