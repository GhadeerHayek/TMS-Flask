from flask import Flask, jsonify, render_template, Blueprint, request
from controller import trainee_controller

trainee_blueprint = Blueprint("trainee", __name__)


@trainee_blueprint.route('/trainee', methods=["GET"])
def dashboard_view():
    return trainee_controller.index(request)


@trainee_blueprint.route('/trainee/programs', methods=["GET"])
def programs_view():
    return trainee_controller.get_programs(request)


@trainee_blueprint.route('/trainee/programs/apply/<training_program_id>', methods=['POST'])
def program_application(training_program_id):
    return trainee_controller.handle_program_application(request, training_program_id)


@trainee_blueprint.route('/trainee/training', methods=["GET"])
def training_view():
    return trainee_controller.get_training(request)


@trainee_blueprint.route('/training/<registration_id>/form', methods=['GET'])
def attendance_form_view(registration_id):
    return trainee_controller.get_attendance_form(request, registration_id)


@trainee_blueprint.route('/training/form/add', methods=['GET'])
def add_attendance_record_view():
    return trainee_controller.get_record_add(request)

@trainee_blueprint.route('/training/form/add', methods=['POST'])
def handle_attendance_record():
    return trainee_controller.handle_attendance_record_add(request)


@trainee_blueprint.route('/program/<program_id>', methods=["GET"])
def one_program_view(program_id):
    return trainee_controller.get_program(request, program_id)


@trainee_blueprint.route('/meetings', methods=["GET"])
def get_meetings_view():
    return trainee_controller.get_meetings(request)


@trainee_blueprint.route('/meetings/add', methods=["GET"])
def get_add_meeting_view():
    return trainee_controller.get_add_meeting(request)


@trainee_blueprint.route('/profile', methods=["GET"])
def profile_view():
    return trainee_controller.get_profile_view(request)


@trainee_blueprint.route('/profile/edit', methods=['POST'])
def profile_edit():
    return trainee_controller.handle_profile_update(request)


@trainee_blueprint.route('/profile/delete', methods=['POST'])
def profile_deactivate():
    return trainee_controller.handle_profile_deactivation(request)
