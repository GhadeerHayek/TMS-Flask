import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load env variables
load_dotenv('.env')

# Setup flask app instance
app = Flask(__name__)

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}/{3}".format(db_user, db_password, db_host, db_name)
db = SQLAlchemy(app)

# Register app blueprints here
from blueprints.mock_blueprint import mock_blueprint
app.register_blueprint(mock_blueprint)