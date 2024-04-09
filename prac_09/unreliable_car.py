from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """An unreliable version of the car"""

    def __init__(self, name, fuel, reliability=float):
        """Initialise UnreliableCar instance, based from Car parent class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Returns a string like a Car"""
        return f"{super().__str__()}"

    def drive(self, distance):
        """Drives like parent car but only drives if value is below reliability"""
        if int(self.reliability) >= randint(0, 100):
            distance = 0
        distance_drive = super().drive(distance)
        return distance_drive

