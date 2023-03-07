from must_knows.main_dataclass import UserService


class TestUserService:
    """Test cases for the UserService class."""

    def test_register(self, connected_db):
        srv = UserService(db=connected_db)
        srv.register("test@user.com", "testpassword", "testpassword")
        uid = srv.login("test@user.com", "testpassword")
        assert uid is not None
