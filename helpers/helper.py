from app import db
from sqlalchemy import text
from datetime import datetime
from flask import jsonify


def resolve_conflict(new_meeting):
    registration_record = db.session.execute(text("""
    SELECT * from training_registration where ID = :registration_id
    """), {
        "registration_id": int(new_meeting["registration_id"])
    }).fetchone()
    if not registration_record:
        return False
    trainee_meetings = db.session.execute(text("""
SELECT `meetingID`,`start_datetime`,`end_datetime`,meetings.`status`
from (meetings JOIN training_registration on meetings.registration_id = training_registration.ID)
WHERE training_registration.status = 'approved' 
GROUP BY training_registration.traineeID 
HAVING training_registration.traineeID = :traineeID;
    """), {
        "traineeID": registration_record[2]
    }).fetchall()
    advisor_meetings = db.session.execute(text("""
SELECT `meetingID`,`start_datetime`,`end_datetime`,meetings.`status`
from (meetings JOIN training_registration on meetings.registration_id = training_registration.ID)
WHERE training_registration.status = 'approved' 
GROUP BY training_registration.advisorID 
HAVING training_registration.advisorID = :advisorID;
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
            # TODO: Handle conflicts (e.g., reschedule conflicting meetings or notify the parties)
            return True
        return False
