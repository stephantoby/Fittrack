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
#INSERT INTO foods (name, calories, protein, serving_size) VALUES
#('Apple', 52, 0.3, 100),
#('Banana', 89, 1.1, 100),   
#('Almonds', 579, 21.2, 100),
#('Egg', 155, 13, 50),
#('Oatmeal', 68, 2.4, 40),
#('Greek Yogurt', 59, 10, 150),
#('Brown Rice', 123, 2.6, 100)
#''')

#cursor.execute('''
#SELECT name FROM foods
#''')

#foods = cursor.fetchall()
#print(foods)


cursor.execute('''
CREATE TABLE IF NOT EXISTS food_entries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
food_id INTEGER NOT NULL,
amount_grams REAL,
calories REAL,
protein REAL,
FOREIGN KEY (food_id) REFERENCES foods(id)
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