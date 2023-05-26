from app import db
from sqlalchemy import text
from datetime import datetime
from flask import jsonify

"""This is a private helper function, aims to check all meetings related to a trainee and an advisor The trainee and 
advisor can only request for meeting whenever there's a training between them. The function searches for conflicts by 
fetching all advisor meetings, all trainee meetings and check the conflict between each one and the other."""


def resolve_conflict(new_meeting):
    # get the registration record, which links between the advisor and trainee
    registration_record = db.session.execute(text("""
            SELECT * from `training_registration` where `ID` = :registration_id
    """), {
        "registration_id": int(new_meeting["registration_id"])
    }).fetchone()
    # just a validation I am used to do, I don't know why
    if not registration_record:
        return False
    # get all the trainee meetings
    trainee_meetings = db.session.execute(text("""
                SELECT `meetingID`,`start_datetime`,`end_datetime`,meetings.`status`
                from (`meetings` JOIN `training_registration` on meetings.`registration_id` = training_registration.`ID`)
                WHERE training_registration.`status` = 'approved' 
                GROUP BY training_registration.`traineeID` 
                HAVING training_registration.`traineeID` = :traineeID;
    """), {
        "traineeID": registration_record[2]
    }).fetchall()
    # get all the advisor meetings
    advisor_meetings = db.session.execute(text("""
            SELECT `meetingID`,`start_datetime`,`end_datetime`,meetings.`status`
            from (`meetings` JOIN `training_registration` on meetings.`registration_id` = training_registration.`ID`)
            WHERE training_registration.`status` = 'approved' 
            GROUP BY training_registration.`advisorID` 
            HAVING training_registration.`advisorID` = :advisorID;
    """), {
        "advisorID": registration_record[3]
    }).fetchall()
    if trainee_meetings and advisor_meetings:
        conflicts = []
        for meeting in advisor_meetings + trainee_meetings:
            if meeting[1] < datetime.strptime(new_meeting["end_datetime"], "%Y-%m-%dT%H:%M") and datetime.strptime(
                    new_meeting["start_datetime"], "%Y-%m-%dT%H:%M") < meeting[2]:
                conflicts.append(meeting)
        if len(conflicts) == 0:
            # TODO: Handle conflicts (e.g., reschedule conflicting meetings or notify the parties) -- or no need
            return True
        return False