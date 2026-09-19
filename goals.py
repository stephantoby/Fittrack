from db import get_connection
from validation import get_valid_weight, get_valid_calories, get_valid_protein, get_valid_date

def set_daily_goals():
    while True:
        goal_type = input("Enter goal type (Bulk/Cut/Maintain): ").strip()
    
        if goal_type == "":
            print("\n Goal type cannot be empty. Please enter a valid type.")
            continue
        #elif get_valid_goal_type(goal_type):
        else:
            break
    
    target_weight = get_valid_weight("Enter your target body weight(kg): ")
    daily_calorie_goal = get_valid_calories("Enter your daily calorie goal: ")
    daily_protein_goal = get_valid_protein("Enter your daily protein goal: ")
 
    
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO goals (goal_type, target_weight, daily_calorie_goal, daily_protein_goal)
    VALUES (?,?,?,?)
    ''', (goal_type, target_weight, daily_calorie_goal, daily_protein_goal))
    
    connection.commit()
    connection.close()
    print("\n")
    print("Successfully Set")

def log_body_weight():
    current_weight = get_valid_weight("Enter your current body weight(kg): ")
    date = get_valid_date("Enter valid date (YYYY-MM-DD): ")
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO body_weights (current_weight, date)
    VALUES (?,?)
  ''', (current_weight, date))

    connection.commit()
    connection.close()
    print("\n")
    print("Successfully Set") 


def view_goals():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    SELECT daily_calorie_goal, daily_protein_goal
    FROM goals
  ''')

    daily_goals = cursor.fetchall()

    connection.close()

    if not daily_goals:
        print("\nNo daily goals have been set yet.")
        return
    
    print("================================")
    print("          DAILY GOALS!       ")
    print("================================\n")

    for number, goal in enumerate(daily_goals, start= 1):
        print(f"{number}.")
        print(f"Daily Calorie Goal: {goal[0]} kcal")
        print(f"Daily Protein Goal: {goal[1]} g")
        print("-----------------------------")

def view_body_weight():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    SELECT current_weight, date
    FROM body_weights
  ''')

    view_weight = cursor.fetchall()

    connection.close()

    if not view_weight:
            print("\nNo weight has been set yet.")
            return
    print("================================")
    print("        BODY WEIGHT!       ")
    print("================================\n")
    
    for number, weight in enumerate(view_weight, start= 1):
        print(f"{number}. {weight[0]} - {weight[1]}")
    

    
  