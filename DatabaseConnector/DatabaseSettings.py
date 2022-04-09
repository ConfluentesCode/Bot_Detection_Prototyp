from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pathlib

current_directory = pathlib.Path(__file__).parent.resolve()

DATABASE_PATH = f'sqlite:////{current_directory}/Database/BotDetection.db'
Base = declarative_base()

engine = create_engine(DATABASE_PATH, echo=False)

SessionCreator = sessionmaker(bind=engine)
session_creator = SessionCreator()
