#!/usr/bin/python3
"""
Contains the class definition of a State.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base

class State(Base):
    """
    State class represents the 'states' table in the database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Relationship with the City class
    cities = relationship("City", backref="state", cascade="all, delete")
