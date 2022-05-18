from flask import request
import db_management


def login_verification():
    pass_text = request.form['pass']
    username_text = request.form['name']
    return db_management.check_login_parameters(username_text, pass_text)
