from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import uvicorn

from app.api import router
from app.database import engine
from app.models import item
from crud import check_current_day_tracker

item.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Полные пути к папкам
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to CRUD API"}

@app.get("/dashboard")
async def dashboard():
    return templates.TemplateResponse("index.html", {"request": {}})

if __name__ == "__main__":
    check_current_day_tracker()
    uvicorn.run("app.main:app", host="0.0.0.0", port=8003, reload=True)