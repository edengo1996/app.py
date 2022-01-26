from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('data.db')
curs = conn.cursor()
curs.execute("""CREATE TABLE users (
            id integer,
            email text,
            password text
            )""")

curs.commit()
curs.close()


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
