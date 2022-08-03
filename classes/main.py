from MealCalendar import MealCalendar

class IForgotTheListAgain:
    def __init__(self):
        self.MyMealPlan = MealCalendar()
    
    def Menu(self):
        while True:
            print("0. View your meal plan")
            print("1. View ingredient list")
            print("2. Add a meal")
            print("3. Remove a meal")
            print("4. List all recipes")
            print("Q. Quit")

            userInput = input("\nWelcome to the main menu. Please select from the options above: ").lower()
            print(userInput)

            match userInput:
                case "0":
                    self.MyMealPlan.printWeeklyMealPlan()
                    print("\n")
                case "1":
                    self.MyMealPlan.sumIngredientsForWeek()
                    print("\n")
                case "2":
                    self.MyMealPlan.addMealToDay()
                    print("\n")
                case "3":
                    self.MyMealPlan.removeMealFromDay()
                    print("\n")
                case "4":
                    self.MyMealPlan.Database.sqlQueryAllRecipes()
                    print("\n")
                case "q":
                    quit()

if __name__ == "__main__":
    # Make an app instance and run it
    myList = IForgotTheListAgain()
    myList.Menu()