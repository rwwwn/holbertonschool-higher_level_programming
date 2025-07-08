#!/usr/bin/python3
"""Add the State object 'Louisiana' to the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to DB
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create and add new state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print new state's ID
    print(new_state.id)
