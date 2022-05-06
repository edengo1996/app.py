from flask import request
import db_management


def process_sign_up():
    pass_text = request.form['pass']
    ver_pass_text = request.form['ver_pass']
    username_text = request.form['name']

    if pass_text != ver_pass_text or not check_valid_username(username_text):
        return False
    db_management.create_new_user(username_text, pass_text)
    return True


def check_valid_username(str_input):
    return db_management.is_username_taken(str_input)
