#schemas.py
from pydantic import BaseModel, field_validator;

class CreateBase(BaseModel):
    name: str
    school_class: int
    section: str
    door_no: int
    address: str
    city: str
    phone_no: str
    blood_group: str | None = None
    father_name: str
    mother_name: str
    yearly_occupation: int | str | None = None

    @field_validator("phone_no")
    def validate_phone(cls, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain digits only")
        if len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        return value

class ResponseModel(CreateBase):
    id: int
    class Config:
        orm_mode = True