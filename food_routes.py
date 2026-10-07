from fastapi import status, HTTPException, APIRouter
from pydantic import BaseModel
from foods import view_foods_in_database, add_food_to_database, update_food_to_database, delete_food_from_database

router = APIRouter()

class Food(BaseModel):
    name: str
    calories: float
    protein: float
    serving_size: int       

class FoodResponse(BaseModel):
    id: int
    name: str
    calories: float
    protein: float
    serving_size: int

@router.get("/foods", response_description= "List all foods", response_model= list[FoodResponse])
def view_food():
    foods = view_foods_in_database()

    result = []
    for food in foods:
        food_dic = { "id": food[0],
                     "name": food[1],
                     "calories": food[2], 
                     "protein": food[3], 
                     "serving_size": food[4]
                     }
        result.append(food_dic)

    return result

@router.post("/foods", status_code=status.HTTP_201_CREATED,  response_model = FoodResponse)
def add_food_entry(food_entry: Food):
    food_id = add_food_to_database(
        food_name=food_entry.name,
        calories=food_entry.calories,
        protein=food_entry.protein,
        serving_size=food_entry.serving_size
    )
   

    return FoodResponse(
        id=food_id,
        name=food_entry.name,
        calories=food_entry.calories,
        protein=food_entry.protein,
        serving_size=food_entry.serving_size
    )

@router.put("/foods/{food_id}", response_description= "Updated food entry",  response_model = FoodResponse)
def update_food_entry(food_id: int, food_entry: Food):
    result = update_food_to_database(food_id, food_entry.name, food_entry.calories, food_entry.protein, food_entry.serving_size)
    if result is None:
        raise HTTPException(status_code=404, detail="Food entry not found.")

    return FoodResponse(
        id= food_id,
        name= food_entry.name,
        calories= food_entry.calories,
        protein=food_entry.protein,
        serving_size=food_entry.serving_size
    )

@router.delete("/foods/{food_id}", response_description= "Deleted food entry")
def delete_food_entry(food_id: int):
    result = delete_food_from_database(food_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Food entry not found.")
    return result