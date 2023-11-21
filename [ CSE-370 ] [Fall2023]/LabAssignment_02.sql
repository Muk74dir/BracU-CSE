CREATE DATABASE labassignment2;
USE labassignment2;
CREATE TABLE employees (
    employee_id CHAR(10),
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(60),
    phone_number CHAR(14),
    hire_date DATE,
    job_id CHAR(10),
    salary INT,
    commission_pct DECIMAL(5,3),
    manager_id CHAR(10),
    department_id CHAR(10)
);

INSERT INTO employees VALUES
  ('EMP001', 'John', 'Doe', 'john.doe@example.com', '555-555-1001', '2023-01-15', 'JOB001', 60000, 0.05, 'MNG001', 'DPT001'),
  ('EMP002', 'Jane', 'Smith', 'jane.smith@example.com', '555-555-2002', '2023-02-20', 'JOB002', 75000, 0.03, 'MNG001', 'DPT002'),
  ('EMP003', 'Michael', 'Johnson', 'michael.j@example.com', '555-555-3003', '2023-03-25', 'JOB003', 55000, 0.02, 'MNG002', 'DPT001'),
  ('EMP004', 'Emily', 'Brown', 'emily.b@example.com', '555-555-4004', '2023-04-10', 'JOB002', 70000, 0.03, 'MNG002', 'DPT003'),
  ('EMP005', 'David', 'Wilson', 'david.w@example.com', '555-555-5005', '2023-05-05', 'JOB001', 62000, 0.04, 'MNG003', 'DPT002'),
  ('EMP006', 'Sara', 'Garcia', 'sara.g@example.com', '555-555-6006', '2023-06-12', 'JOB004', 58000, 0.01, 'MNG003', 'DPT004'),
  ('EMP007', 'Robert', 'Martinez', 'robert.m@example.com', '555-555-7007', '2023-07-18', 'JOB005', 68000, 0.02, 'MNG001', 'DPT005'),
  ('EMP008', 'Amanda', 'Miller', 'amanda.m@example.com', '555-555-8008', '2023-08-21', 'JOB003', 72000, 0.03, 'MNG001', 'DPT006'),
  ('EMP009', 'William', 'Taylor', 'william.t@example.com', '555-555-9009', '2023-09-30', 'JOB002', 64000, 0.03, 'MNG002', 'DPT004'),
  ('EMP010', 'Olivia', 'Anderson', 'olivia.a@example.com', '555-555-1010', '2023-10-03', 'JOB001', 67000, 0.04, 'MNG002', 'DPT005'),
  ('EMP011', 'Mark', 'Johnson', 'mark.j@example.com', '555-555-1101', '2023-11-10', 'JOB005', 65000, 0.025, 'MNG004', 'DPT005'),
  ('EMP012', 'Laura', 'Smith', 'laura.s@example.com', '555-555-1202', '2023-12-05', 'JOB006', 62000, 0.030, 'MNG004', 'DPT005'),
  ('EMP013', 'Daniel', 'Brown', 'daniel.b@example.com', '555-555-1303', '2023-11-15', 'JOB005', 64000, 0.020, 'MNG005', 'DPT005'),
  ('EMP014', 'Sophia', 'Lee', 'sophia.l@example.com', '555-555-1404', '2023-12-20', 'JOB006', 67000, 0.015, 'MNG005', 'DPT005'),
  ('EMP015', 'Eric', 'Miller', 'eric.m@example.com', '555-555-1505', '2023-11-25', 'JOB005', 66000, 0.025, 'MNG006', 'DPT005'),
  ('EMP016', 'Lily', 'Garcia', 'lily.g@example.com', '555-555-1606', '2023-12-30', 'JOB006', 70000, 0.035, 'MNG006', 'DPT005'),
  ('EMP017', 'Henry', 'Davis', 'henry.d@example.com', '555-555-1707', '2023-11-02', 'JOB005', 67000, 0.020, 'MNG007', 'DPT005'),
  ('EMP018', 'Grace', 'Martinez', 'grace.m@example.com', '555-555-1808', '2023-12-07', 'JOB006', 63000, 0.010, 'MNG007', 'DPT005'),
  ('EMP019', 'Andrew', 'Anderson', 'andrew.a@example.com', '555-555-1909', '2023-11-12', 'JOB005', 64000, 0.015, 'MNG008', 'DPT005'),
  ('EMP020', 'Emma', 'Taylor', 'emma.t@example.com', '555-555-2020', '2023-12-15', 'JOB006', 68000, 0.025, 'MNG008', 'DPT005'),
  ('EMP021', 'Nathan', 'White', 'nathan.w@example.com', '555-555-2121', '2023-11-05', 'JOB007', 70000, 0.040, 'MNG009', 'DPT007'),
  ('EMP022', 'Olivia', 'Harris', 'olivia.h@example.com', '555-555-2222', '2023-12-10', 'JOB007', 72000, 0.035, 'MNG009', 'DPT007'),
  ('EMP023', 'Matthew', 'Moore', 'matthew.m@example.com', '555-555-2323', '2023-11-08', 'JOB007', 71000, 0.030, 'MNG010', 'DPT007'),
  ('EMP024', 'Ava', 'Clark', 'ava.c@example.com', '555-555-2424', '2023-12-12', 'JOB007', 73000, 0.025, 'MNG010', 'DPT007'),
  ('EMP025', 'Sarah', 'Johnson', 'sarah.j@example.com', '555-555-2525', '2023-12-31', 'JOB007', 72000, 0.001, 'MNG010', 'DPT007');


-- Q1

SELECT first_name, last_name, email, phone_number, hire_date, department_id
FROM employees
ORDER BY hire_date ASC;

-- Q2

SELECT e1.first_name, e1.last_name, e1.employee_id, e1.phone_number, e1.salary, e1.department_id
FROM employees e1
JOIN(SELECT department_id, MIN(salary) AS min_salary 
	FROM employees
	GROUP BY department_id) e2 
ON e1.department_id = e2.department_id 
AND e1.salary = e2.min_salary;

-- Q3

SELECT e1.first_name, e1.last_name, e1.employee_id, e1.commission_pct, e1.department_id
FROM employees e1
WHERE e1.department_id = 'DPT007' AND e1.commission_pct < ALL (
    SELECT e2.commission_pct
    FROM employees e2
    WHERE e2.department_id = 'DPT005'
);

-- Q4

SELECT department_id, COUNT(*) AS total_employees
FROM employees
GROUP BY department_id
HAVING MAX(salary) > 30000 AND COUNT(*) > 1;


-- Q5

SELECT e.department_id, e.job_id, e.commission_pct
FROM employees e
WHERE e.commission_pct < ANY (
    SELECT commission_pct
    FROM employees e2
    WHERE e2.department_id = e.department_id AND e2.job_id <> e.job_id
);

-- Q6

SELECT DISTINCT manager_id
FROM employees
WHERE manager_id IS NOT NULL
AND manager_id NOT IN (
    SELECT DISTINCT manager_id
    FROM employees
    WHERE salary < 3500
);


-- Q7

SELECT e1.first_name, e1.last_name, e1.employee_id, e1.email, e1.salary, e1.department_id, e1.commission_pct
FROM employees e1
WHERE (e1.manager_id, e1.commission_pct) IN (
    SELECT e2.manager_id, MIN(e2.commission_pct)
    FROM employees e2
    WHERE e2.manager_id IS NOT NULL
    GROUP BY e2.manager_id
);



