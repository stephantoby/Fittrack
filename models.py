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