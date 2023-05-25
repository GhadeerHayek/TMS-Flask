from flask import render_template, flash, redirect, url_for, jsonify
from sqlalchemy import text
import helpers.token as token_helper
import helpers.trainee_helper as trainee_helper
from app import db

programs = [
    ["1", "program1", "program1 description", "area1", "money", "somedate", "somedate"],
    ["2", "program2", "program2 description", "area1", "money", "somedate", "somedate"],
    ["3", "program3", "program3 description", "area1", "money", "somedate", "somedate"],
]
program = ["1", "program1", "program1 description", "area1", "money", "somedate", "somedate"],
trainee = {
    "id": "12",
    "username": "mars2001",
    "email": "ghadeerhayek2001@gmail.com",
    "desired_field": "Web Development",
    "area": "Technology",
    "current_training": 0
}

meetings = [
    ["meetingid1", "meeting for followup", "approved", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"],
    ["meetingid2", "meeting for followup", "approved", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"],
    ["meetingid3", "meeting for followup", "approved", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"]
]

registered_program = [
    "registration id", "program id", "trainee id", "attendance form id", "advisor id", "status "
]

attendance_records = [
    ["0", "1", "2001-09-09", "15:15", "15:15"],
    ["0", "1", "2001-09-09", "15:15", "15:15"],
    ["0", "1", "2001-09-09", "15:15", "15:15"]
]

"""
    function that retrieves the trainee-index form view, it also prepares the data to display in the form view
"""


def index(request):
    # token has the hashed user_id (trainee_id)
    token = request.cookies['token']
    if not token:
        flash('Token not found, invalid request', 'error')
        return redirect(url_for('auth.login_view'))
    trainee1 = trainee_helper.get_trainee_from_token(token)
    # if the query returned nothing -> it actually means we can't render the dashboard
    if not trainee1:
        flash('Trainee is not admitted to the system yet, trainee info: {0}'.format(trainee1), 'error')
        return redirect(url_for('auth.login_view'))
    # If, however, the query returned the row -> render the dashboard
    return render_template('trainee/index.html', trainee=trainee1)


"""
    prepares data for the training programs application view, renders the view with this data
"""


def get_programs(request):
    # from the request, we'll fetch the hashed user_id (trainee)
    # from the trainee, we'll fetch the interested area
    # from this field, we'll select all training programs using the area field
    # finally, return the view alongside with this data
    return render_template('trainee/programs.html', trainee=trainee, programs=programs)


"""
    action function that handles the application request and flashes messages for user in case of success or failure 
    not yet implemented 
"""


def handle_program_application(request):
    pass


"""
    This is the form-view function that renders the current training of a trainee details, which include the program data itself,
     the registration details of the program itself, link to the attendance form, link to schedule meetings
     So i'd guess it's the view that contains three components in one 
"""


def get_training(request):
    # from the request, we'll get the token. From the token, we'll get the hashed user_id (trainee)
    # from this trainee, we'll get its status (on_training)
    # if the current status is not on_training then we'll display an empty page, or a flashed message .. whatever error is
    # if the current_status is on_training, then we'll select the application_registiration record using the trainee_id
    # this record contains IDs
    # data: registiration id, training program id, advisor id, attendance form id, status of the registiration itself
    # the attendance form id is a link to a page that displays all the attendance records related to the whole thing
    # the training program is also a link to a page that displays the training program details in a card format
    # I haven't decided what to do with the advisor ID

    return render_template('trainee/training.html', trainee=trainee, registered_program=registered_program)


"""
    This function prepares the data for the form view that gets the records associated to an Attendance form
"""


def get_attendance_form(request):
    # this request shall contain the token, the form id
    # we'll select all records from the database where there's a match in the form ID then render the view
    return render_template('trainee/attendance-form.html', trainee=trainee, records=attendance_records)


"""
    This function renders the add record to the attendance form record, it's just an add form. 
"""


def get_record_add(request):
    return render_template('/trainee/add-record.html', trainee=trainee)


"""
    This function renders the view that displays the information regarding a selected training program 
"""


def get_program(request):
    return render_template('trainee/one-program.html', trainee=trainee, program=programs[0])


"""
    This function gets all the meetings of a specific user, then prepares this data so that it is rendered with the view 
"""


def get_meetings(request):
    # get the user id from the token in the request
    # select * from meetings where the trainee id = the fetched user id
    return render_template('trainee/meetings.html', trainee=trainee, meetings=meetings)


"""
    This function renders the add new meeting form
"""


def get_add_meeting(request):
    # supposed to get the trainee id and the advisor id associated to the training program and sends that to this form view
    # it also MUST call the function that handles meetings conflict
    return render_template('trainee/new-meeting.html', trainee=trainee)
    z
