from turtle import Turtle

MOVEMENT_SPEED = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def move_up(self):
        self.fd(MOVEMENT_SPEED)

    def go_to_start(self):
        self.goto(0, -300)
