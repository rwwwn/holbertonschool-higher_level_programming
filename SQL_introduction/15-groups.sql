-- Task 15: Count how many rows have the same score, sorted by count
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
