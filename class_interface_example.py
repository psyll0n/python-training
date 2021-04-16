# Python Interfaces - Blueprint for designing Python classes.
class Animal:
   
    def speak(self):
        raise NotImplementedError("Not implemented yet. Please, add an animal sound.")

# Define a subclass of cat animal.
class Cat(Animal):
    def speak(self):
        print('Meow!')

henry = Cat()
print(type(henry))
henry.speak()


# Define a subclass of dog animal.
class Dog(Animal):
    def speak(self):
        print("Woof!")

doggo = Dog()
print(type(doggo))
doggo.speak()


