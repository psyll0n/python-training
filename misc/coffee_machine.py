#! python3

# Initialize global variables
payment_successful = False
powered_on = ""
power_off = ""

# Coins available in the machine
money_available = {
    "quarters": 50,
    "dimes": 50,
    "nickles": 50,
    "pennies": 50,
    "total": 20.5,
}

# Available resources in the coffee machine
existing_resources = {
    "water": 2000,
    "coffee": 500,
    "milk": 1000,
    "money": money_available["total"]
}

# Drink options with ingredients and prices
espresso = {
    "id": "espresso",
    "water": 50,
    "coffee": 18,
    "price": 1.50,
}

latte = {
    "id": "latte",
    "water": 200,
    "coffee": 24,
    "milk": 150,
    "price": 2.50,
}

cappuccino = {
    "id": "cappuccino",
    "water": 250,
    "coffee": 24,
    "milk": 100,
    "price": 3.00,
}

# Drinks dictionary for easy lookup
drinks = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino
}

# Initialize payment data
payment = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
    "total": 0,
}


def power_off_machine():
    """
    Function to handle the power on/off state of the coffee machine.
    It will prompt the user to turn the machine on or off.
    """
    global powered_on, power_off, selection

    # Turn the machine on/off
    power_off = input("Power off the coffee machine? (on/off): ")

    if power_off == "on":
        powered_on = True

        def process_transaction():
            """Processes the transaction and checks if the user has inserted enough money."""
            global payment_successful

            selected_drink = drinks[selection]
            print(f"The price of {selected_drink['id']} is: ${
                  selected_drink['price']:.2f}")

            # Check if the payment is sufficient
            if payment["total"] >= selected_drink["price"]:
                payment_successful = True
                payment["total"] -= selected_drink["price"]
                print("Transaction successful ... 👍")

                # Provide change if needed
                if payment["total"] > 0:
                    print(f"Here is your change: ${payment['total']:.2f}")
            else:
                print("Sorry, that's not enough money. Money refunded. 🚫")
                payment_successful = False

        def sum_amount(payment):
            """
            Prompts the user to insert coins and calculates the total amount.
            """
            # Prompt the user to insert coins
            payment["quarters"] = int(
                input("Please, insert coins [quarters]: "))
            payment["dimes"] = int(input("Please, insert coins [dimes]: "))
            payment["nickles"] = int(input("Please, insert coins [nickles]: "))
            payment["pennies"] = int(input("Please, insert coins [pennies]: "))

            # Calculate total inserted money
            payment["total"] = (payment["quarters"] * 0.25 +
                                payment["dimes"] * 0.10 +
                                payment["nickles"] * 0.05 +
                                payment["pennies"] * 0.01)

            print(f"Total payment: ${payment['total']:.2f}")
            process_transaction()

        def make_coffee(selection):
            """
            Deducts the resources from the coffee machine and serves the selected drink.
            """
            drink = drinks[selection]
            print(f"Making a(n) {selection}...")

            existing_resources["coffee"] -= drink["coffee"]
            existing_resources["water"] -= drink["water"]

            # Deduct milk if the drink contains milk
            if "milk" in drink:
                existing_resources["milk"] -= drink["milk"]

            print(f"Remaining water: {existing_resources['water']}ml")
            print(f"Remaining coffee: {existing_resources['coffee']}g")
            print(f"Remaining milk: {existing_resources['milk']}ml")
            print(f"Here is your {selection}. Enjoy! ☕ \n")

        def check_resources(selection):
            """
            Checks if there are sufficient resources to make the selected drink.
            If resources are sufficient, the user is prompted to insert coins.
            """
            drink = drinks[selection]

            # Check if there's enough water, coffee, and milk (if needed)
            if (existing_resources["water"] >= drink["water"] and
                existing_resources["coffee"] >= drink["coffee"] and
                    ("milk" not in drink or existing_resources["milk"] >= drink["milk"])):

                # Ask for payment and process the transaction
                sum_amount(payment)
                if payment_successful:
                    make_coffee(selection)
            else:
                print("Insufficient resources to make this drink.")

        # Prompt the user for their drink selection
        selection = input(
            "What would you like to order? Espresso, Latte, or Cappuccino? ").lower()

        if selection in drinks:
            check_resources(selection)
        elif selection == "report":
            # Display a report of the remaining resources
            print(f"Water: {existing_resources['water']}ml")
            print(f"Milk: {existing_resources['milk']}ml")
            print(f"Coffee: {existing_resources['coffee']}g")
            print(f"Money: ${existing_resources['money']:.2f}")
        else:
            print("Unknown selection. Please, enter a valid option.")
    else:
        powered_on = False
        print("Powering off ...")


# Start the coffee machine
power_off_machine()
