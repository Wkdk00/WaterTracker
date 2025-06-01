from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models import Tracker

def get_trackers(db: Session):
    return db.query(Tracker).all()

def create_new_daily_tracker(db: Session):
    new_tracker = Tracker(count = 0)
    db.add(new_tracker)
    db.commit()
    db.refresh(new_tracker)
    return new_tracker

def add_glass(db: Session):
    cur_tracker = db.query(Tracker).order_by(desc(Tracker.id)).first()
    cur_tracker.count +=1
    db.commit()
    db.refresh(cur_tracker)
    return cur_tracker

def get_cur_tracker(db: Session):
    return db.query(Tracker).order_by(desc(Tracker.id)).first()