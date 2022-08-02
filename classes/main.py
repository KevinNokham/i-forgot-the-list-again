import sqlite3 as sqlite

# Establish a Connection object that represents the database
con = sqlite.connect("databases/main.db")

# Create a Cursor object in order to perform SQLite commands
cur = con.cursor()

# Generate list of recipe's ingredients and required quantities
ingredientQuantities = cur.execute("")

ingredientQuantities = ingredientQuantities.fetchall()

print(ingredientQuantities[1])