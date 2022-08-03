import sqlite3

class SQLDatabase:
    def __init__(self):
        # Connect to the database
        self.con = sqlite3.connect("databases/main.db")

        # You need this unless unless you want it to return a tuple
        # self.con.row_factory = lambda cursor, row: row[0]

        # Create a cursor in order to execute SQLite queries
        self.cur = self.con.cursor()
    
    # Function only for retrieving recipe names
    def sqlQueryRecipeName(self, recipeID):
        self.con.row_factory = lambda cursor, row: row[0]
        self.cur = self.con.cursor()

        recipeID = str(recipeID)
        res = self.cur.execute("SELECT Name FROM Recipes WHERE Meal_ID = " + recipeID)
        return res.fetchone()

    def sqlQueryRecipeID(self, recipeName):
        self.con.row_factory = lambda cursor, row: row[0]
        self.cur = self.con.cursor()

        res = self.cur.execute("SELECT Meal_ID FROM Recipes WHERE Name = \"" + recipeName + "\"")
        return res.fetchone()

    def sqlQueryPortionSize(self, mealID):
        self.con.row_factory = lambda cursor, row: row[0]
        self.cur = self.con.cursor()

        res = self.cur.execute("SELECT \"Portion Size\" FROM Recipes WHERE Meal_ID = " + mealID)
        return res.fetchone()

    def sqlQueryTotalIngredients(self, recipeID, pyMealQuantity):
        self.con.row_factory = None
        self.cur = self.con.cursor()

        res = self.cur.execute("SELECT Ingredients.Ingredient, " + str(pyMealQuantity) + """ * Quantity AS [Total Quantity], Unit
        FROM Recipes_Ingredients_Quantities
        INNER JOIN Recipes ON Recipes_Ingredients_Quantities.Recipe_ID = Recipes.Meal_ID
        INNER JOIN Ingredients ON Recipes_Ingredients_Quantities.Ingredient_ID = Ingredients.Ingredient_ID
        WHERE Recipe_ID = """ + str(recipeID) +
        " GROUP BY Ingredient, Unit;")
        return res.fetchall()

    def sqlQueryAllRecipes(self):
        self.con.row_factory = None
        self.cur = self.con.cursor()

        res = self.cur.execute("SELECT \"Meal_ID\", Name FROM Recipes")
        for x in res:
            print(f"ID: {x[0]}, {x[1]}")
