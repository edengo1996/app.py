from flask import Flask, render_template, request, flash
import sqlite3

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/')
def hello_world():
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS users (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Username TEXT NOT NULL UNIQUE,
                    Password TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()
    return render_template('index.html')


@app.route('/sign_up')
def sign_up_page():
    return render_template('sign_up_form.html')


@app.route('/sign_up', methods=['POST'])
def process_sign_up():
    if sign_up():
        return "process completed Eden", 201
    return "failed to create a new user", 401


def sign_up():
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
    conn = sqlite3.connect('database.db')
    curs = conn.cursor()
    if curs.execute("SELECT ALL FROM users WHERE username = str_input ") == 0:
        return True
    return False

