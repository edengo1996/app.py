from db_management import create_new_user


def test_signup():
    assert create_new_user("eden", "eden") == 3  # if 'eden' is taken
