USE company;


INSERT INTO EMPLOYEE (ssn, fname, lname, bdate, address, gender, salary, Dno) VALUES
('111111111', 'Ahmed', 'Hassan', '1980-05-12', 'Alexandria', 'M', 9000.00, NULL),
('222222222', 'Sara',  'Ali',    '1985-03-20', 'Cairo',      'F', 8000.00, NULL),
('333333333', 'Omar',  'Khaled', '1990-07-01', 'Giza',        'M', 5000.00, NULL),
('444444444', 'Mona',  'Fathy',  '1992-11-15', 'Alexandria', 'F', 4500.00, NULL);


INSERT INTO DEPARTMENT (Dnumber, Dname, mgr_ssn, mgr_start_date) VALUES
(1, 'Research',       '111111111', '2015-01-01'),
(2, 'Administration', '222222222', '2018-06-01'),
(3, 'Headquarters',   '333333333', '2020-09-15');


UPDATE EMPLOYEE SET Dno = 1 WHERE ssn IN ('111111111', '444444444');
UPDATE EMPLOYEE SET Dno = 2 WHERE ssn = '222222222';
UPDATE EMPLOYEE SET Dno = 3 WHERE ssn = '333333333';


INSERT INTO PROJECT (Pnumber, Pname, Plocation, Dno) VALUES
(10, 'ProductX',        'Alexandria', 1),
(20, 'ProductY',        'Cairo',      2),
(30, 'Computerization', 'Giza',       3);
