from flask import Flask, render_template, flash, request
from models.SignupResults import SignupResults

import db_management
import login_utils
import signup_utils
import os


app = Flask(__name__)
app.secret_key = os.environ.get('flaskLogs_secretKey')

if __name__ == '__main__':
    app.run()


@app.route('/')
def hello_world():
    db_management.create_tables()
    return render_template('index.html')


@app.route('/sign_up')
def sign_up_page():
    return render_template('sign_up_form.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    result = signup_utils.process_sign_up()
    if result == SignupResults.MISMATCHED_PASSWORD:
        flash('passwords do not match', category='error')
        return render_template('sign_up_form.html'), 400
    elif result == SignupResults.SUCCESSFUL_SIGNUP:
        flash('user created successfully', category='info')
        return render_template('sign_up_form.html'), 200
    elif result == SignupResults.DB_COMM_ERROR:
        flash('new user creation failed. try again (DB query failed)', category='error')
        return render_template('sign_up_form.html'), 400
    elif result == SignupResults.USERNAME_TAKEN:
        flash('username is taken', category='error')
        return render_template('sign_up_form.html'), 400
    else:
        flash('Unknown error', category='error')
        return render_template('sign_up_form.html'), 400


@app.route('/login')
def return_login_page():
    return render_template('login_form.html')


@app.route('/login', methods=['POST'])
def process_login():
    password = request.form['pass']
    username = request.form['name']
    if login_utils.login_verification(username, password):
        flash(' You were successfully logged in ' + username, category='info')
        return render_template('login_form.html'), 200
    flash(' failed to login', category='error')
    return render_template('login_form.html'), 401
