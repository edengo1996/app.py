from flask import request

import db_management


def process_sign_up():
    pass_text = request.form['pass']
    ver_pass_text = request.form['ver_pass']
    username_text = request.form['name']

    if pass_text != ver_pass_text or not db_management.check_valid_username(username_text):
        return False
    db_management.create_new_user(username_text, pass_text)
    return True
