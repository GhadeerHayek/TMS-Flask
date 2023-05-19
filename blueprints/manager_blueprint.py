from flask import Flask, jsonify, render_template, Blueprint
from controller import manager_controller

manager_blueprint = Blueprint("manager", __name__)


@manager_blueprint.route('/manager', methods=["GET"])
def dashboard_view():
    return manager_controller.index("token")
