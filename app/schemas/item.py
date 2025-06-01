from pydantic import BaseModel

class DailyTrackerBase(BaseModel):
    count: int

class DailyTracker(DailyTrackerBase):
    id: int

    class Config:
        orm_mode = True

class TrackerCreate(DailyTrackerBase):
    pass