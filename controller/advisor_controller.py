from flask import render_template

advisor = {
    "id": "20",
    "username": "venus2023",
    "email": "someemail@gmail.com",
    "discipline": "Python Programming",
    "department": "comp sci",
    "interest": "AI",
    "phone": "123456",
    "max_number_of_trainees": 5,
    "img":"../../static/assets/img/profile-img.jpg"
}

# the status should be calculated based on enrollment
programs = [
    ["1", "private", "program1", "program1 description", "area1", "money", "sometime", "somedate"],
    ["2",  "uni collaborator", "program2", "program2 description", "area1", "money", "sometime", "somedate"],
    ["3", "private", "program3", "program3 description", "area1", "money", "sometime", "somedate"],
]

trainees = [
    ["1",  "new", "name1", "email1", "df1", "area1"],
    ["2", "on training", "name2", "email2", "df1", "area1"],
    ["3",  "new", "name3", "email3", "df1", "area1"]
]

meetings = [
    ["meetingid1", "meeting for followup", "Approved", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"],
    ["meetingid2", "meeting for followup", "Pending", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"],
    ["meetingid3", "meeting for followup", "Approved", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"]
]



def index(token):
    # from token, fetch advisor id, then fetch the record from the database
    
    return render_template('advisor/index.html', advisor = advisor)


def get_my_trainees(request):
    return render_template('advisor/my_trainees.html', trainees = trainees, advisor = advisor)


def get_trainees_contact(request):
    return render_template('advisor/contact_trainees.html', trainees = trainees, advisor = advisor)


def get_program_materials(request):
    return render_template('advisor/my_programs.html', programs = programs, advisor = advisor)


def get_meeting_requests(request):
    return render_template('advisor/meetings.html', meetings = meetings, advisor = advisor)


def get_meeting_form(request):
    return render_template('advisor/create_meeting.html', advisor = advisor)


def get_attendance_form(request):
    return render_template('advisor/attendance_form.html', advisor = advisor, trainee = trainees[0])


def get_reschedule_form(request):
    return render_template('advisor/reschedule.html', advisor = advisor, trainee = trainees[0])


def get_training_material(request):
    return render_template('advisor/training_program.html', advisor = advisor, programs=programs)