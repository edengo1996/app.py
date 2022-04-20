import sqlite3
from flask import request


def login_verification():
    pass_text = request.form['pass']
    username_text = request.form['name']
    return does_user_exist(username_text, pass_text)


def does_user_exist(str_username, str_pass):
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    curs.execute('''SELECT * FROM users WHERE Username = ? AND Password = ?;''',
                 (str_username, str_pass))
    if len(curs.fetchall()) == 0:
        return False
    return True

