from flask import request, render_template, jsonify
from sqlalchemy import text
from app import db

"""
    This is the function that prepares the data for the 'manager dashboard' view, returns the view with its data
"""


def index(token):
    # from token get id, from the id get the record in the database
    manager_id = "something"
    query = text("SELECT * from ")
    manager = {
        "id": "100",
        "username": "Jupiter2000",
        "email": "jupiter@gmail.com"
    }
    return render_template('manager/index.html', manager=manager)


"""
    This is the function that prepares data for the 'pending trainees' view, and returns the view with its data 
"""


def get_pending_trainees(token):
    # token is the manager id or the manager record

    manager = {
        "id": "100",
        "username": "Jupiter2000",
        "email": "jupiter@gmail.com"
    }
    # query = text("SELECT * from trainees where current_status = 'pending'")
    # result_cursor = db.session.execute(query)
    # rows = result_cursor.fetchall()
    # trainees = []
    # for row in rows:
    #     trainees.append(row._data)
    #  return render_template("manager/pending_trainees.html", manager=manager, trainees=trainees)

    return render_template('manager/pending_trainees.html', manager=manager, trainees=[
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


def approve_trainee(request):
    trainee_id = request.form['trainee_id']
    trainee_result = db.session.execute(
        "UPDATE trainees SET current_status = 'new' where id = :id",
        params={"id": trainee_id}
    );
    num_affected_rows = trainee_result.rowcount
    return jsonify({"affected rows": num_affected_rows})


"""
    This is the function that prepares the data for the view 'deactivate trainee account', 
    returns the view along with its data 
    
"""


def get_deactivate_trainees(token):
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

    return render_template("manager/deactivate_trainee.html", manager=manager, trainees=trainees)


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
