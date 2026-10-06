from unittest import result

from validation import *
from foods import *
from entries import *
from calculations import *
from goals import *
from db import get_connection
#import uvicorn
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
#from .routers import get_food

app = FastAPI()
#app.include_router(get_food.router)


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

@app.get("/foods", response_description= "List all foods", response_model= list[FoodResponse])
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

@app.post("/foods", status_code=status.HTTP_201_CREATED,  response_model = FoodResponse)
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

@app.put("/foods/{food_id}", response_description= "Updated food entry",  response_model = FoodResponse)
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

@app.delete("/foods/{food_id}", response_description= "Deleted food entry")
def delete_food_entry(food_id: int):
    result = delete_food_from_database(food_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Food entry not found.")
    return result

def main():

    while True:
         print("================================")
         print("            FITTRACK      ")
         print("================================\n")
         print("1. Food Management")
         print("2. Daily Nutrition")
         print("3. Goals & Body Weight")
         print("4. Exit\n")

         try:
             choice = int(input("Choose an option: "))
         except ValueError:
             print("Invalid input. Please enter a number")
             continue
         print("\n")

         if choice == 1:
             while True:
                print("================================")
                print("        FOOD MANAGEMENT      ")
                print("================================\n")
                print("1. Add Food")
                print("2. Update Food")
                print("3. View Foods")
                print("4. Delete Food")
                print("5. Return")
                print("--------------------------------")

                try:
                    choice = int(input("Choose an option: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                print("\n")


                if choice == 1:
                    add_food()
                    input(f"\nPress Enter to return to the menu...")

                elif choice == 2:
                    if update_food() == None:
                        input("Press Enter to return to the menu...\n")
                    else:
                        input(f"\nFood has been updated. Press Enter to return to the menu...")
                 
                elif choice == 3:
                  return  

                elif choice == 4:
                    delete_food()
                    input(f"\nPress Enter to return to the menu...")

                elif choice == 5:
                    break
         
                else:
                    print("Invalid choice. Please try again.")

         elif choice == 2:
             while True:
                print("================================")
                print("        DAILY NUTRITION      ")
                print("================================\n")
                print("1. View Daily Totals")
                print("2, View Remaining Nutrition")
                print("3. View Food Log")
                print("4. Log Food")
                print("5. Update Food Entries")
                print("6. Delete Food Entries")
                print("7. Return\n")

                try:
                    choice = int(input("Choose an option: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                print("\n")

                
                if choice == 1:
                    connection = get_connection()
                    cursor = connection.cursor()

                    cursor.execute('''
                    SELECT COUNT(id)
                    FROM food_entries
                  ''')
                    result = cursor.fetchall()
                    food_entries = result[0]
                    total_calories, total_protein = calculate_totals()
                    print("========Daily Totals========")
                    print(f"\nCalories: {total_calories} kcal")
                    print(f"Protein: {total_protein} g")
                    print(f"Foods Logged: {(food_entries[0])}")
                    print("--------------------------------")
                    input(f"\nPress Enter to return to the menu...")

                    connection.close()

                elif choice == 2:
                    connection = get_connection()
                    cursor = connection.cursor()
                    
                    cursor.execute('''
                    SELECT daily_calorie_goal, daily_protein_goal
                    FROM goals
                    ''')
                    
                    result = cursor.fetchall()
                    
                    row = result[0] 
                    
                    daily_calorie_goal = row[0]
                    daily_protein_goal = row[1]
                    
                    total_calories_consumed, total_protein_consumed = calculate_totals()

                    connection.close()
                    
                    print("========Nutrition Remaining========")
                    print(f"\nCalories: {total_calories_consumed} kcal / Goal: {daily_calorie_goal} kcal")
                    print(f"Protein: {total_protein_consumed} g / Goal: {daily_protein_goal} g")
                    print("--------------------------------")
                    remaining_calories, remaining_protein = calculate_remaining(daily_calorie_goal, daily_protein_goal, total_calories_consumed, total_protein_consumed)
                    print(f"\nCalories remaining: {remaining_calories}")
                    print(f"Protein remaining: {remaining_protein}")
                    input(f"\nPress Enter to return to the menu...")

                elif choice == 3:
                    view_food_log()
                elif choice == 4:
                    log_food() 
                elif choice == 5:
                    update_entry()
                elif choice == 6:
                    delete_food()   
                elif choice == 7:
                    break

                else:
                    print("Invalid choice. Please try again.")
   
         elif choice == 3: 
             while True:
                print("================================")
                print("        GOALS & BODY WEIGHT      ")
                print("================================\n")
                print("1. Set / Update Daily Goals")
                print("2. Log Body Weight")
                print("3. View Current Goals")
                print("4. View Body Weight")
                print("5. Update Body Weight")
                print("6. Delete Body Weight")
                print("7. Return\n")
                

                try:
                    choice = int(input("Choose an option: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                print("\n")

                if choice == 1:
                    set_daily_goals()
                elif choice == 2:
                    log_body_weight()
                elif choice == 3:
                    view_goals()
                elif choice == 4:
                    view_body_weight()
                elif choice == 5:
                    update_body_weight()
                elif choice == 6:
                    delete_body_weight()
                elif choice == 7:
                    break

                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
