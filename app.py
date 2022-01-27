from flask import Flask, render_template
import requests
import sqlite3

app = Flask(__name__)




def sign_up():
    print("OK") # insert data into users table.


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/sign_up')
def sign_up_page():
    return render_template('index.html')


@app.route('/sign_up', methods=['POST'])
def process_sign_up():
    sign_up()
    return "did func work?"


if __name__ == '__main__':
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    curs.execute("""CREATE TABLE users (
                    id integer,
                    email text,
                    password text
                    )""")

    curs.commit()
    curs.close()
    app.run()
