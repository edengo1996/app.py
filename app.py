from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/test', methods=['POST'])
def test_path2():
    return True


@app.route('/test')
def test_path():
    return "test path"


@app.route('/')
def hello_world():
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS users (
                       Id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Username TEXT NOT NULL,
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
    if process_sign_up():
        return render_template('signup_completed.html'), 200
    return render_template('signup_railed.html'), 400


@app.route('/login')
def return_login_page():
    return render_template('login_form.html')


@app.route('/login', methods=['POST'])
def process_login():
    if login_verification():
        return render_template('login_completed.html'), 200
    return render_template('login_failed.html'), 401


def login_verification():
    pass_text = request.form['pass']
    username_text = request.form['name']
    return existing_user(username_text, pass_text)


def existing_user(str_username, str_pass):  # work here
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    # curs.execute('SELECT * FROM users WHERE Username = ? AND Password = ?',
                 #(str_username, str_pass)).fetchall()

    curs.execute('''SELECT * FROM users WHERE Username = ? AND Password = ?;''',
                 (str_username, str_pass))
    if len(curs.fetchall()) == 0:
        return False
    return True


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










