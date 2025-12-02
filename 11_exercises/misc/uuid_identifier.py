#!/usr/bin/env python3
# Generating unique identifiers

import uuid


# Use the uuid4 function to create a random sequence of characters using
# the underlying os.random() function.

result = uuid.uuid4()
print("UUID4: ")
print(result)
print(result.hex)
print(result.urn)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Create a UUID using uuid5, which takes a namespace and name value..
# Note that this version is not cryptogrpahically secure.

result = uuid.uuid5(uuid.NAMESPACE_DNS, "python.org")
print("UUID5: ")
print(result)
print(result.hex)
print(result.urn)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
