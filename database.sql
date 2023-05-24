CREATE
DATABASE training_management;

CREATE TABLE users
(
    userID   int          NOT NULL,
    username varchar(250) NOT NULL,
    fullName varchar(250) NOT NULL,
    email    varchar(250) CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
) NOT NULL,
    password varchar(250) NOT NULL,
    classification ENUM('advisor', 'trainee', 'manager'),
	status ENUM('authorized', 'pending'),
	PRIMARY KEY(userID)
);



CREATE TABLE managers
(
    managerID int NOT NULL,
    FOREIGN KEY (managerID) REFERENCES users (userID)
);



CREATE TABLE trainees
(
    login_id           int          NOT NULL,
    traineeID          int          NOT NULL,
    training_materials varchar(250),
    desired_field      int          not null,
    area_of_training   varchar(250) NOT NULL,
    balance            varchar(250),
    FOREIGN KEY (login_id) REFERENCES users (userID),
    FOREIGN KEY (desired_field) REFERENCES desired_fields (ID)
);



CREATE TABLE advisors
(
    advisorID  int NOT NULL,
    discipline varchar(250),
    FOREIGN KEY (advisorID) REFERENCES users (userID)
);



CREATE TABLE desired_fields
(
    ID               int          NOT NULL,
    name             varchar(250) NOT NULL,
    area_of_interest ENUM('Software Development',
        'Healthcare',
        'Machine Learning',
        'Network Security',
        'Data Warehousing',
        'Digital Marketing',
        'Renewable Energy',
        'Graphic Design',
        'Pastry and Baking'
        ) NOT NULL,
    discipline       ENUM('Web Development',
        'Clinical Research',
        'Data Science',
        'Cybersecurity',
        'Database Administration',
        'Marketing',
        'Environmental Science',
        'Graphic Design',
        'Culinary Arts'
        ) NOT NULL,
    PRIMARY KEY (id)
);



CREATE TABLE emails
(
    emailID          varchar(250) NOT NULL,
    sender           int          NOT NULL,
    recipient        int          NOT NULL,
    email_subject    varchar(250) NOT NULL,
    email_attachment varchar(250) NOT NULL,
    email_body       text         NOT NULL,
    PRIMARY KEY (emailID),
    FOREIGN KEY (sender) REFERENCES users (userID),
    FOREIGN KEY (recipient) REFERENCES users (userID)
);



CREATE TABLE balance_sheet
(
    transactionID    int PRIMARY KEY,
    userID           int      not NULL,
    type             ENUM('Credit', 'Debit') NOT NULL,
    amount           double   NOT NULL,
    transaction_time datetime NOT NULL
);



CREATE TABLE meeting
(
    meetingID       int          NOT NULL,
    traineeID       int          NOT NULL,
    advisorID       int          NOT NULL,
    meeting_details varchar(250) NOT NULL,
    meeting_link    varchar(50),
    date            datetime     NOT NULL,
    start_time      datetime     NOT NULL,
    end_time        datetime     NOT NULL,
    status          ENUM('approved', 'cancelled') NOT NULL,
    PRIMARY KEY (meetingID),
    FOREIGN KEY (traineeID) REFERENCES trainees (login_id),
    FOREIGN KEY (advisorID) REFERENCES advisors (advisorID)
);



CREATE TABLE training_program
(
    programID        int           NOT NULL,
    name             varchar(250)  NOT NULL,
    description      varchar(250)  NOT NULL,
    area_of_training varchar(5000) NOT NULL,
    fees             double        not null,
    start_date       datetime      NOT NULL,
    end_date         datetime      NOT NULL,
    PRIMARY KEY (programID)
);



CREATE TABLE training_registration
(
    ID                      int NOT NULL,
    training_program_id     int NOT NULL,
    traineeID               int NOT NULL,
    advisorID               int NOT NULL,
    training_request_status enum('approved', 'rejected', 'pending') NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (training_program_id) REFERENCES training_program (programID),
    FOREIGN KEY (advisorID) REFERENCES advisors (advisorID),
    FOREIGN KEY (traineeID) REFERENCES trainees (login_id)
);



CREATE TABLE attendance_records
(
    ID                 int      NOT NULL,
    training_programID int      NOT NULL,
    date               datetime NOT NULL,
    check_in           datetime NOT NULL,
    check_out          datetime NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (training_programID) REFERENCES training_registration (ID)
);



CREATE TABLE notifications
(
    id                INT PRIMARY KEY AUTO_INCREMENT,
    sender_id         INT,
    recipient_id      INT,
    name              VARCHAR(250) NOT NULL,
    details           VARCHAR(250) DEFAULT '',
    notification_time DATETIME,
    status            VARCHAR(20) CHECK (status IN ('read', 'unread')),
    FOREIGN KEY (sender_id) REFERENCES trainees (login_id),
    FOREIGN KEY (recipient_id) REFERENCES trainees (login_id)
);


/*
 Ghadeer Edit:
 i've edited this one since it shows an sql syntax error
 i've also added a constraint on the email that it has to be unique
 --- CREATE TABLE users ( userID INT NOT NULL, username VARCHAR(250) NOT NULL, fullName VARCHAR(250) NOT NULL, email VARCHAR(250) NOT NULL UNIQUE CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'), password VARCHAR(250) NOT NULL, classification ENUM('advisor', 'trainee', 'manager'), status ENUM('authorized', 'pending'), PRIMARY KEY (userID) );
 --- CREATE TABLE managers(
	managerID int NOT NULL PRIMARY KEY,
    userID int,
    FOREIGN KEY(userID) REFERENCES users(userID)

 --- CREATE TABLE trainees(
	traineeID int NOT NULL PRIMARY KEY,
    userID int,
	training_materials varchar(250),
	desired_field int not null,
	area_of_training ENUM('Software Development',
        'Healthcare',
        'Machine Learning',
        'Network Security',
        'Data Warehousing',
        'Digital Marketing',
        'Renewable Energy',
        'Graphic Design',
        'Pastry and Baking'
        ) NOT NULL,
	balance varchar(250),
	FOREIGN KEY(userID) REFERENCES users(userID)
);
);

 --- CREATE TABLE advisors(
	advisorID int NOT NULL PRIMARY KEY,
    userID int,
	discipline ENUM('Web Development',
							'Clinical Research',
							'Data Science',
							'Cybersecurity',
							'Database Administration',
							'Marketing',
							'Environmental Science',
							'Graphic Design',
							'Culinary Arts'
							) ,
    FOREIGN KEY(userID) REFERENCES users(userID)
);
);

 ---CREATE TABLE balance_sheet
(
    transactionID    int PRIMARY KEY,
    userID           int      not NULL,
    type             ENUM('Credit', 'Debit') NOT NULL,
    amount           double   NOT NULL,
    transaction_time datetime NOT NULL,
    FOREIGN KEY (userID) REFERENCES users(userID)
);

 ---CREATE TABLE meeting
(
    meetingID       int          NOT NULL,
    traineeID       int          NOT NULL,
    advisorID       int          NOT NULL,
    meeting_details varchar(250) NOT NULL,
    meeting_link    varchar(50),
    date            datetime     NOT NULL,
    start_time      datetime     NOT NULL,
    end_time        datetime     NOT NULL,
    status          ENUM('approved', 'cancelled') NOT NULL,
    PRIMARY KEY (meetingID),
    FOREIGN KEY (traineeID) REFERENCES trainees (traineeID),
    FOREIGN KEY (advisorID) REFERENCES advisors (advisorID)
);

 -- CREATE TABLE training_programs
(
    programID        int           NOT NULL,
    name             varchar(250)  NOT NULL,
    description      varchar(250)  NOT NULL,
    area_of_training varchar(5000) NOT NULL,
    fees             double        not null,
    start_date       datetime      NOT NULL,
    end_date         datetime      NOT NULL,
    PRIMARY KEY (programID)
);

 --- CREATE TABLE training_registration
(
    ID                      int NOT NULL,
    training_program_id     int NOT NULL,
    traineeID               int NOT NULL,
    advisorID               int NOT NULL,
    training_request_status enum('approved', 'rejected', 'pending') NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (training_program_id) REFERENCES training_programs (programID),
    FOREIGN KEY (advisorID) REFERENCES advisors (advisorID),
    FOREIGN KEY (traineeID) REFERENCES trainees (traineeID)
);

 --- CREATE TABLE attendance_records
(
    ID                 int      NOT NULL,
    training_programID int      NOT NULL,
    date               date NOT NULL,
    check_in           datetime NOT NULL,
    check_out          datetime NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (training_programID) REFERENCES training_registration (ID)
);

);
 --- CREATE TABLE notifications
(
    ID                INT PRIMARY KEY AUTO_INCREMENT,
    sender_id         INT,
    recipient_id      INT,
    name              VARCHAR(250) NOT NULL,
    details           VARCHAR(250) DEFAULT '',
    notification_time DATETIME,
    status            VARCHAR(20) CHECK (status IN ('read', 'unread')),
    FOREIGN KEY (sender_id) REFERENCES users (userID),
    FOREIGN KEY (recipient_id) REFERENCES users (userID)
);
*/