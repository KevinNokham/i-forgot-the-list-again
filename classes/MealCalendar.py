from SQLDatabase import SQLDatabase

class MealCalendar:
    def __init__(self): 
        # Create empty list of meals for each day
        self.mondayMeals = []
        self.tuesdayMeals = []
        self.wednesdayMeals = []
        self.thursdayMeals = []
        self.fridayMeals = []
        self.saturdayMeals = []
        self.sundayMeals = []

        # Create cumulative list combining all meals from every day of the week
        self.weeklyMealPlan = [self.mondayMeals, self.tuesdayMeals, self.wednesdayMeals, self.thursdayMeals, self.fridayMeals, self.saturdayMeals, self.sundayMeals]
        
        # Create list of days for indexing through each day of the week
        self.daysOfTheWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        # Create database in MealCalendar because I don't know how to create functions that call functions from other classes without instances.
        self.Database = SQLDatabase()

    def printWeeklyMealPlan(self):
        # Prints meal plan for each day of the week
        print("The current meal plan for the week is: ")
        for day in self.daysOfTheWeek:
            print(f'{day: <15} {", ".join(self.weeklyMealPlan[self.daysOfTheWeek.index(day)])}')

    def addMealToDay(self, day, mealID):
        # Adds a meal to a day in the weekly meal plan
        day = day.lower()

        # Check if input is actually valid
        mealName = self.Database.sqlQueryRecipeName(mealID)
        if str(mealName) == "None":
            print("No valid meal found.")

        elif day not in self.daysOfTheWeek:
            print("Not a valid day.")

        # In order to simplify things down to one line of code, append meals to a day's list of meals by indexing the approriate day within weeklyMealPlan
        else:
            self.weeklyMealPlan[self.daysOfTheWeek.index(day)].append(self.Database.sqlQueryRecipeName(mealID))
    
    def removeMealFromDay(self, day, mealID):
        # Removes a meal to a day in the weekly meal plan
        day = day.lower()

        # Check if input is actually valid
        mealName = self.Database.sqlQueryRecipeName(mealID)
        if str(mealName) == "None":
            print("No valid meal found.")

        elif day not in self.daysOfTheWeek:
            print("Not a valid day.")

        # In order to simplify things down to one line of code, append meals to a day's list of meals by indexing the approriate day within weeklyMealPlan
        else:
            self.weeklyMealPlan[self.daysOfTheWeek.index(day)].remove(self.Database.sqlQueryRecipeName(mealID))
    
    def sumIngredientsForWeek(self):
        # Create 3 lists, one for storing the raw SQLite data,
        # another for separate ingredients that need to be a particular unit, and another for the quantity of that ingredient's unit
        rawIngredientsList = []
        unitIngredientsList = []
        quantityIngredientsList = []

        # For each daily meal plan in the week, retrieve it's required ingredients list and add it to rawIngredientsList
        for dailyPlan in self.weeklyMealPlan:
            for meal in dailyPlan:  
                rawIngredientsList.append(self.Database.sqlQueryTotalIngredients(self.Database.sqlQueryRecipeID(meal), 1))
        
        # For each ingredient in rawIngredientsList, add the ingredient and its unit to unitIngredientsList if it does not already exist
        # In addition, record its initial quantity
        # If the same ingredient's unit comes up again in rawIngredientsList, only add to quantity in quantityIngredientsList
        # Honestly this would've been easier if I just reordered the list elements or used SQLite
        for x in rawIngredientsList:
            for y in x:
                print("y is:", y)
                print(y)
                if [y[0], y[2]] not in unitIngredientsList:
                    unitIngredientsList.append([y[0], y[2]])
                    quantityIngredientsList.append(y[1])
                    print("Found unique ingredient unit:", y[0], y[2])
                else:
                    print("Found duplicate.")
                    quantityIngredientsList[unitIngredientsList.index([y[0], y[2]])] += y[1]
                    print("New quantity is", quantityIngredientsList[unitIngredientsList.index([y[0], y[2]])])

# Debug
# myMeals = MealCalendar()
# myMeals.addMealToDay("monday", 1)
# myMeals.addMealToDay("monday", 1)
# myMeals.addMealToDay("tuesday", 1)
# myMeals.addMealToDay("monday", 2)
# myMeals.printWeeklyMealPlan()
# print(myMeals.sumIngredientsForWeek())