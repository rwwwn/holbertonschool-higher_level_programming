#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa along with their state names
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=db_name,
        host="localhost",
        port=3306
    )

    # Execute JOIN query to get cities with state names
    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Print all rows
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()
