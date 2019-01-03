#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State).one()
        print("{}: {}".format(state.id, state.name))
        session.close()
    except NoResultFound:
        print("Nothing")
        session.close()
    except MultipleResultsFound:
        state = session.query(State).order_by(State.id).all()[0]
        print("{}: {}".format(state.id, state.name))
        session.close()
