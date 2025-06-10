from pydantic import BaseModel
from datetime import date

class DailyTrackerBase(BaseModel):

    count: int
    day: date

    class Config:
        from_attributes = True
        orm_mode = True

class DailyTracker(DailyTrackerBase):
    id: int

class TrackerCreate(DailyTrackerBase):
    pass

class CreateUserRequests(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str