from flask import render_template, jsonify, redirect, url_for, flash
from sqlalchemy import text
import helpers.token as tokenHelper
from app import app
from app import db
import os


def login_view():
    return render_template('login.html')


def handle_login(request):
    # get information from request
    email = request.form['email']
    password = request.form['password']
    if not email or not password:
        return flash('Missing email or password', 'error')
    # let's look whether we can find those credentials
    query = text("SELECT * from users where email = :email and password = :password")
    params = {"email": email, "password": password}
    result = db.session().execute(query, params)
    row = result.fetchone()
    # print(row)
    if row is None:
        print("invalid pass")
        flash('Email or password are incorrect, please try again', 'error')
        return redirect(url_for('auth.login_view'))
    # generate token
    token = tokenHelper.generate_token(row)
    classification = row[2]
    print(classification)
    if classification == "manager":
        print("inside manager")
        response = redirect(url_for('manager.dashboard_view'))
    elif classification == "advisor":
        print("inside advisor")
        response = redirect(url_for('advisor.dashboard_view'))
    elif classification == "trainee":
        print("inside trainee")
        response = redirect(url_for('trainee.dashboard_view'))
    else:
        return flash('Something went wrong', 'error')
    response.set_cookie('token', token)
    return response


def signup_view(request):
    classification = request.args.get('classification')
    if classification == "advisor":
        return render_template('registration/advisor_register.html')
    elif classification == "trainee":
        return render_template('registration/trainee_register.html')
    else:
        # If the classification field is somehow tampered, this shows the red flag
        flash('Something went wrong', 'error')
        return redirect(url_for('auth.login_view'))


def handle_trainee_signup(request):
    username = request.form['username']
    fullname = request.form['fullname']
    email = request.form['email']
    desiredField = request.form['desiredField']
    area = request.form['area']
    # TODO: upload required materials to the user-uploads directory
    if not username or not email or not desiredField or not area:
        # TODO: test this
        flash('signup information is missing', 'error')
        return redirect(url_for('auth.signup_view?classification=trainee'))

    query = text(
        """
        INSERT INTO `trainees` (username, fullname, email, desired_field, area_of_training) VALUES (:username,:fullname, :email, :desired_field, :area)""")
    params = {'username': username, 'fullname': fullname, 'email': email, 'desired_field': desiredField, 'area': area}
    result = db.session.execute(query, params)
    if not result:
        flash('failed to add data', 'error')
        return redirect(url_for('auth.signup_view?classification=trainee'))
    # in case of the first query success, this shall be a pending trainee request waiting for the manager approval
    else:
        flash('Successfully added your information, wait for our email')
        db.session.commit()
        return redirect(url_for('auth.login_view'))


def handle_advisor_signup(request):
    username = request.form['username']
    fullname = request.form['fullname']
    email = request.form['email']
    discipline = request.form['discipline']
    # TODO: upload required materials to the user-uploads directory
    if not username or not email or not fullname or not discipline:
        # TODO: test this
        flash('signup information is missing', 'error')
        return redirect(url_for('auth.signup_view?classification=trainee'))

    query = text(
        """
        INSERT INTO advisors (username, fullname, email, discipline) VALUES (:username,:fullname, :email, :discipline)""")
    params = {'username': username, 'fullname': fullname, 'email': email, 'discipline': discipline}
    result = db.session.execute(query, params)
    if not result:
        flash('failed to add data', 'error')
        return redirect(url_for('auth.signup_view?classification=advisor'))
    # in case of the first query success, this shall be a pending trainee request waiting for the manager approval
    else:
        flash('Successfully added your information, wait for our email')
        db.session.commit()
        return redirect(url_for('auth.login_view'))
