from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/')
def hello_world():
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS users (
                    id integer,
                    username text,
                    password text
                    )''')
    conn.commit()
    conn.close()
    return render_template('index.html')


@app.route('/sign_up')
def sign_up_page():
    return render_template('sign_up_form.html')


@app.route('/sign_up', methods=['POST'])
def process_sign_up():
    sign_up()
    return "process completed Eden"


def sign_up():
    print("OK")
    pass_text = request.form['pass']
    ver_pass_text = request.form['ver_pass']
    username_text = request.form['name']

    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    params = (1, username_text, pass_text)
    curs.execute("INSERT INTO users VALUES ( ?, ?, ?)", params)
    conn.commit()
    conn.close()
