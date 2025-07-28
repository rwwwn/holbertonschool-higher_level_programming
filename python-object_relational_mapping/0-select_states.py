#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa in ascending order."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    # Create a cursor
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Clean up
    cur.close()
    db.close()
