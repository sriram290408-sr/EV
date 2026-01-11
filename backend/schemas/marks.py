from pydantic import BaseModel
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

    class Config:
        orm_mode = True
