from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.carSpeed = STARTING_MOVE_DISTANCE

    def addCar(self, car):
        self.cars.append(car)

    def moveCars(self):
        for car in self.cars:
            car.forward(-self.carSpeed)

    def increaseCarSpeed(self):
        self.carSpeed += MOVE_INCREMENT












