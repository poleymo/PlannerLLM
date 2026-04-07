from fastapi import FastAPI
from app.api.routes import agent as agt

app = FastAPI()

app.include_router(agt.router)
#python -m uvicorn app.main:app --reload