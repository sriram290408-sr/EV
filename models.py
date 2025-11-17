from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
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

    marks = relationship("StudentMarks", back_populates="student", uselist=False)


class StudentMarks(Base):
    __tablename__ = "students_marks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students_data.id"), nullable=False, unique=True)
    tamil_mark = Column(Integer, nullable=False)
    english_mark = Column(Integer, nullable=False)
    maths_mark = Column(Integer, nullable=False)
    science_mark = Column(Integer, nullable=False)
    social_mark = Column(Integer, nullable=False)

    student = relationship("StudentData", back_populates="marks")
