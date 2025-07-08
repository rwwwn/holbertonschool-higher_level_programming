#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server on localhost, port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to get all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
