from flask import Flask, render_template, flash

import db_management
import login_utils
import signup_utils


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == '__main__':
    app.run()


@app.route('/')
def hello_world():
    db_management.create_connection()
    return render_template('index.html')


@app.route('/sign_up')
def sign_up_page():
    return render_template('sign_up_form.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    if signup_utils.process_sign_up():
        flash('user created successfully.', "info")
        return render_template('sign_up_form.html'), 200
    flash('This username is already taken, or passwords do not match', 'error')
    return render_template('sign_up_form.html'), 400


@app.route('/login')
def return_login_page():
    return render_template('login_form.html')


@app.route('/login', methods=['POST'])
def process_login():
    if login_utils.login_verification():
        flash('You were successfully logged in Eden', 'info')
        return render_template('login_form.html'), 200
    flash('failed to login', 'error')
    return render_template('login_form.html'), 401

