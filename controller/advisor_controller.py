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

programs = [
    ["1", "program1", "program1 description", "area1", "money", "somedate", "somedate"],
    ["2", "program2", "program2 description", "area1", "money", "somedate", "somedate"],
    ["3", "program3", "program3 description", "area1", "money", "somedate", "somedate"],
]

trainees = [
    ["1", "name1", "email1", "df1", "area1"],
    ["2", "name2", "email2", "df1", "area1"],
    ["3", "name3", "email3", "df1", "area1"]
]

meetings = [
    ["meetingid1", "meeting for followup", "Approved", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"],
    ["meetingid2", "meeting for followup", "Conflict", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"],
    ["meetingid3", "meeting for followup", "Approved", "https://linktoyou",
     "2001-09-09", "15:15", "14:14", "trainee id", "advisor id"]
]



def index(token):
    # from token, fetch advisor id, then fetch the record from the database
    
    return render_template('advisor/index.html', advisor = advisor)


def get_pending_trainees(request):
    return render_template('advisor/pending_trainees.html', trainees = trainees, advisor = advisor)


def get_active_trainees(request):
    return render_template('advisor/my_trainees.html', trainees = trainees, advisor = advisor)


def get_program_materials(request):
    return render_template('advisor/my_programs.html', programs = programs, advisor = advisor)


def get_meeting_requests(request):
    return render_template('advisor/meetings.html', meetings = meetings, advisor = advisor)


def get_reschedule_request(request):
    return render_template('advisor/reschedule.html', meeting = meetings[0], advisor = advisor)


def get_meeting_form(request):
    return render_template('advisor/create_meeting.html', advisor = advisor)


def get_attendance_form(request):
    return render_template('advisor/attendance_form.html', advisor = advisor, trainee = trainees[0])


