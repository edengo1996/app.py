import sqlite3
from flask import request

import db_management


def login_verification():
    pass_text = request.form['pass']
    username_text = request.form['name']
    return db_management.does_user_exist(username_text, pass_text)




