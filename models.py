from pydantic import BaseModel

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

class FoodEntry(BaseModel):
    id: int
    food_id: int
    amount_grams: float
    calories: float
    protein: float

class FoodEntryResponse(BaseModel):
    food_id: int
    amount_grams: float
    calories: float
    protein: float