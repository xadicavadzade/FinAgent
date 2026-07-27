from fastapi import FastAPI

from app.api.dashboard import router as dashboard_router
from app.api.ask import router as ask_router




app = FastAPI(
    title="FinAgent API",
    version="1.0.0",
)

app.include_router(
    dashboard_router,
    prefix="/api/v1",
    tags=["Dashboard"],
)

app.include_router(
    ask_router,
    prefix="/api/v1",
    tags=["Ask AI"],
)
