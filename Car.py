class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"


bmw = Car("black", 20000)
print(bmw)
ferrari = Car("red", 15000)
print(ferrari)
