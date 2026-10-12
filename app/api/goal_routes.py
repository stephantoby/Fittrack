from fastapi import APIRouter
from goals import view_goals_in_database

router = APIRouter(prefix="/goals", tags=["Goals"])

@router.get("/", response_description= "List goals")
def get_goals():
    goals = view_goals_in_database()
    result = []
    for goal in goals:
        goal_dic = { "daily_calorie_goal": goal[0],
                    "daily_protein_goal": goal[1]
                    }
        result.append(goal_dic)
        
        return result