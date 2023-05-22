from flask import render_template

programs = [
    ["1", "program1", "program1 description", "area1", "money", "somedate", "somedate"],
    ["2", "program2", "program2 description", "area1", "money", "somedate", "somedate"],
    ["3", "program3", "program3 description", "area1", "money", "somedate", "somedate"],
]

trainee = {
    "id": "12",
    "username": "mars2001",
    "email": "ghadeerhayek2001@gmail.com",
    "desired_field": "Web Development",
    "area": "Technology",
    "current_training": 0
}

"""
    function that retrieves the trainee-index form view, it also prepares the data to display in the form view
"""


def index(token):
    # after verifying the token, we'll extract the trainee id or the trainee object
    trainee_id = ""
    # we'll execute a select query that fetches all the trainn record from the database
    #

    # we'll send this data along with the template
    return render_template('trainee/index.html', trainee=trainee)


"""
    prepares data for the training programs application view, renders the view with this data
"""


def get_programs_for_trainee(request):
    # select all the training programs whose area matches this trainee area of interest and display their information in a tabular format
    return render_template('trainee/all_programs.html', trainee=trainee, programs=programs)


"""
    action function that handles the application request and flashes messages for user in case of success or failure 
    not yet implemented 
"""


def handle_program_application(request):
    pass


"""
    This is the form-view function that renders the current training of a trainee details, which include the program data itself,
     the registration details of the program itself, link to the attendance form, link to schedule meetings
     So i'd guess it's the view that contains three components in one 
"""


def get_training_program(request):
    # first of all, check the current status of the trainee and check if the current status of the trainee is: on_training
    # then, perform a select query to get the program_registiration
    # this data will include: training program id, advisor id, attendance form id, status of the registiration itself
    # later, 1- we'll get the training program data and display it
    # 2- provide a link to the attendance form, were all the data is displayed and the option to add new record is available

    registered_program = [
        "registration id", "program id", "trainee id", "attendance form id", "advisor id", "status "

    ]
    return render_template('trainee/my_training.html', trainee=trainee, registered_program=registered_program)

def trainee_training_form(request):
    return render_template('trainee/attendance-form.html');