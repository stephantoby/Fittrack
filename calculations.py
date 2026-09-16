from validation import get_valid_serving
from db import get_connection

def calculate_totals():
    total_calories = 0
    total_protein = 0

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        SELECT SUM(calories), SUM(protein)
        FROM food_entries
    ''')


    result = cursor.fetchall()

    connection.close()

    row = result[0]

    total_calories = row[0]
    total_protein = row[1]

    if total_calories is None or total_protein is None:
         total_calories = 0
         total_protein = 0 

    return (total_calories, total_protein)


def get_amount(food_to_log):
        amount = get_valid_serving(f"\nHow many grams of {food_to_log[1]} did you eat? ")
        return amount

def calculate_entry_nutrition(food_to_log, amount):
    calories = (food_to_log[2] * amount ) / food_to_log[4]
    protein = (food_to_log[3] * amount ) / food_to_log[4]

    return (calories, protein)

def calculate_remaining():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    SELECT daily_calorie_goal, SUM(calories)
    FROM goals 
    JOIN food_entries
    ON goals.id = food_entries.id 
  ''')

    result = cursor.fetchall()

    row = result[0]

    return row[0] - row[1]




def calculate_progress():
     return