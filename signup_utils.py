from flask import request
import db_management


def process_sign_up():
    pass_text = request.form['pass']
    ver_pass_text = request.form['ver_pass']
    username_text = request.form['name']

    if pass_text != ver_pass_text:
        return SignupResults.MISMATCHED_PASSWORD
    elif not check_valid_username(username_text):
        return SignupResults.INVALID_USERNAME
    return db_management.create_new_user(username_text, pass_text)


def check_valid_username(str_input):
    return db_management.is_username_taken(str_input)


class SignupResults:
    MISMATCHED_PASSWORD = 1
    SUCCESSFUL_SIGNUP = 2
    INVALID_USERNAME = 3
    DB_COMM_ERROR = 4
