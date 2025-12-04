# classmethod_decorator.py - Demonstrates the use of the `@classmethod` decorator in Python.
#
# The @classmethod decorator is used to define a method that is bound to the class and not the instance of the class.
# This means the method receives the class (`cls`) as its first argument, allowing it to access or modify class state.



class Person:
    """
    A class representing a person with a species attribute.
    Demonstrates the use of the @classmethod decorator.
    """
    # Class variable shared by all instances
    species = "Homo Sapiens"

    @classmethod
    def get_species(cls):
        """
        Class method to get the species of the person.
        The @classmethod decorator ensures that 'cls' refers to the class itself, not an instance.

        Returns:
            str: The species of the person (class attribute).
        """
        # Accessing the class variable via 'cls'
        return cls.species


# Example usage of the Person class and its class method:
if __name__ == "__main__":
    # Calling the class method directly from the class
    print(Person.get_species())  # Output: Homo Sapiens
    # The class method can also be called from an instance, but still receives the class as the first argument
    person_instance = Person()
    print(person_instance.get_species())  # Output: Homo Sapiens
    
