from flask import Flask, render_template, request

import views
import db_management
import os


app = Flask(__name__)
app.secret_key = os.environ.get('flaskLogs_secretKey')
db_management.create_tables()


if __name__ == '__main__':
    app.run()


@app.route('/')
def home_page_bootup():
    return render_template('index.html')


@app.route('/sign_up')
def sign_up_page():
    return render_template('sign_up_form.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    password = request.form['pass']
    verification_password = request.form['ver_pass']
    username = request.form['name']
    return views.signup_response(username, password, verification_password)


@app.route('/login')
def return_login_page():
    return render_template('login_form.html')


@app.route('/login', methods=['POST'])
def process_login():
    password = request.form['pass']
    username = request.form['name']
    return views.login_response(username, password)
