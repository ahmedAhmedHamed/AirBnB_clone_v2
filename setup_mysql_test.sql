-- MySQL setup test

-- A database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- A new user hbnb_test (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- hbnb_test should have all privileges on the database hbnb_dev_db (and only this database)
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Update status
FLUSH PRIVILEGES;
