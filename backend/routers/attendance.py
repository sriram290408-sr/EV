from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.attendance import Attendance
from schemas.attendance import AttendanceUpsert, AttendanceOut
from dependencies.auth import get_current_user

router = APIRouter(prefix="/attendance", tags=["Attendance"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AttendanceOut)
def upsert_attendance(
    data: AttendanceUpsert,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    record = (
        db.query(Attendance)
        .filter(
            Attendance.student_id == data.student_id,
            Attendance.date == data.date,
        )
        .first()
    )

    if record:
        record.status = data.status
    else:
        record = Attendance(**data.dict())
        db.add(record)

    db.commit()
    db.refresh(record)
    return record


@router.get("/{student_id}", response_model=list[AttendanceOut])
def get_attendance(
    student_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    return db.query(Attendance).filter(
        Attendance.student_id == student_id
    ).all()
