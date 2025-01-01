#!/usr/bin/python3
"""
This script takes the name of a state as an argument and lists all cities
of that state using the database `hbtn_0e_4_usa`.
The script is safe from SQL injections.
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

    # Create a cursor to execute the SQL query
    cursor = db.cursor()

    # Execute a single SQL query to fetch all cities of the given state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch and display results
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()
