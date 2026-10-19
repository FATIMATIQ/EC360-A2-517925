from auth_service import register


def test_register_new_user():
    assert register("a@b.com", "pw") == "Registered"


def test_register_duplicate():
    register("c@d.com", "pw")
    assert register("c@d.com", "pw") == "An account with this email already exists"