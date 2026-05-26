"""FastAPI application entry point."""

from fastapi import FastAPI

from src.api.router import api_router

app = FastAPI(title="BUS", description="Background Unified Sender")

app.include_router(api_router)
