from validation import get_valid_calories, get_valid_protein, get_valid_serving
from db import get_connection

def add_food():
    while True:
        food_name = input("Enter the name of the food: ").strip()

        if food_name == "":
            print("\nFood name cannot be empty. Please enter a valid name.")
            continue
        else:
            break

    calories = get_valid_calories("Enter the number of calories: ")
    protein = get_valid_protein("Enter the amount of protein (in grams): ")
    serving_size = get_valid_serving("Enter the serving size: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO foods (name, calories, protein, serving_size)
        VALUES (?,?,?,?)
    ''', (food_name, calories, protein, serving_size))

    connection.commit()
    connection.close()
    print("\nSuccessfully added food to the database.")

def view_foods():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT name, calories, protein, serving_size FROM foods
        ''')
        
        foods = cursor.fetchall()
        for food in foods:
         print(f"Food Name: {food[0]}")
         print(f"Calories: {food[1]} kcal")
         print(f"Protein: {food[2]} g")
         print(f"Servings: {food[3]} g")
         print("------------------------")

def update_food_name(food_to_update):
    while True:
            
            new_name = input(f"Enter the new name for '{food_to_update['name']}' (or press Enter to keep it the same): ").strip()
            if new_name == "":
                new_name = food_to_update['name']
                break
            else:
                print(f"\nFood name updated to: {new_name}")
                food_to_update['name'] = new_name
                break     

def display_food_choices(food_list):
    while True:
        print("   \nYour Foods:   \n")
        print("0. Return to main menu")

        for number, food in enumerate(food_list, start=1):
            print(f"{number}. {food['name']}")

        try:
            choice = int(input("\nChoose a food: "))
            if choice == 0:
                return None
            if choice < 0 or choice > len(food_list):
                print("\nInvalid choice. Please enter a valid number.")
                continue
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue

        if choice >= 1 and choice <= len(food_list):
            food_to_update = food_list[choice - 1]
            return food_to_update

def update_food(foods):
    if not foods:
        print("No foods have been added yet.\n")
        return

    food_to_update = display_food_choices(foods)


    if food_to_update is None:
        return 

    update_food_name(food_to_update)

    print(f"\nCurrent calories: {food_to_update['calories']} kcal")
    new_calories = get_valid_calories(f"Enter the new calorie count for '{food_to_update['name']}': ")
    food_to_update['calories'] = new_calories

    print(f"\nCurrent protein: {food_to_update['protein']} g")
    new_protein = get_valid_protein(f"Enter the new protein count for {food_to_update['name']}: ")
    food_to_update['protein'] = new_protein


def delete_food(foods): 
    while True:
        print("\nYour Foods:   \n")

        if not foods:
            print("No foods have been added yet.")
            return
        
        print("0. Return to main menu")

        for number, food in enumerate(foods, start=1):
            print(f"{number}. {food['name']}")
            
        try:
            choice = int(input("\nChoose a food to delete: "))
            if choice == 0:
                break
            if choice < 0 or choice > len(foods):
                print("\nInvalid choice. Please enter a valid number.")
                continue
            if choice >= 1 and choice <= len(foods):
                deleted_food = foods[choice - 1]
                del foods[choice - 1]
                print(f"\n{deleted_food['name']} has been deleted.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
