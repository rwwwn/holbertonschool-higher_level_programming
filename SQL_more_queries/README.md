# SQL - More Queries

This project is part of the Holberton School curriculum and focuses on advanced SQL operations such as privileges, constraints, joins, and subqueries.

## 📌 Objectives

- Create and manage MySQL users and privileges
- Understand and apply `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`
- Use different types of SQL joins (INNER, LEFT)
- Write queries using subqueries and filtering logic
- Retrieve and organize data from multiple related tables

## 🧠 What I learned

- How to grant/restrict access in MySQL using `GRANT` and `REVOKE`
- Building and linking relational tables with constraints
- Writing efficient queries with `JOIN` and `SUBQUERY`
- Handling NULL values and counting related data
- Sorting and grouping results based on real-world use cases

## 🧾 Key SQL Commands Used

| Command | Purpose |
|--------|---------|
| `CREATE USER IF NOT EXISTS 'user'@'localhost' IDENTIFIED BY 'pwd';` | Create a new MySQL user safely |
| `GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';` | Give full access to a user |
| `GRANT SELECT ON db.table TO 'user'@'localhost';` | Give read-only access |
| `CREATE DATABASE IF NOT EXISTS dbname;` | Create a database if it doesn't already exist |
| `CREATE TABLE IF NOT EXISTS ...` | Create a table safely (won't fail if it exists) |
| `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `DEFAULT`, `NOT NULL` | Table constraints for data integrity |
| `INSERT INTO table (...) VALUES (...);` | Add new records |
| `SELECT ... FROM ... WHERE ...` | Query data with conditions |
| `INNER JOIN`, `LEFT JOIN` | Combine data from multiple tables |
| `SUBQUERY` (`SELECT ... WHERE ... IN/=`) | Use a query inside another |
| `GROUP BY`, `COUNT()` | Aggregate data and count records |
| `ORDER BY ... ASC/DESC` | Sort results by column |

## 🗂️ Files

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
Replace filename.sql with the script name and database_name with the correct database.
---
