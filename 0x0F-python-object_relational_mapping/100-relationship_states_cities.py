#!/usr/bin/python3
"""
Creates a State object “California” with the City “San Francisco”
in the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for California
    california = State(name="California")

    # Create a new City object for San Francisco linked to California
    san_francisco = City(name="San Francisco", state=california)

    # Add and commit the objects to the database
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Print the id of the new state and city
    print(f"State ID: {california.id}, City ID: {san_francisco.id}")

    # Close the session
    session.close()
