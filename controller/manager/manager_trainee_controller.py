from flask import redirect, url_for, request, render_template, jsonify, flash
from sqlalchemy import text
from app import db
import helpers.manager_helper as mghelper
import secrets

manager = {
    "id": "100",
    "username": "Jupiter2000",
    "email": "jupiter@gmail.com"
}

"""
    This is the function that prepares data for the 'pending trainees' view, and returns the view with its data 
"""


def get_pending_trainees(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    # token is the manager id or the manager record
    query = text("SELECT * from trainees where status = 'pending'")
    result_cursor = db.session.execute(query)
    rows = result_cursor.fetchall()
    trainees = []
    for row in rows:
        trainees.append(row._data)
    return render_template("manager/trainee/pending_trainees.html", manager=manager, trainees=trainees)



"""
    This is the controller function that handles the approve button in the pending trainees view
    it's actually not yet implemented or linked to its view
"""


def approve_trainee_registration(request):
    token = request.cookies['token']
    # make sure manager is authorized
    manager = mghelper.verify_manager(token)
    # get hidden form data
    traineeID = request.form['traineeID']
    traineeEmail= request.form['traineeEmail']   
    pass_length = 7
    # secret is python module that generates passwords according to ur prefered length
    password = secrets.token_urlsafe(pass_length)
    # insert trainee to user table first to link it to trainee table using userID(PK->FK relationship)
    user_query = text("INSERT INTO users (password, email, classification) VALUES (:password, :email, 'trainee')")
    user_cursor = db.session.execute(user_query, {'password':password, 'email':traineeEmail})
    # user_rows = user_cursor.fetchall()
    # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
    # print(user_cursor)
    db.session.commit()
    if not user_cursor:
        flash('Failed to approve trainee', 'error')
        return redirect(url_for('manager.get_pending_trainees_view'))
    # get userID from previous query
    userID = user_cursor.lastrowid
    # update trainee table with userID
    trainee_query= text("UPDATE trainees SET status = 'active', userID = :userID  WHERE traineeID = :traineeID")
    trainee_cursor = db.session.execute(trainee_query, {'userID': userID, 'traineeID': traineeID})
    trainee_rows = trainee_cursor.rowcount
    # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
    # print(trainee_rows)
    # commit changes to db
    db.session.commit()
    if not trainee_rows:   
        flash('Failed to approve trainee', 'error')
        return redirect(url_for('manager.get_pending_trainees_view'))
    flash('Trainee approved successfully', 'success')
    return redirect(url_for('manager.get_pending_trainees_view'))



"""
    This is the controller function that handles the reject button in the pending trainees view
    it's actually not yet implemented or linked to its view
"""


def reject_trainee_registration(request):
    token = request.cookies['token']
    # make sure manager is authorized
    manager = mghelper.verify_manager(token)
    # get hidden form data
    traineeID = request.form['traineeID']   
    # update trainee table with userID
    trainee_query= text("UPDATE trainees SET status = 'rejected' WHERE traineeID = :traineeID")
    trainee_cursor = db.session.execute(trainee_query, {'traineeID': traineeID})
    trainee_rows = trainee_cursor.rowcount
    # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
    # print(trainee_rows)
    # commit changes to db
    db.session.commit()
    if not trainee_rows:   
        flash('Failed to approve trainee', 'error')
        return redirect(url_for('manager.get_pending_trainees_view'))
    flash('Trainee rejected successfully', 'success')
    return redirect(url_for('manager.get_pending_trainees_view'))



"""
    This is the function that prepares the data for the view 'deactivate trainee account', 
    returns the view along with its data 

"""


def get_deactivate_trainees(request):
    # token is the manager record from the database
    manager = {
        "id": "100",
        "username": "Jupiter2000",
        "email": "jupiter@gmail.com"
    }
    # implement the query so that you get the trainees deactivation requests
    # i think we are supposed to implement something in the database for it

    # let's just assume this is the result from executing the query
    trainees = [
        ["1", "name1", "email1"],
        ["2", "name2", "email2"],
        ["3", "name3", "email3"],
    ]

    return render_template("manager/trainee/deactivate_trainee.html", manager=manager, trainees=trainees)


"""
    This is the controller function that handles the deactivate button in the deactivate trainees view
    it's actually not yet implemented or linked to its view
"""


def approve_trainee_deactivation(request):
    pass


"""
    This is the controller function that handles the reject button in the deactivate trainees view
    it's actually not yet implemented or linked to its view
"""


def reject_trainee_deactivation(request):
    pass


def get_trainee_account(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    # token is the manager id or the manager record
    query = text("SELECT * from trainees where status = 'inreview'")
    result_cursor = db.session.execute(query)
    rows = result_cursor.fetchall()
    trainees = []
    for row in rows:
        trainees.append(row._data)
    return render_template("manager/trainee/trainee_account_modification.html", manager=manager, trainees=trainees)


def get_trainee_account_details(request):
    # assuming this is a get request, that has the trainee id in its get parameters
    # we should select all the user account details
    # before we do that, we'll render something like a profile.html page
    # which i am going to do later
    
    trainee = [
        "1",
        "1",
        "username",
        "ghadeer",
        "area",
        "df2",
        "status"
    ]
    return render_template("manager/trainee/trainee-profile-details.html", trainee=trainee, manager=manager)
