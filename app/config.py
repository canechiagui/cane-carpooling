from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://usuario:senha@localhost:5432/cane_carpooling"

# Create engine to connect with database
engine = create_engine(DATABASE_URL)

# Create a session t interact with base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base to create models ORM
Base = declarative_base()
