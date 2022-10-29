from turtle import Screen
from player_movement import Player
from car import Car
from event_handlers import ScoreBoard
import time

sc = Screen()
sc.bgcolor('black')
sc.screensize(600, 600)
sc.tracer(0)

sb = ScoreBoard()
player = Player()

sc.listen()
sc.onkey(player.move_up, "w")

is_alive = True
while is_alive:
    time.sleep(0.1)
    sc.update()
    if player.ycor() >= 280:
        sb.add_level()
    car = Car()
    car.move()


sc.exitonclick()
