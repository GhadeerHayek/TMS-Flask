from flask import Flask, jsonify, render_template, Blueprint

advisor_blueprint = Blueprint("advisor", __name__)

@advisor_blueprint.route('/advisor', methods=["GET"])
def dashboard_view():
    return render_template('advisor/index.html')