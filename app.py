from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def sign_up():
    print("OK")
    pass_text = request.form['pass']
    ver_pass_text = request.form['ver_pass']
    username_text = request.form['nm']

    if pass_text != ver_pass_text:
        return "passwords do not match"
    else:
        print("very OK")

        conn = sqlite3.connect('data.db')
        curs = conn.cursor()
        curs.execute("""INSERT INTO TABLE users (id) 
                        VALUE(1)    
                            """)
        curs.execute("""INSERT INTO TABLE users (email) 
                                VALUE(username_text)    
                                    """)
        curs.execute("""INSERT INTO TABLE users (password) 
                                        VALUE(pass_text)    
                                            """)

        curs.commit()
        curs.close()


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
