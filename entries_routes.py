from fastapi import APIRouter
from entries import view_foods_in_database 
from models import FoodEntry, FoodEntryResponse

router = APIRouter(prefix="/entries", tags=["Entries"])

@router.get("/", response_description= "List all food entries")
def view_food():
    food_entries = view_foods_in_database()
    result = []
    for food in food_entries:
        food_dic = {    
            "name": food[0],
            "amount_grams": food[1],
            "calories": food[2],
            "protein": food[3]
        }
        result.append(food_dic)
        
    return result

