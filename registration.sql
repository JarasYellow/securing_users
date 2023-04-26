CREATE TABLE reg_users(
	reg_id int PRIMARY KEY,
	last_name VARCHAR(30) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	email TEXT NOT NULL,
	password_reg VARCHAR(16) NOT NULL
)