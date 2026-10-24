from db import get_connection_pg

def add_food_to_database(food_name, calories, protein, serving_size):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO foods (name, calories, protein, serving_size)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (food_name, calories, protein, serving_size)
            )

            food_id = cursor.fetchone()[0]

    return food_id

def get_foods_in_database():
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT * FROM foods
            ''')
            
            foods = cursor.fetchall()

    return foods

def update_food_to_database(food_id, new_name, new_calories, new_protein, new_serving):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            UPDATE foods
            SET name = %s, calories = %s, protein = %s, serving_size = %s
            WHERE id = %s
            ''', (new_name, new_calories, new_protein, new_serving, food_id))

            if cursor.rowcount == 0:
                return None

    return {
            "id": food_id,
            "name": new_name,
            "calories": new_calories,
            "protein": new_protein,
            "serving_size": new_serving
           }

def delete_food_from_database(food_id):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:

            cursor.execute('''
            DELETE FROM foods 
            WHERE id = %s
            ''', (food_id,))
            
            if cursor.rowcount == 0:
                return None

    return {
            "message": f"Food entry with ID {food_id} has been deleted."
           }
