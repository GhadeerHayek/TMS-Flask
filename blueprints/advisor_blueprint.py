from flask import Flask, jsonify, render_template, Blueprint, request
from controller import advisor_controller

advisor_blueprint = Blueprint("advisor", __name__)


# Advisor Dashboard Form-View Route
@advisor_blueprint.route('/advisor', methods=["GET"])
def dashboard_view():
    return advisor_controller.index(request)


# All-Trainees --> My-Trainees Form-View Route
@advisor_blueprint.route('/advisor/trainess', methods=["GET"])
def active_trainees():
    return advisor_controller.get_my_trainees(request)


# My-Trainees - Current Trainees - check trainee attendance form button / Form-View  Route
@advisor_blueprint.route('/advisor/trainees/<traineeID>/attendance/', methods=["GET"])
def attendance_form(traineeID):
    return advisor_controller.get_attendance_form(request, traineeID)


# My-Trainees - New Trainees Requests Form-View Route
@advisor_blueprint.route('/advisor/trainees/new', methods=["GET"])
def contact_trainees():
    return advisor_controller.get_trainees_contact(request)


# My-Trainees - New Trainees Requests - Approve trainee button Action Route
@advisor_blueprint.route('/advisor/trainees/<traineeID>/approve', methods=["POST"])
def handle_trainee_approval(traineeID):
    return advisor_controller.approve_trainne(request, traineeID)


# My-Trainees - New Trainees Requests - Reject trainee button Action Route
@advisor_blueprint.route('/advisor/trainees/<traineeID>/reject', methods=["POST"])
def handle_trainee_rejection(traineeID):
    return advisor_controller.reject_trainee(request, traineeID)


# Meetings Form-View Route
@advisor_blueprint.route('/advisor/meetings', methods=["GET"])
def get_advisor_meetings_view():
    return advisor_controller.get_meetings(request)


# Arrange-New-Meeting Form-View Route in the Meetings Form-View
@advisor_blueprint.route('/meetings/add', methods=["GET"])
def get_advisor_add_meeting_view():
    # the meeting has to be specific to a training
    return advisor_controller.get_add_meeting(request)


# Add new meeting button Action Route
@advisor_blueprint.route('/meeting/create', methods=["POST"])
def handle_advisor_meeting_add():
    return advisor_controller.handle_meeting_add(request)


# Advisor Profile Modification Action Route
@advisor_blueprint.route('/profile/edit', methods=['POST'])
def advisor_profile_edit():
    return advisor_controller.handle_profile_update(request)


# Advisor Profile Deactivation Action Route
@advisor_blueprint.route('/profile/delete', methods=['POST'])
def advisor_profile_deactivate():
    return advisor_controller.handle_profile_deactivation(request)


@advisor_blueprint.route('/meeting/<meetingID>/approve', methods=['POST'])
def handle_approve_meeting(meetingID):
    return advisor_controller.approve_meeting(request, meetingID)


@advisor_blueprint.route('/meeting/<meetingID>/cancel', methods=['POST'])
def handle_cancel_meeting(meetingID):
    return advisor_controller.cancel_meeting(request, meetingID)

