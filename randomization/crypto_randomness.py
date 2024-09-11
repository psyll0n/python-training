#!/urs/bin/env python3
# Using cryptographically-appropriate methods to generate random data
# that may be sensitive. The secrets module is available in Python 3.6+

import os
import secrets


# The urandom() in the OS module produces random numbers that are
# cryprographically-secure to use for sensitive data.
result = os.urandom(16)
# print([hex(b) for b in result])

# secrets.choice() is a function similat to random.choice() but more secure.
moves = ["rock", "paper", "scissors"]
# print(secrets.choice(moves))

# secrets.token_bytes() is a function that returns a random byte string.
result = secrets.token_bytes(8)
# print(result)

# secrets.token_hex() is a function that returns a random hexadecimal string.
result = secrets.token_hex(8)
# print(result)

# secrets.token_urlsafe() is a function that returns a random URL-safe string.
results = secrets.token_urlsafe()
print(results)
