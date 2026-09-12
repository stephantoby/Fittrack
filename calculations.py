from validation import get_valid_serving

def calculate_totals(food_entries):
    total_calories = 0
    total_protein = 0

    for food in food_entries:
        total_calories += food[2]
        total_protein += food[3]

    return (total_calories, total_protein)

def get_amount(food_to_log):
        amount = get_valid_serving(f"\nHow many grams of {food_to_log[1]} did you eat? ")
        return amount

def calculate_entry_nutrition(food_to_log, amount):
    calories = (food_to_log[2] * amount ) / food_to_log[4]
    protein = (food_to_log[3] * amount ) / food_to_log[4]

    return (calories, protein)
