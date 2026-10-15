from fastapi import APIRouter, status, HTTPException
from app.models import Body_weight, Body_weight_response
from goals import view_body_weight_in_database, update_body_weight_in_database, delete_body_weight_in_database
from app.services.body_weight_service import set_body_weight

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

@router.post("/", status_code = status.HTTP_201_CREATED, response_model =Body_weight_response)
def set_weight(body_weight: Body_weight):
    body_weight_id = set_body_weight(body_weight)

    return {
        "id": body_weight_id,
        "goal_type": body_weight.current_weight,
        "target_weight": body_weight.date
    }

@router.put("/{body_weight_id}", response_description= "Update body weight", response_model=Body_weight_response)
def update_goal(body_weight_id: int , body_weight: Body_weight):
    result = update_body_weight_in_database(body_weight_id, body_weight.current_weight, body_weight.date)
    if result is None:
        raise HTTPException(status_code=404, detail="goal entry not found.")
    
    return Body_weight_response(
        id= body_weight_id,
        current_weight= body_weight.current_weight,
        date= body_weight.date
    )

@router.delete("/{body_weight_id}",response_description= "Deleted weight")
def delete_goals(body_weight_id: int):
    result = delete_body_weight_in_database(body_weight_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Weight not found.")
    return result

