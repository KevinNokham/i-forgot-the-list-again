from MealCalendar import MealCalendar
from SQLDatabase import SQLDatabase

class IForgotTheListAgain:

    """Overall class to manage the application"""
    print("Welcome. Forgot the list again?")
    myMeal = MealCalendar()
    myMeal.addMealToDay("Monday", 1)
    myMeal.addMealToDay("monday", 3)
    myMeal.printWeeklyMealPlan()