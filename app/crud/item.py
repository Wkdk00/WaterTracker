from sqlalchemy.orm import Session
from datetime import date

from app.database import get_db
from app.models import Tracker

def get_trackers(db: Session):
    return db.query(Tracker).all()

def create_new_daily_tracker(db: Session):
    new_tracker = Tracker(count = 0, day=date.today())
    db.add(new_tracker)
    db.commit()
    db.refresh(new_tracker)
    return new_tracker

def add_glass(db: Session):
    cur_tracker = db.query(Tracker).filter(Tracker.day == date.today()).first()
    if not cur_tracker:
        cur_tracker = create_new_daily_tracker(db)
    cur_tracker.count +=1
    db.commit()
    db.refresh(cur_tracker)
    return cur_tracker

def get_cur_tracker(db: Session):
    return db.query(Tracker).filter(Tracker.day == date.today()).first()

def check_current_day_tracker(db: Session = None):
    if db is None:
        db = next(get_db())

    day_tracker = db.query(Tracker).filter(Tracker.day == date.today()).first()
    if day_tracker is None:
        new_day_tracker = Tracker(count=0, day=date.today())
        db.add(new_day_tracker)
        db.commit()
        db.refresh(new_day_tracker)
    return None
