import sqlite3

import pytest
from fastapi.testclient import TestClient

import db
from main import app

SCHEMA = """
CREATE TABLE foods (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, calories REAL, protein REAL, serving_size REAL);
CREATE TABLE food_entries (id INTEGER PRIMARY KEY AUTOINCREMENT, food_id INTEGER NOT NULL, amount_grams REAL, calories REAL, protein REAL, FOREIGN KEY (food_id) REFERENCES foods(id));
CREATE TABLE goals (id INTEGER PRIMARY KEY AUTOINCREMENT, goal_type TEXT, target_weight REAL, daily_calorie_goal REAL, daily_protein_goal REAL);
CREATE TABLE body_weights (id INTEGER PRIMARY KEY AUTOINCREMENT, current_weight REAL, date TEXT);
"""

@pytest.fixture
def client(tmp_path, monkeypatch):
    test_path = tmp_path / "fittrack_test.db"
    with sqlite3.connect(test_path) as connection:
        connection.executescript(SCHEMA)
    monkeypatch.setattr(db, "DATABASE_PATH", str(test_path))
    with TestClient(app) as test_client:
        yield test_client
