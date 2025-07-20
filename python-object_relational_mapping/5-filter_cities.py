#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )

    # Create cursor and execute query
    cur = db.cursor()
    query = """SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id"""
    cur.execute(query, (sys.argv[4],))

    # Fetch results and format output
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))

    # Cleanup
    cur.close()
    db.close()
