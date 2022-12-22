use userdb;
CREATE TABLE kleinkinderen (
 kleinkind_id int(6) NOT NULL ,
 naam varchar(30) DEFAULT NULL,
 voornaam varchar(30) DEFAULT NULL,
 geboortedatum date DEFAULT NULL,
  Primary Key(kleinkind_id)
  )