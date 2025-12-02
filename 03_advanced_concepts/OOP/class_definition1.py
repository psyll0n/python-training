# Class definition
class Car:
    # Class Attributes / Variables
    tires = 4

    # Class Constructor / Initializer (Method with a special name)
    def __init__(self):
        # Object Attributes / Variables
        self.make = ""
        self.model = ""
        self.year = ""
        self.color = ""
        self.moon_roof = ""
        self.engine_running = False

    # Methods
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False


def main():
    print("Hello from the main() method!")
    car1 = Car()
    car2 = Car()

    # Car1 Values
    car1.make = "Tesla"
    car1.model = "Model 3"
    car1.color = "Red"
    car1.year = "2020"
    car1.moon_roof = True

    # Accessing car1 attributes:
    print("Printing car1 details:".center(50, "-"))
    print("Make:  {}".format(car1.make))
    print("Model: {}".format(car1.model))
    print("Year:  {}".format(car1.year))
    print("Color: {}".format(car1.color))
    print("Moon Roof: {}".format(car1.moon_roof))

    # Accessing class attributes:
    print("Class Attributes - tires:".center(50, "-"))
    print("car1: ", car1.tires)
    Car.tires = 25
    print("Car: ", Car.tires)
    print("car2: ", car1.tires)


if __name__ == "__main__":
    main()
