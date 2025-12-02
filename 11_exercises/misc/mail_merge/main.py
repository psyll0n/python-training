# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(
            f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w"
        ) as invitation:
            invitation.write(new_letter)
