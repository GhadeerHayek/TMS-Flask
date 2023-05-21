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
