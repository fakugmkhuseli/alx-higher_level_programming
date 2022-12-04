#!/usr/bin/python3
""" Creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name='California')
    newState = City(name='San Francisco')
    newState.cities.append(newCity)
    session.add(newState)
    session.add(newCity)
    session.commit()
