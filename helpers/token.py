import jwt
from datetime import datetime, timedelta
from flask import flash

""" 
    Generates a token for authentication. 
    It should use a module that i currently can't remember its name 
    It take a parameter, that is the user row in the database, encrypts it, and returns its hash.
"""

SECRET_KEY = "My secert key "


def generate_token(user_record, secret_key):
    # set token expiry date
    exp_time = datetime.utcnow() + timedelta(hours=1)
    # prepare payload
    token_payload = {
        "userID": user_record[0],
        "username": user_record[1],
        "fullName": user_record[2],
        "email": user_record[3],
        "password": user_record[4],
        "classification": user_record[5],
        "status": user_record[6],
        "expire": exp_time.strftime('%Y-%m-%d %H:%M:%S')
    }
    # generate token
    token = jwt.encode(
        token_payload, secret_key, algorithm='HS256')
    return token


"""
    takes in a token, returns the encrypted data within it. 
    So if we assume we've encrypted the user's row in the database, this shall retrieve it. 
"""


def verify_token(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        # if it reaches this line, this means that it's decoded correctly
        # check expiration time
        if 'expire' in payload:
            exp_time = datetime.strptime(payload['expire'], '%Y-%m-%d %H:%M:%S')
            if datetime.utcnow() > exp_time:
                return False
            # token not expired and return data
            payload = {
                "userID": payload["userID"],
                "username": payload["username"],
                "fullName": payload["fullName"],
                "email": payload["email"],
                "password": payload["password"],
                "classification": payload["classification"],
                "status": payload["status"],
            }
            return payload
        else:
            return False
    except jwt.exceptions.DecodeError:
        # if it reaches this line, this means that it's decoded incorrectly
        return False


"""
    Helper function that checks the token to authorize the user
"""


def authorize_user(token):
    # if there's no token -> halt process
    if not token:
        return flash('Unauthorized user, no token', 'error')
    # verify and decode the token
    payload = verify_token(token, secret_key=SECRET_KEY)
    if isinstance(payload, dict):
        return payload
    else:
        return flash('User is not authorized.', 'error')
