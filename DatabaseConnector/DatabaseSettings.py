from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Constants import Constants

Base = declarative_base()

engine = create_engine(Constants.DATABASE_PATH, echo=True)

SessionCreator = sessionmaker(bind=engine)
session_creator = SessionCreator()
