import sqlite3

connection = sqlite3.connect("fittrack.db")
cursor = connection.cursor()

cursor.execute()

connection.close()