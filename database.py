from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://localhost:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
