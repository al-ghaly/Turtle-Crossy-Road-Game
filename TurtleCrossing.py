import time
import random
import sys
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        self.game_is_on = True
        self.speed = {5: 5, 15: 4, 25: 3, 35: 2, 45: 1}
        self.player = Player()
        self.board = Scoreboard()
        self.screen = Screen()
        self.init_screen()
        self.car_manager = CarManager()
        self.play()

    def init_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(key="Up", fun=self.player.move)

    def detect_collision(self):
        for car in self.car_manager.cars:
            if car.distance(self.player) < 25:
                self.board.game_over()
                self.game_is_on = False

    def play(self):

        while self.game_is_on:

            time.sleep(.1)
            self.screen.update()
            chance = random.randint(1, self.speed[self.car_manager.move_distance])
            if chance == 1:
                self.car_manager.create_car()

            self.car_manager.move_cars()

            if self.player.detect_end_line():
                self.player.restart()
                self.car_manager.accelerate()
                self.board.update_level()
                self.board.create()

            self.detect_collision()
            self.car_manager.clean()

    def reset(self):
        self.screen.clear()


    
while True:
    try:
        game = Game()
        time.sleep(3)
        game.reset()
    except:
        break