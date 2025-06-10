from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.database import db_dependency
from app.schemas import DailyTracker
from app.crud import get_trackers, create_new_daily_tracker, add_glass, get_cur_tracker
from app.auth import user_dependency

router = APIRouter()

@router.get('/tracker/', response_model=List[DailyTracker])
def read_trackers(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401)
    #trackers = get_trackers(db=db)
    #return [{"id": t.id,"count": t.count,"day": t.day} for t in trackers]
    return get_trackers(db=db)

@router.post('/tracker/new', response_model=DailyTracker)
def create_tracker(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return create_new_daily_tracker(db=db)

@router.put('/tracker/', response_model=DailyTracker)
def update_tracker(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401)
    return add_glass(db=db)

@router.get('/tracker/current', response_model=DailyTracker)
def read_cur_tracker(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Unauthorized')
#    tracker = get_cur_tracker(db=db).__dict__
#    return tracker
    return get_cur_tracker(db=db)