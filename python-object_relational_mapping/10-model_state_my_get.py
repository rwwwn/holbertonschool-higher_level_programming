#!/usr/bin/python3
"""Print the id of a State object with a given name"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create connection
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for state by name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")
