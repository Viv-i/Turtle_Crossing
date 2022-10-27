from turtle import Turtle
import random

COLORS = ["red", 'blue', 'green', 'violet', 'grey', 'white', 'pink', 'yellow']
MOVEMENT_SPEED = 15
CARS = []


class Car(Turtle):
    def __init__(self):
        super().__init__('square')
        if random.randrange(1, 4) == 1:
            if len(CARS) == 0:
                self.y_spawn_location = random.choice([-200, -150, -100, 0, 50, 100, 200, 250])
                self.shapesize(stretch_len=2, stretch_wid=1)
                self.color(random.choice(COLORS))
                self.penup()
                self.goto(500, self.y_spawn_location)
                CARS.append(self)
            if len(CARS) <= 50:
                self.y_spawn_location = random.choice([-200, -150, -100, 0, 50, 100, 200, 250])
                if CARS[len(CARS) - 1].ycor() != self.y_spawn_location:
                    self.shapesize(stretch_len=2, stretch_wid=1)
                    self.color(random.choice(COLORS))
                    self.penup()
                    self.goto(500, self.y_spawn_location)
                    CARS.append(self)
                else:
                    pass
                    print("didn't create due to overlap")
        for car in CARS:
            if car.xcor() < -500:
                CARS.remove(car)

    def move(self):
        for car in CARS:
            car.backward(MOVEMENT_SPEED)
