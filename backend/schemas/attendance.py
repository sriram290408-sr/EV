from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)
