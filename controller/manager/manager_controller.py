from flask import request, render_template, jsonify, flash, redirect, url_for
from sqlalchemy import text
from app import db
import helpers.manager_helper as mghelper
import smtplib


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
    print(manager)
    return mghelper.verify_manager(token)
    # gmail_user = 'your_email@gmail.com'
    # gmail_password = 'your_password'

    # sent_from = gmail_user
    # # recipient credentials 
    # to = ['person_a@gmail.com', 'person_b@gmail.com']
    # subject = 'Lorem ipsum dolor sit amet'
    # body = 'consectetur adipiscing elit'

    # email_text = """\
    # From: %s
    # To: %s
    # Subject: %s

    # %s
    # """ % (sent_from, ", ".join(to), subject, body)

    # try:
    #     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #     smtp_server.ehlo()
    #     smtp_server.login(gmail_user, gmail_password)
    #     smtp_server.sendmail(sent_from, to, email_text)
    #     smtp_server.close()
    #     print ("Email sent successfully!")
    # except Exception as ex:
    #     print ("Something went wrong….",ex)


def get_system_log(request):
    pass