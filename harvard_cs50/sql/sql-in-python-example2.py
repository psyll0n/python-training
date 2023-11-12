# Searches database popularity of a problem
import csv

from cs50 import SQL

# Open database
db = SQL("sqlite:///favorites.db")

# Prompt user to specify favorite problem.
favorite = input("Favorite: ")

# Search for problems by title
rows = db.execute(
    "SELECT COUNT(*) FROM favorites WHERE problem LIKE ?", "%" + favorite + "%")

# Get first (and only) row...
row = rows[0]

# Print popularity
print(row["COUNT(*)"])
