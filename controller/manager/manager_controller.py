from flask import request, render_template, jsonify, flash, redirect, url_for
from sqlalchemy import text
from app import db
import helpers.manager_helper as mghelper
import smtplib


"""
    This is the function that prepares the data for the 'manager dashboard' view, returns the view with its data
"""
def index(request):
    # from token get id, from the id get the record in the database
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    return render_template('manager/index.html', manager=manager)


# id, transaction name, type(credit/debit), amount, trainee Id, timestamp
def get_balance_sheet(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    # prepare list of balance sheet records
    # token is the manager id or the manager record
    query = text("SELECT * FROM balance_sheet")
    result_cursor = db.session.execute(query)
    rows = result_cursor.fetchall()
    transactions = []
    for row in rows:
        transactions.append(row._data)
    return render_template("manager/billing.html", transactions=transactions, manager=manager)


def get_email_form(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    return render_template("manager/mailing.html", manager=manager)



def send_email(request):
    # sender email credentials 
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    # print(manager.email)

    recipient = request.form['email']
    message = request.form['message']
    subject = request.form['subject']
 
    # return mghelper.verify_manager(manager.email)
    pass


def get_system_log(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    return render_template("manager/logging.html", manager=manager)
