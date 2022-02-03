from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_PATH = 'sqlite:////Users/bjarneschroder/PycharmProjects/Bot_Detection_Prototyp/DatabaseConnector/Database/BotDetection.db'
Base = declarative_base()

engine = create_engine(DATABASE_PATH, echo=False)

SessionCreator = sessionmaker(bind=engine)
session_creator = SessionCreator()
