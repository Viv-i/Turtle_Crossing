from turtle import Screen
from player_movement import Player
from car import Car
import time

sc = Screen()
sc.bgcolor('black')
sc.screensize(600, 600)
sc.tracer(0)

player = Player()
car = Car()

sc.listen()
sc.onkey(player.move_up, "w")

is_alive = True
while is_alive:
    time.sleep(0.1)
    car.move()
    sc.update()
    car.create_car()


sc.exitonclick()
