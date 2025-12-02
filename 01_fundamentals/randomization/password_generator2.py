# Password Generator Project
import random  # Import the random module for random sampling

# List of possible letters, numbers, and symbols to include in the password
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# Welcome message for the user
print("Welcome to the PyPassword Generator!")

# User inputs for how many letters, symbols, and numbers they want in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomized:
# e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91

# Create a dictionary where keys are indices and values are letters
alphabet = {idx: letter for idx, letter in enumerate(letters)}
# Convert the dictionary values (letters) into a list
alphabet_values = list(alphabet.values())
# Randomly sample 'nr_letters' letters from the list
random_values = random.sample(alphabet_values, nr_letters)

# Create a dictionary where keys are indices and values are symbols
symbols_dict = {idy: symbol for idy, symbol in enumerate(symbols)}
# Convert the dictionary values (symbols) into a list
symbol_values = list(symbols_dict.values())
# Randomly sample 'nr_symbols' symbols from the list
random_symbols = random.sample(symbol_values, nr_symbols)

# Create a dictionary where keys are indices and values are numbers
numbers_dict = {idz: number for idz, number in enumerate(numbers)}
# Convert the dictionary values (numbers) into a list
numerical_values = list(numbers_dict.values())
# Randomly sample 'nr_numbers' numbers from the list
random_numbers = random.sample(numerical_values, nr_numbers)

# Merge the lists
combined_list = random_values + random_symbols + random_numbers

# Shuffle the combined list
random.shuffle(combined_list)

# Join the list into a string to remove commas and square brackets
generated_password = "".join(combined_list)
print(generated_password)
