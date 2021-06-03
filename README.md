# 4B3b-Assignments-Project

Hello Everyone,

This repository is for assignment and project submissions. It has different branches (one assigned to every member).

Kindly fork this repository and ONLY upload files in YOUR assigned branch.

Submissions are made by initiating a pull request from YOUR branch in the forked version of the repository, targeting YOUR branch in the parent repository.

Cheers!


SDLC : https://www.tutorialspoint.com/sdlc/sdlc_overview.htm
KEYWORDS : https://www.programiz.com/python-programming/keywords-identifier

CONDITIONALS PYTHON : https://realpython.com/python-conditional-statements/
FUNCTIONS - https://realpython.com/defining-your-own-python-function/
mysql - https://www.w3schools.com/sql/sql_select.asp



########### SQL COMMANDS #####################

CREATE TABLE student (id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY, stu_name VARCHAR(100), age INT(3) NOT NULL, address VARCHAR(100), email VARCHAR(50) )
SELECT * FROM `student`
INSERT INTO student (stu_name, age, address, email) VALUES("Kunle", 34, "10, salami lagos", "kunle@gmail.com")
SELECT * FROM `student`
CREATE TABLE notes (id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT(4), title VARCHAR(40), body VARCHAR(500), FOREIGN KEY (user_id) REFERENCES users(id) )
CREATE TABLE notes (id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT(4), title VARCHAR(40), body VARCHAR(500), FOREIGN KEY (user_id) REFERENCES users(id) )
CREATE TABLE notes (id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT(4), title VARCHAR(40), body VARCHAR(500), FOREIGN KEY user_id REFERENCES users(id) )
SELECT * FROM `notes`
SELECT * FROM `users`
CREATE TABLE notes2 (id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT(4), title VARCHAR(40), body VARCHAR(500), FOREIGN KEY user_id REFERENCES users(id) )
CREATE TABLE notes2 (id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT(4), title VARCHAR(40), body VARCHAR(500), FOREIGN KEY (user_id) REFERENCES users(id) )
SELECT * FROM `users`
INSERT INTO notes2 (user_id, title, body) VALUES(1, "Oh Happy day", "Such a happy day today, i ama having so much fun")
Expand Edit Query failed
INSERT INTO notes2 (user_id, title, body) VALUES(10, "Oh Happy day", "Such a happy day today, i ama having so much fun")

SELECT name, title FROM notes2 
JOIN users
ON users.id = notes2.user_id