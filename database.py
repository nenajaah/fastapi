from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
Resource: 
https://fastapi.tiangolo.com/tutorial/sql-databases/
'''

# Using an SQLite database
SQLALCHEMY_DATABASE_URL = "sqlite:///./adjust_challenge.db"

# Create SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create database session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for database models to inherit from 
Base = declarative_base()