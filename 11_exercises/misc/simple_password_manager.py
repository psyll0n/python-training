#!/usr/bin/env python3
"""Simple Password Manager.

A basic command-line password manager that stores passwords in a dictionary
and copies them to the clipboard when requested.

Usage:
    python3 simple_password_manager.py [account]
    
Features:
- Pre-stored passwords for different accounts
- Clipboard integration using pyperclip
- Command-line interface
- Simple account name lookup

Note: This is a demonstration and is NOT secure for real password management.
Passwords are stored in plain text within the code.

Dependencies:
- pyperclip: For clipboard operations
"""

# Simple and not very secure password manager.

PASSWORDS = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "luggage": "12345",
}

import sys
import pyperclip

# Check if account name was provided as command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 simple_password_manager.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]  # first command-line arg is the account name

# Look up account and copy password to clipboard
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named " + account)
