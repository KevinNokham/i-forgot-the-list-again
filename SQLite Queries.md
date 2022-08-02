## List of every recipe's list of ingredients in database
<!-- SELECT Recipes.Name, Ingredients.Ingredient, Quantity, Unit
FROM Recipes_Ingredients_Quantities
INNER JOIN Recipes ON Recipes_Ingredients_Quantities.Recipe_ID = Recipes.Meal_ID
INNER JOIN Ingredients ON Recipes_Ingredients_Quantities.Ingredient_ID = Ingredients.Ingredient_ID; -->

## Sum of every ingredient from a single recipe by unit in database, has external variable PyMealQuantity
<!-- SELECT Ingredients.Ingredient, PyMealQuantity * Quantity AS [Total Quantity], Unit
FROM Recipes_Ingredients_Quantities
INNER JOIN Recipes ON Recipes_Ingredients_Quantities.Recipe_ID = Recipes.Meal_ID
INNER JOIN Ingredients ON Recipes_Ingredients_Quantities.Ingredient_ID = Ingredients.Ingredient_ID
WHERE Recipe_ID = Meal_ID
GROUP BY Ingredient, Unit -->