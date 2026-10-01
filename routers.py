from fastapi import APIRouter

router = APIRouter()

@router.get("/view-foods/")
def get_food():
    return [{"name": "massa"}]
