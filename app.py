import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load env variables
load_dotenv('.env')

# Setup flask app instance
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}/{3}".format(db_user, db_password, db_host, db_name)
app.config['USER_UPLOADS'] = '/static/user-uploads/'
db = SQLAlchemy(app)

# Register app blueprints here
from blueprints.mock_blueprint import mock_blueprint
app.register_blueprint(mock_blueprint)
from blueprints.auth_blueprint import auth_blueprint
app.register_blueprint(auth_blueprint)
from blueprints.trainee_blueprint import trainee_blueprint
app.register_blueprint(trainee_blueprint)
from blueprints.manager_blueprint import manager_blueprint
app.register_blueprint(manager_blueprint)
from blueprints.advisor_blueprint import advisor_blueprint
app.register_blueprint(advisor_blueprint)
