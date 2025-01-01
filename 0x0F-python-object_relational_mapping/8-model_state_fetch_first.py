#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    # Print the result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
