from validation import get_valid_calories, get_valid_protein, get_valid_serving
from db import get_connection
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/view-foods")
def view_foods():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT name, calories, protein, serving_size FROM foods
        ''')

        foods = cursor.fetchall()
        connection.close()

        return {"Display" : foods }
