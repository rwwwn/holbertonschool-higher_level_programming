-- Task 16: List rows where name is not null or empty, sorted by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
