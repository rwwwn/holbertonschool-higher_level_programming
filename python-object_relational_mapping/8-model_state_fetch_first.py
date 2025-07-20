#!/usr/bin/python3
"""Print the first State object from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch first state ordered by id
    state = session.query(State).order_by(State.id).first()

    # Print result or "Nothing"
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
