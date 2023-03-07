import uuid
from pydantic import BaseModel, EmailStr, root_validator, Field
from must_knows import database, exceptions


class User(BaseModel):
    """User model."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    email: EmailStr
    password: str = Field(min_length=8, max_length=32)
    password_confirmation: str

    @root_validator(pre=True)
    def validate_passwords(cls, values: dict) -> dict:
        if values["password"] != values["password_confirmation"]:
            raise ValueError("Passwords must match")
        return values


class UserSerivce:
    """User operations manager."""

    def __init__(self, db: database.Database) -> None:
        self.db = db

    def register(self, email: EmailStr, password1: str, password2: str) -> None:
        user = User(email=email, password=password1, password_confirmation=password2)
        self.db.add(user)

    def login(self, email: str, password: str) -> uuid.UUID:
        user = next((u for u in self.db.entries if u.email == email), None)
        if user is None or user.password != password:
            raise exceptions.LoginError("Invalid credentials")
        return user.id
