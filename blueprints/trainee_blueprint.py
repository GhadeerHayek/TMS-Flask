from flask import Flask, jsonify, render_template, Blueprint

trainee_blueprint = Blueprint("trainee", __name__)

@trainee_blueprint.route('/trainee', methods=["GET"])
def dashboard_view():
    return render_template('trainee/index.html')