from pydantic import BaseModel

class DailyTrackerBase(BaseModel):
    count: int

class DailyTracker(DailyTrackerBase):
    id: int

    class Config:
        from_attributes = True

class TrackerCreate(DailyTrackerBase):
    pass