from app.models import Body_weight
from goals import set_body_weight_in_database

def set_body_weight(body_weight: Body_weight):
    body_weight_id = set_body_weight_in_database(
        current_weight= body_weight.current_weight,
        date= body_weight.date
        )
    return body_weight_id 