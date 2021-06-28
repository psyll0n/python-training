# keep_the_last_n_items.py - the following code performs a simple text match
# on a sequence of lines and yields the matching line along with the previous
# N lines of context when found.

#! python3

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
<<<<<<< HEAD


=======
<<<<<<< HEAD


# Example use on a file
if __name__ == "__main__":
    with open("somefile.txt") as f:
        for line, prevlines in search(f, "python", 5):
            for pline in prevlines:
                print(pline, end="")
                print("-" * 20)
=======
        
>>>>>>> 51f83aa0df79342ce37a1dae69bfcd0ce4286810
# Example use on a file
if __name__ == "__main__":
    with open("somefile.txt") as f:
        for line, prevlines in search(f, "python", 5):
            for pline in prevlines:
<<<<<<< HEAD
                print(pline, end="")
                print("-" * 20)
=======
                print(pline, end='')
                print('-'*20)
>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c
>>>>>>> 51f83aa0df79342ce37a1dae69bfcd0ce4286810
