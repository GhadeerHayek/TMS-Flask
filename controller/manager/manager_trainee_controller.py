from flask import redirect, url_for, request, render_template, jsonify, flash
from sqlalchemy import text
from app import db
import helpers.manager_helper as mghelper
import secrets



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
    db.session.commit()
    if not trainee_rows:   
        flash('Failed to approve trainee', 'error')
        return redirect(url_for('manager.get_pending_trainees_view'))
    flash('Trainee approved successfully', 'success')
    return redirect(url_for('manager.get_pending_trainees_view'))



"""
    This is the controller function that handles the reject button in the pending trainees view
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
    # commit changes to db
    db.session.commit()
    if not trainee_rows:   
        flash('Failed to approve trainee', 'error')
        return redirect(url_for('manager.get_pending_trainees_view'))
    flash('Trainee rejected successfully', 'success')
    return redirect(url_for('manager.get_pending_trainees_view'))


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
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)    
    userID = request.args.get('id')
    query = text("SELECT * from trainees where userID = :userID")
    result_cursor = db.session.execute(query, {'userID':userID})
    trainee = result_cursor.fetchone()
    # trainee = []
    # for row in rows:
    #     trainee.append(row._data)
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(trainee)
    return render_template("manager/trainee/trainee-profile-details.html", trainee=trainee, manager=manager)


def accept_trainee_modifications(request):
    token = request.cookies['token']
    # make sure manager is authorized
    # manager = mghelper.verify_manager(token)
    # get hidden form data
    traineeID = request.form['traineeID']   
    # update trainee table with userID
    trainee_query= text("UPDATE trainees SET status = 'active' where traineeID = :traineeID")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(traineeID[0])
    trainee_cursor = db.session.execute(trainee_query, {'traineeID': traineeID})
    # commit changes to db
    db.session.commit()
    if not trainee_cursor:   
        flash('Failed to approve trainee modification request', 'error')
        return redirect(url_for('manager.get_trainees_accounts_view'))
    flash('Trainee modifications approved successfully', 'success')
    return redirect(url_for('manager.get_trainees_accounts_view'))



def reject_trainee_modifications(request):
    token = request.cookies['token']
    # make sure manager is authorized
    # manager = mghelper.verify_manager(token)
    # get hidden form data
    traineeID = request.form['traineeID']   
    # update trainee table with userID
    trainee_query= text("UPDATE trainees SET status = 'active' where traineeID = :traineeID")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(traineeID[0])
    trainee_cursor = db.session.execute(trainee_query, {'traineeID': traineeID})
    # commit changes to db
    result = db.session.commit()
    if not result:   
        flash('Failed to approve trainee modification request', 'error')
        return redirect(url_for('manager.get_trainees_accounts_view'))
    flash('Trainee modifications rejected successfully', 'success')
    return redirect(url_for('manager.get_trainees_accounts_view'))



"""
    This is the function that prepares the data for the view 'deactivate trainee account', 
    returns the view along with its data 

"""
def get_deactivate_trainees(request):
    # token is the manager record from the database
    token = request.cookies['token']
    # manager = mghelper.verify_manager(token)
    # token is the manager id or the manager record
    query = text("SELECT * from trainees where status = 'active'")
    result_cursor = db.session.execute(query)
    rows = result_cursor.fetchall()
    trainees = []
    for row in rows:
        trainees.append(row._data)
    # implement the query so that you get the trainees deactivation requests
    # i think we are supposed to implement something in the database for it

    return render_template("manager/trainee/deactivate_trainee.html", manager=manager, trainees=trainees)


"""
    This is the controller function that handles the deactivate button in the deactivate trainees view
    it's actually not yet implemented or linked to its view
"""


def approve_trainee_deactivation(request):
    token = request.cookies['token']
    # make sure manager is authorized
    # manager = mghelper.verify_manager(token)
    # get hidden form data
    traineeID = request.form['traineeID']   
    # update trainee table with userID
    trainee_query= text("UPDATE trainees SET status = 'inactive' where traineeID = :traineeID")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(traineeID[0])
    trainee_cursor = db.session.execute(trainee_query, {'traineeID': traineeID})
    # commit changes to db
    db.session.commit()
    if not trainee_cursor:   
        flash('Failed to deactivate trainee', 'error')
        return redirect(url_for('manager.get_deactivate_trainees_view'))
    flash('Trainee deactivated successfully', 'success')
    return redirect(url_for('manager.get_deactivate_trainees_view'))

"""
    This is the controller function that handles the reject button in the deactivate trainees view
    it's actually not yet implemented or linked to its view
"""
def reject_trainee_deactivation(request):
    token = request.cookies['token']
    # make sure manager is authorized
    # manager = mghelper.verify_manager(token)
    # get hidden form data
    traineeID = request.form['traineeID']   
    # update trainee table with userID
    trainee_query= text("UPDATE trainees SET status = 'rejected' where traineeID = :traineeID")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(traineeID[0])
    trainee_cursor = db.session.execute(trainee_query, {'traineeID': traineeID})
    # commit changes to db
    db.session.commit()
    if not trainee_cursor:   
        flash('Failed to reject trainee', 'error')
        return redirect(url_for('manager.get_deactivate_trainees_view'))
    flash('Trainee rejected successfully', 'success')
    return redirect(url_for('manager.get_deactivate_trainees_view'))

