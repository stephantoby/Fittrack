from fastapi import APIRouter, status, HTTPException
from goals import view_goals_in_database, update_goal_in_database
from app.services.goal_service import set_daily_goals
from app.models import Goals, GoalResponse

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

@router.post("/", status_code = status.HTTP_201_CREATED, response_model =GoalResponse)
def set_goals(goals: Goals):
    goal_id = set_daily_goals(goals)

    return {
        "id": goal_id,
        "goal_type": goals.goal_type,
        "target_weight": goals.target_weight,
        "daily_calorie_goal": goals.daily_calorie_goal,
        "daily_protein_goal": goals.daily_protein_goal
    }

@router.put("/{goal_id}", response_description= "Update goals", response_model=GoalResponse)
def update_goal(goal_id: int , goals: Goals):
    result = update_goal_in_database(goal_id, goals.goal_type, goals.target_weight, goals.daily_calorie_goal, goals.daily_protein_goal)
    if result is None:
        raise HTTPException(status_code=404, detail="goal entry not found.")
    
    return GoalResponse(
        id= goal_id,
        goal_type= goals.goal_type,
        target_weight= goals.target_weight,
        daily_calorie_goal= goals.daily_calorie_goal,
        daily_protein_goal= goals.daily_protein_goal
    )