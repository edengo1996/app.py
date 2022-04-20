from flask import request
import sqlite3


def process_sign_up():
    pass_text = request.form['pass']
    ver_pass_text = request.form['ver_pass']
    username_text = request.form['name']

    if pass_text != ver_pass_text or not check_valid_username(username_text):
        return False
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    params = (username_text, pass_text)
    curs.execute("INSERT INTO users VALUES (NULL, ?, ?)", params)
    conn.commit()
    conn.close()
    return True


def check_valid_username(str_input):
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM users WHERE Username = ?', (str_input,)).fetchall()
    if len(curs.fetchall()) == 0:
        return True
    return False
