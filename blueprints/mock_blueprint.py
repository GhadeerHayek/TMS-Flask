from flask import Blueprint, jsonify
from app import db

mock_blueprint = Blueprint("mock", __name__)

@mock_blueprint.route('/mock', methods=['GET'])
def mock():
    # Testing the database connection
    return jsonify({"status": "trying", "engine name": db.engine.name, "engine driver": db.engine.driver})