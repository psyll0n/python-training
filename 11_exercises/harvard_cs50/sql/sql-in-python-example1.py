from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")

# `db.execute` returns a list dictionaries...
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = 'Mario'")

row = rows[0]
print(row["n"])
