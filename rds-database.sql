-- Ghadeer's edit , 24th May

-- insertion to this table occurs when a manager approves a trainee or an advisor
CREATE TABLE IF NOT EXISTS  users
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
CREATE TABLE IF NOT EXISTS trainees
(
    -- trainee basic information
    traineeID int PRIMARY KEY AUTO_INCREMENT,
    username  VARCHAR(250) NOT NULL,
    fullName  VARCHAR(250) NOT NULL,
    email     VARCHAR(250) NOT NULL UNIQUE CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
) ,
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
        'pending',     -- waiting for admin approval on registration
        'in_review',   -- waiting for admin approval on account update
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
CREATE TABLE IF NOT EXISTS  advisors
(
    -- advisor basic info
    advisorID int PRIMARY KEY AUTO_INCREMENT,
    username  VARCHAR(250) NOT NULL,
    fullName  VARCHAR(250) NOT NULL,
    email     VARCHAR(250) NOT NULL UNIQUE CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
) ,
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
        'pending',   -- waiting for admin approval
        'active',    -- approved by the admin and is on the system + is not training anyone
        'in_review', -- waiting for admin approval on account update
        'training',  -- the advisor has a some trainees assigned to him via the registered training programs
        'rejected',  -- rejected by the admin
        'inactive'   -- the advisor has requested the account deactivation, after the approval from the manager, the status is inactive
        )          default 'pending',
    -- advisor authentication
    userID     int default NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Manager Component
-- the data for this table is actually built-in
CREATE TABLE IF NOT EXISTS managers
(
    managerID int PRIMARY KEY AUTO_INCREMENT,
    username  VARCHAR(250) NOT NULL,
    fullName  VARCHAR(250) NOT NULL,
    email     VARCHAR(250) NOT NULL UNIQUE CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
) ,
    -- manager authentication
    userID    int default NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- All emails manipulation in the system
CREATE TABLE IF NOT EXISTS  emails
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
CREATE TABLE IF NOT EXISTS  balance_sheet
(
    transactionID    int PRIMARY KEY AUTO_INCREMENT,
    userID           int      not NULL,
    type             ENUM ('Credit', 'Debit') NOT NULL,
    amount           double   NOT NULL,
    transaction_time datetime NOT NULL,
    FOREIGN KEY (userID) REFERENCES users (userID) ON DELETE CASCADE ON UPDATE CASCADE

);


CREATE TABLE IF NOT EXISTS meetings
(
    meetingID       int PRIMARY KEY AUTO_INCREMENT,
    registration_id int,
    meeting_details varchar(250) NOT NULL,
    meeting_link    varchar(50) default NULL,
    start_datetime  datetime     NOT NULL,
    end_datetime    datetime     NOT NULL,
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
CREATE TABLE IF NOT EXISTS training_registration
(
    ID                  int PRIMARY KEY AUTO_INCREMENT,
    training_program_id int      NOT NULL,
    traineeID           int      NOT NULL,
    advisorID           int               default NULL,
    status              enum ( 'approved', -- approved by the manager
        'rejected',                        -- rejected by the manager
        'pending',                         -- waiting for approval by the manager
        'finished'                         -- finished by the trainee
        ) NOT NULL,
    registration_time   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (training_program_id) REFERENCES training_programs (programID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (advisorID) REFERENCES advisors (advisorID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (traineeID) REFERENCES trainees (traineeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Attendance Records related to the training registration process

CREATE TABLE IF NOT EXISTS  attendance_records
(
    ID                 int PRIMARY KEY AUTO_INCREMENT,
    training_programID int  NOT NULL,
    date               date NOT NULL,
    check_in           time NOT NULL,
    check_out          time NOT NULL,
    FOREIGN KEY (training_programID) REFERENCES training_registration (ID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Notifications management
CREATE TABLE IF NOT EXISTS  notifications
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