from flask import Flask, jsonify, render_template, Blueprint, request
from controller import trainee_controller

trainee_blueprint = Blueprint("trainee", __name__)


# Dashboard Form-View Route
@trainee_blueprint.route('/trainee', methods=["GET"])
def dashboard_view():
    return trainee_controller.index(request)


# Apply-For-Training-Program Form-View Route
@trainee_blueprint.route('/trainee/programs', methods=["GET"])
def programs_view():
    return trainee_controller.get_programs(request)


# Apply button in the Apply-For-Trainin-Program Action Route
@trainee_blueprint.route('/trainee/programs/apply/<training_program_id>', methods=['POST'])
def program_application(training_program_id):
    return trainee_controller.handle_program_application(request, training_program_id)


# My-Training-Program Form-View Route
@trainee_blueprint.route('/trainee/training', methods=["GET"])
def training_view():
    return trainee_controller.get_training(request)


# Attendance-Records Form-View Route
@trainee_blueprint.route('/training/<registration_id>/form', methods=['GET'])
def attendance_form_view(registration_id):
    return trainee_controller.get_attendance_form(request, registration_id)


# Add new Attendance-Record Form-View Route
@trainee_blueprint.route('/training/<registration_id>/add', methods=['GET'])
def add_attendance_record_view(registration_id):
    return trainee_controller.get_record_add(request, registration_id)


# Add new Attendance-Record Action Route
@trainee_blueprint.route('/training/<registration_id>/add', methods=['POST'])
def handle_attendance_record(registration_id):
    return trainee_controller.handle_attendance_record_add(request, registration_id)


# Display program Form-View in the My-Training-Program Form-View Route
@trainee_blueprint.route('/program/<program_id>', methods=["GET"])
def one_program_view(program_id):
    return trainee_controller.get_program(request, program_id)


# Meetings Form-View Route
@trainee_blueprint.route('/meetings', methods=["GET"])
def get_meetings_view():
    return trainee_controller.get_meetings(request)


# Arrange-New-Meeting Form-View Route in the Meetings Form-View
@trainee_blueprint.route('/meetings/<registration_id>/add', methods=["GET"])
def get_add_meeting_view(registration_id):
    # the meeting has to be specific to a training
    return trainee_controller.get_add_meeting(request, registration_id)


# Add new meeting button Action Route
@trainee_blueprint.route('/meeting/add/<registration_id>', methods=["POST"])
def handle_meeting_add(registration_id):
    return trainee_controller.handle_meeting_add(request, registration_id)


# Trainee Profile Form-View Route
@trainee_blueprint.route('/profile', methods=["GET"])
def profile_view():
    return trainee_controller.get_profile_view(request)


# Trainee Profile Modification Action Route
@trainee_blueprint.route('/profile/edit', methods=['POST'])
def profile_edit():
    return trainee_controller.handle_profile_update(request)


# Trainee Profile Deactivation Action Route
@trainee_blueprint.route('/profile/delete', methods=['POST'])
def profile_deactivate():
    return trainee_controller.handle_profile_deactivation(request)
