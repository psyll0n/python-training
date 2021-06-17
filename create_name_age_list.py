# Ask the user for his input - "name" and write to a file "name.txt"
f = open("username_and_age.txt", "a")
f.write(" name: ")
f.write(input(" What's your name? "))
f.close()


# Ask the user for numerical input - "age" and write to a file "user_age.txt"
f = open("username_and_age.txt", "a")
f.write(" age: ")
f.write(input("What's your age? "))
f.write(";")
f.close()


# Open and read the "name.txt" file after the appending:
f = open("username_and_age.txt", "r")
print(f.read())


# Open and read the file after the appending:
f = open("username_and_age.txt", "r")
print(f.read())
