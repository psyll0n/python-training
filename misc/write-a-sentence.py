# Ask for a sentence.
# Print the length of the sentence.
# Ask for a file name (.txt).
# Write the sentence to the file.
# Run the program from your command line.

name = input("Enter your name: ")
print(f"Hello {name}!")


sentence = input("Enter a sentence: ")
sentence_length = len(sentence)
print(sentence_length)


file_name = input("Enter a file name: ")
file_name = f"{file_name}.txt"


with open(file_name, "w") as f:
    f.write(sentence)
    f.close()


print(f"{name} you have writen {sentence_length} characters to {file_name}")
