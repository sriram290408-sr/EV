from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.users import User
from models.login_log import LoginLog
from schemas.users import UserCreate, UserLogin, Token
from core.hash import hash_password, verify_password
from core.security import create_access_token

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(data: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(400, "Email already exists")

    user = User(email=data.email, password=hash_password(data.password))
    db.add(user)
    db.commit()
    return {"message": "Account created"}

@router.post("/login", response_model=Token)
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(401, "Invalid credentials")

    db.add(LoginLog(user_id=user.id))
    db.commit()

    token = create_access_token(str(user.id))
    return {"access_token": token}
