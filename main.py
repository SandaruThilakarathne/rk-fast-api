from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user, schedules

def create_app() -> FastAPI:
    app = FastAPI()
    origins = [
        "*"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(
        user.router,
        prefix="/users",
    )
    app.include_router(
        schedules.router,
        prefix="/schedules",
    )

    return app


app = create_app()