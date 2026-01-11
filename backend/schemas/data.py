# Backend/schemas/data.py

from pydantic import BaseModel
from uuid import UUID
from datetime import date


class ClassOut(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True


class SectionOut(BaseModel):
    id: UUID
    class_id: UUID
    name: str

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    section_id: UUID
    full_name: str
    roll_number: str
    gender: str | None = None
    dob: date | None = None


class StudentOut(BaseModel):
    id: UUID
    section_id: UUID
    full_name: str
    roll_number: str
    gender: str | None
    dob: date | None

    class Config:
        orm_mode = True
