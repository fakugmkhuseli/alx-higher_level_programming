-- Creates the table id_not_null on the MySQL server.
-- If the table id_not_null already exists,the script should not fail.
CREATE TABLE IF NOT EXISTS `id_not_null` (`id` INT DEFAULT 1, `name` VARCHAR(256));
