#!/usr/bin/env python3
# word_count.py - The script summarizes the word count in a body of text.

"""Tokenizing a string and counting unique words."""

text = (
    "this is a sample text with several words "
    "this is more sample text with some different words"
)

word_counts = {}

# Count occurrences of each unique word in a text.
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1  # Update existing key-value pair.
    else:
        word_counts[word] = 1  # Insert new key-value pair.

# Print the results and format them nicely.
print(f'{"WORD":<12}COUNT')

# Print the word counts and format them for easy viewing.
for word, count in sorted(word_counts.items()):
    print(f"{word:<12}{count}")

print("\nNumber of unique words:", len(word_counts))
