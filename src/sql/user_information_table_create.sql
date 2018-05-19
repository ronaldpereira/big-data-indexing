create table user_information (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	username VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	email VARCHAR(255),
	gender VARCHAR(1),
	ip_address_v4 VARCHAR(255),
	ip_address_v6 VARCHAR(255),
	hash VARCHAR(255),
	company_name VARCHAR(255),
	background_color VARCHAR(50),
	create_time DATE,
	update_time DATE
);