import helpers.token as token_helper
import helpers.helper as helper
from flask import flash, redirect, url_for, jsonify
from app import db
from sqlalchemy import text


def get_trainee_from_token(token):
    payload = token_helper.verify_token(token)
    if not payload:
        flash('Invalid token, invalid request', 'error')
        return redirect(url_for('auth.login_view'))
    # payload has a userID, this is what we're going to use to fetch the trainee record
    query = text("""
                SELECT * from trainees where userID = :userID and status IN ('active', 'on_training')
        """)
    result_set = db.session.execute(query, {'userID': payload['userID']})
    trainee = result_set.fetchone()
    return {
        "traineeID": trainee[0],
        "username": trainee[1],
        "fullName": trainee[2],
        "email": trainee[3],
        "desired_field": trainee[4],
        "area_of_training": trainee[5],
        "status": trainee[6],
        "balance": trainee[7],
        "training_materials": trainee[8],
        "userID": trainee[9],

    }
