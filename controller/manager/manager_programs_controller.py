from flask import request, render_template, jsonify
from sqlalchemy import text
import helpers.manager_helper as mghelper
from app import db



"""
    gets all available programs, returns the view that displays all the programs alongside with this data
"""
def get_all_programs(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)

    # token is the manager id or the manager record
    query = text("SELECT * FROM training_programs")
    result_cursor = db.session.execute(query)
    rows = result_cursor.fetchall()
    programs = []
    for row in rows:
        programs.append(row._data)
    return render_template("manager/training-program/all_programs.html", manager=manager, programs=programs)


"""
    gets the view the has the add program form 
"""


def get_add_program(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    # must prepare areas so that it could be a drop-down list
    areas = ['area1', 'area2', 'area3']
    return render_template('manager/training-program/add_program.html', manager=manager, areas=areas)


"""
    handles the action of the add program form 
"""


def handle_add_program(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    pass


"""
    gets the view that has the edit program form, where this form inputs are already filled in with the program data 
"""


def get_edit_program(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    # must prepare areas so that it could be a drop-down list
    areas = ['area1', 'area2', 'area3']
    # also must fetch the program details from the database and fill it in the form
    program = ['1', 'program name', 'program description', 'area1', 200, '2001-09-09', '2001-09-10'
               ]
    return render_template('manager/training-program/update_program.html', manager=manager, areas=areas, program=program)


"""
    handles the action of the edit program form
"""


def handle_edit_program(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    pass


"""
    handles the action of the delete program form
"""


def handle_delete_program(request):
    token = request.cookies['token']
    manager = mghelper.verify_manager(token)
    pass
