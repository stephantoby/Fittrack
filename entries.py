from foods import display_food_choices
from calculations import get_amount, calculate_entry_nutrition
from validation import get_valid_serving

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
    
    print("================================")
    print("          Food Log!       ")
    print("================================\n")

    for number, food in enumerate(food_entries, start= 1):
        print(f"{number}.")
        print(f"{food['name']}")
        print(f"Amount: {food['amount_grams']} g")
        print(f"Calories: {food['calories']} kcal")
        print(f"Protein: {food['protein']} g")
        print("-----------------------------")

def update_entry(foods_entries, foods):
    if not foods_entries:
        print("No foods have been added yet.\n")
        return

    food_to_update = display_food_choices(foods_entries)

    if food_to_update is None:
        return 

    print(f"\nYou have selected: {food_to_update['name']} - {food_to_update['amount_grams']} g")

    input(f"\nPress Enter to update the details")

    original_food = None

    for food in foods:
        if food['name'] == food_to_update['name']:
            original_food = food
            break

    if original_food is None:
        print("Food not found in the list.")
        return

    print(f"\nCurrent amount served: {food_to_update['amount_grams']} g")
    new_amount = get_valid_serving(f"Enter the new amount for '{food_to_update['name']}': ")
    food_to_update['amount_grams'] = new_amount

    calories, protein = calculate_entry_nutrition(original_food, new_amount)
    food_to_update['calories'] = calories
    food_to_update['protein'] = protein

    input(f"\nFood entry has been updated. Press Enter to return to the main menu...")

def delete_food(food_entries): 
    while True:
        print("\nYour Foods:   \n")

        if not food_entries:
            print("No foods have been added yet.")
            return
        
        print("0. Return to main menu")

        for number, food in enumerate(food_entries, start=1):
            print(f"{number}. {food['name']}")
            
        try:
            choice = int(input("\nChoose a food to delete: "))
            if choice == 0:
                break
            if choice < 0 or choice > len(food_entries):
                print("\nInvalid choice. Please enter a valid number.")
                continue
            if choice >= 1 and choice <= len(food_entries):
                deleted_food = food_entries[choice - 1]
                del food_entries[choice - 1]
                print(f"\n{deleted_food['name']} has been deleted.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
