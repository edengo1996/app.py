import sqlite3
from flask import request

import db_management


def login_verification():
    pass_text = request.form['pass']
    username_text = request.form['name']
    return db_management.check_if_user_exists(username_text, pass_text)




