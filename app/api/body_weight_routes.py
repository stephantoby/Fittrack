from fastapi import APIRouter
from app.models import Body_weight, Body_weight_response
from goals import view_body_weight_in_database

router = APIRouter(prefix="/body_weight", tags=["Body_weight"])

@router.get("/", response_description= "List body_weight")
def get_body_weight():
    body_weight = view_body_weight_in_database()
    result = []
    for weight in body_weight:
        weight_dic = { "current_weight": weight[0],
                    "date": weight[1]
                    }
        result.append(weight_dic)
        
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

@router.delete("/{goal_id}",response_description= "Deleted goal entries")
def delete_goals(goal_id: int):
    result = delete_goal_in_database(goal_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Goal entry not found.")
    return result

