use test;

DROP TABLE IF EXISTS users;
CREATE TABLE users(
	id INT(10) PRIMARY KEY AUTO_INCREMENT,
	fname VARCHAR(10),
	sname VARCHAR(15),
	birth_year SMALLINT(2) UNSIGNED,
	birth_date DATE,
	salary DECIMAL(6,2) UNSIGNED,
	create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	order_id INT(10)
);

-- ALTER TABLE users ADD order_id INT(10);

TRUNCATE TABLE users;

INSERT INTO users (fname,sname,birth_year,birth_date,salary, order_id) VALUES
	('Maria', 'Petrova', 1990, '1990-01-20', 9999.99, 1),
	('Pesho','Petrov', 2001, '1990-02-28', 9999.990, 1),
	('Ivan', 'Ivanov',1926, '1990-01-20',  0009999.99, 2);

CREATE TABLE orders(
	id INT(10) PRIMARY KEY AUTO_INCREMENT NOT NULL,
	order_name VARCHAR(5),
	value DECIMAL(6,2)
);

-- ONE TO MANY RELATION:
-- 	USERS => ORDERS

ALTER TABLE orders MODIFY order_name VARCHAR(10);
desc orders;

TRUNCATE TABLE users;

INSERT INTO orders (order_name,`value`) VALUES
	('Order1', 99.99),
	('Order2', 5.40);


SELECT * FROM users;

DELETE FROM orders WHERE id=9;

DELETE FROM users WHERE order_id=9;

