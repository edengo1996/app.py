from flask import render_template, flash
from models.SignupResults import SignupResults

import login_utils
import signup_utils


def login_response(username, password):
    if login_utils.login_verification(username, password):
        flash(' You were successfully logged in ' + username, category='info')
        return render_template('login_form.html'), 200
    flash(' failed to login', category='error')
    return render_template('login_form.html'), 401


def signup_response(username, password, verification_password):
    result = signup_utils.process_sign_up(username, password, verification_password)
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
