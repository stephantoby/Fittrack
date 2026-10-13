from goals import set_daily_goals_in_database
from app.models import Goals

def set_daily_goals(goals: Goals):
    goal_id = set_daily_goals_in_database(
        goal_type= goals.goal_type,
        target_weight= goals.target_weight,
        daily_calorie_goal=goals.daily_calorie_goal,
        daily_protein_goal=goals.daily_protein_goal
        )
    return goal_id