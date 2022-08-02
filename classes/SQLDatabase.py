import sqlite3

class SQLDatabase:
    def __init__(self):
        # Connect to the database
        self.con = sqlite3.connect("databases/main.db")

        # You need this unless unless you want it to return a tuple
        self.con.row_factory = lambda cursor, row: row[0]

        # Create a cursor in order to execute SQLite queries
        self.cur = self.con.cursor()
    
    # Function only for retrieving recipe names
    def sqlQueryRecipeName(self, recipeID):
        recipeID = str(recipeID)
        res = self.cur.execute("SELECT Name FROM Recipes WHERE Meal_ID = " + recipeID)
        return res.fetchone()
