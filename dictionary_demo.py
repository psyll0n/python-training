# Create a blank dictionary

phonebook = {}

name = input("Enter name: ")
number = int(input("Enter phone number: "))


phonebook[name] = number


print(phonebook)

print(phonebook["Alex"])
