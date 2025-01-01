#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' (upper N)
from the database `hbtn_0e_0_usa`.
The script accepts three arguments: MySQL username, password, and database name.
Results are sorted in ascending order by `states.id`.
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

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and display all results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
