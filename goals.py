from db import get_connection
from validation import get_valid_weight, get_valid_calories, get_valid_protein

def set_daily_goals():
    while True:
        goal_type = input("Enter goal type (Bulk/Cut/Maintain): ").strip()
    
        if goal_type == "":
            print("\n Goal type cannot be empty. Please enter a valid type.")
            continue
        #elif get_valid_goal_type(goal_type):
        else:
            break
    
    body_weight = get_valid_weight("Enter your body weight(kg): ")
    daily_calorie_goal = get_valid_calories("Enter your daily calorie goal: ")
    daily_protein_goal = get_valid_protein("Enter your daily protein goal: ")
 
    
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO goals (goal_type, target_weight, daily_calorie_goal, daily_protein_goal)
    VALUES (?,?,?,?)
    ''', (goal_type, body_weight, daily_calorie_goal, daily_protein_goal))
    
    connection.commit()
    connection.close()
    print("\n")
    print("Successfully Set")

def log_body_weight():
    return

def view_goals(daily_goals):
    if not daily_goals:
        print("\nNo daily goals have been set yet.")
        return
    
    print("================================")
    print("          Daily Goals!       ")
    print("================================\n")

    for number, goal in enumerate(daily_goals, start= 1):
        print(f"{number}.")
        print(f"Daily Calorie Goal: {goal['daily_calorie_goal']} kcal")
        print(f"Daily Protein Goal: {goal['daily_protein_goal']} g")
        print("-----------------------------")

def view_body_weight():
    return
  