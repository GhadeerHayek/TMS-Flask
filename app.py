from flask import Flask
from blueprints import mock_blueprint
from dotenv import load_dotenv

# load env variables
load_dotenv('.env')
# setup flask app instance
app = Flask(__name__)

# register app blueprints here
app.register_blueprint(mock_blueprint.mock_blueprint)
