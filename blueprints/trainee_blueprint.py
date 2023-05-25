from flask import Flask, jsonify, render_template, Blueprint, request
from controller import trainee_controller

trainee_blueprint = Blueprint("trainee", __name__)


@trainee_blueprint.route('/trainee', methods=["GET"])
def dashboard_view():
    return trainee_controller.index(request)


@trainee_blueprint.route('/trainee/programs', methods=["GET"])
def programs_view():
    return trainee_controller.get_programs(request)


@trainee_blueprint.route('/trainee/training', methods=["GET"])
def training_view():
    return trainee_controller.get_training(request)


@trainee_blueprint.route('/training/form', methods=["GET"])
def attendance_form_view():
    return trainee_controller.get_attendance_form(request)


@trainee_blueprint.route('/training/form/add', methods=["GET"])
def add_attendance_record_view():
    return trainee_controller.get_record_add(request)


@trainee_blueprint.route('/trainee/training/program', methods=["GET"])
def one_program_view():
    return trainee_controller.get_program(request)


@trainee_blueprint.route('/meetings', methods=["GET"])
def get_meetings_view():
    return trainee_controller.get_meetings(request)


@trainee_blueprint.route('/meetings/add', methods=["GET"])
def get_add_meeting_view():
    return trainee_controller.get_add_meeting(request)
