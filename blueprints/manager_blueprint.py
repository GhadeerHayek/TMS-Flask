from flask import Blueprint, request
from controller.manager import manager_trainee_controller, manager_controller, manager_advisor_controller, \
    manager_programs_controller

manager_blueprint = Blueprint("manager", __name__)


@manager_blueprint.route('/manager', methods=["GET"])
def dashboard_view():
    return manager_controller.index(request)


# Manager-Trainee Routes
@manager_blueprint.route('/trainees/pending', methods=["GET"])
def get_pending_trainees_view():
    return manager_trainee_controller.get_pending_trainees(request)


@manager_blueprint.route('/trainees/deactivate', methods=["GET"])
def get_deactivate_trainees_view():
    return manager_trainee_controller.get_deactivate_trainees(request)


@manager_blueprint.route('/trainees/account', methods=["GET"])
def get_trainees_accounts_view():
    return manager_trainee_controller.get_trainee_account(request)


@manager_blueprint.route('/trainees/account/details', methods=["GET"])
def get_trainees_accounts_details_view():
    return manager_trainee_controller.get_trainee_account_details(request)

# Manager-Advisor Routes


@manager_blueprint.route('/advisors/pending', methods=["GET"])
def get_pending_advisors_view():
    return manager_advisor_controller.get_pending_advisors(request)


@manager_blueprint.route('/advisors/deactivate', methods=["GET"])
def get_deactivate_advisors_view():
    return manager_advisor_controller.get_deactivate_advisors(request)


@manager_blueprint.route('/advisors/account', methods=["GET"])
def get_advisors_accounts_view():
    return manager_advisor_controller.get_advisor_account(request)


@manager_blueprint.route('/advisors/account/details', methods=["GET"])
def get_advisors_accounts_details_view():
    return manager_advisor_controller.get_advisor_account_details(request)


@manager_blueprint.route('/programs', methods=["GET"])
def get_all_programs_view():
    return manager_programs_controller.get_all_programs(request)


@manager_blueprint.route('/programs/create', methods=["GET"])
def get_add_program_view():
    return manager_programs_controller.get_add_program(request)


@manager_blueprint.route('/programs/edit', methods=["GET"])
def get_edit_program_view():
    return manager_programs_controller.get_edit_program(request)

# Manager - Billing
@manager_blueprint.route('/billing', methods=["GET"])
def get_balance_sheet_view():
    return manager_controller.get_balance_sheet(request)



# Manager - System Log