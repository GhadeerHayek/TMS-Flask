from flask import Flask, jsonify, render_template, Blueprint

manager_blueprint = Blueprint("manager", __name__)

@manager_blueprint.route('/manager', methods=["GET"])
def dashboard_view():
    return render_template('manager/index.html')