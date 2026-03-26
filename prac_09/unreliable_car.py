from cars import Car
import random
class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random.randint(0, 100)
        if random < self.reliability:
