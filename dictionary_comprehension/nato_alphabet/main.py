import pandas as pd

# Create a dictionary in this format:
data = pd.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def main():
    word = input("Enter a word: ").upper()
    try:
        # Create a list of the phonetic code words from a word that the user entered.
        word_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet are valid values...")
        main()
    else:
        print(word_list)


if __name__ == "__main__":
    main()
