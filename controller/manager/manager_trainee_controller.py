from flask import request, render_template, jsonify
from sqlalchemy import text
from app import db

manager = {
    "id": "100",
    "username": "Jupiter2000",
    "email": "jupiter@gmail.com"
}

"""
    This is the function that prepares data for the 'pending trainees' view, and returns the view with its data 
"""


def get_pending_trainees(request):
    # token is the manager id or the manager record

    # query = text("SELECT * from trainees where current_status = 'pending'")
    # result_cursor = db.session.execute(query)
    # rows = result_cursor.fetchall()
    # trainees = []
    # for row in rows:
    #     trainees.append(row._data)
    #  return render_template("manager/pending_trainees.html", manager=manager, trainees=trainees)

    return render_template('manager/trainee/pending_trainees.html', manager=manager, trainees=[
        ["1", "name1", "email1", "df1", "area1"],
        ["2", "name2", "email2", "df1", "area1"],
        ["3", "name3", "email3", "df1", "area1"]
    ])


"""
    This is the controller function that handles the approve button in the pending trainees view
    it's actually not yet implemented or linked to its view
"""


def approve_trainee_registration(request):
    pass


"""
    This is the controller function that handles the reject button in the pending trainees view
    it's actually not yet implemented or linked to its view
"""


def reject_trainee_registration(request):
    pass


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
    # from the token, get the manager id
    manager = {
        "id": "100",
        "username": "Jupiter2000",
        "email": "jupiter@gmail.com"
    }
    # get all account modification requests from the database

    # here's a mock of the returned data
    trainess = [
        ["1", "", "name1", "somehow the account details object"],
        ["2", "", "name2", "somehow the account details object"],
        ["3", "", "name3", "somehow the account details object"]
    ]
    return render_template("manager/trainee/trainee_account_modification.html", manager=manager, trainees=trainess)


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
