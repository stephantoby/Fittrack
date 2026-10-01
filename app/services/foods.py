from db import get_connection
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/view-foods")
def view_foods():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM foods
        ''')

        foods = cursor.fetchall()
        connection.close()

        for food in foods:
              food_dic = { "id": food[0],
                           "name": food[1],
                           "calories": food[2], 
                           "protein": food[3], 
                           "serving_size": food[4]
                           }

        return food_dic
