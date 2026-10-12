from fastapi import APIRouter, status, HTTPException
from entries import view_foods_in_database, delete_foodentry_in_database
from models import FoodEntry, FoodEntryResponse
from entries_services import create_food_entry, update_food_entry

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

@router.post("/", status_code = status.HTTP_201_CREATED, response_model =FoodEntryResponse)
def log_food_entry(food_entry: FoodEntry):
    try:
        food_entry_id, calories, protein = create_food_entry(food_entry)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    return FoodEntryResponse(
        id=food_entry_id,
        food_id=food_entry.food_id,
        amount_grams=food_entry.amount_grams,
        calories=calories,
        protein=protein
    )
@router.put("/{entry_id}", response_description= "Updated food entry", response_model=FoodEntryResponse)
def update_entry(entry_id: int, food_entry: FoodEntry):
    result = update_food_entry(entry_id, food_entry)

    if result is None:
            raise HTTPException(status_code=404, detail="Food entry not found.")
    
    return FoodEntryResponse(
        id=result["id"],
        food_id=result["food_id"],
        amount_grams=result["amount_grams"],
        calories=result["calories"],
        protein=result["protein"]
    )

@router.delete("/{entry_id}", response_description= "Deleted food entry")
def delete_food_entry(entry_id: int):
    result = delete_foodentry_in_database(entry_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Food entry not found.")
    return result
    