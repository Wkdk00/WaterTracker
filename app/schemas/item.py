from pydantic import BaseModel
from datetime import date

class DailyTrackerBase(BaseModel):
    count: int
    day: date

class DailyTracker(DailyTrackerBase):
    id: int

    class Config:
        from_attributes = True

class TrackerCreate(DailyTrackerBase):
    pass