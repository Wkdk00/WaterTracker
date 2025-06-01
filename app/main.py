from fastapi import FastAPI
from app.api import router
from app.database import engine
from app.models import item

item.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to CRUD API"}