#!/usr/bin/python3
"""Start link class to table in database 
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State  # important: import State before create_all

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
