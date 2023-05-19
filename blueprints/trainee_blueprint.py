from flask import Flask, jsonify, render_template, Blueprint
from controller import trainee_controller
trainee_blueprint = Blueprint("trainee", __name__)

@trainee_blueprint.route('/trainee', methods=["GET"])
def dashboard_view():
    return trainee_controller.index("token")