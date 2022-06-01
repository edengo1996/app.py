import db_management


def login_assert():
    assert db_management.check_login_parameters("s", "s")
