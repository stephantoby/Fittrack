import pytest

def calculate_entry_nutrition(food_to_log, amount):
    calories = (food_to_log[2] * amount) / food_to_log[4]
    protein = (food_to_log[3] * amount) / food_to_log[4]

    return (calories, protein)

# Your completed Unit Test
def test_calculate_entry_nutrition_extreme():
    # 1. ARRANGE
    # Index 2 = 300 cal, Index 3 = 20g protein, Index 4 = 100g base serving
    mock_food = ["Apple", "Snack", 70, 6.0, 50] 
    log_amount = -50  # User is logging 50 grams (half a serving)
    
    # Mathematical expectation: 
    # Calories: (300 * 50) / 100 = 150
    # Protein:  (20 * 50) / 100 = 10
    #expected_result = (150.0, 10.0)

    # 2. ACT
    result = calculate_entry_nutrition(mock_food, log_amount)

    # 3. ASSERT
    assert result == (-70.0, -6.0)

def test_calculate_nutrition_division_by_zero():
    broken_food = ["Bad Data Food", "Error", 200, 10, 0] # Base weight is 0!
    
    with pytest.raises(ZeroDivisionError):
        calculate_entry_nutrition(broken_food, 100)

def calculate_remaining(daily_calorie_goal, daily_protein_goal, total_calories_consumed, total_protein_consumed):
    remaining_calories = daily_calorie_goal - total_calories_consumed
    remaining_protein = daily_protein_goal - total_protein_consumed
    return (remaining_calories, remaining_protein)

# 1. EXTREME CASE: Perfect Match (Zero Remaining)
# What if the user hits their calorie and protein goals exactly to the digit?
def test_calculate_remaining_perfect_match():
    # Arrange & Act
    result = calculate_remaining(2000, 150, 2000, 150)
    
    # Assert
    assert result == (0, 0)

# 2. EXTREME CASE: Massive Overeating (Negative Remaining)
# What if the user goes way over their daily allowances? 
# This checks if your function safely outputs negative numbers (surplus).
def test_calculate_remaining_massive_surplus():
    # User goal is 1800cal / 120g protein, but they consume 3500cal / 200g protein
    result = calculate_remaining(1800, 120, 3500, 200)
    
    assert result == (-1700, -80)

# 3. EXTREME CASE: Total Fasting (Zero Consumed)
# What if it's the start of the day and the user hasn't logged a single thing yet?
def test_calculate_remaining_zero_consumed():
    result = calculate_remaining(2500, 180, 0, 0)
    
    assert result == (2500, 180)

# 4. EXTREME CASE: Zero Goals Set
# What if a user clears their profile and sets their goals to 0, but still logs food?
def test_calculate_remaining_zero_goals():
    result = calculate_remaining(0, 0, 500, 40)
    
    assert result == (-500, -40)
