-- Lists all records with a score >= 10 in the table "second_table" of the database "hbtn_0c_0" in the MySQL server.
-- Records are to be ordered by score (top first)
SELECT `score`, `name`
FROM `second_table`
WHERE `sore` >= 10
ORDER BY `score` DESC;
