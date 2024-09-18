import random


friends = ["Alex", "Alice", "Bob", "Charlie", "David", "Emanuel", "Fred"]

# Option 1
print(random.choice(friends))

# Option 2
random_index = random.randint(0, 7)
print(friends[random_index])
