#!/usr/bin/env python3
# remove_duplicates.py - Remove duplicates in a file and sorts the output.

text = "to be or not to be that is the question"

unique_words = set(text.split())

for word in sorted(unique_words):
    print(word, end=" ")
