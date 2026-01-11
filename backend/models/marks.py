import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Mark(Base):
    __tablename__ = "marks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id", ondelete="CASCADE"))
    subject = Column(String, nullable=False)
    marks = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
