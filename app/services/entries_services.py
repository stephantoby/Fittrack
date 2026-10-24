from fastapi import HTTPException
from app.models import FoodEntry
from entries import get_food_by_id, log_food_entry_to_database, update_food_entry_in_database, calculate_totals_in_db
from calculations import calculate_entry_nutrition

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
    food = get_food_by_id(food_entry.food_id)
    if not food:
        raise HTTPException(status_code=404, detail=f"Food with ID {food_entry.food_id} not found.")
    
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

def calculate_totals_service():
    total_calories, total_protein= calculate_totals_in_db()

    return {
            "total_calories": total_calories,
            "total_protein": total_protein
           }



