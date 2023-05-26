from flask import Blueprint, jsonify, render_template, flash, request
from app import db

mock_blueprint = Blueprint("mock", __name__)

trainee = ["1", "name1", "email1", "df1", "area1"]


@mock_blueprint.route('/', methods=['GET'])
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
    return render_template('manager/trainee/pending_trainees.html', manager=manager, trainees=[
        ["1", "name1", "email1", "df1", "area1"],
        ["2", "name2", "email2", "df1", "area1"],
        ["3", "name3", "email3", "df1", "area1"]
    ])


@mock_blueprint.route('/mock2', methods=['GET'])
def mock2():
    return render_template('manager/profile-details.html',
                           manager={
                               "id": "100",
                               "username": "Jupiter2000",
                               "email": "jupiter@gmail.com"
                           })


@mock_blueprint.route('/test', methods=['GET'])
def mock3():
    meetings = [
        ["meetingid1", "meeting for followup", "approved", "https://linktoyou",
         "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"],
        ["meetingid2", "meeting for followup", "approved", "https://linktoyou",
         "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"],
        ["meetingid3", "meeting for followup", "approved", "https://linktoyou",
         "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"]
    ]
    return render_template('trainee/meetings.html', trainee=trainee, meetings=meetings)
@mock_blueprint.route('/mock4', methods=["GET"])
def mock4():
    return render_template('trainee/new-meeting.html', trainee=trainee)

@mock_blueprint.route('/mock5', methods=["GET"])
def mock5():
    return jsonify(request.cookies)