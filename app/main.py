from fastapi import FastAPI
from app.routers import auth


app = FastAPI(title="Bank API")
app.include_router(auth.router)