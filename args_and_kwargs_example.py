# args = arguments
# kwargs = keyword arguments

# Example:
# def func_name(name, *args, **kwargs)

def func_name(*args):
    print(args)
    print(type(args))


func_name(1, 5, 8, 'Python', 'Coding')


def print_args(*args):
    for arg in args:
        print(arg)

print('Computer', 'Coffee', 'Cup', 'Monitor', 'Lamp')


def my_func(**kwargs):
    print(kwargs)
    print(type(kwargs))


my_func(name='Kalob', drink='Cofee', hobby='Gardening')


def my_func(**kwargs):
    for key, value in kwargs.items():
        print("Key: ", key, " \t\t", "Value: ", value)

my_func(name='Kalob', drink='Cofee', hobby='Gardening')


def order(name, *dishes, **kwargs):
    print(f"Hello {name}")
    for dish in dishes:
         print(f"\tYou ordered {dish}")

    if kwargs.get("address"):
        address = kwargs.get("address")
        print(f"We are delivering to {address}")
    else:
        print("You did not provide an address!")

order("Zephyr", "tacos", "cat food")
