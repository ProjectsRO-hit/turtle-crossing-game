import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

mandy_the_turtle = Player()



game_is_on = True

screen.listen()
screen.onkey(mandy_the_turtle.move_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()