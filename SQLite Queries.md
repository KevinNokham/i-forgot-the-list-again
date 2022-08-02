## List of every recipe's list of ingredients in database
<!-- SELECT Recipes.Name, Ingredients.Ingredient, Quantity, Unit
FROM Recipes_Ingredients_Quantities
INNER JOIN Recipes ON Recipes_Ingredients_Quantities.Recipe_ID = Recipes.Meal_ID
INNER JOIN Ingredients ON Recipes_Ingredients_Quantities.Ingredient_ID = Ingredients.Ingredient_ID; -->

## Sum of every ingredient from each recipe by unit in database
<!-- SELECT Ingredients.Ingredient, SUM(Quantity), Unit
FROM Recipes_Ingredients_Quantities
INNER JOIN Recipes ON Recipes_Ingredients_Quantities.Recipe_ID = Recipes.Meal_ID
INNER JOIN Ingredients ON Recipes_Ingredients_Quantities.Ingredient_ID = Ingredients.Ingredient_ID
GROUP BY Ingredient, Unit -->