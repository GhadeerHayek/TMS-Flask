from flask import render_template
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


def get_pending_users():
    query = text("SELECT * from trainees where current_status = 'pending'")
    result_cursor = db.session.execute(query)
    rows = result_cursor.fetchall()
    final_result = []
    for row in rows:
        final_result.append(row)
    return final_result
