from db import get_connection_pg


def log_food_entry_to_database(food_id, amount_grams, calories, protein):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            INSERT INTO food_entries (food_id, amount_grams, calories, protein)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            ''', (food_id, amount_grams, calories, protein))

            entry_id = cursor.fetchone()[0]
    return entry_id

def get_food_by_id(food_id):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT id, name, calories, protein, serving_size
            FROM foods
            WHERE id = %s
        ''', (food_id,))

            food = cursor.fetchone()

    return food

def view_foods_in_database():
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT foods.name, food_entries.amount_grams, food_entries.calories, food_entries.protein 
            FROM food_entries
            JOIN foods 
            ON food_entries.food_id = foods.id
            ''')
            
            food_entries = cursor.fetchall()
            return food_entries

def get_foodentry_by_id(food_id):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT id, food_id, amount_grams, calories, protein
            FROM food_entries
            WHERE id = %s
        ''', (food_id,))

        food = cursor.fetchone()[0]

    return food

def update_food_entry_in_database(entry_id, food_id, amount_grams, calories, protein):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            UPDATE food_entries 
            SET food_id = %s,
                amount_grams = %s, 
                calories = %s, 
                protein = %s
            WHERE id = %s
            ''', (food_id, amount_grams, calories, protein, entry_id))
            
            if cursor.rowcount == 0:
                return None
    return {
            "id": entry_id,
            "food_id": food_id,
            "amount_grams": amount_grams,
            "calories": calories,
            "protein": protein
            }

def delete_foodentry_in_database(entry_id):
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            DELETE FROM food_entries
            WHERE id = %s
            ''', (entry_id,))
            
            if cursor.rowcount == 0:
                return None
    return {
            "message": f"Food entry with ID {entry_id} has been deleted."
            }

def calculate_totals_in_db():
    with get_connection_pg() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT  
                COALESCE(SUM(calories), 0), 
                COALESCE(SUM(protein), 0)
            FROM food_entries
        ''')
            result = cursor.fetchone()

    return result