from app.database import Base
from sqlalchemy import Column, Integer

class Tracker(Base):
    __tablename__ = 'tracker'

    id = Column(Integer, primary_key=True)
    count = Column(Integer)