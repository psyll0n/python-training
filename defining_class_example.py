
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Notice that the .__init__() method’s signature is indented four spaces. 
# The body of the method is indented by eight spaces. 
# This indentation is vitally important.
# It tells Python that the .__init__() method belongs to the Dog class.
# In the body of .__init__(), there are two statements using the self variable:

#  self.name = name creates an attribute called name and assigns to it the value of the name parameter.
#  self.age = age creates an attribute called age and assigns to it the value of the age parameter.



# Attributes created in .__init__() are called instance attributes. An instance attribute’s value is specific to a particular instance of the class. 
# All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.

# On the other hand, class attributes are attributes that have the same value for all class instances. 
# You can define a class attribute by assigning a value to a variable name outside of .__init__().

# For example, the following Dog class has a class attribute called species with the value "Canis familiaris":

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# To pass arguments to the name and age parameters, put values into the parentheses after the class name:

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)


# After you create the Dog instances, you can access their instance attributes using dot notation:

print(buddy.name)
print(buddy.species)
print(buddy.age)

print(miles.name)
print(miles.species)
print(miles.age)


# Instance methods are functions that are defined inside a class and can only be called from an instance of that class. 
# Just like .__init__(), an instance method’s first parameter is always self.

class SpeakingDog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# This SpeakingDog class has two instance methods:

# .description() returns a string displaying the name and age of the dog.
# .speak() has one parameter called sound and returns a string containing the dog’s name and the sound the dog makes.

benjy = SpeakingDog("Benjy", 6)
charly = SpeakingDog("Charly", 1)


print(benjy.name)
print(benjy)
print(benjy.species)
print(benjy.description())
print(benjy.speak("woof woof!"))


print(charly.name)
print(charly)
print(charly.species)
print(charly.description())
print(charly.speak("woof woof!"))

