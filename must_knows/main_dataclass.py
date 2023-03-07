import uuid
from dataclasses import dataclass
from must_knows import exceptions, database


@dataclass
class User:
    """User model."""

    id: uuid.UUID
    email: str
    password: str


class UserService:
    """User operations manager."""

    def __init__(self, db: database.Database) -> None:
        self.db = db

    def register(self, email: str, password1: str, password2: str) -> None:
        if password1 != password2:
            raise exceptions.ValidationError("Password must match")
        user = User(id=uuid.uuid4(), email=email, password=password1)
        self.db.add(user)

    def login(self, email: str, password: str) -> uuid.UUID:
        user = next((u for u in self.db.entries if u.email == email), None)
        if user is None or user.password != password:
            raise exceptions.LoginError("Invalid credentials")
        return user.id
