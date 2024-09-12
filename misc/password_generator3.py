import random

# List of possible letters, numbers, and symbols to include in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message for the user
print("Welcome to the PyPassword Generator!")

def get_user_input(prompt):
    """Function to get a valid integer input from the user"""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive integer.")

# User inputs for how many letters, symbols, and numbers they want in the password
nr_letters = get_user_input("How many letters would you like in your password?\n")
nr_symbols = get_user_input("How many symbols would you like?\n")
nr_numbers = get_user_input("How many numbers would you like?\n")

# Function to generate random characters
def generate_random_characters(n, character_set):
    """Generate a list of n random characters from a given character set."""
    return random.sample(character_set, n)

# Generate the password components
random_letters = generate_random_characters(nr_letters, letters)
random_symbols = generate_random_characters(nr_symbols, symbols)
random_numbers = generate_random_characters(nr_numbers, numbers)

# Merge and shuffle the components to form the final password
password_list = random_letters + random_symbols + random_numbers
random.shuffle(password_list)

# Convert the list to a string to get the final password
generated_password = ''.join(password_list)

# Output the final password
print(f"Your generated password is: {generated_password}")
