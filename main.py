from fastapi import FastAPI
from app.api.food_routes import router
from app.api.entries_routes import router as entries_router
from app.api.goal_routes import router as goals_router
from app.api.body_weight_routes import router as body_weight_router

def start_app():
    app = FastAPI()
    app.include_router(router)
    app.include_router(entries_router)
    app.include_router(goals_router)
    app.include_router(body_weight_router)

    return app

app = start_app()

def main():
    if __name__ == "__main__":
        main()
