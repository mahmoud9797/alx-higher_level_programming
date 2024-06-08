-- calculate the number of students with the same score
SELECT `score`, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
