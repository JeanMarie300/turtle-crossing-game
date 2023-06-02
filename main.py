import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(player.moveUp, "Up")
game_is_on = True
count = 1
while game_is_on:
    time.sleep(0.5)
    screen.update()

    if count % 6 == 0:
        car = Car()
        car_manager.addCar(car)

    car_manager.moveCars()

    if player.ycor() > 290 :
        player.resetPosition()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        car_manager.increaseCarSpeed()

    for car in car_manager.cars:
        if player.distance(car) < 20 :
            game_is_on = False
            scoreboard.gameOver()

    count += 1

screen.exitonclick()
