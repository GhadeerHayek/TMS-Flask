from flask import Flask, jsonify, render_template, Blueprint, request
from controller import advisor_controller
advisor_blueprint = Blueprint("advisor", __name__)

@advisor_blueprint.route('/advisor', methods=["GET"])
def dashboard_view():
    return advisor_controller.index("token")


@advisor_blueprint.route('/advisor/trainees/contact', methods=["GET"])
def contact_trainees():
    return advisor_controller.get_trainees_contact(request)


@advisor_blueprint.route('/advisor/trainess', methods=["GET"])
def active_trainees():
    return advisor_controller.get_my_trainees(request)


@advisor_blueprint.route('/program', methods=["GET"])
def program_material():
    return advisor_controller.get_program_materials(request)


@advisor_blueprint.route('/advisor/meetings', methods=["GET"])
def meetings():
    return advisor_controller.get_meeting_requests(request)


@advisor_blueprint.route('/advisor/reschedule', methods=["GET"])
def reschedule():
    return advisor_controller.get_reschedule_form(request)


@advisor_blueprint.route('/advisor/meeting/create', methods=["GET"])
def create_meeting():
    return advisor_controller.get_meeting_form(request)


@advisor_blueprint.route('/advisor/trainee/attendance', methods=["GET"])
def attendance_form():
    return advisor_controller.get_attendance_form(request)

@advisor_blueprint.route('/advisor/trainingprogram', methods=["GET"])
def training_program():
    return advisor_controller.get_training_material(request)


