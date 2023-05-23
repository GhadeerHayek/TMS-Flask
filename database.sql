CREATE DATABASE training_management;

CREATE TABLE users(
	userID int NOT NULL,
	username varchar(250) NOT NULL,
	fullName varchar(250) NOT NULL,
	email varchar(250) CHECK(managerEmail LIKE '%_@_%_.__%') NOT NULL,
    password varchar(250) NOT NULL,
    classification ENUM('advisor', 'trainee', 'manager')
	status ENUM('authorized', 'pending'),
	PRIMARY KEY(userId)
);


CREATE TABLE manager(
	managerID int NOT NULL,
    FOREIGN KEY(managerID) REFERENCES user(userId)
);


CREATE TABLE trainees(
	traineeID int NOT NULL,
	training_materials varchar(250),
	desired_field varchar(250),
	area_of_training varchar(250) NOT NULL,
	balance varchar(250),
    FOREIGN KEY(traineeID) REFERENCES user(userId)
    FOREIGN KEY(desired_field) REFERENCES id(desired_field)
);


CREATE TABLE advisors(
	advisorID int NOT NULL,
	descipline varchar(250),
	advisorType varchar(50) NOT NULL,
    FOREIGN KEY(advisorID) REFERENCES user(userId)
);


CREATE TABLE desired_fields(
	ID int NOT NULL,
	name varchar(250) NOT NULL,
	area_of_interest varchar(250) NOT NULL,
    discipline varchar(250) NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE emails(
	emailID varchar(250) NOT NULL,
	from varchar(250) NOT NULL,
	to varchar(250) NOT NULL,
	email_subject varchar(250) NOT NULL,
	email_attachment varchar(250) NOT NULL,
	email_body text NOT NULL,
	PRIMARY KEY(emailID),
	FOREIGN KEY(from) REFERENCES user(userId),
	FOREIGN KEY(to) REFERENCES user(userId)

);

CREATE TABLE balance_sheet (
    transactionID int PRIMARY KEY,
	userID int not NULL,
    type NOT NULL ENUM('Credit', 'Debit'),
    amount double NOT NULL,
	transaction_time datetime NOT NULL,
	FOREIGN KEY(userID) REFERENCES user(userId)
    FOREIGN KEY(courseID) REFERENCES training_course(courseID)
);

CREATE TABLE meeting(
    meetingID int NOT NULL,
	traineeID int NOT NULL,
	advisorID int NOT NULL,
	meeting_details varchar(250) NOT NULL,
	meeting_link varchar(50),
	date datetime NOT NULL,
	start_time datetime NOT NULL,
	end_time datetime NOT NULL,
	status NOT NULL ENUM('approved', 'cancelled'),
	PRIMARY KEY(traineeID, courseName, feedbackID),
    FOREIGN KEY(traineeID) REFERENCES trainee(traineeID),
    FOREIGN KEY(advisorID) REFERENCES advisor(advisorID)
);


CREATE TABLE training_program(
	programID int NOT NULL,
	name varchar(250) NOT NULL,
	description varchar(250) NOT NULL,
    area_of_training varchar(5000) NOT NULL,
	-- fees double 
	start_date datetime NOT NULL,
	end_date datetime NOT NULL,
	PRIMARY KEY(programID)
);


CREATE TABLE training_registeration(
	ID int NOT NULL,
	training_program_id int NOT NULL,
	traineeID int NOT NULL,
    advisorID int NOT NULL,
	training_request_status NOT NULL enum('approved', 'rejected', 'pending'),
	PRIMARY KEY(ID),
    FOREIGN KEY(training_program_id) REFERENCES training_program(programID),
    FOREIGN KEY(advisorID) REFERENCES advisors(advisorID),
    FOREIGN KEY(traineeID) REFERENCES trainee(traineeID)
);


CREATE TABLE attendance_records(
	ID int NOT NULL,
    training_programID int NOT NULL,
	date datetime NOT NULL,
	check_in datetime NOT NULL,
	check_out datetime NOT NULL,
	PRIMARY KEY(ID),
    FOREIGN KEY(traineeID) REFERENCES trainee(traineeID),
    FOREIGN KEY(training_programID) REFERENCES training_registeration(ID)
);