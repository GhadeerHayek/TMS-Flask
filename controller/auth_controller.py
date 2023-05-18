from flask import render_template, jsonify


def login_view():
    return render_template('login.html')


def handle_login(request):
    # assuming that we will return a success or failure response
    result = True
    response = {}
    if result:
        response["status"] = "success"
        response["message"] = "logged in"
        response["token"] = "a token"
    else:
        response["status"] = "failure"
        response["message"] = "nothing"
    return response


def signup_view(classification):
    classification = "trainee"
    if classification == "advisor":
        return render_template('registration/advisor_register.html')
    elif classification == "trainee":
        return render_template('registration/trainee_register.html')
    else:
        pass


def handle_signup(request):
    # assuming that we will return a success or failure response
    result = True
    response = {}
    if result:
        response["status"] = "success"
        response["message"] = "signed up"
    else:
        response["status"] = "failure"
        response["message"] = "nothing"
    return response
