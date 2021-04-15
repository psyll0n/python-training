# Define a basic dictionary

person = {"name": "Kalob", "course": "Python for Everybody", "role": "Teacher"}

# Loop through all keys in in the 'person' dictionary and print each key value pair.
# Example "unpacking of a dictionary in python

for key in person:
    value = person[key]
    print(key, value)


person.items()

for key, value in person.items():
    print(f"Key: {key} \t\t Value: {value}")
