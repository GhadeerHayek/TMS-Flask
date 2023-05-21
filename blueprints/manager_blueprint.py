from flask import Flask, jsonify, render_template, Blueprint
from controller import manager_controller

manager_blueprint = Blueprint("manager", __name__)


@manager_blueprint.route('/manager', methods=["GET"])
def dashboard_view():
    return manager_controller.index("token")


@manager_blueprint.route('/trainees/pending', methods=["GET"])
def get_pending_trainees():
    return manager_controller.get_pending_trainees()

@manager_blueprint.route('/trainees', methods=["GET"])
def get_trainees():
    return render_template("manager/pending_trainees.html")