from turtle import Screen
from player_movement import Player
from car import CarManager
from event_handlers import ScoreBoard
import time


sc = Screen()
sc.bgcolor('black')
sc.screensize(600, 600)
sc.tracer(0)

car_manager = CarManager()
sb = ScoreBoard()
player = Player()

sc.listen()
sc.onkey(player.move_up, "w")

is_alive = True
while is_alive:
    time.sleep(0.1)
    sc.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.garage:
        if car.distance(player) < 18:
            is_alive = False
            sb.game_over()

    if player.ycor() >= 300:
        time.sleep(1.5)
        sb.add_level()
        player.go_to_start()
        car_manager.add_speed()
        if sb.score == 5:
            car_manager.add_difficulty()
        if sb.score == 10:
            car_manager.add_difficulty()


sc.exitonclick()
