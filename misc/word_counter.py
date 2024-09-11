#!/usr/bin/env python3
# word_counter.py - count the words in a file. The script is
# similar to word_counter2.py, but it differentiates with use of the Python 'collections' library.

from collections import Counter


text = (
    "this is a sample text with several words "
    "this is more sample text with some different words"
)


text.split()

counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f"{word:<12}{count}")


print("Number of uniques keys:", len(counter.keys()))
