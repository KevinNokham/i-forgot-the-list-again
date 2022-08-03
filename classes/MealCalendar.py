from ast import Continue
from enum import unique
from unittest import skip
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
        self.weeklyMealPlan = [self.mondayMeals, self.tuesdayMeals, self.wednesdayMeals, self.thursdayMeals,
            self.fridayMeals, self.saturdayMeals, self.sundayMeals]
        
        # Create list of days for indexing through each day of the week
        self.daysOfTheWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        # Create database in MealCalendar because I don't know how to create functions that call functions from other classes without instances.
        self.Database = SQLDatabase()

    def printWeeklyMealPlan(self):
        # Prints meal plan for each day of the week
        print("The current meal plan for the week is: ")
        for day in self.daysOfTheWeek:
            print(f'{day.capitalize(): <15} {", ".join(self.weeklyMealPlan[self.daysOfTheWeek.index(day)])}')

    def addMealToDay(self):
        # Adds a meal to a day in the weekly meal plan
        self.Database.sqlQueryAllRecipes()

        while True:
            mealID = input("Enter a meal ID from the selection above: ")
            mealName = self.Database.sqlQueryRecipeName(mealID)
            if str(mealName) == "None":
                print("No valid meal found.")
            else:
                break

        mealPortion = self.Database.sqlQueryPortionSize(mealID)
        print(f"{mealName} has {mealPortion} portions.")

        while mealPortion >= 1:
            self.printWeeklyMealPlan()
            day = input(f"Choose a day to eat this ({mealPortion} left): ")

            while day not in self.daysOfTheWeek:
                print("No valid day found.")
                day = input(f"Choose a day to eat this ({mealPortion} left): ")

            day = day.lower()

            # In order to simplify things down to one line of code, append meals to a day's list of meals by indexing
            # the approriate day within weeklyMealPlan
            self.weeklyMealPlan[self.daysOfTheWeek.index(day)].append(self.Database.sqlQueryRecipeName(mealID))
            mealPortion -= 1
    
    def removeMealFromDay(self):
        # Removes a meal from a day
        self.printWeeklyMealPlan()
        day = input("Choose a day: ").lower()
        while day not in self.daysOfTheWeek:
            print("No valid day found.")
            day = input("Choose a day: ")
        
        mealList = list(enumerate(self.weeklyMealPlan[self.daysOfTheWeek.index(day)], 1))
        for x in mealList:
            print(x)
        
        userInput = input("Enter a meal's number to remove it: ")
        self.weeklyMealPlan[self.daysOfTheWeek.index(day)].pop(int(userInput) - 1)
    
    def sumIngredientsForWeek(self):
        # Create 3 lists, one for storing the raw SQLite data,
        # another for separate ingredients that need to be a particular unit, and another for the quantity of that ingredient's unit
        rawIngredientsList = []
        unitIngredientsList = []
        quantityIngredientsList = []
        mealList = []
        mealCountPortions = []

        # For each daily meal plan in the week, retrieve it's required ingredients list and add it to rawIngredientsList
        for dailyPlan in self.weeklyMealPlan:
            for meal in dailyPlan:
                mealList.append(meal)
    
        uniqueMealList = set(mealList)
        for x in uniqueMealList:
            mealCountPortions.append([x, mealList.count(x), self.Database.sqlQueryPortionSize(str(self.Database.sqlQueryRecipeID(x)))])

        for x in mealCountPortions:
            if x[1] >= x[2]:
                x[1] /= x[2]
            rawIngredientsList.append(self.Database.sqlQueryTotalIngredients(self.Database.sqlQueryRecipeID(x[0]), x[1]))

        for x in rawIngredientsList:
            for y in x:
                print(y)