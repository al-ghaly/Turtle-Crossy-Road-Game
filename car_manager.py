from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        x = 320
        y = random.randint(-250, 250)
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(x, y)
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def accelerate(self):
        self.move_distance += MOVE_INCREMENT

    def clean(self):
        for car in self.cars.copy():
            if -320 > car.xcor():
                self.cars.remove(car)
