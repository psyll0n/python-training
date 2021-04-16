class Animal:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def speak(self):
        print("What does the animal say?")

class Cat(Animal):

    def speak(self):
        print('Meooowww!')

henry = Cat("Henry", "9 lbs")
print(type(henry))
henry.speak()

class Dog(Animal):

    def speak(self):
        print("Woof Woof!")


veto = Dog("Veto", "20 lbs")
print(type(veto))
veto.speak()

