from flask import request, render_template, jsonify, flash, redirect, url_for
from sqlalchemy import text
from app import db
import helpers.manager_helper as mghelper


manager = {
    "id": "100",
    "username": "Jupiter2000",
    "email": "jupiter@gmail.com"
}

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
    # prepare list of balance sheet records
    transactions = [
        ["1", "program registration", "credit", 100, "some trainee id", "some datetime"],
        ["2", "program registration 2", "credit", 100, "some trainee id", "some datetime"],
        ["3", "program registration 3", "credit", 100, "some trainee id", "some datetime"],
    ]
    return render_template("manager/billing.html", transactions=transactions, manager=manager)


def get_email_form(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    return render_template("manager/mailing.html", manager=manager)



def send_email(request):
    pass


def get_system_log(request):
    pass