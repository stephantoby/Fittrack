from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_food():
    response = client.get("/foods/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_food_invalid_calories():
    response = client.post(
        "/foods/",
        json={
            "name": "Chicken",
            "calories": "hello",
            "protein": 31,
            "serving_size": 100
        }
    )

    assert response.status_code == 422