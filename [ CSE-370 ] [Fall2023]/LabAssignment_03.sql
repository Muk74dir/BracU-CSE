CREATE DATABASE IF NOT EXISTS lab_assignment03;

USE lab_assignment03;

CREATE TABLE customer (
	customer_id varchar(10) not null,
	customer_name varchar(20) not null,
	customer_street varchar(30),
	customer_city varchar(30),
	primary key (customer_id)
);

CREATE TABLE branch(
	branch_name varchar(15),
	branch_city varchar(30),
	assets int,
	primary key (branch_name),
	check (assets >= 0)
);

CREATE TABLE account (
	branch_name varchar(15),
	account_number varchar(10) not null,
	balance int,
	primary key (account_number),
	check (balance >= 0)
);

CREATE TABLE loan (
	loan_number varchar(10) not null,
	branch_name varchar(15),
	amount int,
	primary key (loan_number)
);

CREATE TABLE depositor (
	customer_id varchar(10) not null,
	account_number varchar(10) not null,
	primary key (customer_id,account_number),
	foreign key (customer_id) references customer(customer_id),
	foreign key (account_number) references account(account_number)
);

CREATE TABLE borrower (
	customer_id varchar(10) not null,
	loan_number varchar(10) not null,
	primary key (customer_id, loan_number),
	foreign key (customer_id) references customer(customer_id),
	foreign key (loan_number) references loan(loan_number)
);

INSERT INTO customer VALUES
('C-101','Jones', 'Main', 'Harrison'),
('C-201','Smith', 'North', 'Rye'),
('C-211','Hayes', 'Main', 'Harrison'),
('C-212','Curry', 'North', 'Rye'),
('C-215','Lindsay', 'Park', 'Pittsfield'),
('C-220','Turner', 'Putnam', 'Stamford'),
('C-222','Williams', 'Nassau', 'Princeton'),
('C-225','Adams', 'Spring', 'Pittsfield'),
('C-226','Johnson', 'Alma', 'Palo Alto'),
('C-233','Glenn', 'Sand Hill', 'Woodside'),
('C-234','Brooks', 'Senator', 'Brooklyn'),
('C-255','Green', 'Walnut', 'Stamford');


INSERT INTO branch VALUES
('Downtown', 'Brooklyn',9000000),
('Redwood', 'Palo Alto',2100000),
('Perryridge', 'Horseneck',1700000),
('Mianus', 'Horseneck',400000),
('Round Hill', 'Horseneck',8000000),
('Pownal', 'Bennington',300000),
('North Town', 'Rye',3700000),
('Brighton', 'Brooklyn',7100000);


INSERT INTO account VALUES
('Downtown','A-101',500),
('Mianus','A-215',700) ,
('Perryridge','A-102',400),
('Round Hill','A-305',350),
('Brighton','A-201',900),
('Redwood','A-222',700),
('Brighton','A-217',750);


INSERT INTO loan VALUES
('L-17', 'Downtown', 1000),
('L-23', 'Redwood', 2000),
('L-15', 'Perryridge', 1500),
('L-14', 'Downtown', 1500),
('L-93', 'Mianus', 500),
('L-11', 'Round Hill', 900),
('L-16', 'Perryridge', 1300);


INSERT INTO depositor VALUES
('C-226', 'A-101'),
('C-201', 'A-215'),
('C-211', 'A-102'),
('C-220', 'A-305'),
('C-226', 'A-201'),
('C-101', 'A-217'),
('C-215', 'A-222');


INSERT INTO borrower VALUES
('C-101', 'L-17'),
('C-201', 'L-23'),
('C-211', 'L-15'),
('C-226', 'L-14'),
('C-212', 'L-93'),
('C-201', 'L-11'),
('C-222', 'L-17'),
('C-225', 'L-16');



-- Question [ 01 ] 
SELECT c.customer_name, b.loan_number
FROM customer c
JOIN borrower b ON c.customer_id = b.customer_id
JOIN loan l ON b.loan_number = l.loan_number
WHERE l.branch_name = 'Downtown';

-- Question [ 02 ]
SELECT 
c1.customer_name AS Customer1,
c2.customer_name AS Customer2,
c1.customer_city AS City
FROM customer c1
JOIN customer c2 ON c1.customer_city = c2.customer_city
WHERE c1.customer_id < c2.customer_id;

-- Question [ 03 ]
SELECT a.branch_name AS Branch_name,
SUM(0.04 * a.balance) AS Total_Interest
FROM account a
GROUP BY a.branch_name;

-- Question [ 04 ]
SELECT a.account_number, b.branch_city, a.balance
FROM account a
JOIN branch b ON a.branch_name = b.branch_name
WHERE (b.branch_city, a.balance) IN (
    SELECT b.branch_city, MAX(a.balance) AS Highest_Balance
    FROM account a
    JOIN branch b ON a.branch_name = b.branch_name
    GROUP BY b.branch_city
);


-- Question [ 05 ]
SELECT l.loan_number, l.amount, c.customer_name
FROM loan l
JOIN borrower b ON l.loan_number = b.loan_number
JOIN customer c ON b.customer_id = c.customer_id
ORDER BY l.amount ASC, l.loan_number DESC
LIMIT 5;

-- Question [ 06 ]
SELECT c.customer_name
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM depositor d
    WHERE d.customer_id = c.customer_id
)
AND EXISTS (
    SELECT 1
    FROM borrower b
    JOIN loan l ON b.loan_number = l.loan_number
    WHERE l.branch_name = 'Perryridge' AND b.customer_id = c.customer_id
);

-- Question [ 07 ]
SELECT c.customer_name, SUM(l.amount) AS total_loan
FROM customer c
JOIN borrower b ON c.customer_id = b.customer_id
JOIN loan l ON b.loan_number = l.loan_number
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(b.loan_number) >= 2;











