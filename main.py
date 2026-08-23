import json

def add_food(foods):
    while True:
        food_name = input("Enter the name of the food: ")
        if food_name == "":
            print("\nFood name cannot be empty. Please enter a valid name.")
            continue
        else:
            break

    while True:
        try:
            calories = float(input("Enter the number of calories: "))
            if calories <= 0 or calories > 10000:
                print("Calories cannot be zero or negative or exceed 10000. Please enter a valid number.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter numeric values for calories.")
            continue

    while True:
        try:
            protein = float(input("Enter the amount of protein (in grams): "))
            if protein < 0 or protein > 400:
                print("Protein cannot be negative or exceed 400. Please enter a valid number.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter numeric values for protein.")
            continue
    
    food = {
            "name": food_name,
            "calories": calories,
            "protein": protein
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

def main():

    foods = load_foods()

    while True:
         print("================================")
         print("    Food Tracker!   ")
         print("================================\n")
         print("1. Add Food")
         print("2. View Foods")
         print("3. Calculate Total Calories and Protein")
         print("4. Exit\n")
         print("--------------------------------")

         try:
             choice = int(input("Choose an option: "))
         except ValueError:
             print("Invalid input. Please enter a number.")
             continue


         if choice == 1:
             
             add_food(foods)
             save_foods(foods)
             input(f"\nPress Enter to return to the main menu...")

            
         elif choice == 2:
            view_foods(foods)
            input(f"\nPress Enter to return to the main menu...")

         elif choice == 3:
            total_calories, total_protein = calculate_totals(foods)
            print(f"\nTotal calories: {total_calories} kcal")
            print(f"Total protein: {total_protein} g")
            input(f"\nPress Enter to return to the main menu...")

         elif choice == 4:
            save_foods(foods)
            break
         
         else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
