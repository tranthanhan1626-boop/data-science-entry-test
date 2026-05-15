# Defines a Car class and prints car information in "Year Make Model" format.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car()