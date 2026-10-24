from db import get_connection_pg

def set_daily_goals_in_database(goal_type, target_weight, daily_calorie_goal, daily_protein_goal):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            INSERT INTO goals (goal_type, target_weight, daily_calorie_goal, daily_protein_goal)
            VALUES (%s,%s,%s,%s)
            RETURNING id
            ''', (goal_type, target_weight, daily_calorie_goal, daily_protein_goal))
            
            if cursor.rowcount == 0:
                return None
            
            goal_id = cursor.fetchone()[0]

    return goal_id

def set_body_weight_in_database(current_weight, date):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            INSERT INTO body_weights (current_weight, date)
            VALUES (%s,%s)
            RETURNING id 
            ''', (current_weight, date))
            
            if cursor.rowcount == 0:
                return None
            
            body_weight_id = cursor.fetchone()[0]

    return body_weight_id 

def get_goals_in_database():
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT daily_calorie_goal, daily_protein_goal
            FROM goals
            ''')
            
            daily_goals = cursor.fetchall()
            
    return daily_goals

def view_body_weight_in_database():
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT current_weight, date
            FROM body_weights
            ''')
            view_weight = cursor.fetchall()

    return view_weight

def update_goal_in_database(goal_id, goal_type, target_weight, daily_calorie_goal, daily_protein_goal):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            UPDATE goals
            SET goal_type = %s, target_weight = %s, daily_calorie_goal = %s, daily_protein_goal = %s
            WHERE id = %s
            ''', (goal_type, target_weight, daily_calorie_goal, daily_protein_goal, goal_id))
            
            if cursor.rowcount == 0:
                return None

    return {
            "id": goal_id,
            "goal_type": goal_type,
            "target_weight": target_weight,
            "daily_calorie_goal": daily_calorie_goal,
            "daily_protein_goal": daily_protein_goal
            }


def update_body_weight_in_database(body_weight_id, current_weight, date):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            UPDATE body_weights 
            SET current_weight = %s, 
                date = %s
            WHERE id = %s
            ''', (current_weight, date, body_weight_id))
            
            if cursor.rowcount == 0:
                return None
            
    return {
            "id": body_weight_id,
            "current_weight": current_weight,
            "date": date
            }

def delete_goal_in_database(goal_id):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            DELETE 
            FROM goals
            WHERE id = %s
            ''', (goal_id,))
            
            if cursor.rowcount == 0:
                return None
                     
    return {
           "message": f"Goal entry with ID {goal_id} has been deleted."
           }

def delete_body_weight_in_database(body_weight_id: int):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            DELETE FROM body_weights 
            WHERE id = %s  
            ''', (body_weight_id,))
            
            if cursor.rowcount == 0:
                return None
    return{
            "message": f"Goal entry with ID {body_weight_id} has been deleted."
          }
