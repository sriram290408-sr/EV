from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import date


class ClassOut(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


class SectionOut(BaseModel):
    id: UUID
    class_id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


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

    model_config = ConfigDict(from_attributes=True)
