# Markhus Dammar
# 11/11/19
# This is the init file for the Car class

class Car():
    def __init__(self, make, model, color, year, mileage, price):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = int(mileage)
        self.price = price

    def make(self):
        print(f"The car was made by {self.make}")

    def model(self):
        print(f"The model is {self.model}.")

    def color(self):
        print(f"The car's color is {self.color}")

    def year(self):
        print(f"The {self.make} {self.model} was made in {self.year}")

    def mileage(self):
        print(f"Current, the {self.make} {self.model} has {self.mileage} on it.")

    def price(self):
        print(f"This {self.make} {self.model} costs ${self.price}")
