from pydantic import BaseModel, ConfigDict
from uuid import UUID


class MarkCreate(BaseModel):
    student_id: UUID
    subject: str
    marks: int


class MarkOut(BaseModel):
    id: UUID
    student_id: UUID
    subject: str
    marks: int

    model_config = ConfigDict(from_attributes=True)
