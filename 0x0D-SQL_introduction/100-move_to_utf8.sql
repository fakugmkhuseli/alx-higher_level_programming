-- Converts "hbtn_0c_0" database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in the  MySQL server.
USE `hbtn_0c_0`
ALTER `first_name`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
