from fastapi import FastAPI
from app.api.food_routes import router
from app.api.entries_routes import router as entries_router
from app.api.goal_routes import router as goals_router
from app.api.body_weight_routes import router as body_weight_router
from fastapi.middleware.cors import CORSMiddleware

def start_app():
    app = FastAPI()
    app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)
    app.include_router(router)
    app.include_router(entries_router)
    app.include_router(goals_router)
    app.include_router(body_weight_router)

    return app

app = start_app()

def main():
    if __name__ == "__main__":
        main()
