#! python3

# Import the prettytable library
# Ref: https://pypi.org/project/prettytable/
from prettytable import PrettyTable

# Create an object called `table` by using the `PrettyTable` class in the prettytable lib.
table = PrettyTable()

# Create a basic table with two columns and three rows by using the `table` object.
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

table.align = "l"
print(table)
