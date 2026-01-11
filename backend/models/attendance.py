import uuid
from datetime import datetime
from sqlalchemy import Column, Date, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id", ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
