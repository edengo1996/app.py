from flask import request
import db_management
from models.SignupResults import SignupResults


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
