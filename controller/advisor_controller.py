from flask import render_template


def index(token):
    # from token, fetch advisor id, then fetch the record from the database
    advisor = {
        "id": "20",
        "username": "venus2023",
        "email": "someemail@gmail.com",
        "discipline": "Python Programming",
        "max_number_of_trainees": 5,
    }
    return render_template('advisor/index.html', advisor=advisor)
