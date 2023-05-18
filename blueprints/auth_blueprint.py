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
    print(request, "is going to controller function")
    return jsonify(auth_controller.handle_login(request))


# this is the route that returns the signup form view
@auth_blueprint.route('/signup', methods=['GET'])
def signup_view():
    # query string from request
    return auth_controller.signup_view(request.args.get('classification'))


# this is the route that handles the signup request
@auth_blueprint.route('/auth/signup', methods=['POST'])
def signup():
    return jsonify(auth_controller.handle_signup(request))
