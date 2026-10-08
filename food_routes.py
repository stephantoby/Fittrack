from fastapi import status, HTTPException, APIRouter
from foods import view_foods_in_database, add_food_to_database, update_food_to_database, delete_food_from_database
from food_service import create_food
from models import Food, FoodResponse

router = APIRouter(prefix="/foods", tags=["Foods"])


@router.get("/", response_description= "List all foods", response_model= list[FoodResponse])
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

@router.post("/", status_code=status.HTTP_201_CREATED,  response_model = FoodResponse)
def add_food_entry(food_entry: Food):
    food_id = create_food(food_entry)
   
    return FoodResponse(
        id=food_id,
        name=food_entry.name,
        calories=food_entry.calories,
        protein=food_entry.protein,
        serving_size=food_entry.serving_size
    )

@router.put("/{food_id}", response_description= "Updated food entry",  response_model = FoodResponse)
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

@router.delete("/{food_id}", response_description= "Deleted food entry")
def delete_food_entry(food_id: int):
    result = delete_food_from_database(food_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Food entry not found.")
    return result