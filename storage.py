import json

def save_foods(foods):
    with open("foods.json", "w") as file:
        json.dump(foods, file)

def load_foods():
    try:
        with open("foods.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_log(food_entries):
    with open("food_logs.json", "w") as file:
        json.dump(food_entries, file)

def load_log():
    try:
        with open("food_logs.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_goals(Daily_goals):
    with open("Daily_goals.json", "w") as file:
        json.dump(Daily_goals, file)

def load_goals():
    try:
        with open("Daily_goals.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
