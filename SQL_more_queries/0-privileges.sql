-- List all privileges of users user_0d_1 and user_0d_2 on localhost.
-- Store existence of user_0d_1.
SET @USER1_EXISTS = (SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost');
-- Build revoke statement for extra dynamic privileges of user_0d_1.
SET @SQL1 = IF(
	@USER1_EXISTS = 1,
	"REVOKE IF EXISTS AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN ON *.* FROM 'user_0d_1'@'localhost'",
	"SELECT 1"
);
-- Prepare statement for user_0d_1 cleanup.
PREPARE STMT1 FROM @SQL1;
-- Execute statement for user_0d_1 cleanup.
EXECUTE STMT1;
-- Deallocate statement for user_0d_1 cleanup.
DEALLOCATE PREPARE STMT1;
-- Store existence of user_0d_2.
SET @USER2_EXISTS = (SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost');
-- Build revoke statement for extra dynamic privileges of user_0d_2.
SET @SQL2 = IF(
	@USER2_EXISTS = 1,
	"REVOKE IF EXISTS AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN ON *.* FROM 'user_0d_2'@'localhost'",
	"SELECT 1"
);
-- Prepare statement for user_0d_2 cleanup.
PREPARE STMT2 FROM @SQL2;
-- Execute statement for user_0d_2 cleanup.
EXECUTE STMT2;
-- Deallocate statement for user_0d_2 cleanup.
DEALLOCATE PREPARE STMT2;
-- Show grants for user_0d_1.
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- Show grants for user_0d_2.
SHOW GRANTS FOR 'user_0d_2'@'localhost';
