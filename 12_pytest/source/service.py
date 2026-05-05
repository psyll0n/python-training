import requests

database = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
    3: {"name": "Charlie", "age": 35},
}


# This function retrieves a user from the database by their ID.
def get_user(user_id):
    """
    Retrieves a user from the database by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.
    Returns:
        dict: A dictionary containing the user's information if found, otherwise None.
    """
    return database.get(user_id)


# This function retrieves all users from the database. In a real application, this would likely involve
# making an API call to a remote server, but for simplicity, we will just return the values from our local
# database dictionary.
def get_db_users():
    """
    Retrieves all users from the database.

    Returns:
        list: A list of dictionaries, each containing information about a user.
    """
    # In a real application, this function would make an API call to a remote server to retrieve the users.
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    raise requests.HTTPError("Failed to retrieve users from the database")
