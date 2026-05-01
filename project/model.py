from sqlalchemy import Column, Integer, String
from database_try import base

class User(base):
    __tablename__ = "table"
    roll_num = Column(Integer, primary_key=True, index=True)
    student = Column(String(255))
    role = Column(String(255))



