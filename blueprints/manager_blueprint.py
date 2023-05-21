from flask import Flask, jsonify, render_template, Blueprint
from controller import manager_controller

manager_blueprint = Blueprint("manager", __name__)


@manager_blueprint.route('/manager', methods=["GET"])
def dashboard_view():
    return manager_controller.index("token")


@manager_blueprint.route('/trainees/pending', methods=["GET"])
def get_pending_trainees_view():
    token ="mock"
    return manager_controller.get_pending_trainees(token)


@manager_blueprint.route('/trainees/deactivate', methods=["GET"])
def get_deactivate_trainees_view():
    token ="mock"
    return manager_controller.get_deactivate_trainees(token)
