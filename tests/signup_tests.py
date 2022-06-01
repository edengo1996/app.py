import db_management


def login_assert():
    assert db_management.create_new_user("eden", "eden") == 2 # if 'eden does not exists
