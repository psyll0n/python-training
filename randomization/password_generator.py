#!/usr/bin/env python3

# Create a temp password using Python.

import secrets
import string


#  Create a function that generates a random password.
def generate_pass(num_chars=15):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    result = "".join(secrets.choice(potential_chars) for i in range(num_chars))
    return result


#  Function to return a temp password and enforce 1 number and 1 upper case letter.
def generate_strong_pass(num_chars=15):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    while True:
        result = "".join(secrets.choice(potential_chars) for i in range(num_chars))

        if any(c.isupper() for c in result) and any(c.isdigit() for c in result):
            break

    return result


# Create a temp password.
# print(generateTempPass(15))

# Create a strong temp password.
print(generate_strong_pass(15))


#  Create a temp password, hard-to-guess URL.
resultUrl = "https://my.example.com?reset="
resultUrl += secrets.token_urlsafe(16)
print(resultUrl)
