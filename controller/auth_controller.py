from flask import render_template, jsonify, redirect, url_for, flash
from sqlalchemy import text

from app import app
from app import db
import os


def login_view():
    return render_template('login.html')


def handle_login(request):
    email = request.form['email']
    password = request.form['password']
    if not email or not password:
        return flash('Missing email or password', 'error')
    # let's look whether we can find those credentials
    query = text("SELECT * from users where email = :email and password = :password")
    params = {"email": email, "password": password}
    result = db.session().execute(query, params)
    row = result.fetchone()
    if not row:
        return flash('Email or password are incorrect, please try again', 'error')
    # generate token

    classification = row[3]
    print(classification)
    print("=============================================================================================")
    print(result)
    print("=============================================================================================")
    if classification == "manager":
        return redirect(url_for('manager.dashboard_view'))
    elif classification == "advisor":
        return redirect(url_for('advisor.dashboard_view'))
    elif classification == "trainee":
        return redirect(url_for('trainee.dashboard_view'))
    else:
        # error
        pass


def signup_view(classification):
    if classification == "advisor":
        return render_template('registration/advisor_register.html')
    elif classification == "trainee":
        return render_template('registration/trainee_register.html')
    else:
        pass


def handle_trainee_signup(request):
    username = request.form['username']
    email = request.form['email']
    desiredField = request.form['desiredField']
    area = request.form['area']
    # cv = request.form['cv']
    if not username or not email or not desiredField or not area:
        # return error message
        pass
    query = text(
        "INSERT INTO trainees (username, email, desired_field, area, current_status) VALUES (:username, :email, :desired_field, :area, 'pending')")
    params = {'username': username, 'email': email, 'desired_field': desiredField, 'area': area}
    result = db.session.execute(query, params)
    db.session.commit()
    if result:
        return redirect(url_for('auth.login_view'))
    return result


def handle_advisor_signup(request):
    username = request.form['username']
    email = request.form['email']
    discipline = request.form['discipline']
    # cv = request.form['cv']
    if not username or not email or not discipline:
        # return error message
        pass
    query = text(
        "INSERT INTO advisors (username, email, discipline, current_status) VALUES (:username, :email, :discipline, 'pending')")
    params = {'username': username, 'email': email, 'discipline': discipline}
    result = db.session.execute(query, params)
    db.session.commit()
    if result:
        return redirect(url_for('auth.login_view'))
    return result
