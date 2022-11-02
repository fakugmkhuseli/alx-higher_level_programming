-- Lists all cities contained in the database "hbtn_0d_usa".
-- Each record should display: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id.
SELECT a.`id`, a.`name`, b.`name`
FROM `cities` AS a
INNER JOIN `states` AS b
ON a.`states_id` = b.`id`
ORDER BY a.`id`;
