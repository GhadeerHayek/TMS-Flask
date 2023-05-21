from flask import Flask, jsonify, render_template, Blueprint, request
from controller import manager_controller

manager_blueprint = Blueprint("manager", __name__)


@manager_blueprint.route('/manager', methods=["GET"])
def dashboard_view():
    return manager_controller.index(request)


@manager_blueprint.route('/trainees/pending', methods=["GET"])
def get_pending_trainees_view():
    return manager_controller.get_pending_trainees(request)


@manager_blueprint.route('/trainees/deactivate', methods=["GET"])
def get_deactivate_trainees_view():
    return manager_controller.get_deactivate_trainees(request)


@manager_blueprint.route('/trainees/account', methods=["GET"])
def get_trainees_accounts_view():
    return manager_controller.get_trainee_account(request)


@manager_blueprint.route('/account/details', methods=["GET"])
def get_trainees_accounts_details_view():
    return manager_controller.get_trainee_account_details(request)
