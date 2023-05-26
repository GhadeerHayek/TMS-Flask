from flask import Blueprint, request
from controller.manager import manager_trainee_controller, manager_controller, manager_advisor_controller, manager_programs_controller

manager_blueprint = Blueprint("manager", __name__)


@manager_blueprint.route('/manager', methods=["GET"])
def dashboard_view():
    return manager_controller.index(request)


# Manager-Trainee Routes
@manager_blueprint.route('/trainees/pending', methods=["GET"])
def get_pending_trainees_view():
    return manager_trainee_controller.get_pending_trainees(request)


@manager_blueprint.route('/approve/trainee/', methods=["POST"])
def approve_trainee():
    return manager_trainee_controller.approve_trainee_registration(request)


@manager_blueprint.route('/reject/trainee/', methods=["POST"])
def reject_trainee():
    return manager_trainee_controller.reject_trainee_registration(request)


@manager_blueprint.route('/training/requests', methods=["GET"])
def get_training_requests():
    return manager_trainee_controller.get_training_requests_view(request)


@manager_blueprint.route('/training/requests/approve', methods=["POST"])
def approve_training_requests():
    return manager_trainee_controller.approve_training_request(request)


@manager_blueprint.route('/training/requests/reject', methods=["POST"])
def reject_training_requests():
    return manager_trainee_controller.reject_training_request(request)


@manager_blueprint.route('/trainees/deactivate/all', methods=["GET"])
def get_deactivate_trainees_view():
    return manager_trainee_controller.get_deactivate_trainees(request)


@manager_blueprint.route('/trainees/deactivate', methods=["POST"])
def deactivate_trainee():
    return manager_trainee_controller.approve_trainee_deactivation(request)


@manager_blueprint.route('/trainees/reject/deactivate', methods=["POST"])
def reject_deactivate_trainee():
    return manager_trainee_controller.reject_trainee_deactivation(request)


@manager_blueprint.route('/trainees/account', methods=["GET"])
def get_trainees_accounts_view():
    return manager_trainee_controller.get_trainee_account(request)


@manager_blueprint.route('/trainees/account/details', methods=["GET"])
def get_trainees_accounts_details_view():
    return manager_trainee_controller.get_trainee_account_details(request)


@manager_blueprint.route('/trainees/approve/modifications', methods=["POST"])
def accept_trainee_modification():
    return manager_trainee_controller.accept_trainee_modifications(request)


@manager_blueprint.route('/trainees/reject/modifications', methods=["POST"])
def reject_trainee_modification():
    return manager_trainee_controller.reject_trainee_modifications(request)


# Manager-Advisor Routes


@manager_blueprint.route('/advisors/pending', methods=["GET"])
def get_pending_advisors_view():
    return manager_advisor_controller.get_pending_advisors(request)


@manager_blueprint.route('/approve/advisor', methods=["POST"])
def approve_advisor():
    return manager_advisor_controller.approve_advisors_registration(request)


@manager_blueprint.route('/reject/advisor', methods=["POST"])
def reject_advisor():
    return manager_advisor_controller.reject_advisors_registration(request)


@manager_blueprint.route('/advisors/account', methods=["GET"])
def get_advisors_accounts_view():
    return manager_advisor_controller.get_advisor_account(request)


@manager_blueprint.route('/advisors/account/details', methods=["GET"])
def get_advisors_accounts_details_view():
    return manager_advisor_controller.get_advisor_account_details(request)


@manager_blueprint.route('/advisors/approve/modifications', methods=["POST"])
def accept_advisor_modification():
    return manager_advisor_controller.accept_advisor_modifications(request)


@manager_blueprint.route('/advisors/account/details', methods=["POST"])
def reject_advisor_modification():
    return manager_advisor_controller.reject_advisor_modifications(request)


@manager_blueprint.route('/advisors/deactivate/all', methods=["GET"])
def get_deactivate_advisors_view():
    return manager_advisor_controller.get_deactivate_advisors(request)


@manager_blueprint.route('/advisor/deactivate', methods=["POST"])
def deactivate_advisor():
    return manager_advisor_controller.approve_advisor_deactivation(request)


@manager_blueprint.route('/advisor/reject/deactivate', methods=["POST"])
def reject_deactivate_advisor():
    return manager_advisor_controller.reject_advisor_deactivation(request)

# Progam Routes

@manager_blueprint.route('/programs', methods=["GET"])
def get_all_programs_view():
    return manager_programs_controller.get_all_programs(request)


@manager_blueprint.route('/programs/create/form', methods=["GET"])
def get_add_program_view():
    return manager_programs_controller.get_add_program(request)


@manager_blueprint.route('/program/create', methods=["POST"])
def add_program():
    return manager_programs_controller.handle_add_program(request)


@manager_blueprint.route('/programs/edit', methods=["GET"])
def get_edit_program_view():
    return manager_programs_controller.get_edit_program(request)


@manager_blueprint.route('/programs/edit/save', methods=["POST"])
def edit_program():
    return manager_programs_controller.handle_edit_program(request)


@manager_blueprint.route('/program/delete', methods=["POST"])
def delete_program():
    return manager_programs_controller.handle_delete_program(request)

# Manager - Billing
@manager_blueprint.route('/billing', methods=["GET"])
def get_balance_sheet_view():
    return manager_controller.get_balance_sheet(request)



# Manager - Emailing
@manager_blueprint.route('/email/create', methods=["GET"])
def get_email_form():
    return manager_controller.get_email_form(request)


@manager_blueprint.route('/email/send', methods=["POST"])
def send_email():
    return manager_controller.send_email(request)



# Manager - System Log
@manager_blueprint.route('/systemlog', methods=["GET"])
def get_system_log():
    return manager_controller.get_system_log(request)
