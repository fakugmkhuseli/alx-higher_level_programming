-- Creates the database "hbtn_0d_usa" and the table "cities" (in the database hbtn_0d_usa) on the MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities`.`hbtn_0d_usa` (
    PRIMARY KEY(`id`), 
    `id` INT NOT NULL AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    FOREIGN KEY(`state_id`)
    REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
