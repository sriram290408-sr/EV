from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.login_log import LoginLog
from schemas.login_log  import LoginLogOut
from dependencies.auth import get_current_user

router = APIRouter(prefix="/logs", tags=["Login Logs"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/login", response_model=list[LoginLogOut])
def get_login_logs(
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    return db.query(LoginLog).order_by(LoginLog.login_time.desc()).all()
