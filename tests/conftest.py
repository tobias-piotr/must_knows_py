from typing import Generator
import pytest
from must_knows import database


@pytest.fixture()
def connected_db() -> Generator[database.Database, None, None]:
    """Yield connected database.

    Disconnect on teardown.
    """
    db = database.Database()
    db.connect()
    yield db
    db.disconnect()
