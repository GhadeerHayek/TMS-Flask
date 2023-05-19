from flask import render_template

"""
    function that retrieves the trainee-index form view, it also prepares the data to display in the form view
"""
def index(token):
    # after verifying the token, we'll extract the trainee id or the trainee object
    trainee_id = ""
    # we'll execute a select query that fetches all the trainn record from the database
    #
    trainee = {
        "id":"12",
        "username":"mars2001",
        "email":"ghadeerhayek2001@gmail.com",
        "desired_field":"Web Development",
        "area":"Technology",
        "current_training":0
    }
    # we'll send this data along with the template
    return render_template('trainee/index.html', trainee = trainee)
