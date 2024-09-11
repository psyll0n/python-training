#!/usr/bin/env python3
# Local functions example.


def sort_by_last_letter(strings):
    # last_letter is a local function
    def last_letter(s):
        return s[-1]

    return sorted(strings, key=last_letter)


list_of_strings = ["hello", "from", "a", "local", "function"]
sorted_by_last_letter = []

if __name__ == "__main__":
    sorted_by_last_letter = [sort_by_last_letter(list_of_strings)]


print(sorted_by_last_letter)
