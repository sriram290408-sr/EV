from pydantic import BaseModel
from uuid import UUID
from datetime import date

class AttendanceUpsert(BaseModel):
    student_id: UUID
    date: date
    status: bool

class AttendanceOut(BaseModel):
    id: UUID
    student_id: UUID
    date: date
    status: bool

    class Config:
        orm_mode = True
