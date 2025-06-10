from app.database import Base
from sqlalchemy import Column, Integer, Date, String
from datetime import date

class Tracker(Base):
    __tablename__ = 'tracker'

    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    day = Column(Date, default=date.today)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hashed_password = Column(String)