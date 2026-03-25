-- List all privileges of users user_0d_1 and user_0d_2 on localhost.
-- Revoke extra dynamic privileges on newer MySQL versions for user_0d_1.
REVOKE IF EXISTS AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER ON *.* FROM 'user_0d_1'@'localhost';
-- Revoke extra dynamic privileges on newer MySQL versions for user_0d_2.
REVOKE IF EXISTS AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER ON *.* FROM 'user_0d_2'@'localhost';
-- Show grants for user_0d_1.
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- Show grants for user_0d_2.
SHOW GRANTS FOR 'user_0d_2'@'localhost';
