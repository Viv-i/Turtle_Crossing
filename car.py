from turtle import Turtle
import random

COLORS = ["red", 'blue', 'green', 'violet', 'grey', 'white', 'pink', 'yellow']
MOVEMENT_SPEED = 10
Y_SPAWN_LOCATION = [-200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
X_SPAWN_LOCATION = [260, 330, 400, 490]
CARS = []


class Car(Turtle):
    def __init__(self):
        super().__init__('square')
        # if random.randrange(1, 2) == 1:
        #     for car in CARS:
        #         if self.distance(car) < 15:
        #             pass
        #         else:
        #             self.shapesize(stretch_len=2, stretch_wid=1)
        #             self.color(random.choice(COLORS))
        #             self.penup()
        #             self.goto(random.choice(X_SPAWN_LOCATION), random.choice(Y_SPAWN_LOCATION))
        #             self.setheading(180)
        #             CARS.append(self)

    def move(self):
        for car in CARS:
            car.backward(MOVEMENT_SPEED)
            print('should be moving')
        # self.all_cars[:] = [car for car in self.all_cars if car.xcor() < -500]

    def create_car(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(random.choice(X_SPAWN_LOCATION), random.choice(Y_SPAWN_LOCATION))
        CARS.append(new_car)
