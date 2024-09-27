#! python3

class User:
    # Init function definition
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # Setting up a default value of the `followers` attribute.
        self.followers = 0
        self.following = 0

    # Definition of a new method
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Instantiating an object by using the blueprint, a.k.a `Class` called `User`
user_1 = User("001", "angela")
print(user_1.id, user_1.username)
print(user_1.followers)

# Instantiating a second object by using the same class
user_2 = User("002", "alex")
print(user_2.id, user_2.username)

# Calling the `follow` method on the `user_1` object and specifying `user_2` as variable.
user_1.follow(user_2)
print(f"{user_1.username} has {user_1.followers} followers.")
print(f"{user_1.username} is following {user_1.following} users.")

print(f"{user_2.username} has {user_2.followers} followers.")
print(f"{user_2.username} is following {user_2.following} users.")