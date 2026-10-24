from entries import calculate_totals_in_db

def calculate_totals():
    total_calories = 0
    total_protein = 0

    result = calculate_totals_in_db()

    row = result[0]

    total_calories = row[0]
    total_protein = row[1]

    if total_calories is None or total_protein is None:
         total_calories = 0
         total_protein = 0 

    return (total_calories, total_protein)

def calculate_entry_nutrition(food_to_log, amount):
    calories = (food_to_log[2] * amount ) / food_to_log[4]
    protein = (food_to_log[3] * amount ) / food_to_log[4]

    return (calories, protein)

def calculate_remaining(daily_calorie_goal, daily_protein_goal, total_calories_consumed, total_protein_consumed):
    remaining_calories = daily_calorie_goal - total_calories_consumed
    remaining_protein = daily_protein_goal - total_protein_consumed

    return (remaining_calories,remaining_protein)


def calculate_progress():
     return