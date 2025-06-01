from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import DailyTracker
from app.crud import get_trackers, create_new_daily_tracker, add_glass

router = APIRouter()

@router.get('/traker/', response_model=List[DailyTracker])
def read_trackers(db: Session = Depends(get_db)):
    return get_trackers(db=db)

@router.post('/traker/', response_model=DailyTracker)
def create_tracker(db: Session = Depends(get_db)):
    return create_new_daily_tracker(db=db)

@router.put('/tracker/', response_model=DailyTracker)
def update_tracker(db: Session = Depends(get_db)):
    return add_glass(db=db)