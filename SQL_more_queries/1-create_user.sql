-- Create user_0d_1 with all privileges on the server.
-- Drop user_0d_1 if already present to reset privileges.
DROP USER IF EXISTS 'user_0d_1'@'localhost';
-- Create user_0d_1 with required password.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to user_0d_1.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
