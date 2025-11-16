# models.py
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class StudentData(Base):
    __tablename__ = "students_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    school_class = Column(Integer, nullable=False)
    section = Column(String, nullable=False)
    door_no = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    phone_no = Column(String, nullable=False)
    blood_group = Column(String)
    father_name = Column(String, nullable=False)
    mother_name = Column(String, nullable=False)
    yearly_occupation = Column(Integer)
