from app.models import FoodEntry
from entries import get_food_by_id, log_food_entry_to_database, calculate_entry_nutrition, get_foodentry_by_id, update_food_entry_in_database

def create_food_entry(food_entry:FoodEntry):
    food = get_food_by_id(food_entry.food_id)
    if not food:
        raise ValueError(f"Food with ID {food_entry.food_id} not found.")

    actual_calories, actual_protein = calculate_entry_nutrition(food, food_entry.amount_grams)

    food_entry_id = log_food_entry_to_database(
        food_id= food_entry.food_id,
        amount_grams= food_entry.amount_grams,
        calories= actual_calories,
        protein= actual_protein
    )
    
    return (food_entry_id, actual_calories, actual_protein)

def update_food_entry(entry_id, food_entry:FoodEntry):
    food = get_foodentry_by_id(food_entry.food_id)
    if not food:
        raise ValueError(f"Food with ID {food_entry.food_id} not found.")
    
    actual_calories, actual_protein = calculate_entry_nutrition(food, food_entry.amount_grams)

    result = update_food_entry_in_database(entry_id, food_entry.food_id, food_entry.amount_grams, actual_calories, actual_protein)

    if result is None:
        return None

    return {
    "id": entry_id,
    "food_id": food_entry.food_id,
    "amount_grams": food_entry.amount_grams,
    "calories": actual_calories,
    "protein": actual_protein
}

