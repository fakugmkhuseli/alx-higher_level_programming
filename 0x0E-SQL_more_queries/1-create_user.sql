-- Creates the MySQL server user "user_od_1".
-- "user_0d_1" should have all privileges on your MySQL server.
CREATE USER
       IF NOT EXISTS 'user_0d_1'@'localhost'
       IDENTIFIED WITH 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
       ON *.*
       TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

