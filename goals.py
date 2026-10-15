from db import get_connection
from validation import get_valid_weight, get_valid_calories, get_valid_protein, get_valid_date

def set_daily_goals_in_database(goal_type, target_weight, daily_calorie_goal, daily_protein_goal):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO goals (goal_type, target_weight, daily_calorie_goal, daily_protein_goal)
    VALUES (?,?,?,?)
    ''', (goal_type, target_weight, daily_calorie_goal, daily_protein_goal))

    if cursor.rowcount == 0:
        return None
    
    goal_id = cursor.lastrowid
    
    connection.commit()
    connection.close()

    return goal_id

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
 
    result = set_daily_goals_in_database(goal_type, target_weight, daily_calorie_goal, daily_protein_goal)

    if result is None:
        return None
    
    print("\n")
    print("Successfully Set")

def set_body_weight_in_database(current_weight, date):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO body_weights (current_weight, date)
    VALUES (?,?)
    ''', (current_weight, date))

    if cursor.rowcount == 0:
        return None
    
    body_weight_id = cursor.lastrowid
    
    connection.commit()
    connection.close()

    return body_weight_id

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

def view_goals_in_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    SELECT daily_calorie_goal, daily_protein_goal
    FROM goals
    ''')
    
    daily_goals = cursor.fetchall()
    
    connection.close()

    return daily_goals

def view_goals():

    daily_goals = view_goals_in_database()

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

def view_body_weight_in_database():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    SELECT current_weight, date
    FROM body_weights
    ''')
    
    view_weight = cursor.fetchall()
    
    connection.close()

    return view_weight


def view_body_weight():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    SELECT current_weight, date
    FROM body_weights
  ''')

    view_weight = view_body_weight_in_database


    if not view_weight:
        print("\nNo weight has been set yet.")
        return
    print("================================")
    print("        BODY WEIGHT!       ")
    print("================================\n")
    
    for number, weight in enumerate(view_weight, start= 1):
        print(f"{number}. {weight[0]} - {weight[1]}")

def display_weights(weight_list):
    while True:
        print("   \nYour Weights:   \n")
        print("0. Return to main menu")

        for number, weight in enumerate(weight_list, start=1):
            print(f"{number}. {weight[1]} - {weight[2]}") 
    
        try:
            choice = int(input("\nChoose an Entry: "))
            if choice == 0:
                return None
            if choice < 0 or choice > len(weight_list):
                print("\nInvalid choice. Please enter a valid number.")
                continue
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue
    
        if choice >= 1 and choice <= len(weight_list):
            weight_to_update = weight_list[choice - 1]
            return weight_to_update

def update_goal_in_database(goal_id, goal_type, target_weight, daily_calorie_goal, daily_protein_goal):
    connection = get_connection()
    try:
        cursor = connection.cursor()
    
        cursor.execute('''
            UPDATE goals
            SET goal_type = ?, target_weight = ?, daily_calorie_goal = ?, daily_protein_goal = ?
            WHERE id = ?
        ''', (goal_type, target_weight, daily_calorie_goal, daily_protein_goal, goal_id))
    
        if cursor.rowcount == 0:
            return None
    
        connection.commit()
        return {
        "id": goal_id,
        "goal_type": goal_type,
        "target_weight": target_weight,
        "daily_calorie_goal": daily_calorie_goal,
        "daily_protein_goal": daily_protein_goal
        }
    finally:
        connection.close()

def update_body_weight_in_database(body_weight_id, current_weight, date):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        UPDATE body_weights 
        SET current_weight = ?, 
            date = ?
        WHERE id = ?
    ''', (current_weight, date, body_weight_id))
   
    connection.commit()
    connection.close()
    
    return {
    "id": body_weight_id,
    "current_weight": current_weight,
    "date": date
    }
   
def update_body_weight():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    SELECT *
    FROM body_weights
    ''')
    
    body_weights = cursor.fetchall()

    weight_to_update = display_weights(body_weights)

    if weight_to_update is None:
        return 
    
    print(f"\nYou have selected: {weight_to_update[1]} - {weight_to_update[2]} ")
    
    input(f"\nPress Enter to update the details")
    
    print(f"\nCurrent weight: {weight_to_update[1]} ")
    new_weight = get_valid_weight(f"Enter the new weight for '{weight_to_update[1]}': ")
    new_date = get_valid_date(f"Enter the new date: ")
    
    cursor.execute('''
        UPDATE body_weights 
        SET current_weight = ?, 
            date = ?
        WHERE id = ?
    ''', (new_weight, new_date, weight_to_update[0]))
    
    connection.commit()
    connection.close()
    
    input(f"\n Weight history has been updated. Press Enter to return to the menu...")

def delete_goal_in_database(goal_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
    
        cursor.execute('''
        DELETE 
        FROM goals
        WHERE id = ?
        ''', (goal_id,))
    
        if cursor.rowcount == 0:
            return None
    
        connection.commit()  
        return {
            "message": f"Goal entry with ID {goal_id} has been deleted."
            }
    finally:
        connection.close()

def delete_body_weight_in_database(body_weight_id: int):
    connection = get_connection()
    try:
        cursor = connection.cursor()

        cursor.execute('''
        DELETE FROM body_weights 
        WHERE id = ?  
        ''', (body_weight_id,))
    
        connection.commit()
        return{
            "message": f"Goal entry with ID {body_weight_id} has been deleted."
            }
    finally:
        connection.close()


def delete_body_weight():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    SELECT *
    FROM body_weights
    ''')
    
    body_weights = cursor.fetchall()
    
    weight_to_update = display_weights(body_weights)
    
    if weight_to_update is None:
        return 
    
    print(f"\nYou have selected: {weight_to_update[1]} - {weight_to_update[2]} ")
    
    input(f"\nPress Enter to delete weight")
    
    cursor.execute('''
    DELETE FROM body_weights 
    WHERE id = ?  
    ''', (weight_to_update[0],))
    
    connection.commit()
    connection.close()
    
    input(f"\n Weight history has been updated. Press Enter to return to the menu...")
    
  