#! python3


# Example function with two positional arguments.
def greeting(name, location):
    print(f"Hello, {name}!")
    print(f"Your location is {location}")
    print(f"How are you doing today, {name}?")


greeting("Alex", "Sofia")


# Example function with two keyword arguments.
def greeting_with_name(name="George", location="London"):
    print(f"Hello, {name}!")
    print(f"Your location is {location}")
    print(f"How are you doing today, {name}?")


greeting_with_name()
