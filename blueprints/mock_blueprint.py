from flask import Flask, Blueprint, jsonify
from database import engine

mock_blueprint = Blueprint("mock", __name__)


@mock_blueprint.route('/mock', methods=['GET'])
def mock():
    # testing the database connection
    return jsonify({"status": "trying", "engine name": engine.name, "engine driver": engine.driver})
