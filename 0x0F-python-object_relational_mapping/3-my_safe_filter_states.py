#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the `states`
table of `hbtn_0e_0_usa` where `name` matches the argument, while
being safe from MySQL injection.
The script accepts four arguments: MySQL username, password, database name,
and the state name to search.
Results are sorted in ascending order by `states.id`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch states matching the name (safe from injection)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and display all results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
