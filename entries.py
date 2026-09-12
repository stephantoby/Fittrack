from foods import display_food_choices
from calculations import get_amount, calculate_entry_nutrition
from validation import get_valid_serving
from db import get_connection

def log_food():
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute('''
        SELECT id, name, calories, protein, serving_size FROM foods
        ''')

        foods = cursor.fetchall()
        
        food_to_log = display_food_choices(foods)

        if food_to_log is None:
            return
        
        amount = get_amount(food_to_log)
        food_name = food_to_log[1]  # Assuming the name is at index 1 in the food tuple

        actual_calories, actual_protein = calculate_entry_nutrition(food_to_log, amount)

        print(f"{food_name}")
        print(f"Calories: {actual_calories} Kcal")
        print(f"Protein: {actual_protein} g")

        input("\nPress enter to continue...")

        cursor.execute('''
        INSERT INTO food_entries (food_id, amount_grams, calories, protein)
        VALUES (?, ?, ?, ?)
        ''', (food_to_log[0], amount, actual_calories, actual_protein))

        connection.commit()
        connection.close()


def view_food_log():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    SELECT foods.name, food_entries.amount_grams, food_entries.calories, food_entries.protein 
    FROM food_entries
    JOIN foods 
        ON food_entries.food_id = foods.id
    ''')

    food_entries = cursor.fetchall()

    if not food_entries:
        print("\nNo foods have been added yet.")
        return
    
    print("================================")
    print("          Food Log!       ")
    print("================================\n")

    for number, food in enumerate(food_entries, start= 1):
        print(f"{number}.{food[0]}")
        print(f"Amount: {food[1]} g")
        print(f"Calories: {food[2]} kcal")
        print(f"Protein: {food[3]} g")
        print("-----------------------------")

    connection.close()

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
'''
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
'''