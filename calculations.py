from validation import get_valid_serving

def calculate_totals(food_entries):
    total_calories = 0
    total_protein = 0

    for food in food_entries:
        total_calories += food["calories"]
        total_protein += food["protein"]

    return (total_calories, total_protein)

def get_amount(food_to_log):
        amount = get_valid_serving(f"\nHow many grams of {food_to_log['name']} did you eat? ")
        return amount

def calculate_entry_nutrition(food_to_log, amount):
    calories = (food_to_log['calories'] * amount ) / food_to_log['serving_size']
    protein = (food_to_log['protein'] * amount ) / food_to_log['serving_size']

    return (calories, protein)
