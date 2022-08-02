import sqlite3 as sqlite

con = sqlite.connect("databases/main.db")
cur = con.cursor()

res = cur.execute("SELECT Recipes.Name, Ingredients.Ingredient, Quantity, Unit FROM Recipes_Ingredients_Quantities INNER JOIN Recipes ON Recipes_Ingredients_Quantities.Recipe_ID = Recipes.Meal_ID INNER JOIN Ingredients ON Recipes_Ingredients_Quantities.Ingredient_ID = Ingredients.Ingredient_ID")
# print(res.fetchall())
listOfIngredients = res.fetchall()
print(listOfIngredients[1])