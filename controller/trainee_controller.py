from flask import render_template, flash, redirect, url_for, jsonify
from sqlalchemy import text
import helpers.token as token_helper
import helpers.trainee_helper as trainee_helper
from app import db
import time

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
    payload = token_helper.verify_token(token)
    # if the query returned nothing -> it actually means we can't render the dashboard
    if not payload:
        flash('Invalid token', 'error')
        return redirect(url_for('auth.login_view'))
    # If, however, the query returned the row -> render the dashboard
    return render_template('trainee/index.html', trainee=payload)


"""
    prepares data for the training programs application view, renders the view with this data
"""


def get_programs(request):
    # from the request, we'll fetch the hashed user_id (trainee)
    token = request.cookies['token']
    trainee1 = token_helper.verify_token(token)
    if not trainee1:
        flash("Invalid token", 'error')
        return redirect(url_for('auth.login_view'))
    # from the trainee, we'll fetch the interested area
    # from this field, we'll select all training programs using the area field
    query = text("""
        SELECT * from training_programs where area_of_training = :area
    """)
    result_set = db.session.execute(query, {"area": trainee1['area_of_training']}).fetchall()
    # finally, return the view alongside with this data
    return render_template('trainee/programs.html', trainee=trainee1, programs=result_set)


"""
    action function that handles the training program application request and flashes messages for user in case of success or failure 
    not yet implemented 
"""


def handle_program_application(request, training_program_id):
    # from the request, we'll fetch the hashed user_id (trainee)
    token = request.cookies['token']
    trainee1 = token_helper.verify_token(token)
    if not trainee1:
        flash("Invalid token", 'error')
        return redirect(url_for('auth.login_view'))
    # the trainee can only have one training program at a time, so check that first
    current_status = db.session.execute(
        text(
            """
            SELECT status from trainees where traineeID = :traineeID
            """
        ), {
            "traineeID": trainee1['traineeID']
        }
    ).fetchone()[0]
    if current_status == 'on_training':
        flash('You are already on training', 'error')
        # TODO: is sufficient to flash messages?
        return redirect(request.referrer)
    else:
        # if not, then add the training program to the registered training programs
        # the default registration status is pending, waiting for approval by the manager
        query = text(""" INSERT INTO training_registration  (training_program_id, traineeID, status)
        VALUES (:training_program_id, :traineeID, 'pending');
        """)
        params = {'training_program_id': training_program_id, 'traineeID': trainee1["traineeID"]}
        result = db.session.execute(query, params)
        if not result:
            flash('failed to apply, please try again')
            return redirect(request.referrer)
        db.session.commit()
        flash("Your training application is in review, wait for reply", 'error')
        # NOTE: the trainee can submit any number of application as long as his status is active
        # the manager should see all of these applications.
        # once an application is approved, the trainee status has to be "on_training", assigns advisor, assigns form_id
        # but what happens for all other applications? revoked?
        return redirect(url_for('trainee.programs_view'))


"""
    This is the form-view function that renders the current training of a trainee details,
    which include the program data itself,
    the registration details of the program itself,
    link to the attendance form,
    link to schedule meetings.
    So i'd guess it's the view that contains three components in one 
    
    to get the current training, I are assuming that there's a status: approved that indicates current training
    and the finished trainings are marked as completed, so i can guarantee the current training is only selected 
"""


def get_training(request):
    # from the request, we'll fetch the hashed user_id (trainee)
    token = request.cookies['token']
    trainee1 = token_helper.verify_token(token)
    if not trainee1:
        flash("Invalid token", 'error')
        return redirect(url_for('auth.login_view'))
    # from this trainee, we'll get its status (on_training)
    current_status = db.session.execute(
        text(
            """
            SELECT status from trainees where traineeID = :traineeID
            """
        ), {
            "traineeID": trainee1['traineeID']
        }
    ).fetchone()[0]
    # if the current status is not on_training then we'll display an empty page,
    # or a flashed message .. whatever error is
    if current_status != 'on_training':
        flash("No current training to display")
        return redirect(request.referrer)
    else:
        # if the current_status is on_training, then we'll select the application_registiration record using the trainee_id
        query = text("""
                        SELECT * from training_registration where traineeID = :traineeID and status = 'approved'
                    """)
        registered_program1 = db.session.execute(query, {"traineeID": trainee1['traineeID']}).fetchone()
        # this record contains IDs
        # data: registiration id, training program id, advisor id, attendance form id, status of the registiration itself
        # the attendance form id is a link to a page that displays all the attendance records related to the whole thing
        # the training program is also a link to a page that displays the training program details in a card format
        # I haven't decided what to do with the advisor ID, i could display an advisor card
        if not registered_program1:
            flash("Failed to get training", 'error')
        return render_template('trainee/training.html', trainee=trainee1, registered_program=registered_program1)


"""
    This function prepares the data for the form view that gets the records associated to an Attendance form
"""


def get_attendance_form(request, registration_id):
    # from the request, we'll fetch the hashed user_id (trainee)
    token = request.cookies['token']
    trainee1 = token_helper.verify_token(token)
    if not trainee1:
        flash("Invalid token", 'error')
        return redirect(url_for('auth.login_view'))
    # from the attendance_records, we'll select all records that belong to a specific registration_id
    # i think this is a list of records objects
    attendance_records1 = db.session.execute(
        text("""
            SELECT * 
            from attendance_records 
            WHERE training_programID = :registration_id 
        """), {
            "registration_id": registration_id
        }
    ).fetchall()
    if not attendance_records1:
        flash("No records found")
    return render_template('trainee/attendance-form.html', trainee=trainee1, registration_id=registration_id,
                           records=attendance_records1)


"""
    This function renders the add record to the attendance form record, it's just an add form. 
"""


def get_record_add(request, registration_id):
    return render_template('/trainee/add-record.html', registration_id=registration_id, trainee=trainee)


"""
    This function handles the add attendance record functionality 

"""


def handle_attendance_record_add(request, registration_id):
    # check the token for authorization purposes
    # from the request, we'll fetch the hashed user_id (trainee)
    token = request.cookies['token']
    trainee1 = token_helper.verify_token(token)
    if not trainee1:
        flash("Invalid token", 'error')
        return redirect(url_for('auth.login_view'))
    # get the registration id from path parameters
    date = request.form['date']
    check_in = request.form['startTime']
    check_out = request.form['endTime']
    # insert record into database
    result = db.session.execute(
        text("""
    INSERT INTO attendance_records (training_programID, date,check_in, check_out) VALUES (:registration_id, :date, :check_in, :check_out)
    """),
        {"registration_id": registration_id,
         "date": date,
         "check_in": check_in,
         "check_out": check_out
         }
    ).rowcount
    # flash
    if not result:
        flash("failed to insert records", 'error')
    db.session.commit()
    return redirect(request.referrer)


"""
    This function renders the view that displays the information regarding a selected training program 
"""


def get_program(request, program_id):
    # ensure token existence
    # from the request, we'll fetch the hashed user_id (trainee)
    token = request.cookies['token']
    trainee1 = token_helper.verify_token(token)
    if not trainee1:
        flash("Invalid token", 'error')
        return redirect(url_for('auth.login_view'))
    # select the program_id no matter is the case
    program = db.session.execute(
        text("""
            SELECT * from training_programs where programID = :programID
        """),
        {
            "programID": program_id
        }
    ).fetchone()
    if not program:
        flash("program not found", 'error')
    return render_template('trainee/one-program.html', trainee=trainee1, program=program)


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


"""
    This is the function that prepares the profile view for a specific trainee
    it prepares the data and renders the trainee profile view 
"""


def get_profile_view(request):
    token = request.cookies['token']
    if not token:
        flash('Token not found, invalid request', 'error')
        return redirect(url_for('auth.login_view'))
    trainee1 = token_helper.verify_token(token)
    # if the query returned nothing -> it actually means we can't render the dashboard
    if not trainee1:
        flash('Invalid token', 'error')
        return redirect(url_for('auth.login_view'))
    return render_template('trainee/trainees-profile.html', trainee=trainee1)


"""
    This is the function that handles account modifications requests. 
"""


def handle_profile_update(request):
    # the profile update request contains all the trainee information
    username = request.form['username']
    fullname = request.form['fullName']
    area_of_training = request.form['area']
    desired_field = request.form['desiredField']
    email = request.form['email']
    # those value can not be null, there's a default value
    # TODO: maybe i should check for their format
    token = request.cookies['token']
    trainee1 = token_helper.verify_token(token)
    if not trainee1:
        flash("Invalid token", 'error')
        return redirect(url_for('auth.login_view'))
    # proceed with the update
    query = text("""
            UPDATE trainees 
            SET username=:username,
            fullname=:fullname,
            area_of_training=:area,
            desired_field = :desired_field,
            email=:email,
            status = 'in_review'
            WHERE traineeID = :traineeID;
        """)
    params = {
        "username": username,
        "fullname": fullname,
        "area": area_of_training,
        "desired_field": desired_field,
        "email": email,
        "traineeID": trainee1["traineeID"]
    }
    result_set = db.session.execute(query, params).rowcount
    # the user information is updated, but the thing is, this information must be reviewed, so the status must be pending
    if result_set > 0:
        # success
        db.session.commit()
        flash('Account modification is in manager review, your account is onhold until. Check your email')
        return redirect(url_for('auth.login_view'))
    else:
        flash('Failed to submit account modification, try again', 'error')
        return redirect(url_for('trainee.profile_view'))


"""
    This is the function that handles account deactivation requests.
"""


def handle_profile_deactivation(request):
    token = request.cookies['token']
    trainee1 = token_helper.verify_token(token)
    if not trainee1:
        flash("Invalid token", 'error')
        return redirect(url_for('auth.login_view'))
    # proceed with the update
    query = text("""
                UPDATE trainees 
                SET status = 'inactive'
                WHERE traineeID = :traineeID;
            """)
    params = {
        "traineeID": trainee1["traineeID"]
    }
    result_set = db.session.execute(query, params).rowcount
    # the user information is updated, but the thing is, this information must be reviewed, so the status must be pending
    if result_set > 0:
        # success
        db.session.commit()
        flash('Account deactivation is in manager review. Check your email')
        return redirect(url_for('auth.login_view'))
    else:
        flash('Failed to submit account deactivation, try again', 'error')
        return redirect(url_for('trainee.profile_view'))
