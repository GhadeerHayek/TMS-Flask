from flask import Flask, jsonify, render_template, Blueprint
from controller import advisor_controller
advisor_blueprint = Blueprint("advisor", __name__)

@advisor_blueprint.route('/advisor', methods=["GET"])
def dashboard_view():
    return advisor_controller.index("token")