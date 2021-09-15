CREATE TABLE persons(id int PRIMARY KEY auto_increment)
first_name varchar(255) not null,
last_name varchar(255));

INSERT INTO persons(first_name, last_name)
values ('toto','tata'), ('titi','minet');