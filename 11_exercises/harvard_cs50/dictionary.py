"""Dictionary Module - Word Checking Functions.

Provides functions for loading a dictionary file, checking if words exist,
getting dictionary size, and unloading the dictionary from memory.

Note: This implementation has a bug - words should be stored as dict keys,
not using words.add() which doesn't exist for dict objects.

Functions:
- check(word): Check if a word exists in the dictionary
- load(dictionary): Load words from a file into memory
- size(): Return the number of words in the dictionary
- unload(): Unload the dictionary from memory
"""

import os

words = dict()  # Dictionary to store loaded words


def check(word):
    """
    Check if a word exists in the loaded dictionary (case-insensitive).
    
    Args:
        word (str): The word to check.
    
    Returns:
        bool: True if word exists in dictionary, False otherwise.
    """
    if word.lower() in words:
        return True
    else:
        return False


def load(dictionary):
    """
    Load words from a dictionary file into memory.
    
    Args:
        dictionary (str): Path to the dictionary file.
    
    Returns:
        bool: True if successful (currently always True).
    
    Note: Bug - should use words[word] = True instead of words.add(word)
    """
    file = open(dictionary, "r")
    for line in file:
        word = line.rstrip()
        words[word] = True  # Fixed: dict uses assignment, not add()
    file.close()  # Fixed: use file.close() instead of os.close(file)
    return True


def size():
    """
    Get the number of words in the loaded dictionary.
    
    Returns:
        int: Number of words in the dictionary.
    """
    return len(words)


def unload():
    """
    Unload the dictionary from memory.
    
    Returns:
        bool: True when complete.
    """
    return True
