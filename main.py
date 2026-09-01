import json

def invalid_calorie(calories):
    return calories <= 0 or calories > 10000

def invalid_protein(protein):
    return protein < 0 or protein > 400

def invalid_serving(serving):
    return serving < 0 or serving > 500

def get_valid_calories(prompt):
    while True:
        try:
            calories = float(input(prompt))
    
            if invalid_calorie(calories):
                print("Calories cannot be less than zero or negative or exceed 10000.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter numeric values for calories.")
            continue
    return calories

def get_valid_protein(prompt):
    while True:
        try:
            protein = float(input(prompt))
            if invalid_protein(protein):
                print("Protein cannot be negative or exceed 400. Please enter a valid number.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter numeric values for protein.")
            continue
    return protein

def get_valid_serving(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if invalid_serving(amount):
                print("Serving cannot be negative or exceed 500. Please enter a valid number.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter numeric values for protein.")
            continue
    return amount


def add_food(foods):
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

    
    food = {
            "name": food_name,
            "calories": calories,
            "protein": protein,
            "serving_size": serving_size
            }

    foods.append(food)

def view_foods(foods):
        if not foods:
            print("\nNo foods have been added yet.")
            return
        
        for food in foods:
         print(f"Food Name: {food['name']}")
         print(f"Calories: {food['calories']} kcal")
         print(f"Protein: {food['protein']} g")
         print(f"Servings: {food['serving_size']} g")
         print("------------------------")

def calculate_totals(foods):
    total_calories = 0
    total_protein = 0

    for food in foods:
        total_calories += food["calories"]
        total_protein += food["protein"]

    return (total_calories, total_protein)

def save_foods(foods):
    with open("foods.json", "w") as file:
        json.dump(foods, file)

def load_foods():
    try:
        with open("foods.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

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

def display_food_choices(foods):
    while True:
        print("   \nYour Foods:   \n")
        print("0. Return to main menu")

        for number, food in enumerate(foods, start=1):
            print(f"{number}. {food['name']}")

        try:
            choice = int(input("\nChoose a food: "))
            if choice == 0:
                return None
            if choice < 0 or choice > len(foods):
                print("\nInvalid choice. Please enter a valid number.")
                continue
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue

        if choice >= 1 and choice <= len(foods):
            food_to_update = foods[choice - 1]
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

def get_amount(food_to_log):
        amount = get_valid_serving(f"\nHow many grams of {food_to_log['name']} did you eat? ")
        return amount

def calculate_entry_nutrition(food_to_log, amount):
    calories = (food_to_log['calories'] * amount ) / food_to_log['serving_size']
    protein = (food_to_log['protein'] * amount ) / food_to_log['serving_size']

    return (calories, protein)

def log_food(foods, food_entries):
    
        food_to_log = display_food_choices(foods)

        if food_to_log is None:
            return
        
        amount = get_amount(food_to_log)
        food_name = food_to_log['name']

        actual_calories, actual_protein = calculate_entry_nutrition(food_to_log, amount)

        print(f"{food_name}")
        print(f"Calories: {actual_calories} Kcal")
        print(f"Protein: {actual_protein} g")

        input("\nPress enter to continue...")

        food_entry = {
            "name": food_name,
            "amount_grams": amount,
            "calories": actual_calories,
            "protein": actual_protein
            }
        
        food_entries.append(food_entry)

def view_food_log(food_entries):
    if not food_entries:
        print("\nNo foods have been added yet.")
        return
   
    for number, food in enumerate(food_entries, start= 1):
        print(f"{number}.")
        print(f"{food['name']}")
        print(f"Amount: {food['amount_grams']} g")
        print(f"Calories: {food['calories']} kcal")
        print(f"Protein: {food['protein']} g")
        print("------------------------")


    
def save_log(food_entries):
    with open("food_logs.json", "w") as file:
        json.dump(food_entries, file)

def load_log():
    try:
        with open("food_logs.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []



  
def main():

    foods = load_foods()
    food_entries = load_log()

    while True:
         print("================================")
         print("    Food Tracker!   ")
         print("================================\n")
         print("1. Add Food")
         print("2. Update Food")
         print("3. View Foods")
         print("4. Delete Food")
         print("5. Log Foods")
         print("6. View Food Log")
         print("7. Calculate Total Calories and Protein")
         print("8. Exit\n")
         print("--------------------------------")

         try:
             choice = int(input("Choose an option: "))
         except ValueError:
             print("Invalid input. Please enter a number.")
             continue
         print("\n")


         if choice == 1:
             
             add_food(foods)
             save_foods(foods)
             input(f"\nPress Enter to return to the main menu...")

         elif choice == 2:

             if update_food(foods) == None:
                 input("Press Enter to return to the main menu...\n")
             else:
                 input(f"\nFood has been updated. Press Enter to return to the main menu...")
                 save_foods(foods)

            
         elif choice == 3:
            view_foods(foods)
            input(f"\nPress Enter to return to the main menu...")

         elif choice == 4:
             delete_food(foods)
             save_foods(foods)
             input(f"\nPress Enter to return to the main menu...")

         elif  choice == 5:
             log_food(foods, food_entries)
             save_log(food_entries)

         elif choice == 6:
             view_food_log(food_entries)

         elif choice == 7:
            total_calories, total_protein = calculate_totals(foods)
            print(f"\nTotal calories: {total_calories} kcal")
            print(f"Total protein: {total_protein} g")
            input(f"\nPress Enter to return to the main menu...")

         elif choice == 8:
            break
         
         else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
