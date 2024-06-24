
SELECT * FROM greenleavesbank.user;

CREATE TABLE IF NOT EXISTS greenleavesbank.employee ( 
id INT AUTO_INCREMENT PRIMARY KEY,
firstname varchar(20),
lastname varchar(20),
dept varchar(10),
salary int(10)
);

SELECT * FROM greenleavesbank.employeedetails;
insert into greenleavesbank.employee values(100,'Thomas','jefferson','Sales',5000);
insert into greenleavesbank.employee values(200,'Jason','moana','Technology',5500);
insert into greenleavesbank.employee values(300,'Mayla','lee','Technology',7000);
insert into greenleavesbank.employee values(400,'Nisha','singh','Marketing',9500);
insert into greenleavesbank.employee values(500,'Randy','finn','Technology',6000);


CREATE TABLE IF NOT EXISTS greenleavesbank.runners ( 
id INT PRIMARY KEY,
name varchar(20)
);

insert into greenleavesbank.runners values(1,'John Doe');
insert into greenleavesbank.runners values(2,'Jane Doe');
insert into greenleavesbank.runners values(3,'Alice Jones');
insert into greenleavesbank.runners values(4,'Bobby Louis');
insert into greenleavesbank.runners values(5,'Lisa Romero');

CREATE TABLE IF NOT EXISTS greenleavesbank.races ( 
id INT PRIMARY KEY,
event varchar(20),
winner_id varchar(20)
);

insert into greenleavesbank.races values(1,'10 meter dash',2);
insert into greenleavesbank.races values(2,'500 meter dash',3);
insert into greenleavesbank.races values(3,'Cross-country',2);
insert into greenleavesbank.races values(4,'Triahlon',null);

select * from greenleavesbank.runners where id NOT IN (SELECT winner_id FROM greenleavesbank.races);


select * from greenleavesbank.runners where id NOT IN (SELECT winner_id FROM greenleavesbank.races WHERE winner_id IS NOT NULL);



CREATE TABLE IF NOT EXISTS greenleavesbank.employeedetails ( 
id INT PRIMARY KEY,
firstname varchar(20),
street varchar(100),
houseNumber int,
DateOfBirth date
);

insert into greenleavesbank.employeedetails values(100,'Thomas','Bakers Street','250','2019-05-21');
insert into greenleavesbank.employeedetails values(200,'Jason','Springs Street','928','1992-06-22');
insert into greenleavesbank.employeedetails values(600,'Yemennnn','High street','111','2008-03-22');
insert into greenleavesbank.employeedetails values(500,'Randy','High street','111','2008-03-24');

CREATE TABLE IF NOT EXISTS greenleavesbank.officelocation ( 
officename varchar(100),
street varchar(100)
);
insert into greenleavesbank.officelocation values('Building A','Bakers Street');
insert into greenleavesbank.officelocation values('Building B','High street');
insert into greenleavesbank.officelocation values('Building C','Springs Street');

CREATE TABLE IF NOT EXISTS greenleavesbank.bonus ( 
id int(100),
bonus int(10)
);
insert into greenleavesbank.bonus values(100,2000);
insert into greenleavesbank.bonus values(200,5500);
insert into greenleavesbank.bonus values(300,6000);
insert into greenleavesbank.bonus values(400,1000);
insert into greenleavesbank.bonus values(500,0);

select a.id,
a.firstname,
b.street,
b.DateOfBirth
from greenleavesbank.employee a
left outer join greenleavesbank.employeedetails b
on a.id = b.id;

select count(*) as NumberOfEmployees from greenleavesbank.employee;

select 
a.firstname,
b.street,
b.DateOfBirth,
c.officename,
'Yes' as LivesNearToOffice
from greenleavesbank.employee as a
left outer join greenleavesbank.employeedetails as b
on a.id = b.id
inner join greenleavesbank.officelocation as c
on b.street = c.street;

select distinct street , count(*) from greenleavesbank.employeedetails group by 1;


select id, CONCAT_WS(' ',firstname,lastname) as fullname
FROM greenleavesbank.employee;

select * from greenleavesbank.employee where dept = 'Technology'
order by id desc;

#QUESTION1

CREATE TABLE greenleavesbank.envelope(id int, user_id int);
CREATE TABLE greenleavesbank.docs(idnum int, pageseq int, doctext varchar(100));

INSERT INTO greenleavesbank.envelope VALUES
  (1,1),
  (2,2),
  (3,3);

INSERT INTO greenleavesbank.docs(idnum,pageseq) VALUES
  (1,5),
  (2,6),
  (null,0);

SET SQL_SAFE_UPDATES = 0;

UPDATE greenleavesbank.docs SET doctext = COALESCE(doctext, pageseq);
UPDATE greenleavesbank.docs SET doctext=pageseq;

select * from greenleavesbank.docs;

select * from greenleavesbank.docs
WHERE EXISTS (
  SELECT 1 FROM dbo.docs
  WHERE id=envelope.id
);

#Question2

select * from greenleavesbank.envelope,greenleavesbank.docs;
#it will be 1st table* 2nd table = 3x3 =9



