from turtle import Turtle
from player_movement import Player
import random

COLORS = ["red", 'blue', 'green', 'violet', 'grey', 'white', 'pink', 'yellow']
MOVEMENT_SPEED = 20



class CarManager:
    def __init__(self):
        self.garage = []
        self.movement_speed = MOVEMENT_SPEED
        # LOWER THE NUMBER TO INCREASE DIFFICULTY, 1 = HARDEST
        self.difficulty = 4

    def create_car(self):
        new_car = Turtle('square')
        if random.randrange(1, self.difficulty) == 1:
            if len(self.garage) == 0:
                new_car.y_spawn_location = random.choice([-200, -150, -100, 0, 50, 100, 200, 250])
                new_car.shapesize(stretch_len=2, stretch_wid=1)
                new_car.color(random.choice(COLORS))
                new_car.penup()
                new_car.goto(500, new_car.y_spawn_location)
                self.garage.append(new_car)
            if len(self.garage) <= 50:
                new_car.y_spawn_location = random.choice([-200, -150, -100, 0, 50, 100, 200, 250])
                if self.garage[len(self.garage) - 1].ycor() != new_car.y_spawn_location:
                    new_car.shapesize(stretch_len=2, stretch_wid=1)
                    new_car.color(random.choice(COLORS))
                    new_car.penup()
                    new_car.goto(500, new_car.y_spawn_location)
                    self.garage.append(new_car)
                else:
                    pass
                    print("didn't create due to overlap")
        for car in self.garage:
            if car.xcor() < -500:
                self.garage.remove(car)

    def move(self):
        for car in self.garage:
            car.backward(MOVEMENT_SPEED)

    def add_speed(self):
        self.movement_speed += 20

    def add_difficulty(self):
        self.difficulty -= 1
        print(f'current difficulty is 1/{self.difficulty}')


