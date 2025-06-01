from fastapi import FastAPI
from app.api import router
from app.database import engine
from app.models import item
from fastapi.staticfiles import StaticFiles#
from fastapi.templating import Jinja2Templates#

item.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to CRUD API"}

@app.get("/dashboard")
async def dashboard():
    return templates.TemplateResponse("index.html", {"request": {}})