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
            print("Invalid input. Please enter numeric values for serving size.")
            continue
    return amount