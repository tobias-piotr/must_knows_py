from typing import Any
from must_knows import exceptions


class Database:
    """Simple, in-memory database."""

    def __init__(self) -> None:
        self._entries: list[Any] = []
        self._connected = False

    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

    def add(self, entry: Any) -> None:
        if self._connected is False:
            raise exceptions.DatabaseError("Database is disconnected")
        self._entries.append(entry)

    @property
    def entries(self) -> list:
        if self._connected is False:
            raise exceptions.DatabaseError("Database is disconnected")
        return self._entries
