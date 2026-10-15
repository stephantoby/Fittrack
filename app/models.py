from pydantic import BaseModel
from datetime import date

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
    food_id: int
    amount_grams: float

class FoodEntryResponse(BaseModel):
    id: int
    food_id: int
    amount_grams: float
    calories: float
    protein: float

class Goals(BaseModel):
    goal_type: str
    target_weight: float 
    daily_calorie_goal: float
    daily_protein_goal: float

class GoalResponse(BaseModel):
    id: int
    goal_type: str
    target_weight: float
    daily_calorie_goal: float
    daily_protein_goal: float

class Body_weight(BaseModel):
    current_weight: float
    date: date

class Body_weight_response(BaseModel):
    id: int
    current_weight: float
    date: date