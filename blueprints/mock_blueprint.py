from flask import Blueprint, jsonify, render_template, flash
from app import db

mock_blueprint = Blueprint("mock", __name__)

@mock_blueprint.route('/mock', methods=['GET'])
def mock():
    # Testing the database connection
    return jsonify({"status": "trying", "engine name": db.engine.name, "engine driver": db.engine.driver})

@mock_blueprint.route('/view', methods=['GET'])
def mock_view():
    # just to look what the view would look like
    # flash("You're in the pending trainees page")
    manager = {
        "id": "100",
        "username": "Jupiter2000",
        "email": "jupiter@gmail.com"
    }
    return render_template('manager/pending_trainees.html', manager=manager, trainees=[
        ["1","name1","email1","df1", "area1"],
        ["2", "name2", "email2", "df1", "area1"],
        ["3", "name3", "email3", "df1", "area1"]
    ])