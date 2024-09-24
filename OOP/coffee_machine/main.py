from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


"""
-= Explanation =-

Menu Class:

* The get_items() method is called to display the available drinks to the user (e.g., "latte/espresso/cappuccino").
* The find_drink(order_name) method is used to find a specific drink the user wants to order.

CoffeeMaker Class:

* The report() method is used to display the current status of the machine’s resources (e.g., water, milk, coffee).
* The is_resource_sufficient(drink) method checks if there are enough resources to make the selected drink.
* The make_coffee(order) method deducts the resources and makes the coffee if the payment is successful.

MoneyMachine Class:

* The report() method displays the current profit.
* The make_payment(cost) method asks the user to insert coins and checks if the payment is sufficient.

How It Works:

* The machine will keep running, displaying the menu options and waiting for the user to make a selection (espresso, latte, cappuccino).
* If the user types "report", it will show the current resources and total money earned.
* If the user types "off", the machine will shut down.
* If the user selects a valid drink, the program checks if the resources are sufficient and processes the payment before making the drink.
"""


def coffee_machine_program():
    # Create instances of the necessary classes
    menu = Menu()  # Menu object to handle drinks
    coffee_maker = CoffeeMaker()  # CoffeeMaker object to manage resources
    money_machine = MoneyMachine()  # MoneyMachine object to handle payments

    # Power the machine on and keep running while user hasn't chosen to turn it off
    powered_on = True

    while powered_on:
        # Get the available menu items
        options = menu.get_items()

        # Prompt the user for input
        choice = input(f"What would you like? ({options}): ").lower()

        if choice == "off":
            powered_on = False
            print("Turning off the coffee machine...")
        elif choice == "report":
            # Print the reports for resources and profit
            coffee_maker.report()
            money_machine.report()
        else:
            # Find the drink the user has selected
            drink = menu.find_drink(choice)

            if drink:
                # Check if the resources are sufficient
                if coffee_maker.is_resource_sufficient(drink):
                    # Ask the user for payment
                    if money_machine.make_payment(drink.cost):
                        # Make the coffee
                        coffee_maker.make_coffee(drink)
            else:
                print(f"Sorry, we don't have {choice} on the menu.")


# Run the coffee machine program
coffee_machine_program()
