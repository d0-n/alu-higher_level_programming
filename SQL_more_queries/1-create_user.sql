-- Create user_0d_1 with all privileges on the server.
-- Create user_0d_1 if missing.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Ensure user_0d_1 password is set as required.
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to user_0d_1.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
