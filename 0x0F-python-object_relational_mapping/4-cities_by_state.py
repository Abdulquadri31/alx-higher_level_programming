#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`.
The script accepts three arguments: MySQL username, password, and database name.
Results are sorted in ascending order by `cities.id`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute the SQL query
    cursor = db.cursor()

    # Execute a single SQL query to fetch all cities and their corresponding states
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch and display all results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
