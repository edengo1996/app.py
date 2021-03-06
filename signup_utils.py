import db_management
from models.SignupResults import SignupResults


def process_sign_up(username: str, password: str, verification_password: str) -> int:
    if password != verification_password:
        return SignupResults.MISMATCHED_PASSWORD
    elif not check_valid_username(username):
        return SignupResults.USERNAME_TAKEN
    return db_management.create_new_user(username, password)


def check_valid_username(username) -> bool:
    return db_management.is_username_not_taken(username)
