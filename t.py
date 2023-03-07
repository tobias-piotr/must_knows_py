import uuid
from pydantic import BaseModel, EmailStr, root_validator, Field


class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    email: EmailStr
    password: str = Field(min_length=8, max_length=32)
    password_confirmation: str

    @root_validator(pre=True)
    def validate_passwords(cls, values: dict) -> dict:
        if values["password"] != values["password_confirmation"]:
            raise ValueError("Passwords must match")
        return values


user = User(email="test@email.com", password="ddddd", password_confirmation="asd")
