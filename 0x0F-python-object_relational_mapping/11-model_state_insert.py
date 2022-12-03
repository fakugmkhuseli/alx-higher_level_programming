#!/usr/bin/python3
""" Prints the State object with the name passes as argumentfrom the database
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana= State(name='Louisiana')
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
