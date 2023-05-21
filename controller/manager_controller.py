from flask import request,render_template, jsonify
from sqlalchemy import text
from app import db


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


def get_pending_trainees():
    query = text("SELECT * from trainees where current_status = 'pending'")
    result_cursor = db.session.execute(query)
    rows = result_cursor.fetchall()
    trainees = []
    for row in rows:
        trainees.append(row._data)

    # TODO: when you implement the query
    #  return render_template("manager/pending_trainees.html", manager=manager, trainees=trainees)
    manager = {
        "id": "100",
        "username": "Jupiter2000",
        "email": "jupiter@gmail.com"
    }
    return render_template('manager/pending_trainees.html', manager=manager, trainees=[
        ["1", "name1", "email1", "df1", "area1"],
        ["2", "name2", "email2", "df1", "area1"],
        ["3", "name3", "email3", "df1", "area1"]
    ])

def approve_trainee(request):
    trainee_id = request.form['trainee_id']
    trainee_result = db.session.execute(
        "UPDATE trainees SET current_status = 'new' where id = :id",
        params={"id":trainee_id}
    );
    num_affected_rows = trainee_result.rowcount
    return jsonify({"affected rows" : num_affected_rows})