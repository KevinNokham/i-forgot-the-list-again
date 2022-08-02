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