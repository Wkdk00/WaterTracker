from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import DailyTracker
from app.crud import get_trackers, create_new_daily_tracker, add_glass

router = APIRouter()

@router.get('/traker/', response_model=List[DailyTracker])
def read(db: Session =  Depends(get_db)):
    trackers = get_trackers(db=db)
    return trackers

@router.post('/traker/', response_model=DailyTracker)
def create(db: Session =  Depends(get_db)):
    tracker = create_new_daily_tracker(db=db)
    return tracker

@router.put('/tracker/', response_model=DailyTracker)
def update(db: Session = Depends(get_db)):
    update_tracker = add_glass(db=db)
    return update_tracker