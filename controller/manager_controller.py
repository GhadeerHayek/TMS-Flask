from flask import render_template


def index(token):
    # from token get id, from the id get the record in the database
    manager = {
        "id": "100",
        "username":"Jupiter2000",
        "email":"jupiter@gmail.com"
    }
    return render_template('manager/index.html', manager=manager)
