import db_management


def login_verification(username: str, password: str) -> bool:
    return db_management.check_login_parameters(username, password)
