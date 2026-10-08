from foods import add_food_to_database, view_foods_in_database, update_food_to_database, delete_food_from_database
from models import Food

def create_food(food_entry: Food):
    food_id = add_food_to_database(
        food_name=food_entry.name,
        calories=food_entry.calories,
        protein=food_entry.protein,
        serving_size=food_entry.serving_size
    )
    return food_id