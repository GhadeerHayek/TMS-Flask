from flask import request, render_template, jsonify
from sqlalchemy import text
from app import db

"""
    This is the function that prepares the data for the 'manager dashboard' view, returns the view with its data
"""


def index(request):
    # from token get id, from the id get the record in the database
    manager_id = "something"
    query = text("SELECT * from ")
    manager = {
        "id": "100",
        "username": "Jupiter2000",
        "email": "jupiter@gmail.com"
    }
    return render_template('manager/index.html', manager=manager)


