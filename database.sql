-- Ghadeer's edit , 24th May

-- insertion to this table occurs when a manager approves a trainee or an advisor
CREATE TABLE users
(
    userID         INT PRIMARY KEY AUTO_INCREMENT,
    password       VARCHAR(250) NOT NULL,
    -- TODO: test purpose only
    email          VARCHAR(250),
    classification ENUM ('advisor', 'trainee', 'manager')

--        username VARCHAR(250) NOT NULL,
--        fullName VARCHAR(250) NOT NULL,
--        email VARCHAR(250) NOT NULL UNIQUE CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),

--        status ENUM('authorized', 'pending'),
);

-- Trainee component
-- insertion to this table occurs when a trainee registers through the signup form
CREATE TABLE trainees
(
    -- trainee basic information
    traineeID          int PRIMARY KEY AUTO_INCREMENT,
    username           VARCHAR(250) NOT NULL,
    fullName           VARCHAR(250) NOT NULL,
    email              VARCHAR(250) NOT NULL UNIQUE CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    -- to make the database simpler, those two fields are pre-defined list
    desired_field      VARCHAR(250) NOT NULL,
    area_of_training   ENUM ('Software Development',
        'Healthcare',
        'Machine Learning',
        'Network Security',
        'Data Warehousing',
        'Digital Marketing',
        'Renewable Energy',
        'Graphic Design',
        'Pastry and Baking'
        ),
    -- trainee statuses
    status             ENUM (
        'pending',     -- waiting for admin approval
        'active',      -- approved by the admin and is on the system + has no training
        'on_training', -- the trainee has a registered a training program
        'rejected',    -- rejected by the admin
        'inactive'     -- the trainee has requested the account deactivation, after the approval from the manager, the status is inactive
        )                           default 'pending',
    balance            double       default 0,
    -- this is the path to the directory where the user files are stored
    training_materials varchar(250) default '',
    -- this id references the users table for authentication purpose only
    userID             int          default NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Advisor Component
-- insertion to this table is done via the registration form
CREATE TABLE advisors
(
    -- advisor basic info
    advisorID  int PRIMARY KEY AUTO_INCREMENT,
    username   VARCHAR(250) NOT NULL,
    fullName   VARCHAR(250) NOT NULL,
    email      VARCHAR(250) NOT NULL UNIQUE CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    -- to make the database simpler, the discipline is from a pre-defined list
    discipline ENUM ('Web Development',
        'Clinical Research',
        'Data Science',
        'Cybersecurity',
        'Database Administration',
        'Marketing',
        'Environmental Science',
        'Graphic Design',
        'Culinary Arts'
        ),
    -- advisor statuses
    status     ENUM (
        'pending',  -- waiting for admin approval
        'active',   -- approved by the admin and is on the system + is not training anyone
        'training', -- the advisor has a some trainees assigned to him via the registered training programs
        'rejected', -- rejected by the admin
        'inactive'  -- the advisor has requested the account deactivation, after the approval from the manager, the status is inactive
        )          default 'pending',
    -- advisor authentication
    userID     int default NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Manager Component
-- the data for this table is actually built-in
CREATE TABLE managers
(
    managerID int PRIMARY KEY AUTO_INCREMENT,
    username  VARCHAR(250) NOT NULL,
    fullName  VARCHAR(250) NOT NULL,
    email     VARCHAR(250) NOT NULL UNIQUE CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    -- manager authentication
    userID    int default NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- All emails manipulation in the system
CREATE TABLE emails
(
    emailID          int PRIMARY KEY AUTO_INCREMENT,
    sender           int          NOT NULL,
    recipient        int          NOT NULL,
    email_subject    varchar(250) NOT NULL,
    email_attachment varchar(250) NOT NULL,
    email_body       text         NOT NULL,
    FOREIGN KEY (sender) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (recipient) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Balance Sheet is where the system keeps its billing records
CREATE TABLE balance_sheet
(
    transactionID    int PRIMARY KEY AUTO_INCREMENT,
    userID           int                      not NULL,
    type             ENUM ('Credit', 'Debit') NOT NULL,
    amount           double                   NOT NULL,
    transaction_time datetime                 NOT NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE

);


CREATE TABLE meeting
(
    meetingID       int PRIMARY KEY AUTO_INCREMENT,
    traineeID       int          NOT NULL,
    advisorID       int          NOT NULL,
    meeting_details varchar(250) NOT NULL,
    meeting_link    varchar(50),
    date            datetime     NOT NULL,
    start_time      datetime     NOT NULL,
    end_time        datetime     NOT NULL,
    -- for meeting management purposes, there's a status field
    status          ENUM (
        'approved', -- approved by the advisor
        'cancelled' -- cancelled by the advisor
        -- what about rescheduled? this question until the meeting feature is implemented
        )                        NOT NULL,
    FOREIGN KEY (traineeID) REFERENCES trainees (traineeID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (advisorID) REFERENCES advisors (advisorID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Training Program Component, it is equal to our summer training programs
CREATE TABLE training_programs
(
    programID        int PRIMARY KEY AUTO_INCREMENT,
    name             varchar(250) NOT NULL,
    description      varchar(250) NOT NULL,
    area_of_training ENUM ('Software Development',
        'Healthcare',
        'Machine Learning',
        'Network Security',
        'Data Warehousing',
        'Digital Marketing',
        'Renewable Energy',
        'Graphic Design',
        'Pastry and Baking'
        ),
    fees             double       not null,
    start_date       date         NOT NULL,
    end_date         date         NOT NULL
);


-- Training Registration process
CREATE TABLE training_registration
(
    ID                      int PRIMARY KEY AUTO_INCREMENT,
    training_program_id     int NOT NULL,
    traineeID               int NOT NULL,
    advisorID               int NOT NULL,
    training_request_status enum (
        'approved', -- approved by the manager
        'rejected', -- rejected by the manager
        'pending'   -- waiting for approval by the manager
        )                       NOT NULL,
    FOREIGN KEY (training_program_id) REFERENCES training_programs (programID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (advisorID) REFERENCES advisors (advisorID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (traineeID) REFERENCES trainees (traineeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Attendance Records related to the training registration process

CREATE TABLE attendance_records
(
    ID                 int PRIMARY KEY AUTO_INCREMENT,
    training_programID int  NOT NULL,
    date               date NOT NULL,
    check_in           time NOT NULL,
    check_out          time NOT NULL,
    FOREIGN KEY (training_programID) REFERENCES training_registration (ID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Notifications management
CREATE TABLE notifications
(
    id                INT PRIMARY KEY AUTO_INCREMENT,
    sender_id         INT,
    recipient_id      INT,
    name              VARCHAR(250) NOT NULL,
    details           VARCHAR(250) DEFAULT '',
    notification_time DATETIME,
    status            VARCHAR(20) CHECK (status IN ('read', 'unread')),
    -- Why the reference is userID, i guess because the notifications are general and available to all components on the system
    -- i am unsure about this, i hope to make sure when i implement it
    FOREIGN KEY (sender_id) REFERENCES trainees (userID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (recipient_id) REFERENCES trainees (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Those are some insert statements that should demonstrate the signup process


insert into managers (managerID, username, fullName, email, userID)
VALUES (1, 'mars2001', 'ghadeerhayek', 'ghadeerhayek2001@gmail.com', 1);


insert into users
VALUES (1, 'ghadeer123', 'ghadeerhayek2001@gmail.com', 'manager');

update managers
set userID = 1
where managerID = 1;
-- trying to insert a trainee

-- this query is executed when we try to signup user
insert into trainees (traineeID, username, fullName, email, desired_field, area_of_training)
values (1, 'venus2020', 'traineeghadeer', 'ghadeerhayek2001@gmail.com', 'some desired field', 'Software Development');

-- if admin approves the trainee
insert into users
VALUES (2, 'ghadeer123', 'trainee123', 'ghadeerhayek2001@gmail.com');
update trainees
SET userID = 2
where traineeID = 1;


-- trying to insert an advisor

insert into advisors (advisorID, username, fullName, email, discipline)
VALUES (1, 'jupiter1010', 'advisorghadeer', 'ghadeerhayek2001@gmail.com', 'Web Development');

-- if admin approves the advisor
insert into users
VALUES (3, 'ghadeer123', 'advisor', 'ghadeerhayek2001@gmail.com');
update advisors
set userID = 3
where advisorID = 1;


--Ayah Edit 25/5
ALTER TABLE `managers` ADD `department` VARCHAR(250) NOT NULL AFTER `username`;
ALTER TABLE `managers` ADD `phone` int NOT NULL AFTER `username`;
