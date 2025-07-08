

CREATE DATABASE Employee_DB;

USE Employee_DB;

CREATE TABLE Employee_Registration (
    Serial_No INT PRIMARY KEY AUTO_INCREMENT,
    Employee_Name VARCHAR(100) NOT NULL,
    Designation VARCHAR(100) NOT NULL,
    Department VARCHAR(100) NOT NULL
);

INSERT INTO Employee_Registration (Employee_Name, Designation, Department)
VALUES 
    ('Anushka Alla', 'Software Engineer', 'IT'),
    ('Kalyan', 'HR Manager', 'Human Resources'),
    ('Varsha', 'Accountant', 'Finance');

SELECT * FROM Employee_Registration;

UPDATE Employee_Registration
SET Designation = 'Senior Software Engineer'
WHERE Serial_No = 1;

DELETE FROM Employee_Registration
WHERE Serial_No = 2;

SELECT * FROM Employee_Registration;
