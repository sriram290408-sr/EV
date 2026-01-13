from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime


class LoginLogOut(BaseModel):
    id: UUID
    user_id: UUID
    login_time: datetime

    model_config = ConfigDict(from_attributes=True)
