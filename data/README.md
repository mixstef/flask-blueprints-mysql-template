# Database init
To use this example flask template, a mysql database and specific inital content must be present.

## Create test table

	> CREATE TABLE employee (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) CHARACTER SET utf8 COLLATE utf8_bin,age INT,salary DECIMAL(10,2));
	Query OK, 0 rows affected (1.11 sec)

	> SHOW TABLES;
	+------------------+
	| Tables_in_testdb |
	+------------------+
	| employee         |
	+------------------+
	1 row in set (0.00 sec)

	> DESCRIBE employee;
	+--------+---------------+------+-----+---------+----------------+
	| Field  | Type          | Null | Key | Default | Extra          |
	+--------+---------------+------+-----+---------+----------------+
	| id     | int(11)       | NO   | PRI | NULL    | auto_increment |
	| name   | varchar(100)  | YES  |     | NULL    |                |
	| age    | int(11)       | YES  |     | NULL    |                |
	| salary | decimal(10,2) | YES  |     | NULL    |                |
	+--------+---------------+------+-----+---------+----------------+
	4 rows in set (0.00 sec)

## Insert sample employees

	> INSERT INTO employee (name,age,salary) VALUES('Tom Jones',23,1500.00),('Jane Doe',31,2500.00),('Pepe le Moko',30,3200.00);
	Query OK, 3 rows affected (1.01 sec)
	Records: 3  Duplicates: 0  Warnings: 0

	> SELECT * FROM employee;
	+----+--------------+------+---------+
	| id | name         | age  | salary  |
	+----+--------------+------+---------+
	|  1 | Tom Jones    |   23 | 1500.00 |
	|  2 | Jane Doe     |   31 | 2500.00 |
	|  3 | Pepe le Moko |   30 | 3200.00 |
	+----+--------------+------+---------+
	3 rows in set (0.00 sec)


