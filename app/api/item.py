from fastapi import APIRouter, Depends
from typing import List

from app.database import db_dependency
from app.schemas import DailyTracker
from app.crud import get_trackers, create_new_daily_tracker, add_glass, get_cur_tracker

router = APIRouter()

@router.get('/tracker/', response_model=List[DailyTracker])
def read_trackers(db: db_dependency):
    return get_trackers(db=db)

@router.post('/tr/new', response_model=DailyTracker)
def create_tracker(db: db_dependency):
    return create_new_daily_tracker(db=db)

@router.put('/tracker/', response_model=DailyTracker)
def update_tracker(db: db_dependency):
    return add_glass(db=db)

@router.get('/tracker/current', response_model=DailyTracker)
def read_cur_tracker(db: db_dependency):
    return get_cur_tracker(db=db)