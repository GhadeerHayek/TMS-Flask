from flask import Flask, jsonify, render_template, Blueprint, request
from controller import trainee_controller
trainee_blueprint = Blueprint("trainee", __name__)

@trainee_blueprint.route('/trainee', methods=["GET"])
def dashboard_view():
    return trainee_controller.index("token")


@trainee_blueprint.route('/trainee/programs', methods=["GET"])
def trainee_programs_view():
    return trainee_controller.get_programs_for_trainee(request)

@trainee_blueprint.route('/trainee/training', methods=["GET"])
def trainee_training_view():
    return trainee_controller.get_training_program(request)


@trainee_blueprint.route('/trainee/training/form', methods=["GET"])
def trainee_training_form_view():
    return trainee_controller.trainee_training_form(request)