-- calculate the number of students with the same score
SELECT count(*) AS number, `score`
FROM second_table
GROUP BY score
ORDER BY number DESC;
