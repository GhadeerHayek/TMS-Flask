-- Ghadeer's edit , 24th May

-- insertion to this table occurs when a manager approves a trainee or an advisor
CREATE TABLE IF NOT EXISTS users
(
    userID         INT PRIMARY KEY AUTO_INCREMENT,
    password       VARCHAR(250) NOT NULL,
    email          VARCHAR(250),
    classification ENUM ('advisor', 'trainee', 'manager')
);


-- Trainee component
-- insertion to this table occurs when a trainee registers through the signup form
CREATE TABLE IF NOT EXISTS trainees
(
    traineeID          INT PRIMARY KEY AUTO_INCREMENT,
    username           VARCHAR(250) NOT NULL,
    fullName           VARCHAR(250) NOT NULL,
    email              VARCHAR(250) NOT NULL UNIQUE,
    desired_field      VARCHAR(250) NOT NULL,
    area_of_training   ENUM (
        'Software Development',
        'Healthcare',
        'Machine Learning',
        'Network Security',
        'Data Warehousing',
        'Digital Marketing',
        'Renewable Energy',
        'Graphic Design',
        'Pastry and Baking'
    ),
    status             ENUM (
        'pending',
        'in_review',
        'active',
        'on_training',
        'rejected',
        'inactive'
    ) DEFAULT 'pending',
    balance            DOUBLE DEFAULT 0,
    training_materials VARCHAR(250) DEFAULT '',
    userID             INT DEFAULT NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Advisor Component
-- insertion to this table is done via the registration form
CREATE TABLE IF NOT EXISTS advisors
(
    advisorID    INT PRIMARY KEY AUTO_INCREMENT,
    username     VARCHAR(250) NOT NULL,
    fullName     VARCHAR(250) NOT NULL,
    email        VARCHAR(250) NOT NULL UNIQUE,
    discipline   ENUM (
        'Web Development',
        'Clinical Research',
        'Data Science',
        'Cybersecurity',
        'Database Administration',
        'Marketing',
        'Environmental Science',
        'Graphic Design',
        'Culinary Arts'
    ),
    status       ENUM (
        'pending',
        'active',
        'in_review',
        'training',
        'rejected',
        'inactive'
    ) DEFAULT 'pending',
    userID       INT DEFAULT NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Manager Component
-- the data for this table is actually built-in
CREATE TABLE IF NOT EXISTS managers
(
    managerID INT PRIMARY KEY AUTO_INCREMENT,
    username  VARCHAR(250) NOT NULL,
    fullName  VARCHAR(250) NOT NULL,
    email     VARCHAR(250) NOT NULL UNIQUE,
    userID    INT DEFAULT NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- All emails manipulation in the system
CREATE TABLE IF NOT EXISTS emails
(
    emailID          INT PRIMARY KEY AUTO_INCREMENT,
    sender           INT NOT NULL,
    recipient        INT NOT NULL,
    email_subject    VARCHAR(250) NOT NULL,
    email_attachment VARCHAR(250) NOT NULL,
    email_body       TEXT NOT NULL,
    FOREIGN KEY (sender) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (recipient) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Balance Sheet is where the system keeps its billing records
CREATE TABLE IF NOT EXISTS balance_sheet
(
    transactionID    INT PRIMARY KEY AUTO_INCREMENT,
    userID           INT NOT NULL,
    type             ENUM ('Credit', 'Debit') NOT NULL,
    amount           DOUBLE NOT NULL,
    transaction_time DATETIME NOT NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);



CREATE TABLE IF NOT EXISTS meetings
(
    meetingID       INT PRIMARY KEY AUTO_INCREMENT,
    registration_id INT,
    meeting_details VARCHAR(250) NOT NULL,
    meeting_link    VARCHAR(50) DEFAULT NULL,
    start_datetime  DATETIME NOT NULL,
    end_datetime    DATETIME NOT NULL,
    status          ENUM ('approved', 'cancelled', 'pending') NOT NULL,
    CONSTRAINT fk_meetings_registration
        FOREIGN KEY (registration_id)
        REFERENCES training_registration (ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- Training Program Component, it is equal to our summer training programs
CREATE TABLE IF NOT EXISTS training_programs
(
    programID        INT PRIMARY KEY AUTO_INCREMENT,
    name             VARCHAR(250) NOT NULL,
    description      VARCHAR(250) NOT NULL,
    area_of_training ENUM (
        'Software Development',
        'Healthcare',
        'Machine Learning',
        'Network Security',
        'Data Warehousing',
        'Digital Marketing',
        'Renewable Energy',
        'Graphic Design',
        'Pastry and Baking'
    ),
    fees             DOUBLE NOT NULL,
    start_date       datetime NOT NULL,
    end_date         datetime NOT NULL
);



-- Training Registration process
CREATE TABLE IF NOT EXISTS training_registration
(
    ID                  INT PRIMARY KEY AUTO_INCREMENT,
    training_program_id INT NOT NULL,
    traineeID           INT NOT NULL,
    advisorID           INT DEFAULT NULL,
    status              ENUM (
        'approved',
        'rejected',
        'pending',
        'finished'
    ) NOT NULL,
    registration_time   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (training_program_id) REFERENCES training_programs (programID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (advisorID) REFERENCES advisors (advisorID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (traineeID) REFERENCES trainees (traineeID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Attendance Records related to the training registration process

CREATE TABLE IF NOT EXISTS attendance_records
(
    ID                 INT PRIMARY KEY AUTO_INCREMENT,
    training_programID INT NOT NULL,
    date               DATE NOT NULL,
    check_in           TIME NOT NULL,
    check_out          TIME NOT NULL,
    FOREIGN KEY (training_programID) REFERENCES training_registration (ID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Notifications management
CREATE TABLE IF NOT EXISTS notifications
(
    id                INT PRIMARY KEY AUTO_INCREMENT,
    sender_id         INT,
    recipient_id      INT,
    name              VARCHAR(250) NOT NULL,
    details           VARCHAR(250) DEFAULT '',
    notification_time DATETIME,
    status            VARCHAR(20) CHECK (status IN ('read', 'unread')),
    FOREIGN KEY (recipient_id) REFERENCES trainees (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

