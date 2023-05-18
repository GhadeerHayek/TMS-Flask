import os
from sqlalchemy import create_engine

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')


db_url = "mysql+pymysql://{0}:{1}@{2}/{3}".format(db_user, db_password, db_host, db_name)

engine = create_engine(db_url)

print(engine.name)
print(engine.driver)