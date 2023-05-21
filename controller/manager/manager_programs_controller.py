from flask import request, render_template, jsonify
from sqlalchemy import text
from app import db

manager = {
    "id": "100",
    "username": "Jupiter2000",
    "email": "jupiter@gmail.com"
}
"""
    gets all available programs, returns the view that displays all the programs alongside with this data
"""


def get_all_programs(request):
    # execute query to select all the training programs
    # prepare the resultSet
    # return the view with the result
    # program has: id, name, description, area, fees, start date, end date
    programs = [
        ["1", "program1", "program1 description", "area1", "money", "somedate", "somedate"],
        ["2", "program2", "program2 description", "area1", "money", "somedate", "somedate"],
        ["3", "program3", "program3 description", "area1", "money", "somedate", "somedate"],
    ]
    return render_template("manager/training-program/all_programs.html", manager=manager, programs=programs)


"""
    gets the view the has the add program form 
"""


def get_add_program(request):
    # must prepare areas so that it could be a drop-down list
    areas = ['area1', 'area2', 'area3']
    return render_template('manager/training-program/add_program.html', manager=manager, areas=areas)


"""
    handles the action of the add program form 
"""


def handle_add_program(request):
    pass


"""
    gets the view that has the edit program form, where this form inputs are already filled in with the program data 
"""


def get_edit_program(request):
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
    pass


"""
    handles the action of the delete program form
"""


def handle_delete_program(request):
    pass
