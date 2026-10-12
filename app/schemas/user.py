import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator


class UserCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=100) # Field is neaded to make constraints
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

    @field_validator("password")
    @classmethod
    def password_fits_bcrypt(cls, v: str) -> str:
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password is too long (max 72 bytes)")
        return v


class UserResponse(BaseModel):
    
    """ 
        ConfigDict() - option for all scheme
        from_attribute - by default Pydantic can read only Dict,
        but with this option it will can read Classes too
    """

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    full_name: str
    email: EmailStr
    created_at: datetime