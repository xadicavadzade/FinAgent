from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.dashboard import router as dashboard_router
from app.api.ask import router as ask_router

app = FastAPI(
    title="FinAgent API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5500",
        "https://finance-agent-4.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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