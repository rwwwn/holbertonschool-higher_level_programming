# 📚 SQL - More Queries

This project is part of the Holberton School curriculum. It focuses on more advanced SQL concepts including table relationships, user permissions, and complex queries.

## 📌 Objectives

- Manage MySQL users and assign privileges using GRANT and REVOKE
- Apply table constraints: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL
- Use SQL joins (INNER JOIN, LEFT JOIN) to combine data across tables
- Write subqueries and filter results based on complex logic
- Retrieve and analyze data from related tables efficiently

## 🧠 Key Learnings

- Creating secure and flexible MySQL user permissions
- Designing relational databases using constraints and keys
- Writing powerful queries using joins and subqueries
- Handling NULL values and applying aggregation functions
- Organizing and presenting data using GROUP BY and ORDER BY


## 🗂️ SQL Files and Descriptions

Each `.sql` file contains one task with a single SQL statement, prefixed by comments for clarity.

| File | Description |
|------|-------------|
| 0-privileges.sql | Show all privileges of specific users |
| 1-create_user.sql | Create a new user with full access |
| 2-create_read_user.sql | Create user with SELECT access only |
| 3-force_name.sql | Table with NOT NULL name column |
| 4-never_empty.sql | Table with default ID value |
| 5-unique_id.sql | Table with unique ID constraint |
| 6-states.sql | Create `states` table with primary key |
| 7-cities.sql | Create `cities` table with foreign key to `states` |
| 8-cities_of_california_subquery.sql | Cities in California using subquery |
| 9-cities_by_state_join.sql | Cities with their states using JOIN |
| 10-genre_id_by_show.sql | Shows with their genre IDs |
| 11-genre_id_all_shows.sql | All shows (with or without genres) |
| 12-no_genre.sql | Shows with no genres |
| 13-count_shows_by_genre.sql | Count shows per genre |
| 14-my_genres.sql | Genres for the show Dexter |
| 15-comedy_only.sql | All shows in the Comedy genre |
| 16-shows_by_genre.sql | All shows and their genres (including NULLs) |

## 💻 Usage

To run any SQL file:

```bash
cat filename.sql | mysql -uroot -p database_name
```
Replace filename.sql with the script name and database_name with your MySQL database name.
---
