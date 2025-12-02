"""Fantasy Game Inventory System.

A simple inventory management system for a fantasy game that displays items
and their quantities, along with a total item count.

Features:
- Dictionary-based inventory storage
- Formatted inventory display
- Total item count calculation
"""

# Sample inventory with various fantasy game items
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def displayInventory(inventory):
    """
    Display the contents of an inventory dictionary.
    
    Args:
        inventory (dict): Dictionary with item names as keys and quantities as values.
    
    Prints each item with its quantity and the total count of all items.
    """
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)  # Display quantity and item name
        item_total += v  # Accumulate total count
    print("Total number of items: " + str(item_total))


displayInventory(stuff)
