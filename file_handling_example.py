import os

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this:

f = open("/home/psyll0n/python/python-master/demofile.txt", "r")
print(f.read())

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f = open("demofile.txt", "r")
print(f.read(5))


# You can return one line by using the readline() method:

f = open("demofile.txt", "r")
print(f.readline())


# By calling readline() two times, you can read the two first lines:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


# By looping through the lines of the file, you can read the whole file, line by line:

f = open("demofile.txt", "r")
for x in f:
    print(x)

# It is a good practice to always close the file when you are done with it.

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# Open the file "demofile.txt" and append content to the file:

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())


# Open the file "demofile.txt" and overwrite the content:

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())


# Create a file called "myfile.txt":

f = open("myfile.txt", "x")


# To delete a file, you must import the OS module 'import os', and run its os.remove() function:

os.remove("myfile.txt")

# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")


# To delete an entire folder, use the os.rmdir() method:

import os

os.rmdir("myfolder")
