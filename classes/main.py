from operator import indexOf
import sqlite3 as sqlite

# # Establish a Connection object that represents the database
# con = sqlite.connect("databases/main.db")

# # Create a Cursor object in order to perform SQLite commands
# cur = con.cursor()

# # Generate list of recipe's ingredients and required quantities
# ingredientQuantities = cur.execute("")

# ingredientQuantities = ingredientQuantities.fetchall()

# print(ingredientQuantities[1])
class MealCalendar:

    def __init__(self):
        daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        mondayMeals = []
        tuesdayMeals = []
        wednesdayMeals = []
        thursdayMeals = []
        fridayMeals = []
        saturdayMeals = []
        sundayMeals = []
        weeklyMealPlan = [mondayMeals, tuesdayMeals, wednesdayMeals, thursdayMeals, fridayMeals, saturdayMeals, sundayMeals]
        
        self.mondayMeals = mondayMeals
        self.tuesdayMeals = tuesdayMeals
        self.wednesdayMeals = wednesdayMeals
        self.thursdayMeals = thursdayMeals
        self.fridayMeals = fridayMeals
        self.saturdayMeals = saturdayMeals
        self.sundayMeals = sundayMeals

        self.weeklyMealPlan = weeklyMealPlan
        self.daysOfTheWeek = daysOfTheWeek

    def printWeeklyMealPlan(self):
        for day in self.daysOfTheWeek:
            print(f'{day: <15} {", ".join(self.weeklyMealPlan[self.daysOfTheWeek.index(day)])}')

    def addMealToDay(self, day, meal):
        if day.lower() == "monday":
            self.mondayMeals.append(meal)

class IForgotTheListAgain:

    """Overall class to manage the application"""
    print("Welcome. Forgot the list again?")
    print("Your meal plan for the week is the following: ")
    myMealPlan = MealCalendar()
    myMealPlan.addMealToDay("MONDAY", "Ham and Cheese Sandwich")
    myMealPlan.printWeeklyMealPlan()