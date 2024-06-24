Create database Sample2;
# create databse creates the database which is also called as schema '
# and can be seen in left hand side tab under schemas
SHOW DATABASES;
drop database Sample2;

# create a table with primary key 

CREATE TABLE IF NOT EXISTS Sample2.tblGender ( 
id INT NOT NULL PRIMARY KEY,
Gender varchar(20)
);

insert into Sample2.tblGender values(1,'Male');
insert into  Sample2.tblGender values(2,'Female');
insert into Sample2.tblGender values(3,'Unknown');


CREATE TABLE IF NOT EXISTS Sample2.tblPerson ( 
id INT NOT NULL PRIMARY KEY,
Name varchar(10),
Email varchar(20),
GenderID INT
);





