# Class definition
class Car:
    # Class Attributes / Variables
    tires = 4

    # Class Constructor / Initializer (Method with a special name)
    def __init__(self, make, model, year, color, moon_roof=False):
        # Object Attributes / Variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running = False

    # Methods
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False


def main():
    print("Hello from the main() method!")
    car1 = Car("Ford", "Mustang", "2010", "Blue")
    car2 = Car("Tesla", "Model 3", "2020", "Red", True)

    # Accessing car1 attributes:
    print("Printing car1 details:".center(50, "-"))
    print("Make:  {}".format(car1.make))
    print("Model: {}".format(car1.model))
    print("Year:  {}".format(car1.year))
    print("Color: {}".format(car1.color))
    print("Moon Roof: {}".format(car1.moon_roof))

    # Accessing car2 attributes:
    print("Printing car2 details:".center(50, "-"))
    print("Make:  {}".format(car2.make))
    print("Model: {}".format(car2.model))
    print("Year:  {}".format(car2.year))
    print("Color: {}".format(car2.color))
    print("Moon Roof: {}".format(car2.moon_roof))

    # Accessing class attributes:
    print("Class Attributes:".center(50, "-"))
    print("car1: ", car1.tires)
    print("car2: ", car1.tires)
    print("Car: ", Car.tires)


if __name__ == "__main__":
    main()
