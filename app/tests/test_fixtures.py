import pytest

@pytest.fixture
def sample_food():
    return {
        "name": "Rice",
        "calories": 300,
        "protein": 6
    }


def test_food_name(sample_food):
    assert sample_food["name"] == "Rice"