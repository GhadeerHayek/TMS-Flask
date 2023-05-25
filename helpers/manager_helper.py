from flask import jsonify, redirect, url_for, flash
from sqlalchemy import text
import helpers.token as tokenHelper
from app import app
from app import db


def verify_manager(token):
    if not token:
        flash('Token not found', 'error')
        return redirect(url_for('auth.login_view')) 
    payload = tokenHelper.verify_token(token)
    if not payload:
        flash('Paylod not found', 'error')
        return redirect(url_for('auth.login_view'))
    query = text("SELECT * from managers where userID ")
    result_set = db.session.execute(query, {'userID':payload['userID']})
    manager = result_set.fetchone()
    if not manager: 
        flash('Manager is not listed', 'error')
        return(redirect(url_for('auth.login')))
    return manager

