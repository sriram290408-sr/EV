from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class LoginLogOut(BaseModel):
    id: UUID
    user_id: UUID
    login_time: datetime

    class Config:
        orm_mode = True
