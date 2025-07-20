# Python - Object Relational Mapping (ORM) with SQLAlchemy

This project focuses on how to interact with a MySQL database using Python and SQLAlchemy ORM. The tasks cover everything from defining database models to querying and manipulating data using object-oriented approaches.

## 📚 Summary

We implemented the following key components:

- Defined the `State` and `City` classes using SQLAlchemy's declarative base.
- Created and populated MySQL databases using `.sql` scripts.
- Used SQLAlchemy sessions to:
  - Retrieve records.
  - Add new entries.
  - Update and delete records.
  - Perform filtering, sorting, and joins.
- Ensured code compliance with `pycodestyle`.

## 📁 Files

| File Name                       | Description                                                  |
|--------------------------------|--------------------------------------------------------------|
| `model_state.py`               | Defines the `State` class and the base model.               |
| `model_city.py`                | Defines the `City` class linked to the `states` table.      |
| `6-model_state.py`             | Creates the `states` table in the database.                 |
| `7-model_state_fetch_all.py`   | Lists all `State` objects.                                  |
| `8-model_state_fetch_first.py` | Prints the first state in the table.                        |
| `9-model_state_filter_a.py`    | Filters and prints states that contain the letter "a".      |
| `10-model_state_my_get.py`     | Retrieves a state by name.                                  |
| `11-model_state_insert.py`     | Adds a new state named "Louisiana".                         |
| `12-model_state_update_id_2.py`| Updates state name with ID 2.                               |
| `13-model_state_delete_a.py`   | Deletes all states with names containing "a".               |
| `14-model_city_fetch_by_state.py` | Prints all cities along with their states.              |

## 🛠️ Useful Commands

| Command                                                   | Purpose                                 |
|-----------------------------------------------------------|-----------------------------------------|
| `chmod +x script.py`                                      | Make a Python file executable.          |
| `mysql -u root -p -e "DROP DATABASE IF EXISTS db;"`       | Drop a database via MySQL CLI.          |
| `cat file.sql | mysql -u root -p`                         | Run SQL script to populate database.    |
| `pycodestyle file.py`                                     | Check code style for Python files.      |
| `./script.py root root dbname`                            | Run the script with DB credentials.     |

---

✅ All files were tested and validated using SQLAlchemy and `pycodestyle`.  
✅ Final outputs were verified using sample data.

---
