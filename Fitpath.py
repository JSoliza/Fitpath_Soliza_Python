def calculate_bmr(weight, height, age):
    # Calculate Basal Metabolic Rate (BMR) based on weight, height, and age
    return 10 * weight + 6.25 * height - 5 * age + 5

def calculate_calories(weight, height, age, activity_level):
    # Calculate total calories based on BMR and activity level
    bmr = calculate_bmr(weight, height, age)
    activity_multiplier = {
        "very active": 1.725,
        "active": 1.55,
        "rarely": 1.375,
        "never": 1.2,   
    }.get(activity_level.lower(), 1.2)  # Default to 1.2 activity level if not found
    return bmr * activity_multiplier

def calculate_recommended_calories(weight, height, age, activity_level, goal_type, goal_weight=None):
    #Calculate recommended calories based on goal (1 for weight loss, 2 for maintenance
    maintenance_calories = calculate_calories(weight, height, age, activity_level)
    
    if goal_type == 1:  # Weight of user lose fat
        daily_deficit = 550  # Deficit to set by 0.5 kg weight loss per week
        return maintenance_calories - daily_deficit
    elif goal_type == 2:  # Maintenance of calories
        return maintenance_calories
    else:
        return None 
    
def add_meal(meals, meal_type, protein, fats, carbs, calories):
   #add a meal to the user meal list
    meal = {
        'meal_type': meal_type,
        'protein': protein,
        'fats': fats,
        'carbs': carbs,
        'calories': calories
    }
    meals.append(meal)

def update_meal(meals, meal_index, protein, fats, carbs, calories):
    #update an existing meal in the meal list
    if 0 <= meal_index < len(meals):
        meal = meals[meal_index]
        meal['protein'] = protein
        meal['fats'] = fats
        meal['carbs'] = carbs
        meal['calories'] = calories
        return True
    return False

def delete_meal(meals, meal_index):
    #Delete a meal from the meal lis
    if 0 <= meal_index < len(meals):
        del meals[meal_index]
        return True
    return False

def view_meals(meals):
    # View all meals in the list recorded
    if not meals:
        return "No meals recorded."
    meal_details = []
    for i, meal in enumerate(meals, 1):
        meal_details.append(f"{i}. {meal['meal_type']} - "
                            f"Protein: {meal['protein']} g, "
                            f"Fats: {meal['fats']} g, "
                            f"Carbs: {meal['carbs']} g, "
                            f"Calories: {meal['calories']} kcal")
    return "\n".join(meal_details)

def main():
    users = {}

    while True:
        print("\n:-------------------------------------------------------:")
        print(":    FitPath - Main Menu                                :")
        print(":-------------------------------------------------------:")
        print(": [Select choices from 1-6]                             :")
        print(":-------------------------------------------------------:")
        print(": 1. Register/Update User                               :")
        print(": 2. Add/Update/Delete Meals                            :")
        print(": 3. View User Information                              :")
        print(": 4. View Macros and Calories                           :")
        print(": 5. Delete User                                        :")
        print(": 6. Exit                                               :")
        print(":-------------------------------------------------------:")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Register and update User
            print("\n:----------------------------------:")
            print(": Register/Update User Information :")
            print(":----------------------------------:")
            name = input("Enter your name: ").strip()
            age = int(input("Enter your age: ").strip())
            weight = float(input("Enter your weight (kg): ").strip())
            height = float(input("Enter your height (cm): ").strip())
            activity_level = input("Enter your activity level (Never, Rarely, Active, Very Active): ").strip()
            goal_type = int(input("Enter your fitness goal (1 - Weight Loss, 2 - Maintenance): ").strip())

            if goal_type == 1:
                goal_weight = float(input("Enter your goal weight (kg): ").strip())
                users[name] = {'age': age, 'weight': weight, 'height': height, 'activity_level': activity_level, 'goal_weight': goal_weight, 'meals': []}
            else:
                users[name] = {'age': age, 'weight': weight, 'height': height, 'activity_level': activity_level, 'meals': []}

            print("User information registered/updated successfully!")

        elif choice == "2":
            # here to add or delete or update meals
            print("\n:------------------------------:")
            print(": Add/Update/Delete Meals       :")
            print(":------------------------------:")
            name = input("Enter your name: ").strip()

            if name not in users:
                print("User not found. Please register first.")
                continue

            meals = users[name]['meals']
            print("\nSelect meal action:")
            print("1. Add Meal")
            print("2. Update Meal")
            print("3. Delete Meal")
            meal_action = input("Enter your choice: ").strip()

            if meal_action == "1":
                #to add a new meal
                meal_type = input("Enter meal type (Breakfast, Lunch, Dinner, Snacks): ").strip()
                protein = float(input("Enter Protein (g): ").strip())
                fats = float(input("Enter Fats (g): ").strip())
                carbs = float(input("Enter Carbs (g): ").strip())
                calories = float(input("Enter Calories: ").strip())
                add_meal(meals, meal_type, protein, fats, carbs, calories)
                print("Meal added successfully!")

            elif meal_action == "2":
                #updating an existing meal recorded in list
                if not meals:
                    print("No meals to update.")
                    continue

                print("\nSelect a meal to update:")
                print(view_meals(meals))
                meal_index = int(input("Enter the meal number: ").strip()) - 1

                protein = float(input("Enter new Protein (g): ").strip())
                fats = float(input("Enter new Fats (g): ").strip())
                carbs = float(input("Enter new Carbs (g): ").strip())
                calories = float(input("Enter new Calories: ").strip())

                if update_meal(meals, meal_index, protein, fats, carbs, calories):
                    print("Meal updated successfully!")
                else:
                    print("Invalid meal number.")

            elif meal_action == "3":
                #here to delete existing meal
                if not meals:
                    print("No meals to delete.")
                    continue

                print("\nSelect a meal to delete:")
                print(view_meals(meals))
                meal_index = int(input("Enter the meal number: ").strip()) - 1

                if delete_meal(meals, meal_index):
                    print("Meal deleted successfully!")
                else:
                    print("Invalid meal number.")

        elif choice == "3":
            #to view recorded user information
            name = input("Enter your name to view information: ").strip()

            if name not in users:
                print("User not found.")
            else:
                user = users[name]
                print("---------------------------------------------------------")
                print(f"| Name            : {name}")
                print(f"| Age             : {user['age']}")
                print(f"| Weight          : {user['weight']} kg")
                print(f"| Height          : {user['height']} cm")
                print(f"| Activity Level  : {user['activity_level']}")
                goal = "Weight Loss" if 'goal_weight' in user else "Maintenance"
                print(f"| Goal            : {goal}")
                if 'goal_weight' in user:
                    print(f"| Goal Weight     : {user['goal_weight']} kg")
                print("---------------------------------------------------------")
                print("|                      Meal Details                     |")
                print("---------------------------------------------------------")
                print(view_meals(user['meals']))
                print("---------------------------------------------------------")

        elif choice == "4":
            # to view the macros and calories compare
            name = input("Enter your name to view macros and calories: ").strip()

            if name not in users:
                print("User not found.")
            else:
                user = users[name]
                goal_type = 1 if 'goal_weight' in user else 2
                recommended_calories = calculate_recommended_calories(user['weight'], user['height'], user['age'], user['activity_level'], goal_type, user.get('goal_weight'))
                
                total_protein = sum(meal['protein'] for meal in user['meals'])
                total_fats = sum(meal['fats'] for meal in user['meals'])
                total_carbs = sum(meal['carbs'] for meal in user['meals'])
                total_calories = sum(meal['calories'] for meal in user['meals'])

                print("---------------------------------------------------------")
                print(f"| Recommended Daily Calories : {recommended_calories} kcal")
                print(f"| Total Calories from Meals  : {total_calories} kcal")
                print("---------------------------------------------------------")
                print(f"| Total Protein Consumed     : {total_protein} g")
                print(f"| Total Fats Consumed        : {total_fats} g")
                print(f"| Total Carbs Consumed       : {total_carbs} g")
                print("---------------------------------------------------------")

        elif choice == "5":
            # to delete the user
            name = input("Enter your name to delete account: ").strip()

            if name in users:
                del users[name]
                print(f"User {name} deleted successfully!")
            else:
                print("User not found.")

        elif choice == "6":
            # to end program stop looping exit
            print("Exiting the program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()