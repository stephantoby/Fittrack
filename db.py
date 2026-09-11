import sqlite3

def get_connection():
    connection = sqlite3.connect("fittrack.db")
    return connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS foods (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
calories REAL,
protein REAL,
serving_size REAL
)
''')

#cursor.execute('''
#SELECT name FROM foods
#''')

#foods = cursor.fetchall()
#print(foods)


cursor.execute('''
CREATE TABLE IF NOT EXISTS food_entries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
amount_grams REAL,
calories REAL,
protein REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS goals (
id INTEGER PRIMARY KEY AUTOINCREMENT,
daily_calories_goal REAL,
daily_protein_goal REAL
)
''')

connection.commit()
connection.close()