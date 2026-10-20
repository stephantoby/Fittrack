import pytest

FOOD = {"name": "Rice", "calories": 300, "protein": 6, "serving_size": 100}
GOAL = {"goal_type": "bulk", "target_weight": 82, "daily_calorie_goal": 2800, "daily_protein_goal": 160}
WEIGHT = {"current_weight": 76, "date": "2026-10-19"}


def create_food(client):
    response = client.post("/foods/", json=FOOD)
    assert response.status_code == 201, response.text
    return response.json()["id"]


def test_empty_lists(client):
    for path in ("/foods/", "/entries/", "/goals/", "/body_weight/"):
        response = client.get(path)
        assert response.status_code == 200, response.text
        assert response.json() == []


def test_food_crud(client):
    food_id = create_food(client)
    assert client.get("/foods/").json()[0]["name"] == "Rice"
    updated = {**FOOD, "name": "Brown rice"}
    response = client.put(f"/foods/{food_id}", json=updated)
    assert response.status_code == 200, response.text
    assert response.json()["name"] == "Brown rice"
    assert client.delete(f"/foods/{food_id}").status_code == 200
    assert client.get("/foods/").json() == []
    assert client.put(f"/foods/{food_id}", json=FOOD).status_code == 404
    assert client.delete(f"/foods/{food_id}").status_code == 404


@pytest.mark.parametrize("field,bad_value", [("calories", "invalid"), ("protein", "invalid"), ("serving_size", "invalid")])
def test_food_invalid_numeric_input(client, field, bad_value):
    assert client.post("/foods/", json={**FOOD, field: bad_value}).status_code == 422
    assert client.get("/foods/").json() == []


def test_entries_crud_and_missing_food(client):
    assert client.post("/entries/", json={"food_id": 999, "amount_grams": 100}).status_code == 404
    food_id = create_food(client)
    response = client.post("/entries/", json={"food_id": food_id, "amount_grams": 50})
    assert response.status_code == 201, response.text
    entry = response.json()
    assert entry["calories"] == pytest.approx(150)
    assert entry["protein"] == pytest.approx(3)
    entry_id = entry["id"]
    assert len(client.get("/entries/").json()) == 1
    response = client.put(f"/entries/{entry_id}", json={"food_id": food_id, "amount_grams": 100})
    assert response.status_code == 200, response.text
    assert response.json()["calories"] == pytest.approx(300)
    assert client.delete(f"/entries/{entry_id}").status_code == 200
    assert client.get("/entries/").json() == []
    assert client.put(f"/entries/{entry_id}", json={"food_id": food_id, "amount_grams": 100}).status_code == 404
    assert client.delete(f"/entries/{entry_id}").status_code == 404


def test_goals_crud(client):
    response = client.post("/goals/", json=GOAL)
    assert response.status_code == 201, response.text
    goal_id = response.json()["id"]
    assert len(client.get("/goals/").json()) == 1
    changed = {**GOAL, "daily_calorie_goal": 3000}
    response = client.put(f"/goals/{goal_id}", json=changed)
    assert response.status_code == 200, response.text
    assert response.json()["daily_calorie_goal"] == 3000
    assert client.delete(f"/goals/{goal_id}").status_code == 200
    assert client.get("/goals/").json() == []
    assert client.put(f"/goals/{goal_id}", json=GOAL).status_code == 404
    assert client.delete(f"/goals/{goal_id}").status_code == 404


def test_body_weight_crud(client):
    response = client.post("/body_weight/", json=WEIGHT)
    assert response.status_code == 201, response.text
    weight_id = response.json()["id"]
    assert len(client.get("/body_weight/").json()) == 1
    changed = {**WEIGHT, "current_weight": 77}
    response = client.put(f"/body_weight/{weight_id}", json=changed)
    assert response.status_code == 200, response.text
    assert response.json()["current_weight"] == 77
    assert client.delete(f"/body_weight/{weight_id}").status_code == 200
    assert client.get("/body_weight/").json() == []
    assert client.put(f"/body_weight/{weight_id}", json=WEIGHT).status_code == 404
    assert client.delete(f"/body_weight/{weight_id}").status_code == 404


def test_multiple_goals_and_weights_are_returned(client):
    for n in (1, 2):
        assert client.post("/goals/", json={**GOAL, "goal_type": f"goal-{n}"}).status_code == 201
        assert client.post("/body_weight/", json={**WEIGHT, "current_weight": 75 + n}).status_code == 201
    assert len(client.get("/goals/").json()) == 2
    assert len(client.get("/body_weight/").json()) == 2
