from flask import Flask, Blueprint, render_template, url_for, redirect, request, jsonify
from controller import auth_controller

auth_blueprint = Blueprint("auth", __name__)


# this is the route that returns the login form view
@auth_blueprint.route('/login', methods=['GET'])
def login_view():
    return auth_controller.login_view()


# this is the route that handles the login request
@auth_blueprint.route('/auth/login', methods=['POST'])
def login():
    return auth_controller.handle_login(request)


# this is the route that returns the signup form view
@auth_blueprint.route('/signup', methods=['GET'])
def signup_view():
    # query string from request
    classification = request.args.get('classification')
    print(classification)
    return auth_controller.signup_view(classification)


# this is the route that handles the signup request
@auth_blueprint.route('/auth/signup', methods=['POST'])
def signup():
    result = {}
    # inputs from request are: hidden classification
    classification = request.form['classification']
    if classification == 'trainee':
        return auth_controller.handle_trainee_signup(request)
    elif classification == 'advisor':
        # TODO: call for advisor signup function and return result
        return auth_controller.handle_advisor_signup(request)
    else:
        # TODO: tampered classification, flash error message
        result = {"status": "error"}
