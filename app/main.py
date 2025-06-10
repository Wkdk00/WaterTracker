from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import os
import uvicorn

from app.api import router
from app.database import engine
from app.models import item
from crud import check_current_day_tracker
from auth import auth_router, get_current_user

app = FastAPI()
app.include_router(auth_router)
app.include_router(router)
item.Base.metadata.create_all(bind=engine)

user_dependency = Annotated[dict, Depends(get_current_user)]


# Полные пути к папкам
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/")
def read_root(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401)
    return {'User':user}

@app.get("/dashboard")
async def dashboard(user: user_dependency):
    return templates.TemplateResponse("index.html", {"request": {}, "user": user})

if __name__ == "__main__":
    check_current_day_tracker()
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)