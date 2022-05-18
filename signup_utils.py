from flask import request
import db_management


def process_sign_up():
    password = request.form['pass']
    verification_password = request.form['ver_pass']
    username = request.form['name']

    if password != verification_password:
        return SignupResults.MISMATCHED_PASSWORD
    elif not check_valid_username(username):
        return SignupResults.INVALID_USERNAME
    return db_management.create_new_user(username, password)


def check_valid_username(username):
    return db_management.is_username_not_taken(username)


class SignupResults:
    MISMATCHED_PASSWORD = 1
    SUCCESSFUL_SIGNUP = 2
    INVALID_USERNAME = 3
    DB_COMM_ERROR = 4
