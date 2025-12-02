#!/usr/bin/env python3
"""reading_files_example.py - Demonstrates file reading with command-line arguments.

This module shows:
- Using sys.argv to get command-line arguments
- Opening and reading files
- Basic error handling with try/except
- User input for file operations

Usage:
    python3 reading_files_example.py <filename>

Note:
    This example uses bare except clause for simplicity.
    In production, use specific exceptions: except FileNotFoundError, etc.
"""

from sys import argv

try:
    # Unpack command-line arguments
    # argv[0] is script name, argv[1] is first argument (filename)
    script, filename = argv
    
    # Open the file in read mode (default)
    # Note: Should use 'with' statement for proper file handling
    txt = open(filename)

    # Display file contents
    print(f"Here is your file {filename}:")
    print(txt.read())  # Read entire file content

    # Prompt user to type filename again (for practice)
    print("Type the filename again:")
    file_again = input(">")
    
    # Open and read the file again
    txt_again = open(file_again)
    print(txt_again.read())
    
    # Note: Files should be closed after use
    # Better practice: use 'with open() as f:' which auto-closes
    
except ValueError:
    # Raised when not enough arguments provided to unpack
    print("Usage: python3 reading_files_example.py <textfile_name>")
except FileNotFoundError:
    # Raised when specified file doesn't exist
    print(f"Error: File '{filename}' not found")
except Exception as e:
    # Catch any other unexpected errors
    print(f"An error occurred: {e}")
    print("\nUsage: python3 reading_files_example.py <textfile_name>")
